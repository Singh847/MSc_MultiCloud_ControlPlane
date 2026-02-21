
import json
from pathlib import Path
from .base import ProviderClient

class AzureMockClient(ProviderClient):
    def __init__(self, data_dir: str):
        self.path = Path(data_dir) / "azure_inventory.json"

    def fetch_raw_inventory(self):
        return json.loads(self.path.read_text())
