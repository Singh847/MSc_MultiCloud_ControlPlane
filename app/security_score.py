from typing import Any, Dict
from .models import Resource

WEIGHTS = {
    "public_exposure": 30,
    "unencrypted_data": 25,
    "admin_iam": 20,
    "high_cost": 10,
    "compute_attack_surface": 15,
}

def calculate_risk(resource: Resource) -> Dict[str, Any]:
    score = 0
    factors: Dict[str, int] = {}

    if resource.public:
        score += WEIGHTS["public_exposure"]
        factors["public_exposure"] = WEIGHTS["public_exposure"]

    if resource.type in {"storage.bucket", "db.sql"} and not resource.encrypted:
        score += WEIGHTS["unencrypted_data"]
        factors["unencrypted_data"] = WEIGHTS["unencrypted_data"]

    if resource.iam_admin:
        score += WEIGHTS["admin_iam"]
        factors["admin_iam"] = WEIGHTS["admin_iam"]

    if resource.monthly_cost_estimate > 500:
        score += WEIGHTS["high_cost"]
        factors["high_cost"] = WEIGHTS["high_cost"]

    if resource.type == "compute.vm" and resource.public:
        score += WEIGHTS["compute_attack_surface"]
        factors["compute_attack_surface"] = WEIGHTS["compute_attack_surface"]

    return {
        "risk_score": min(score, 100),
        "risk_factors": factors,
    }
