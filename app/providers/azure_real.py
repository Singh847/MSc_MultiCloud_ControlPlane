from typing import Any, Dict, List

from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.authorization import AuthorizationManagementClient


class AzureRealClient:
    """
    Pulls real Azure inventory using Azure CLI auth.
    Returns provider-native raw items which your normalize() converts later.
    """

    def __init__(self, subscription_id: str):
        self.subscription_id = subscription_id
        self.credential = AzureCliCredential()

        self.compute = ComputeManagementClient(self.credential, subscription_id)
        self.storage = StorageManagementClient(self.credential, subscription_id)
        self.authz = AuthorizationManagementClient(self.credential, subscription_id)

    def fetch_raw_inventory(self) -> List[Dict[str, Any]]:
        raw: List[Dict[str, Any]] = []

        # 1) Storage accounts
        for sa in self.storage.storage_accounts.list():
            raw.append({
                "id": sa.id,
                "type": "storage.bucket",
                "location": sa.location or "unknown",
                "name": sa.name,
                "tags": sa.tags or {},
                "internet_exposed": False,
                "encryption_enabled": True,
                "monthly_cost_estimate": 0.0,
            })

        # 2) Virtual machines
        for vm in self.compute.virtual_machines.list_all():
            raw.append({
                "id": vm.id,
                "type": "compute.vm",
                "location": vm.location or "unknown",
                "name": vm.name,
                "tags": vm.tags or {},
                "internet_exposed": False,
                "encryption_enabled": True,
                "monthly_cost_estimate": 0.0,
            })

        # 3) Role assignments (RBAC) - subscription scope
        scope = f"/subscriptions/{self.subscription_id}"

        try:
            for ra in self.authz.role_assignments.list_for_scope(scope):
                raw.append({
                    "id": ra.id,
                    "type": "iam.user",
                    "location": "global",
                    "name": getattr(ra, "principal_id", None) or "principal",
                    "tags": {},
                    "role_is_owner": False,  # improve later with role definition name lookup
                    "monthly_cost_estimate": 0.0,
                })
        except Exception as e:
            # If your account doesn't have permission to read role assignments,
            # we still return storage + VM inventory (dissertation-safe).
            raw.append({
                "id": f"rbac-error:{type(e).__name__}",
                "type": "meta.note",
                "location": "global",
                "name": "RBAC role assignments not accessible (permission limited)",
                "tags": {"error": str(e)},
                "internet_exposed": False,
                "encryption_enabled": True,
                "monthly_cost_estimate": 0.0,
            })

        return raw
