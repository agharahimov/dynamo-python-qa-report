from __future__ import annotations
from dataclasses import asdict
from typing import Any, Dict, Iterable, List

from dynamo_qa.core.models import Element


DEFAULT_FIELDS = [
    "element_id",
    "category",
    "family_name",
    "type_name",
    "level",
    "mark",
    "fire_rating",
    "width_mm",
    "comments",
]


def extract_records(elements: Iterable[Element], fields: List[str] | None = None) -> List[Dict[str, Any]]:
    """Convert Element objects into flat dictionaries for reporting."""
    use_fields = fields or DEFAULT_FIELDS
    out: List[Dict[str, Any]] = []
    for el in elements:
        d = asdict(el)
        out.append({k: d.get(k) for k in use_fields})
    return out
