"""Print a pass/fail validation report for the combined Zambezi NLU file.

Run from the repository root:  python scripts/validate_report.py
"""
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
matches = sorted(ROOT.rglob("combined_multilingual.jsonl"))
if not matches:
    raise SystemExit("combined_multilingual.jsonl not found in this repository")

records = [json.loads(line) for line in matches[0].read_text(encoding="utf-8").splitlines()]
df = pd.json_normalize(records)  # nested fields become e.g. "baby_development.summary"

LANGUAGES = ["English", "Shona", "Ndebele", "Nyanja", "Tonga", "Bemba", "Lozi"]
REQUIRED = [
    "language", "week",
    "baby_development.length", "baby_development.weight", "baby_development.summary",
    "maternal_changes.body_changes", "maternal_changes.tips", "maternal_changes.plan",
]


def filled(column):
    return df[column].notna() & df[column].astype(str).str.strip().ne("")

checks = {
    "required_columns": set(REQUIRED).issubset(df.columns),
    "valid_languages": df["language"].isin(LANGUAGES).all(),
    "all_languages_present": set(df["language"]) == set(LANGUAGES),
    "weeks_between_1_and_40": df["week"].between(1, 40).all(),
    "40_weeks_per_language": (df.groupby("language")["week"].nunique() == 40).all(),
    "unique_language_week": not df.duplicated(["language", "week"]).any(),
    "baby_summary_filled": filled("baby_development.summary").all(),
    "body_changes_filled": filled("maternal_changes.body_changes").all(),
    "tips_filled": filled("maternal_changes.tips").all(),
    "plan_filled": filled("maternal_changes.plan").all(),
}

passed = sum(bool(v) for v in checks.values())
print(f"File: {matches[0].relative_to(ROOT)} ({len(df)} records)")
print(f"Checks passed: {passed} of {len(checks)} ({100 * passed / len(checks):.0f}%)")
for name, result in checks.items():
    print(f"  {'PASS' if result else 'FAIL'}  {name}")

missing = df[~filled("maternal_changes.plan")][["language", "week"]]
if len(missing):
    print("Records with no plan:", ", ".join(f"{l} week {w}" for l, w in missing.values))

raise SystemExit(0 if passed == len(checks) else 1)
