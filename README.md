# Zambezi NLU: Multilingual Maternal & SRH Health Dataset

**Zambezi NLU** is a multilingual maternal and SRH health Natural Language Understanding (NLU) dataset developed by Dawa Health to support research, development and evaluation of NLP systems for African languages.

It covers seven languages: English, Shona, Ndebele, Nyanja, Tonga, Bemba and Lozi.

The dataset provides structured pregnancy and maternal health information to support multilingual conversational AI, question answering, semantic understanding and digital maternal health assistants. It also includes an English benchmark for testing whether a system recognises the assumptions built into health questions. The benchmark covers maternal health, sexual and reproductive health, cervical cancer and neonatal health.

| | |
|---|---|
| **Dataset format** | JSON and JSONL |
| **License** | CC BY 4.0 |
| **Copyright** | © 2026 Dawa Health |
| **Funding** | Grand Challenges Canada, UNICEF Femtech Ventures, and TogetHER for Health |
| **Contact** | developers@dawa-health.com |

## Contents

| Part | Location | Description |
|---|---|---|
| Pregnancy information (JSON) | `json/` | Week-by-week pregnancy information, one structured file per language |
| Pregnancy information (JSONL) | `dawamom_<language>.jsonl` | The same content flattened to one record per week, one file per language |
| Combined file | `combined_multilingual.jsonl` | All seven languages in a single JSONL file |
| Benchmark | [`benchmark/`](benchmark/README.md) | 821 assumptions from 657 questions on maternal health, SRH, cervical cancer and neonatal health, with veracity and assumption-type labels |

## Languages and authors

Each language set covers 40 weeks of pregnancy and was written and reviewed by first-language speakers. The authors are health and development professionals: medical doctors, midwives, medical licentiates, clinical officers, physiotherapists and development officers.

| Language | Files | Authors |
|---|---|---|
| English | `DawaMom_English_dataset.json`, `dawamom_english.jsonl` | Tafadzwa K Munzwa, Takunda G Mugwagwa, Farai V Mutanga |
| Shona | `DawaMom_Shona_dataset.json`, `dawamom_shona.jsonl` | Tinowimba Katsumbe, Tafadzwa Muchoza, Wisdom Mukoko, Charles Zhou |
| Ndebele | `DawaMom_isiNdebele_dataset.json`, `dawamom_isindebele.jsonl` | Zanele Dube, Vezilizwi Maphosa, Sibongikhosi Moyo, Talent Mujombi, Nobukhosi Ndlovu |
| Nyanja | `DawaMom_chiNyanja_dataset.json`, `dawamom_chinyanja.jsonl` | Charity S Phiri, Aaron Chiwala, Precious Milanzi |
| Tonga | `DawaMom_chiTonga_dataset.json`, `dawamom_chitonga.jsonl` | Angela S Chikambwe, Mercy Musonda, Judy Mweemba |
| Bemba | `DawaMom_Bemba_dataset.json`, `dawamom_bemba.jsonl` | Mumbi Chileshe, Audrine Chitalu |
| Lozi | `DawaMom_lozi_dataset.json`, `dawamom_lozi.jsonl` | Hilda M Lifumbo, Kamutumwa S Imanga |

English terms inside the local-language text were kept on purpose, because speakers code-switch.

## Benchmark

The [Zambezi NLU Benchmark](benchmark/README.md) pairs each question with an assumption it carries, a label for whether that assumption is true, and a label for the kind of assumption it is. It is written in plain patient-style English for the Zambian care context.

It is intended for evaluation only. Do not use it as training data, or results on it will no longer be meaningful.

| | |
|---|---|
| File | `benchmark/zambezi_nlu_benchmark.jsonl` |
| Size | 821 assumptions from 657 questions |
| Topics | Maternal health, sexual and reproductive health, cervical cancer, neonatal health |
| Language | English |
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

## Limitations

- **Scope.** The pregnancy information covers the 40 weeks of pregnancy only. It is not a complete maternal or SRH health reference.
- **Topic gaps.** Not every locally important topic is covered in every language. For example, malaria prevention, HIV testing and preeclampsia were not found in the Bemba set.
- **Parallel, not identical.** Each language set was written by its own authors, so content and wording differ between languages. The sets are not sentence-aligned translations.
- **Question-and-answer data.** The pregnancy information is structured prose, not question-and-answer pairs. Only the English benchmark is in question form.
- **Benchmark language.** The benchmark is English only and written for the Zambian care context.
- **Expert authorship is not model validation.** A model trained on this data can still produce incorrect or unsafe health information. Its outputs need their own clinical and native-speaker review.

## Related models

The pregnancy information was used to train Dawa Health's MedGemma maternal health adapters:

- [dawahealth/medgemma-maternal-lora](https://huggingface.co/dawahealth/medgemma-maternal-lora) (v1)
- [dawahealth/medgemma-maternal-lora-v2](https://huggingface.co/dawahealth/medgemma-maternal-lora-v2) (v2)

Those adapters were also trained on material that is not part of this dataset and is not open source: cervical cancer FAQs, question-and-answer pairs drawn from documents, a contraception question-and-answer set, and de-identified user conversations.

## Contributing

Corrections and additions are welcome, especially from first-language speakers and clinicians. Open an issue or pull request on this repository, or email developers@dawa-health.com. Only contribute material you have the right to share, and never include personal or patient information.

## Citation

Munzwa, T. K., et al. (2026). *Zambezi NLU: Multilingual Maternal & SRH Health Dataset* [Data set]. Dawa Health. CC BY 4.0.

```bibtex
@dataset{zambezi_nlu_2026,
  author    = {Munzwa, Tafadzwa K. and others},
  title     = {Zambezi NLU: Multilingual Maternal & SRH Health Dataset},
  year      = {2026},
  publisher = {Dawa Health},
  license   = {CC-BY-4.0},
  note      = {Multilingual maternal health dataset covering seven African languages}
}
```
