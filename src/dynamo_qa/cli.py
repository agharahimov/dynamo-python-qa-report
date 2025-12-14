from __future__ import annotations
import argparse
from collections import Counter
from pathlib import Path
from typing import Dict, List

from dynamo_qa.core.extract import extract_records
from dynamo_qa.io.loaders import load_elements_from_json
from dynamo_qa.io.writers import write_csv, write_json, write_summary
from dynamo_qa.qa.checks import attach_issues, run_checks
from dynamo_qa.qa.rules import QARules


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="dynamo-qa",
        description="Generate QA/QC reports from mock Revit-like elements (portable Dynamo/Python prototype).",
    )
    parser.add_argument("--input", default="data/sample_elements.json", help="Path to input JSON data.")
    parser.add_argument("--outdir", default="reports", help="Output directory for reports.")
    args = parser.parse_args()

    elements = load_elements_from_json(args.input)
    rules = QARules()

    base_records = extract_records(elements)
    all_issues: List[Dict] = []
    enriched = []

    severity_counter = Counter()

    for el, rec in zip(elements, base_records):
        issues = run_checks(el, rules)
        all_issues.append({"element_id": el.element_id, "issues": issues})
        for i in issues:
            severity_counter[i["severity"]] += 1
        enriched.append(attach_issues(rec, issues))

    outdir = Path(args.outdir)
    write_csv(outdir / "report.csv", enriched)
    write_json(outdir / "report.json", {"records": enriched, "issues": all_issues})
    write_summary(outdir / "summary.txt", total=len(elements), total_issues=sum(severity_counter.values()), by_severity=dict(severity_counter))

    print(f"✅ Wrote: {outdir/'report.csv'}")
    print(f"✅ Wrote: {outdir/'report.json'}")
    print(f"✅ Wrote: {outdir/'summary.txt'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
