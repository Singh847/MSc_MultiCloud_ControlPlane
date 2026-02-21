from typing import Callable, List, Dict, Any
from ..models import Resource

Finding = Dict[str, Any]
RuleFn = Callable[[Resource], List[Finding]]

def rule_no_public_storage(resource: Resource) -> List[Finding]:
    if resource.type == "storage.bucket" and resource.public:
        return [{
            "rule": "no_public_storage",
            "severity": "HIGH",
            "message": "Storage bucket is public.",
            "provider": resource.provider,
            "resource_id": resource.resource_id,
        }]
    return []

def rule_encryption_required(resource: Resource) -> List[Finding]:
    if resource.type in {"storage.bucket", "db.sql"} and not resource.encrypted:
        return [{
            "rule": "encryption_required",
            "severity": "HIGH",
            "message": "Encryption is disabled for a sensitive resource.",
            "provider": resource.provider,
            "resource_id": resource.resource_id,
        }]
    return []

def rule_no_admin_iam(resource: Resource) -> List[Finding]:
    if resource.type == "iam.user" and resource.iam_admin:
        return [{
            "rule": "no_admin_iam",
            "severity": "MEDIUM",
            "message": "IAM identity has admin/owner privileges.",
            "provider": resource.provider,
            "resource_id": resource.resource_id,
        }]
    return []

DEFAULT_RULES: List[RuleFn] = [
    rule_no_public_storage,
    rule_encryption_required,
    rule_no_admin_iam,
]

def evaluate(resources: List[Resource], rules: List[RuleFn] = DEFAULT_RULES) -> List[Finding]:
    findings: List[Finding] = []
    for r in resources:
        for rule in rules:
            findings.extend(rule(r))
    return findings
