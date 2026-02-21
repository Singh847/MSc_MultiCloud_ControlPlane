import json
from pathlib import Path
from typing import Dict, List, Optional
from collections import defaultdict

from .config import settings
from .models import Resource
from .normalize import normalize

from .providers.aws_mock import AWSMockClient
from .providers.gcp_mock import GCPMockClient
from .providers.azure_mock import AzureMockClient

from .policies.engine import evaluate
from .security_score import calculate_risk
from .drift import detect_drift


def build_clients():
    # ✅ Deploy-safe: use only mock clients by default
    clients = {
        "aws": AWSMockClient(settings.data_dir),
        "gcp": GCPMockClient(settings.data_dir),
        "azure": AzureMockClient(settings.data_dir),
    }

    # Optional: keep "real" mode support without breaking deploy
    # Only try to import Azure SDK when azure_mode == "real"
    if settings.azure_mode == "real":
        try:
            from .providers.azure_real import AzureRealClient  # lazy import
            clients["azure"] = AzureRealClient(settings.azure_subscription_id)
        except Exception as e:
            # If Azure SDK isn't installed (e.g., on Render), fall back to mock
            print(f"[WARN] Azure real mode unavailable ({e}). Falling back to AzureMockClient.")
            clients["azure"] = AzureMockClient(settings.data_dir)

    return clients


def collect_resources(providers: List[str]) -> List[Resource]:
    clients = build_clients()
    resources: List[Resource] = []

    for p in providers:
        if p not in clients:
            raise ValueError(f"Unknown provider '{p}'. Available: {list(clients.keys())}")

        raw_items = clients[p].fetch_raw_inventory()
        for item in raw_items:
            resources.append(normalize(p, item))

    return resources


def snapshot_file(name: str) -> Path:
    Path(settings.snapshot_dir).mkdir(parents=True, exist_ok=True)
    return Path(settings.snapshot_dir) / f"{name}.json"


def save_snapshot(name: str, resources: List[Resource]) -> None:
    payload = [r.model_dump() for r in resources]
    snapshot_file(name).write_text(json.dumps(payload, indent=2), encoding="utf-8")


def load_snapshot(name: str) -> List[Resource]:
    data = json.loads(snapshot_file(name).read_text(encoding="utf-8"))
    return [Resource(**x) for x in data]


def build_report(providers: Optional[List[str]] = None) -> Dict[str, object]:
    if providers is None:
        providers = settings.enabled_providers

    resources = collect_resources(providers)

    # ✅ cost per provider
    cost_per_provider = defaultdict(float)
    for r in resources:
        cost_per_provider[r.provider] += float(r.monthly_cost_estimate)

    findings = evaluate(resources)

    risk_scores = []
    for r in resources:
        rsk = calculate_risk(r)
        risk_scores.append({
            "provider": r.provider,
            "resource_id": r.resource_id,
            "risk_score": rsk.get("risk_score", 0),
            "risk_factors": rsk.get("risk_factors", []),
        })

    return {
        "summary": {
            "resource_count": len(resources),
            "finding_count": len(findings),
            "monthly_cost_total_estimate": round(sum(r.monthly_cost_estimate for r in resources), 2),
            "cost_per_provider": {k: round(v, 2) for k, v in cost_per_provider.items()},
            "providers": providers,
        },
        "resources": [r.model_dump() for r in resources],
        "findings": findings,
        "risk_scores": risk_scores,
    }


def build_drift_report(old_snapshot: str, new_snapshot: str) -> Dict[str, object]:
    old = load_snapshot(old_snapshot)
    new = load_snapshot(new_snapshot)
    drift = detect_drift(old, new)
    return {"old": old_snapshot, "new": new_snapshot, "drift": drift}