from typing import Any, Dict
from .models import Resource

def normalize(provider: str, item: Dict[str, Any]) -> Resource:
    if provider == "aws":
        return Resource(
            provider="aws",
            resource_id=item["arn"],
            type=item["kind"],
            region=item["region"],
            name=item.get("name"),
            tags=item.get("tags", {}),
            public=item.get("public", False),
            encrypted=item.get("encrypted", True),
            iam_admin=item.get("iam_admin", False),
            monthly_cost_estimate=float(item.get("monthly_cost_estimate", 0.0)),
        )

    if provider == "azure":
        return Resource(
            provider="azure",
            resource_id=item["id"],
            type=item["type"],
            region=item["location"],
            name=item.get("name"),
            tags=item.get("tags", {}),
            public=item.get("internet_exposed", False),
            encrypted=item.get("encryption_enabled", True),
            iam_admin=item.get("role_is_owner", False),
            monthly_cost_estimate=float(item.get("monthly_cost_estimate", 0.0)),
        )

    if provider == "gcp":
        return Resource(
            provider="gcp",
            resource_id=item["selfLink"],
            type=item["resourceType"],
            region=item["region"],
            name=item.get("name"),
            tags=item.get("labels", {}),
            public=item.get("public", False),
            encrypted=item.get("encrypted", True),
            iam_admin=item.get("iam_admin", False),
            monthly_cost_estimate=float(item.get("monthly_cost_estimate", 0.0)),
        )

    raise ValueError(f"Unknown provider: {provider}")
