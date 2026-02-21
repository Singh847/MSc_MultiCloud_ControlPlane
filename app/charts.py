from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List

import matplotlib.pyplot as plt


def chart_resources_by_provider(resources: List[Dict[str, Any]], out_path: str) -> str:
    counts = Counter([r.get("provider", "unknown") for r in resources])

    labels = list(counts.keys())
    values = list(counts.values())

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)

    plt.figure()
    plt.bar(labels, values)
    plt.xlabel("Provider")
    plt.ylabel("Resource Count")
    plt.title("Resources per Provider")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

    return out_path


def chart_findings_by_severity(findings: List[Dict[str, Any]], out_path: str) -> str:
    counts = Counter([f.get("severity", "UNKNOWN") for f in findings])

    labels = list(counts.keys())
    values = list(counts.values())

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)

    plt.figure()
    plt.bar(labels, values)
    plt.xlabel("Severity")
    plt.ylabel("Finding Count")
    plt.title("Findings by Severity")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

    return out_path


def cost_by_provider(resources: List[Dict[str, Any]]) -> Dict[str, float]:
    agg = defaultdict(float)
    for r in resources:
        agg[r.get("provider", "unknown")] += float(r.get("monthly_cost_estimate", 0.0))
    return dict(agg)
