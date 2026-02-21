
import json
from pathlib import Path
from .base import ProviderClient

class GCPMockClient(ProviderClient):
    def __init__(self, data_dir: str):
        self.path = Path(data_dir) / "gcp_inventory.json"

    def fetch_raw_inventory(self):
        return json.loads(self.path.read_text())
