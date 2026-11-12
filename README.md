# Zambezi NLU: Multilingual Maternal & SRH Health Dataset

**Zambezi NLU** is a multilingual maternal and SRH health Natural Language Understanding (NLU) dataset developed by Dawa Health to support research, development and evaluation of NLP systems for African languages.

It covers seven languages: English, Shona, Ndebele, Nyanja, Tonga, Bemba and Lozi.

The dataset provides structured pregnancy and maternal health information to support multilingual conversational AI, question answering, semantic understanding and digital maternal health assistants. It also includes an English benchmark for testing whether a system recognises the assumptions built into maternal and SRH questions.

**Dataset format:** JSON and JSONL.

**License:** CC BY 4.0.

**Copyright:** © 2026 Dawa Health.

**Funding:** Grand Challenges Canada, UNICEF Femtech Ventures, and TogetHER for Health.

## Contents

| Part | Location | Description |
|---|---|---|
| Pregnancy information (JSON) | `json/` | Week-by-week pregnancy information, one structured file per language |
| Pregnancy information (JSONL) | `dawamom_<language>.jsonl` | The same content flattened to one record per week, one file per language |
| Combined file | `combined_multilingual.jsonl` | All seven languages in a single JSONL file |
| Benchmark | [`benchmark/`](benchmark/README.md) | 821 assumptions from 657 maternal and SRH questions, with veracity and assumption-type labels |

## Languages and authors

Each language set covers 40 weeks of pregnancy and was written by first-language speakers.

| Language | Files | Authors |
|---|---|---|
| English | `DawaMom_English_dataset.json`, `dawamom_english.jsonl` | Tafadzwa K Munzwa, Takunda G Mugwagwa, Farai V Mutanga |
| Shona | `DawaMom_Shona_dataset.json`, `dawamom_shona.jsonl` | Tinowimba Katsumbe, Tafadzwa Muchoza, Wisdom Mukoko, Charles Zhou |
| Ndebele | `DawaMom_isiNdebele_dataset.json`, `dawamom_isindebele.jsonl` | Zanele Dube, Vezilizwi Maphosa, Sibongikhosi Moyo, Talent Mujombi, Nobukhosi Ndlovu |
| Nyanja | `DawaMom_chiNyanja_dataset.json`, `dawamom_chinyanja.jsonl` | Charity S Phiri, Aaron Chiwala, Precious Milanzi |
| Tonga | `DawaMom_chiTonga_dataset.json`, `dawamom_chitonga.jsonl` | Angela S Chikambwe, Mercy Musonda, Judy Mweemba |
| Bemba | `DawaMom_Bemba_dataset.json`, `dawamom_bemba.jsonl` | Mumbi Chileshe, Audrine Chitalu |
| Lozi | `DawaMom_lozi_dataset.json`, `dawamom_lozi.jsonl` | Hilda M Lifumbo, Kamutumwa S Imanga |

## Benchmark

The [Zambezi NLU Benchmark](benchmark/README.md) pairs each question with an assumption it carries, a label for whether that assumption is true, and a label for the kind of assumption it is. It is written in plain patient-style English for the Zambian care context and is intended for evaluation only.

| | |
|---|---|
| File | `benchmark/zambezi_nlu_benchmark.jsonl` |
| Size | 821 assumptions from 657 questions |
| Annotators | Tafadzwa K Munzwa (Medical Doctor), Tariro F Munzwa (AI Engineer) |

See the [benchmark README](benchmark/README.md) for the record format, labels, sources and suggested evaluation.

## Data format

**JSON.** Each file holds the dataset name, language, authors and license, followed by a list of 40 weekly entries with baby development, maternal changes, tips and a plan for the week.

**JSONL.** One record per week:

```json
{
  "id": "dawamom_english_dataset_fixed_week_1",
  "language": "dawamom_english_dataset_fixed",
  "week": 1,
  "text": "Week 1 ...: Baby development — ... Maternal changes — ... Tips — ... Plan — ...",
  "dataset": "NLP Maternal Health Dataset",
  "authors": ["Tafadzwa K Munzwa", "Takunda G Mugwagwa", "Farai V Mutanga"],
  "license": "CC-BY-4.0"
}
```

## Loading

```python
import json

with open("dawamom_english.jsonl", encoding="utf-8") as f:
    records = [json.loads(line) for line in f]
```

## Intended use

This dataset is for research and for developing and evaluating NLP systems. It is not medical advice and should not be used to make decisions about an individual's care.

## Citation

Munzwa, T. K., et al. (2026). *Zambezi NLU: Multilingual Maternal & SRH Health Dataset* [Data set]. Dawa Health. CC BY 4.0.

```bibtex
@dataset{zambezi_nlu_2026,
  author    = {Munzwa, Tafadzwa K. and others},
  title     = {Zambezi NLU: Multilingual Maternal & SRH Health Dataset},
  year      = {2025},
  publisher = {Dawa Health},
  license   = {CC-BY-4.0},
  note      = {Multilingual maternal health dataset covering seven African languages}
}
```
