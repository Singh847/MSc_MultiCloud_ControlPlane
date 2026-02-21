from pydantic import BaseModel
from typing import List

class Settings(BaseModel):
    enabled_providers: List[str] = ["aws", "azure", "gcp"]
    data_dir: str = "data"
    snapshot_dir: str = "snapshots"
    outputs_dir: str = "outputs"

    azure_subscription_id: str = ""
    azure_mode: str = "mock"  # "mock" or "real"


settings = Settings(
    azure_subscription_id="16639a4b-56d6-4577-886d-328bd89508df",
    azure_mode="real"
)
