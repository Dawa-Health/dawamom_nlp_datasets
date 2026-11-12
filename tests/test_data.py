import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
JSON_FILES = sorted(ROOT.glob("json/**/*.json"))
JSONL_FILES = sorted(p for p in ROOT.rglob("*.jsonl") if ".git" not in p.parts)


def test_data_files_exist():
    assert JSON_FILES and JSONL_FILES


@pytest.mark.parametrize("path", JSON_FILES, ids=lambda p: p.name)
def test_json_parses(path):
    json.loads(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("path", JSONL_FILES, ids=lambda p: p.name)
def test_jsonl_parses(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines, "file is empty"
    for n, line in enumerate(lines, 1):
        assert line.strip(), f"blank line {n}"
        assert isinstance(json.loads(line), dict), f"line {n} is not an object"
