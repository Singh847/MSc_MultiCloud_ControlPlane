
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class ProviderClient(ABC):
    @abstractmethod
    def fetch_raw_inventory(self) -> List[Dict[str, Any]]:
        raise NotImplementedError
