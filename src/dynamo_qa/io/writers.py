from __future__ import annotations
import csv
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List


def write_csv(path: str | Path, rows: List[Dict[str, Any]]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        p.write_text("", encoding="utf-8")
        return

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: str | Path, payload: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def write_summary(path: str | Path, total: int, total_issues: int, by_severity: Dict[str, int]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        f"Total elements: {total}",
        f"Total issues: {total_issues}",
        "",
        "Issues by severity:",
    ]
    for sev in ["ERROR", "WARN", "INFO"]:
        lines.append(f"- {sev}: {by_severity.get(sev, 0)}")

    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
