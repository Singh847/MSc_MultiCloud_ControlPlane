from __future__ import annotations

from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from .service import build_report
from .charts import chart_resources_by_provider, chart_findings_by_severity

app = FastAPI(title="MSc Multi-Cloud Control Plane")
templates = Jinja2Templates(directory="app/templates")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request, providers: str = Query("azure")):
    provider_list = [p.strip() for p in providers.split(",") if p.strip()]
    report = build_report(provider_list)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "summary": report["summary"],
            "resources": report["resources"],
            "findings": report["findings"],
        },
    )


@app.get("/methodology", response_class=HTMLResponse)
def methodology(request: Request):
    return templates.TemplateResponse("methodology.html", {"request": request})


@app.get("/charts/resources.png")
def chart_resources(providers: str = Query("azure")):
    provider_list = [p.strip() for p in providers.split(",") if p.strip()]
    report = build_report(provider_list)
    out = "outputs/charts/resources_by_provider.png"
    chart_resources_by_provider(report["resources"], out)
    return FileResponse(out, media_type="image/png")


@app.get("/charts/findings.png")
def chart_findings(providers: str = Query("azure")):
    provider_list = [p.strip() for p in providers.split(",") if p.strip()]
    report = build_report(provider_list)
    out = "outputs/charts/findings_by_severity.png"
    chart_findings_by_severity(report["findings"], out)
    return FileResponse(out, media_type="image/png")
