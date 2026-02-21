from __future__ import annotations
from pathlib import Path
from typing import Any, Dict
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def export_report_pdf(report: Dict[str, Any], output_path: str) -> str:
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(out),
        pagesize=A4,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
    )

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Multi-Cloud Control Plane Report", styles["Title"]))
    story.append(Paragraph(f"Generated (UTC): {datetime.utcnow().isoformat()}Z", styles["Normal"]))
    story.append(Spacer(1, 12))

    summary = report.get("summary", {})
    story.append(Paragraph(f"Providers: {', '.join(summary.get('providers', []))}", styles["BodyText"]))
    story.append(Paragraph(f"Total resources: {summary.get('resource_count', 0)}", styles["BodyText"]))
    story.append(Paragraph(f"Total findings: {summary.get('finding_count', 0)}", styles["BodyText"]))

    doc.build(story)
    return str(out)
