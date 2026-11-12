# Zambezi NLU Benchmark: Assumptions in Maternal and SRH Questions

A benchmark of 821 assumptions drawn from 657 maternal, sexual and reproductive health questions, written for the Zambian care context. Each record pairs a question with one assumption the question carries, a label saying whether that assumption is true, and a label for the kind of assumption it is.

It is part of [Zambezi NLU](../README.md), developed by Dawa Health.

**File:** `zambezi_nlu_benchmark.jsonl` (UTF-8, one JSON object per line)
**Language:** English, in plain patient-style wording
**License:** CC BY 4.0

## What it tests

People asking health questions often build beliefs into the question itself. Some of those beliefs are false, and a few are dangerous. "Since the law only covers girls under 16, is there anything else I can do?" assumes something about the law before any answer is given.

A good health assistant should notice the assumption, check it, and correct it when it is wrong, instead of answering only the surface question. This benchmark supports three evaluations:

1. **Veracity:** given a question and an assumption, decide whether the assumption is true.
2. **Assumption type:** classify the assumption as a presupposition, an implicature, or world knowledge.
3. **Response quality:** given only the question, check whether a model's answer addresses the false assumptions listed for it.

## Record format

```json
{
  "assumption_id": "pv.24.1",
  "question_id": "pv.24",
  "subset": "pv",
  "question": "Since the government fixed the maternal death problem, why is my sister's clinic still turning women away?",
  "assumption": "Maternal mortality in Zambia has been resolved.",
  "veracity": "False",
  "assumption_type": "presupposition",
  "assumption_type_neha": "presupposition",
  "assumption_type_rupak": "presupposition",
  "persona": "adult woman",
  "assumption_category": "overstated_progress",
  "source_reference": "Brief p5 - MMR 398/100,000, among the world's highest"
}
```

| Field | Description |
|---|---|
| `assumption_id` | Unique ID for the record. Starts with the `question_id`. |
| `question_id` | ID of the question. Shared by all assumptions from the same question. |
| `subset` | Source group, taken from the first part of the ID. See [Subsets](#subsets). |
| `question` | The question as a patient or member of the public might ask it. |
| `assumption` | One belief the question carries or implies. |
| `veracity` | Whether the assumption is true. See [Labels](#labels). |
| `assumption_type` | Final (adjudicated) assumption type. |
| `assumption_type_neha` | Assumption type from the first annotator. *TODO: rename, see [Known limitations](#known-limitations).* |
| `assumption_type_rupak` | Assumption type from the second annotator. *TODO: rename.* |
| `persona` | Who is asking. Filled for the `pv` subset only, otherwise `null`. |
| `assumption_category` | Kind of belief or barrier involved. `pv` subset only. |
| `source_reference` | Law, regulation or brief the veracity label rests on. `pv` subset only. |

A question with several assumptions appears on several lines: 559 questions have one assumption, 32 have two and 66 have three.

## Labels

### Veracity

| Value | Records | Meaning |
|---|---|---|
| `True` | 489 | The assumption is correct. |
| `False` | 305 | The assumption is incorrect. |
| `false_unsure` | 24 | The assumption is false or cannot be confirmed as true. Used in the `obgyn` subset only. |
| `UNVERIFIABLE` | 3 | The sources neither confirm nor refute the assumption. Used in the `pv` subset only. |

### Assumption type

| Value | Records | Meaning |
|---|---|---|
| `presupposition` | 391 | Something the question takes for granted in order to make sense. |
| `implicature` | 320 | Something the question suggests without stating it outright. |
| `world knowledge` | 110 | A background fact the question relies on. |

The two annotators gave the same type for 799 of the 821 records. The 22 disagreements were resolved in `assumption_type`.

## Subsets

| Subset | Questions | Records | True | False | Other | Content |
|---|---|---|---|---|---|---|
| `obgyn` | 94 | 94 | 70 | 0 | 24 `false_unsure` | Obstetric and gynaecological instruments, procedures and conditions |
| `obs` | 143 | 143 | 70 | 73 | | Obstetrics: pregnancy, labour, delivery and the period after birth |
| `gyn` | 100 | 100 | 63 | 37 | | Gynaecology: periods, fertility, contraception, infections, cancers |
| `surg` | 3 | 3 | 3 | 0 | | Gynaecological surgery and care around operations |
| `repro` | 1 | 1 | 1 | 0 | | Reproductive biology |
| `gen` | 13 | 13 | 7 | 6 | | General emergencies: sepsis, clotting failure, wounds, fluid on the lungs |
| `uth` | 46 | 46 | 22 | 24 | | Medical conditions in pregnancy and specialist obstetric care |
| `stg` | 139 | 139 | 67 | 72 | | Antenatal care, labour, bleeding, pre-eclampsia, malaria, HIV and abortion care |
| `zsti` | 45 | 126 | 89 | 37 | | Sexually transmitted infections in Zambia |
| `whocx` | 49 | 128 | 88 | 40 | | Cervical cancer screening and treatment of pre-cancer |
| `pv` | 24 | 28 | 9 | 16 | 3 `UNVERIFIABLE` | Termination of pregnancy law and access to family planning in Zambia |
| **Total** | **657** | **821** | **489** | **305** | **27** | |

*TODO: add the source document for each subset (guideline title, edition and year) so users can verify the labels.*

Two question styles are present. Most subsets use full first-person questions ("My waters broke at 32 weeks, will I be sent home to rest?"). The `zsti` and `whocx` subsets use short lowercase search-style queries with no question mark ("what percentage of women with gonorrhoea have no symptoms").

## Loading

```python
import json

with open("zambezi_nlu_benchmark.jsonl", encoding="utf-8") as f:
    records = [json.loads(line) for line in f]
```

```python
from datasets import load_dataset

ds = load_dataset("json", data_files="zambezi_nlu_benchmark.jsonl", split="train")
```

## Suggested evaluation

- **Veracity:** report accuracy and macro-F1, overall and per subset. Because `false_unsure` and `UNVERIFIABLE` are each used in one subset only, either score a two-way task on the 794 `True`/`False` records, or state clearly how you mapped the other two values.
- **Assumption type:** report accuracy and macro-F1 against `assumption_type`.
- **Response quality:** send each distinct question once, then judge whether the answer corrects every assumption labelled `False` for that `question_id`. Group records by `question_id` to do this.

There is no train/test split. The benchmark is intended for evaluation only; do not train on it and then report scores on it.

## How it was built

*TODO: confirm or correct this section.*

Questions were written to reflect how women and families in Zambia ask about maternal, sexual and reproductive health, with assumptions and veracity labels grounded in clinical guidelines and, for the `pv` subset, in Zambian law and policy. Question wording was then simplified into everyday language while keeping the medical term in brackets where the question is about that term.

The annotation scheme (assumptions extracted per question, veracity, and the presupposition / implicature distinction) follows Srikanth et al. (2024). No records from that dataset are included here.

*TODO: name the annotators and their roles, and describe how disagreements were adjudicated.*

## Known limitations

- **Annotator field names.** `assumption_type_neha` and `assumption_type_rupak` are carried over from the template this benchmark was built on. They should be renamed to reflect who labelled these records.
- **Mixed veracity schemes.** Four veracity values are in use across subsets, as described above.
- **Plain-language rewording.** 287 questions were reworded into lay language and have not yet had clinical review.
- **Uneven subsets.** `surg` and `repro` are too small to report on separately.
- **Context-specific answers.** Labels reflect Zambian guidelines and law at the time of writing. They may not hold in other countries or after guidelines are revised.
- **English only.** The other Zambezi NLU languages are not yet covered.

## Intended use

This benchmark is for research and for evaluating NLP systems. It is not medical or legal advice, and the labels should not be used to make decisions about an individual's care.

## Citation

```bibtex
@dataset{zambezi_nlu_2025,
  author    = {Munzwa, Tafadzwa K.},
  title     = {Zambezi NLU: Multilingual Maternal & SRH Health Dataset},
  year      = {2025},
  publisher = {Dawa Health},
  license   = {CC-BY-4.0}
}
```

The annotation scheme is based on:

```bibtex
@inproceedings{srikanth-etal-2024-pregnant,
  author    = {Srikanth, Neha and Sarkar, Rupak and Mane, Heran and Aparicio, Elizabeth and Nguyen, Quynh and Rudinger, Rachel and Boyd-Graber, Jordan},
  title     = {Pregnant Questions: The Importance of Pragmatic Awareness in Maternal Health Question Answering},
  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
  year      = {2024},
  address   = {Mexico City, Mexico},
  publisher = {Association for Computational Linguistics},
  pages     = {7253--7268},
  doi       = {10.18653/v1/2024.naacl-long.403},
  url       = {https://aclanthology.org/2024.naacl-long.403/}
}
```

## Funding

Grand Challenges Canada, UNICEF Femtech Ventures and TogetHER for Health.

© 2025 Dawa Health.
