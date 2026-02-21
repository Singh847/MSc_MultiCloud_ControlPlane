import json
from pathlib import Path
from typing import Any, Dict, List
from rich.console import Console
from rich.table import Table
from .models import Resource

console = Console()

def print_inventory(resources: List[Resource]) -> None:
    table = Table(title="Multi-Cloud Inventory (Normalized)")
    table.add_column("Provider")
    table.add_column("Type")
    table.add_column("Region")
    table.add_column("Name")
    table.add_column("Public")
    table.add_column("Encrypted")
    table.add_column("£/month")

    for r in resources:
        table.add_row(
            r.provider,
            r.type,
            r.region,
            r.name or "-",
            str(r.public),
            str(r.encrypted),
            f"{r.monthly_cost_estimate:.2f}",
        )

    console.print(table)

def print_findings(findings: List[Dict[str, Any]]) -> None:
    table = Table(title="Policy Findings")
    table.add_column("Severity")
    table.add_column("Rule")
    table.add_column("Provider")
    table.add_column("Resource")
    table.add_column("Message")

    for f in findings:
        table.add_row(
            str(f.get("severity")),
            str(f.get("rule")),
            str(f.get("provider")),
            str(f.get("resource_id")),
            str(f.get("message")),
        )

    console.print(table)

def export_json(path: str, payload: Dict[str, Any]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, indent=2), encoding="utf-8")
