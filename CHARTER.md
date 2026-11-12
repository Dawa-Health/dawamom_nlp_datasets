# Zambezi NLU Project Charter

This charter describes what the Zambezi NLU project is for, what it covers, who is responsible for it and how decisions are made. It applies to everything in this repository.

## 1. Mission

Zambezi NLU exists to make accurate maternal and sexual and reproductive health (SRH) language data openly available for African languages, so that researchers and developers can build and evaluate health NLP systems that work for the women who need them.

## 2. Goals

- Publish health content written and reviewed by first-language speakers who are also health or development professionals.
- Cover languages that are poorly served by existing NLP resources, starting with English, Shona, Ndebele, Nyanja, Tonga, Bemba and Lozi.
- Provide a benchmark that lets anyone test a system on health questions in the Zambian care context.
- Keep the data open, documented and easy to load, with known problems stated plainly.

## 3. Scope

**In scope**

- Week-by-week pregnancy information in the seven languages (`json/`, `jsonl/`).
- The English cervical cancer FAQ.
- The Zambezi NLU Benchmark (`benchmark/`).
- Documentation, validation tests and scripts that support the data.
- New languages, new maternal and SRH topics, and corrections to existing content.

**Out of scope**

- Personal, patient or user data of any kind, including de-identified conversations.
- Model weights and training code. Dawa Health's models are published separately.
- Medical advice. The dataset is a research resource and is not a clinical reference.
- Content that Dawa Health or the contributor does not have the right to share.

## 4. Principles

- **Clinical accuracy first.** Health content is reviewed by a qualified health professional before it is merged.
- **Language authority.** Content in a language is written or reviewed by a first-language speaker. Code-switching with English is kept where speakers use it.
- **Openness.** The data and its history are public. Problems are recorded in the README, not hidden.
- **Privacy.** Nothing that could identify a person is accepted.
- **Evaluation integrity.** The benchmark is for evaluation only and is not to be used as training data.

## 5. Roles and responsibilities

| Role | Responsibilities |
|---|---|
| **Project steward** (Dawa Health) | Owns the repository, holds the copyright, sets direction and appoints maintainers. |
| **Maintainers** | Review and merge pull requests, cut releases, keep documentation and tests current, and enforce this charter and the Code of Conduct. |
| **Clinical reviewers** | Check health content for accuracy and safety. At least one must approve any change to health content. |
| **Language reviewers** | Check content in their first language for correctness and natural wording. At least one must approve any change to that language's files. |
| **Contributors** | Anyone who opens an issue or pull request. Contributors follow the contributing guide and the Code of Conduct. |

Current maintainers and reviewers:

| Name | Role | Area |
|---|---|---|
| Tariro F Munzwa | Maintainer | Repository and releases |
| Tafadzwa K Munzwa, M.D. | Clinical reviewer | Health content |
| Kudzai Mwedzi | Language reviewer | Local-language content |

The authors of each language set are listed in the [README](README.md).

## 6. Decision making

- **Day-to-day changes** are decided by pull request review. A change is merged when it has the approvals in section 7 and the automated checks pass.
- **Maintainers aim for consensus.** If maintainers cannot agree, the project steward decides.
- **Larger changes** need an issue for discussion first, open for at least seven days. These include adding a language or topic, changing the data format, changing the license, or changing this charter.
- **Clinical disagreements** are settled by the clinical reviewers, with reference to current national and WHO guidance. Where guidance differs between countries, the content says which it follows.

## 7. How changes are made

1. Open an issue describing the problem or proposal, unless the change is a small correction.
2. Create a branch and make the change. Nobody commits directly to `main`.
3. Open a pull request using the template.
4. Automated checks run on the pull request.
5. Review and approval:
   - any change: one maintainer;
   - health content: one maintainer and one clinical reviewer;
   - content in a local language: one maintainer and one language reviewer for that language.
6. A maintainer merges the pull request.

Details are in [CONTRIBUTING.md](CONTRIBUTING.md).

## 8. Quality

- Every data file is covered by automated validation tests that run on each pull request. They check that files parse, that record counts and fields are as documented, and that the JSONL files match their JSON sources.
- Known issues are listed in the README until they are fixed.
- Corrections from first-language speakers and clinicians are treated as a priority.

## 9. Releases

- Releases use version numbers of the form `MAJOR.MINOR.PATCH`.
  - **MAJOR**: a change to the data format, or a change to the benchmark that makes results not comparable with earlier versions.
  - **MINOR**: new languages, topics or records.
  - **PATCH**: corrections to existing content or documentation.
- Each release has a tag and an entry in the changelog.
- Benchmark results should always state the dataset version they were run on.

## 10. License and contributions

The project is licensed under the [Apache License, Version 2.0](LICENSE). Copyright is held by Dawa Health. Contributions are accepted under the same license, and contributors confirm they have the right to share what they submit.

## 11. Code of Conduct

Everyone taking part in the project follows the [Code of Conduct](CODE_OF_CONDUCT.md). Reports go to developers@dawa-health.com.

## 12. Funding and independence

The project has been supported by Grand Challenges Canada, UNICEF Femtech Ventures and TogetHER for Health. Funders do not decide what content is merged; that is decided through the process in this charter.

## 13. Changes to this charter

Changes to this charter are proposed by pull request, discussed in an issue for at least seven days, and approved by the project steward.

## Contact

developers@dawa-health.com
