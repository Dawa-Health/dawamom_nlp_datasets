# Changelog

All notable changes to Zambezi NLU are recorded in this file.

Version numbers follow the scheme in the [project charter](CHARTER.md):

- **MAJOR**: a change to the data format, or a change to the benchmark that makes results not comparable with earlier versions.
- **MINOR**: new languages, topics or records.
- **PATCH**: corrections to existing content or documentation.

Each entry is grouped under Added, Changed, Fixed or Removed. Benchmark results should state the dataset version they were run on.

## Unreleased

### Added

- Cervical cancer FAQ: 100 English question-and-answer pairs, 50 for the general public and 50 for health professionals (`json/cervical_cancer-faq.json`, `jsonl/cervical_cancer-faq.jsonl`).
- Combined multilingual JSONL file with one shared schema across all seven languages (280 records).
- Project charter (`CHARTER.md`).
- Code of Conduct (`CODE_OF_CONDUCT.md`).
- Contributing guide (`CONTRIBUTING.md`).
- Data validation tests (`tests/test_data.py`) and a GitHub Actions workflow that runs them on every pull request (`.github/workflows/validate.yml`).
- This changelog.

### Changed

- **License changed from CC BY 4.0 to Apache License 2.0** for the dataset, the benchmark and all code. Copies obtained earlier under CC BY 4.0 remain under that license.
- Per-language JSONL files now hold one record per week with the same nested fields as the JSON source, in place of a single flattened `text` field.
- README rewritten to describe the current file formats, the field names used in each language, the cervical cancer FAQ and the license.
- "Known issues in the current files" section added to the README.

### Known issues

These are documented in the README and not yet fixed:

- Lozi: some fields in weeks 30, 32, 33, 36 and 38 are in Ndebele, and the maternal fields for week 37 are in Nyanja.
- Lozi: from week 13 the maternal fields are nested inside the baby development object; weeks 14 and 17 have wrong length or weight values.
- Tonga: placeholder summary in week 23; weights for weeks 17 and 22 are too high.
- Nyanja: the baby weight field is named `kulemera` in weeks 1 to 10 and `ulemera` in weeks 11 to 40.
- Ndebele: tips and plan sit at the top level of each weekly entry.

## Earlier history

Changes made before this changelog was started are recorded in the [commit history](https://github.com/Dawa-Health/zambezi-nlu/commits/main). They include the original week-by-week pregnancy information in seven languages and the Zambezi NLU Benchmark (821 assumptions from 657 questions).
