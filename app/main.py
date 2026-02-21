import argparse
from pathlib import Path

from .config import settings
from .service import build_report, save_snapshot, collect_resources, build_drift_report
from .report import print_inventory, print_findings, export_json

try:
    from .pdf_report import export_report_pdf
    PDF_OK = True
except Exception:
    PDF_OK = False


def parse_args():
    p = argparse.ArgumentParser(description="Advanced Enhanced Multi-Cloud Control Plane (CLI)")
    p.add_argument("--providers", nargs="+", default=settings.enabled_providers, choices=["aws", "azure", "gcp"])
    p.add_argument("--snapshot", help="Save snapshot name (e.g. run1)")
    p.add_argument("--drift", nargs=2, metavar=("OLD", "NEW"), help="Compare two snapshots")
    p.add_argument("--export", default=str(Path(settings.outputs_dir) / "report.json"), help="Export JSON path")
    p.add_argument("--export-pdf", default=str(Path(settings.outputs_dir) / "report.pdf"), help="Export PDF path")
    return p.parse_args()


def main():
    args = parse_args()

    if args.drift:
        old_name, new_name = args.drift
        payload = build_drift_report(old_name, new_name)
        export_json(args.export, payload)
        print(f"[OK] Drift exported to: {args.export}")
        return

    report = build_report(args.providers)
    resources = collect_resources(args.providers)

    print_inventory(resources)
    print_findings(report["findings"])  # type: ignore[arg-type]

    export_json(args.export, report)
    print(f"[OK] JSON exported to: {args.export}")

    if PDF_OK:
        pdf_path = export_report_pdf(report, args.export_pdf)
        print(f"[OK] PDF exported to: {pdf_path}")

    if args.snapshot:
        save_snapshot(args.snapshot, resources)
        print(f"[OK] Snapshot saved: {args.snapshot}")


if __name__ == "__main__":
    main()
