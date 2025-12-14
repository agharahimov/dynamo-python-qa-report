from __future__ import annotations
import re
from dataclasses import dataclass
from typing import Pattern


@dataclass(frozen=True)
class QARules:
    """Simple, configurable QA/QC rules that mimic BIM standards checks."""
    require_mark: bool = True
    require_fire_rating_for_categories: tuple[str, ...] = ("Doors", "Walls")
    mark_pattern: Pattern[str] = re.compile(r"^[A-Z]{1,3}-\d{1,4}$")  # e.g., W-001, ME-12

    min_width_mm: float = 0.0
