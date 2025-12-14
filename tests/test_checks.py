from dynamo_qa.core.models import Element
from dynamo_qa.qa.checks import run_checks
from dynamo_qa.qa.rules import QARules


def test_missing_mark_is_error():
    rules = QARules(require_mark=True)
    el = Element(element_id=1, category="Walls", mark="")
    issues = run_checks(el, rules)
    assert any(i["code"] == "MARK_MISSING" and i["severity"] == "ERROR" for i in issues)


def test_width_invalid():
    rules = QARules(min_width_mm=0.0)
    el = Element(element_id=2, category="Doors", width_mm=-1)
    issues = run_checks(el, rules)
    assert any(i["code"] == "WIDTH_INVALID" for i in issues)
