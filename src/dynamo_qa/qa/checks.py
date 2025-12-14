from __future__ import annotations
from typing import Any, Dict, List

from dynamo_qa.core.models import Element
from dynamo_qa.qa.rules import QARules


def run_checks(el: Element, rules: QARules) -> List[Dict[str, Any]]:
    """
    Returns a list of issues. Each issue is a dict with fields:
    - code: short identifier
    - severity: INFO/WARN/ERROR
    - message: human readable
    """
    issues: List[Dict[str, Any]] = []

    # Mark checks
    mark = (el.mark or "").strip()
    if rules.require_mark and not mark:
        issues.append({"code": "MARK_MISSING", "severity": "ERROR", "message": "Mark parameter is missing/empty."})
    elif mark and not rules.mark_pattern.match(mark):
        issues.append({"code": "MARK_BAD_FORMAT", "severity": "WARN", "message": f"Mark '{mark}' does not match pattern."})

    # Fire rating checks for certain categories
    if el.category in rules.require_fire_rating_for_categories:
        fr = el.fire_rating
        if fr is None or str(fr).strip() == "" or str(fr).lower() == "null":
            issues.append({"code": "FIRERATING_MISSING", "severity": "ERROR", "message": "FireRating is required for this category."})

    # Width checks
    if el.width_mm is not None:
        try:
            w = float(el.width_mm)
            if w <= rules.min_width_mm:
                issues.append({"code": "WIDTH_INVALID", "severity": "ERROR", "message": f"Width_mm={w} must be > {rules.min_width_mm}."})
        except (TypeError, ValueError):
            issues.append({"code": "WIDTH_NOT_NUMBER", "severity": "ERROR", "message": "Width_mm must be numeric."})

    return issues


def attach_issues(record: Dict[str, Any], issues: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Add issue count + flattened issue text to a record for CSV/JSON output."""
    record = dict(record)
    record["issue_count"] = len(issues)
    record["issues"] = "; ".join([f"{i['severity']}:{i['code']}" for i in issues]) if issues else ""
    return record
