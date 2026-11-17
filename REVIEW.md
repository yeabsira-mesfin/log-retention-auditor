# Task description

An analyst needs to find precisely which days of evidence are missing for each log stream, even when archival exports overlap. The existing Python application inventories records. Implement `python retention.py gaps INPUT.json` as specified in ASSIGNMENT.md. Add CSV ingestion with columns stream,first,last, a multi-stream summary with missing-day counts and longest gap, and parity checks against JSON. Use interval arithmetic that handles billion-day ranges without enumerating days. Test adjacent coverage, clipped intervals, empty files and multiple streams.

## How to judge completion

Run `python -m unittest discover -s tests -v` and `python acceptance.py` from the repository root. All existing tests, new tests and 72 decision cases should pass. Inspect retention.py, acceptance.py, tests/, README.md and any new implementation modules. Exercise the documented reporting command with a fresh synthetic example, reverse the input records, and compare the outputs. Feed invalid types and verify a nonzero exit, a stderr diagnostic and unchanged input. Check the reporting feature independently of the example matrix.

## Other notes for reviewers

Use synthetic data and temporary files. The expected values belong only to the acceptance runner. Check the algorithm on unseen inputs and record the actual commands and results.

## Final questionnaire

Copy the new live compare problem ID from the platform. Enter actual active hours (minutes divided by 60). Primary language: Python. Task type: feature implementation and regression testing. Source: a new MIT-licensed starter prepared with Codex. Use the sections above for task description, how to judge completion and reviewer notes. Record actual outcome, completion evidence, changed files, commands, turn count, flag count and observed flag categories. Include exact quotes or turn references when explaining a flag. Leave run-specific fields open until the session ends.
