
from pydantic import BaseModel, Field
from typing import Dict, Optional

class Resource(BaseModel):
    provider: str
    resource_id: str
    type: str
    region: str
    name: Optional[str] = None
    tags: Dict[str, str] = Field(default_factory=dict)
    public: bool = False
    encrypted: bool = True
    iam_admin: bool = False
    monthly_cost_estimate: float = 0.0
