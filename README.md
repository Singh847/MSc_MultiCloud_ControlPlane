l🚀 Advanced Multi-Cloud Control Plane

MSc Dissertation Project – Cloud Governance & Security Automation

📌 Overview

The Advanced Multi-Cloud Control Plane is a Python-based cloud governance and security orchestration platform designed to:

Collect resource inventories across multiple cloud providers

Detect misconfigurations using policy rules

Calculate security posture scores

Detect configuration drift between snapshots

Generate structured JSON and PDF reports

Expose REST API endpoints for automation

Provide a lightweight web dashboard interface

This project simulates real-world enterprise multi-cloud governance architecture across:

AWS

Azure

GCP

It demonstrates cloud engineering, DevSecOps automation, API design, reporting systems, and architecture modularity.

🏗 Architecture Overview
MSc_MultiCloud_ControlPlane
│
├── app/
│   ├── api.py              # FastAPI REST API
│   ├── main.py             # CLI entry point
│   ├── service.py          # Core orchestration logic
│   ├── config.py           # Application configuration
│   ├── drift.py            # Drift detection engine
│   ├── security_score.py   # Security posture scoring
│   ├── report.py           # Console & JSON reporting
│   ├── pdf_report.py       # PDF export functionality
│   ├── normalize.py        # Data normalization layer
│   ├── models.py           # Data models
│   │
│   ├── providers/
│   │   ├── aws_mock.py
│   │   ├── azure_mock.py
│   │   ├── azure_real.py
│   │   ├── gcp_mock.py
│   │   └── base.py
│   │
│   ├── policies/
│   │   └── engine.py       # Policy evaluation engine
│   │
│   └── templates/
│       ├── index.html
│       └── methodology.html
│
├── data/                   # Sample cloud inventories
├── requirements.txt
└── README.md
🔥 Core Features
✅ 1. Multi-Cloud Resource Collection

Collects inventory from:

AWS (mock)

Azure (mock + real option)

GCP (mock)

Resources are normalized into a unified internal format.

🔐 2. Policy Engine

Evaluates cloud resources against governance and security policies such as:

Public exposure risks

Missing encryption

Weak configurations

Insecure settings

The policies/engine.py module drives rule-based evaluation.

📊 3. Security Score Calculation

The platform calculates a security posture score based on:

Number of failed controls

Severity weighting

Resource criticality

This simulates enterprise-level security posture management.

📁 4. Snapshot & Drift Detection

The system supports:

--snapshot run1
--drift run1 run2

Drift detection compares historical snapshots and identifies:

Added resources

Removed resources

Modified configurations

This models real-world cloud configuration drift monitoring.

📄 5. Report Generation

Supports:

Console output

JSON export

PDF export (if PDF dependencies installed)

Example:

--export outputs/report.json
--export-pdf outputs/report.pdf
🌐 6. REST API (FastAPI)

Launch the API:

uvicorn app.api:app --reload

Then open:

http://127.0.0.1:8000/docs

You get interactive Swagger documentation.

🖥 7. CLI Interface

Run:

python -m app.main

Available options:

--providers aws azure gcp
--snapshot run1
--drift old_snapshot new_snapshot
--export path.json
--export-pdf path.pdf
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/Singh847/MSc_MultiCloud_ControlPlane.git
cd MSc_MultiCloud_ControlPlane
2️⃣ Create Virtual Environment

Windows:

python -m venv .venv
.venv\Scripts\Activate.ps1

Mac/Linux:

python3 -m venv .venv
source .venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
🚀 How to Use
Run CLI Mode
python -m app.main

Example with providers:

python -m app.main --providers aws azure

Save snapshot:

python -m app.main --snapshot run1

Drift comparison:

python -m app.main --drift run1 run2
Run API Mode
uvicorn app.api:app --reload

Open:

http://127.0.0.1:8000/docs
🧠 What This Project Demonstrates

Multi-cloud architecture understanding

Policy-based governance engine design

Modular Python architecture

REST API development (FastAPI)

CLI tooling

Security posture scoring

Drift detection logic

Snapshot versioning

Report automation (JSON + PDF)

Normalization layer abstraction

Provider abstraction design pattern

🏆 Academic & Professional Value

This MSc project reflects real-world enterprise cloud governance platforms such as:

Prisma Cloud

Azure Defender

AWS Security Hub

Cloud Custodian

HashiCorp Sentinel

It demonstrates strong capability in:

Cloud Engineering

DevSecOps

Security Automation

Platform Architecture

Infrastructure Governance

🔮 Future Improvements

Real AWS SDK integration

Real GCP SDK integration

Terraform state ingestion

CI/CD integration

Kubernetes integration

RBAC implementation

Docker containerization

Deployment to Azure/AWS

## Run API
uvicorn app.api:app --reload
https://msc-multicloud-controlplane.onrender.com/docs


👨‍💻 Author

Sumeer Singh Rana
MSc Computing – Cloud & Cybersecurity
GitHub: https://github.com/Singh847
