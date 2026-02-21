from typing import Dict, List, Any
from .models import Resource

def _index(resources: List[Resource]) -> Dict[str, Resource]:
    return {r.resource_id: r for r in resources}

def detect_drift(old: List[Resource], new: List[Resource]) -> Dict[str, List[Dict[str, Any]]]:
    old_map = _index(old)
    new_map = _index(new)

    created = [new_map[k].model_dump() for k in (new_map.keys() - old_map.keys())]
    deleted = [old_map[k].model_dump() for k in (old_map.keys() - new_map.keys())]

    changed: List[Dict[str, Any]] = []
    for rid in (old_map.keys() & new_map.keys()):
        if old_map[rid].model_dump() != new_map[rid].model_dump():
            changed.append({
                "resource_id": rid,
                "before": old_map[rid].model_dump(),
                "after": new_map[rid].model_dump(),
            })

    return {"created": created, "deleted": deleted, "changed": changed}
