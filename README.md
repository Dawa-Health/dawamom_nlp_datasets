# Zambezi NLU: Multilingual Maternal & SRH Health Dataset

**Zambezi NLU** is a multilingual maternal and SRH health Natural Language Understanding (NLU) dataset developed by Dawa Health to support research, development and evaluation of NLP systems for African languages.

It covers seven languages: English, Shona, Ndebele, Nyanja, Tonga, Bemba and Lozi.

The dataset provides structured pregnancy and maternal health information to support multilingual conversational AI, question answering, semantic understanding and digital maternal health assistants. It also includes an English cervical cancer FAQ of 100 question-and-answer pairs, and an English benchmark for testing whether a system recognises the assumptions built into health questions. The benchmark covers maternal health, sexual and reproductive health, cervical cancer and neonatal health.

| | |
|---|---|
| **Dataset format** | JSON and JSONL |
| **License** | [Apache License 2.0](LICENSE) |
| **Copyright** | © 2026 Dawa Health |
| **Funding** | Grand Challenges Canada, UNICEF Femtech Ventures, and TogetHER for Health |
| **Contact** | developers@dawa-health.com |

## Contents

| Part | Location | Description |
|---|---|---|
| Pregnancy information (JSON) | `json/` | Week-by-week pregnancy information, one structured file per language |
| Pregnancy information (JSONL) | `dawamom_<language>.jsonl` | The same content with one record per week (40 lines), one file per language |
| Combined file | `combined_multilingual.jsonl` | All seven languages in a single JSONL file with one shared schema (280 lines) |
| Cervical cancer FAQ | [`jsonl/cervical_cancer-faq.jsonl`](jsonl/cervical_cancer-faq.jsonl) | 100 English question-and-answer pairs on cervical cancer: 50 for the general public and 50 for health professionals |
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

## Cervical cancer FAQ

[`jsonl/cervical_cancer-faq.jsonl`](jsonl/cervical_cancer-faq.jsonl) holds 100 question-and-answer pairs on cervical cancer, written in English for the Zambian care context. It covers causes and HPV, vaccination, screening (Pap smear, VIA, HPV testing), diagnosis and staging, treatment, and prevention programmes.

| | |
|---|---|
| File | `jsonl/cervical_cancer-faq.jsonl` |
| Size | 100 question-and-answer pairs |
| Audiences | `layman` (ids 1 to 50), `medical_professional` (ids 51 to 100) |
| Language | English |

Unlike the benchmark, the FAQ can be used as training data.

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

**Combined JSONL.** `combined_multilingual.jsonl` has one record per language per week (7 × 40 = 280 lines), ordered English, Bemba, Tonga, Nyanja, Lozi, Shona, Ndebele. Every record has the same fields, with English field names:

```json
{
  "language": "English",
  "week": 12,
  "baby_development": {
    "length": "3.15 inches (8 centimeters) long [cite: 419]",
    "weight": "1 ounce (about 28 grams) [cite: 419]",
    "summary": "The eyes move closer together ..."
  },
  "maternal_changes": {
    "body_changes": "Your healthcare provider can now feel your uterus ...",
    "tips": "Many women benefit from Kegel exercises ...",
    "plan": "Now is a great time to look at your diet. ..."
  }
}
```

A field is `null` where the source has no value, for example length and weight in the first weeks.

**Per-language JSONL.** Each `dawamom_<language>.jsonl` file has one record per week (40 lines). A record is the weekly entry from that language's JSON file, unchanged, so it keeps the source's own field names and nesting. The English, Bemba and Tonga files use the English field names shown above. The other four use field names in their own language:

| Shared name | Shona | Ndebele | Nyanja | Lozi |
|---|---|---|---|---|
| `week` | `vhiki` | `iviki` | `sabata` | `sunda` |
| `baby_development` | `kukura_kwemwana` | `ukukhula_komntwana` | `kukula_kwa_mwana` | `kuhula_kwa_mbututu` |
| `length` | `urefu` | `ubude` | `utali` | `butelele` |
| `weight` | `uremu` | `isisindo` | `kulemera` / `ulemera` | `buima` |
| `summary` | `pfupiso` | `isifingqo` | `pfupiso` | `pfupiso` |
| `maternal_changes` | `shanduko_kuna_amai` | `untshintsho_kuma` | `zosintha_kwa_mayi` | `linchincheho_kwa_mahe` |
| `body_changes` | `kushanduka_kwemuviri` | `untshintsho_emzimbeni` | `zosintha_za_thupi` | `linchincheho_za_mubili` |
| `tips` | `zvingabatsire` | `izixwayiso` | `malangizo` | `mikwa_yakumbweshafaza` |
| `plan` | `zvekuronga_pavhiki` | `okuhlelelwe_iviki` | `zakukonzekera` | `zakuitukiseza_sunda_ye` |

Three per-language files also differ in nesting; see Limitations. Use the combined file if you need one schema across languages.

The JSONL records do not carry the dataset name, authors or license. Those apply to every record and are given in this README and in the JSON files.

Text fields contain source markers of the form `[cite: N]`, which point to passages in the authors' source documents. Strip them before training or display if they are not wanted.

**Cervical cancer FAQ.** One record per question-and-answer pair:

```json
{
  "id": 1,
  "audience": "layman",
  "question": "What is cervical cancer?",
  "answer": "Cervical cancer is a disease of the cervix, the lower part of the uterus that connects to the vagina. ..."
}
```

`audience` is `layman` for questions a member of the public might ask and `medical_professional` for clinical and programme questions.

## Loading

```python
import json

# One language
with open("dawamom_english.jsonl", encoding="utf-8") as f:
    records = [json.loads(line) for line in f]

# All languages, then filter
with open("combined_multilingual.jsonl", encoding="utf-8") as f:
    combined = [json.loads(line) for line in f]

shona = [r for r in combined if r["language"] == "Shona"]

# Cervical cancer FAQ, public-facing questions only
with open("jsonl/cervical_cancer-faq.jsonl", encoding="utf-8") as f:
    faq = [json.loads(line) for line in f]

public_faq = [r for r in faq if r["audience"] == "layman"]
```

## Intended use

This dataset is for research and for developing and evaluating NLP systems. It is not medical advice and should not be used to make decisions about an individual's care.

## Limitations

- **Scope.** The pregnancy information covers the 40 weeks of pregnancy only. It is not a complete maternal or SRH health reference.
- **Topic gaps.** Not every locally important topic is covered in every language. For example, malaria prevention, HIV testing and preeclampsia were not found in the Bemba set.
- **Parallel, not identical.** Each language set was written by its own authors, so content and wording differ between languages. The sets are not sentence-aligned translations, and some figures differ between languages for the same week.
- **Question-and-answer data.** The pregnancy information is structured prose, not question-and-answer pairs. Only the cervical cancer FAQ and the benchmark are in question form, and both are English only.
- **Cervical cancer FAQ.** The answers are short summaries. Figures and guideline references in them, such as incidence statistics and screening intervals, reflect the sources available when they were written and may be out of date. Check them against current national guidelines before relying on them.
- **Benchmark language.** The benchmark is English only and written for the Zambian care context.
- **Expert authorship is not model validation.** A model trained on this data can still produce incorrect or unsafe health information. Its outputs need their own clinical and native-speaker review.

### Known issues in the current files

The JSONL files reproduce the source text exactly, so the following are present in both the JSON and JSONL files. The combined file fixes the structural differences but not the content.

- **Lozi: text in other languages.** Some fields in weeks 30, 32, 33, 36 and 38 are in Ndebele, and the maternal fields for week 37 are in Nyanja. In the combined file these records are still labelled `Lozi`.
- **Lozi: nesting and values.** From week 13 the body changes, tips and plan fields sit inside the baby development object instead of a separate maternal changes object. Week 17 has a weight ("0.5kgs") in the length field, and the week 14 weight ("0.5kgs") is too high.
- **Tonga: values.** The week 23 baby summary is a placeholder ("Not provided in the document for this week."). The weights for weeks 17 ("11kg") and 22 ("4kg") are too high, and several lengths have no unit.
- **Nyanja: field name.** The baby's weight is `kulemera` in weeks 1 to 10 and `ulemera` in weeks 11 to 40.
- **Ndebele: nesting.** Tips and plan sit at the top level of each weekly entry, not inside the maternal changes object.
- **Formatting.** Length and weight are free text and are not in a consistent unit or style across languages. A few fractions appear as garbled characters (Bemba, weeks 31 to 35) or as math markup (Tonga).

## Related models

The pregnancy information was used to train Dawa Health's MedGemma maternal health adapters:

- [dawahealth/medgemma-maternal-lora](https://huggingface.co/dawahealth/medgemma-maternal-lora) (v1)
- [dawahealth/medgemma-maternal-lora-v2](https://huggingface.co/dawahealth/medgemma-maternal-lora-v2) (v2)

Those adapters were also trained on cervical cancer FAQs, and on material that is not part of this dataset and is not open source: question-and-answer pairs drawn from documents, a contraception question-and-answer set, and de-identified user conversations.

## License

Copyright 2026 Dawa Health.

The dataset, the benchmark and any code in this repository are licensed under the [Apache License, Version 2.0](LICENSE). You may use, modify and redistribute them, including commercially, provided you keep the copyright and license notices and state any changes you make.

## Contributing

Corrections and additions are welcome, especially from first-language speakers and clinicians. Open an issue or pull request on this repository, or email developers@dawa-health.com. Contributions are accepted under the same Apache 2.0 license. Only contribute material you have the right to share, and never include personal or patient information.

## Citation

Munzwa, T. K., et al. (2026). *Zambezi NLU: Multilingual Maternal & SRH Health Dataset* [Data set]. Dawa Health. Apache License 2.0.

```bibtex
@dataset{zambezi_nlu_2026,
  author    = {Munzwa, Tafadzwa K. and others},
  title     = {Zambezi NLU: Multilingual Maternal & SRH Health Dataset},
  year      = {2026},
  publisher = {Dawa Health},
  license   = {Apache-2.0},
  note      = {Multilingual maternal health dataset covering seven African languages}
}
```
