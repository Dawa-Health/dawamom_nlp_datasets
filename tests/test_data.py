"""Validation tests for the Zambezi NLU data files.

Run from the repository root with:  python -m pytest
"""
import json
from collections import defaultdict
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WEEKS = list(range(1, 41))
LANGUAGES = {"English", "Shona", "Ndebele", "Nyanja", "Tonga", "Bemba", "Lozi"}
# The week number is stored under a different field name in some languages.
WEEK_KEYS = ("week", "vhiki", "iviki", "sabata", "sunda")

FAQ_JSON = ROOT / "json" / "cervical_cancer-faq.json"
# The pregnancy source files: every JSON file in json/ except the FAQ.
JSON_FILES = sorted(p for p in ROOT.glob("json/*.json") if p != FAQ_JSON)
ALL_JSONL = sorted(
    p for p in ROOT.rglob("*.jsonl")
    if not {".git", "tests"} & set(p.relative_to(ROOT).parts)
)
FAQ_FILE = ROOT / "jsonl" / "cervical_cancer-faq.jsonl"
BENCHMARK_FILE = ROOT / "benchmark" / "zambezi_nlu_benchmark.jsonl"
# Every other JSONL file holds week-by-week pregnancy records.
PREGNANCY_JSONL = [
    p for p in ALL_JSONL
    if p != FAQ_FILE and "benchmark" not in p.relative_to(ROOT).parts
]


def name(path):
    return str(path.relative_to(ROOT))


def read_jsonl(path):
    records = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        assert line.strip(), f"{name(path)}: line {n} is blank"
        try:
            record = json.loads(line)
        except json.JSONDecodeError as err:
            pytest.fail(f"{name(path)}: line {n} is not valid JSON ({err})")
        assert isinstance(record, dict), f"{name(path)}: line {n} is not an object"
        records.append(record)
    assert records, f"{name(path)} is empty"
    return records


def week_of(record, where):
    keys = [k for k in WEEK_KEYS if k in record]
    assert len(keys) == 1, f"{where}: expected one week field, found {keys}"
    return record[keys[0]]


# --- Files are present ------------------------------------------------------

def test_expected_files_are_present():
    assert len(JSON_FILES) == 7, f"expected 7 pregnancy files in json/, found {len(JSON_FILES)}"
    assert FAQ_JSON.exists(), f"missing {name(FAQ_JSON)}"
    assert PREGNANCY_JSONL, "no pregnancy JSONL files found"
    assert FAQ_FILE.exists(), f"missing {name(FAQ_FILE)}"
    assert BENCHMARK_FILE.exists(), f"missing {name(BENCHMARK_FILE)}"


# --- JSON source files ------------------------------------------------------

@pytest.mark.parametrize("path", JSON_FILES, ids=name)
def test_json_file(path):
    data = json.loads(path.read_text(encoding="utf-8"))

    assert data.get("language") in LANGUAGES, f"unexpected language: {data.get('language')}"
    assert data.get("authors"), "authors are missing"
    assert data.get("license") == "Apache-2.0", f"license is {data.get('license')!r}, expected 'Apache-2.0'"

    lists = [v for v in data.values() if isinstance(v, list) and v and isinstance(v[0], dict)]
    assert len(lists) == 1, "expected exactly one list of weekly entries"
    weeks = [week_of(entry, name(path)) for entry in lists[0]]
    assert weeks == WEEKS, f"weeks should be 1 to 40 in order, got {weeks}"


def test_json_files_cover_all_languages():
    found = {json.loads(p.read_text(encoding="utf-8")).get("language") for p in JSON_FILES}
    assert found == LANGUAGES


# --- Pregnancy JSONL files --------------------------------------------------

@pytest.mark.parametrize("path", PREGNANCY_JSONL, ids=name)
def test_pregnancy_jsonl(path):
    records = read_jsonl(path)

    if len(records) == 40:
        # One language per file.
        weeks = [week_of(r, name(path)) for r in records]
        assert weeks == WEEKS, f"weeks should be 1 to 40 in order, got {weeks}"
    else:
        # Combined file: every language must have weeks 1 to 40.
        by_language = defaultdict(list)
        for r in records:
            assert "language" in r, "records in a combined file need a 'language' field"
            by_language[r["language"]].append(week_of(r, name(path)))
        assert len(by_language) == 7, f"expected 7 languages, found {sorted(by_language)}"
        assert len(records) == 280, f"expected 280 records, found {len(records)}"
        for language, weeks in by_language.items():
            assert sorted(weeks) == WEEKS, f"{language}: weeks should be 1 to 40, got {sorted(weeks)}"


# --- Cervical cancer FAQ ----------------------------------------------------

def test_cervical_cancer_faq():
    records = read_jsonl(FAQ_FILE)
    assert len(records) == 100, f"expected 100 records, found {len(records)}"
    assert [r.get("id") for r in records] == list(range(1, 101)), "ids should be 1 to 100 in order"

    for r in records:
        assert set(r) == {"id", "audience", "question", "answer"}, f"id {r.get('id')}: unexpected fields {sorted(r)}"
        assert r["audience"] in {"layman", "medical_professional"}, f"id {r['id']}: bad audience {r['audience']!r}"
        assert r["question"].strip() and r["answer"].strip(), f"id {r['id']}: empty question or answer"

    questions = [r["question"].strip().lower() for r in records]
    assert len(set(questions)) == len(questions), "duplicate questions found"


def test_cervical_cancer_faq_jsonl_matches_json():
    groups = json.loads(FAQ_JSON.read_text(encoding="utf-8"))["cervical_cancer_faq"]
    expected = [
        {"id": q["id"], "audience": audience, "question": q["question"], "answer": q["answer"]}
        for key, audience in (("layman_questions", "layman"),
                              ("medical_professional_questions", "medical_professional"))
        for q in groups[key]
    ]
    assert read_jsonl(FAQ_FILE) == expected, "the FAQ JSONL file does not match the FAQ JSON file"


# --- Benchmark --------------------------------------------------------------

def test_benchmark():
    records = read_jsonl(BENCHMARK_FILE)
    assert len(records) == 821, f"expected 821 records, found {len(records)}"
