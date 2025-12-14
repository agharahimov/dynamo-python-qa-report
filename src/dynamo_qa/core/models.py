from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping, Optional


@dataclass(frozen=True)
class Element:
    """Portable representation of a Revit element for data extraction & QA checks."""
    element_id: int
    category: str
    family_name: Optional[str] = None
    type_name: Optional[str] = None
    level: Optional[str] = None
    mark: Optional[str] = None
    fire_rating: Optional[str] = None
    width_mm: Optional[float] = None
    comments: Optional[str] = None

    @staticmethod
    def from_mapping(d: Mapping[str, Any]) -> "Element":
        return Element(
            element_id=int(d.get("ElementId")),
            category=str(d.get("Category", "")),
            family_name=d.get("FamilyName"),
            type_name=d.get("TypeName"),
            level=d.get("Level"),
            mark=d.get("Mark"),
            fire_rating=d.get("FireRating"),
            width_mm=d.get("Width_mm"),
            comments=d.get("Comments"),
        )
