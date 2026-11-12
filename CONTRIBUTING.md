# Contributing to Zambezi NLU

Thank you for helping to improve Zambezi NLU. Corrections and additions are welcome, especially from first-language speakers and clinicians.

By taking part you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md). How the project is run is described in the [project charter](CHARTER.md).

## Ways to contribute

- **Report a problem.** A wrong fact, an unsafe statement, a mistranslation, text in the wrong language, a formatting error.
- **Correct existing content.** Fix a value, a sentence or a field.
- **Add content.** A new language, a new topic, or more records for an existing one.
- **Improve the project.** Documentation, validation tests, scripts.

You do not need to write code to contribute. If you are not comfortable with Git, open an issue describing the correction, or email developers@dawa-health.com, and a maintainer will make the change and credit you.

## Rules for all contributions

- **No personal or patient information.** Never include names, contact details, case details or conversations from real people, even if de-identified.
- **Only share what you have the right to share.** Do not copy text from books, websites, guidelines or other datasets unless their license allows it. Say where information came from.
- **Health content must be accurate and safe.** Base it on current national or WHO guidance, and say which in the pull request.
- **Local-language content must be written or checked by a first-language speaker.** Do not submit unreviewed machine translation.
- **Do not train on the benchmark.** Do not copy benchmark questions into the training data files.

## Reporting a problem

Open an issue and include:

- the file, language and week or record id;
- what is wrong;
- what it should say, if you know;
- a source, for clinical corrections.

For anything involving personal information that has been published by mistake, do not open a public issue. Email developers@dawa-health.com.

## Making a change

Nobody commits directly to `main`. All changes go through a pull request.

1. **Open an issue first** for anything larger than a small correction, so it can be discussed before you do the work. Adding a language or topic, or changing the data format, always needs an issue.

2. **Fork the repository and create a branch.** Name it after the change:

   ```bash
   git checkout -b fix/tonga-week-17-weight
   git checkout -b add/kaonde-pregnancy-weeks
   git checkout -b docs/loading-example
   ```

3. **Make the change.** See "Editing the data" below.

4. **Run the checks** on your machine:

   ```bash
   pip install pytest
   python -m pytest
   ```

5. **Commit** with a short message that says what changed and where:

   ```
   Fix Tonga week 17 baby weight (11kg -> 0.11 kg)
   ```

6. **Open a pull request** against `main` and fill in the template. Link the issue it resolves.

7. **Respond to review.** Push further commits to the same branch. A maintainer merges the pull request once it is approved and the checks pass.

## Editing the data

- **The JSON files in `json/` are the source.** Make content changes there first.
- **Keep the JSONL files in step.** Update the matching record in the per-language JSONL file and in the combined file in the same pull request. The tests fail if they differ from the JSON source.
- **Keep the structure.** Do not rename, add, remove or move fields unless the pull request is specifically about the format and has an agreed issue.
- **One record per line** in JSONL files, UTF-8, no trailing commas, no blank lines.
- **Use `null` for a missing value.** Do not write placeholder text such as "Not provided".
- **Write lengths and weights with a number and a unit**, for example `"16 cm"` or `"0.16 kg"`.
- **Leave existing `[cite: N]` markers alone.** Do not add new ones.
- **Keep changes small.** One language or one kind of fix per pull request is easier to review.

### Adding a language or topic

Open an issue first. The proposal should name the authors and the first-language reviewer, and say what guidance the content is based on. A new language set should cover all 40 weeks and use the same fields as the existing sets. Add the authors to the README.

### Changing the benchmark

Changes to benchmark records change results, so they need an issue and are released as a new version. See the [benchmark README](benchmark/README.md).

## Review and approval

| Change | Approvals needed |
|---|---|
| Documentation, tests, scripts | One maintainer |
| Health content | One maintainer and one clinical reviewer |
| Content in a local language | One maintainer and one language reviewer for that language |

Reviewers check that the content is accurate and safe, reads naturally in its language, matches the documented format and contains no personal information. Maintainers aim to give a first response within seven days.

## Automated checks

Every pull request runs the validation tests automatically with GitHub Actions. A pull request cannot be merged until they pass. The checks confirm that:

- every JSON and JSONL file parses;
- each language has weeks 1 to 40 exactly once, and record counts match the README;
- records have the documented fields;
- the JSONL files match the JSON sources.

If a check fails, open the "Checks" tab on the pull request to see which test failed and why, fix it, and push again. The same tests run locally with `python -m pytest`.

## Releases

Maintainers make releases. Version numbers follow the scheme in the [charter](CHARTER.md): MAJOR for format or benchmark-breaking changes, MINOR for new content, PATCH for corrections. Each release is tagged in Git and described in `CHANGELOG.md`. If your change should be mentioned in the changelog, add a line under "Unreleased" in your pull request.

## Credit

Contributors are credited in the changelog. Authors of new language sets are listed in the README.

## License

The project is licensed under the [Apache License, Version 2.0](LICENSE). By submitting a contribution you agree that it is licensed under the same terms, and you confirm that you have the right to submit it.

## Questions

Open an issue, or email developers@dawa-health.com.
