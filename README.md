🚀 Advanced Multi-Cloud Security Control Plane

A Python-based cloud governance and security orchestration platform designed to detect misconfigurations, calculate security posture scores, and monitor configuration drift across multi-cloud environments.


🌍 Live Deployment

🔗 Dashboard
https://msc-multicloud-controlplane.onrender.com/

📘 API Docs (Swagger)
https://msc-multicloud-controlplane.onrender.com/docs

💓 Health Check
https://msc-multicloud-controlplane.onrender.com/health

🎯 Problem It Solves

Multi-cloud adoption (AWS, Azure, GCP) introduces:

Fragmented security visibility

Policy inconsistencies

Configuration drift

Weak governance enforcement

This platform centralizes security evaluation and governance automation into a single control plane.

🏗 Architecture Overview
Cloud Providers (AWS / Azure / GCP)
            ↓
Inventory Collection Layer
            ↓
Normalization Engine
            ↓
Policy Evaluation Engine
            ↓
Security Scoring Module
            ↓
Drift Detection Engine
            ↓
Reporting (Console / JSON / PDF)
            ↓
REST API + Web Dashboard
Core Modules

service.py – Orchestration engine

policies/engine.py – Policy evaluation framework

security_score.py – Posture scoring logic

drift.py – Snapshot comparison engine

normalize.py – Cross-cloud abstraction layer

pdf_report.py – Report export automation

providers/ – Cloud provider abstraction pattern

🔥 Core Capabilities
✅ Multi-Cloud Inventory Collection

AWS (mock)

Azure (mock + real option)

GCP (mock)

Unified normalization format

🔐 Policy Engine

Detects:

Public exposure risks

Missing encryption

Insecure configurations

Misaligned governance controls

📊 Security Posture Scoring

Weighted scoring model based on:

Control failures

Severity levels

Resource criticality

📁 Drift Detection

Compare infrastructure snapshots:

--snapshot run1
--drift run1 run2

Detects:

Added resources

Removed resources

Modified configurations

📄 Automated Reporting

Console output

JSON export

PDF export

🖥 CLI Usage

Run:

python -m app.main

Examples:

python -m app.main --providers aws azure
python -m app.main --snapshot run1
python -m app.main --drift run1 run2
python -m app.main --export report.json
🌐 REST API (FastAPI)

Start API locally:

uvicorn app.api:app --reload

Access:

http://127.0.0.1:8000/docs

Live:
https://msc-multicloud-controlplane.onrender.com/docs

🛠 Tech Stack

Python

FastAPI

Uvicorn

Modular Architecture

Policy-as-Code Pattern

Cloud Provider Abstraction

Snapshot Versioning

JSON + PDF Reporting

🧠 Engineering Highlights

This project demonstrates:

Multi-cloud architecture design

Policy-based governance modeling

Drift detection algorithms

Abstraction layer design pattern

API-first backend architecture

Security automation principles

Inspired by enterprise platforms such as:

Prisma Cloud

Azure Defender

AWS Security Hub

Cloud Custodian

🔮 Roadmap

Real AWS & GCP SDK integration

Terraform state ingestion

CI/CD pipeline integration

Kubernetes workload support

Role-Based Access Control (RBAC)

Full Docker production deployment

👨‍💻 Author

Sumeer Singh Rana
Cloud Security | DevSecOps | Platform Engineering
GitHub: https://github.com/Singh847

🎯 Why This Version Is Stronger

✔ Clean structure
✔ Clear problem statement
✔ Enterprise tone
✔ No coursework vibe
✔ Impact-first presentation
✔ Easy to scan in 30 seconds
