from __future__ import annotations
import json
from pathlib import Path
from typing import List

from dynamo_qa.core.models import Element


def load_elements_from_json(path: str | Path) -> List[Element]:
    p = Path(path)
    data = json.loads(p.read_text(encoding="utf-8"))
    return [Element.from_mapping(d) for d in data]
