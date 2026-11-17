# Log Retention Auditor

An analyst needs to find precisely which days of evidence are missing for each log stream, even when archival exports overlap.

## Required decision command

`python retention.py gaps INPUT.json` reads a raw JSON object as shown under input in examples/. For each requested stream, intersect the records for that stream with the closed audit window [start,end]. Each record has a stream and inclusive first and last day. Merge coverage and return an object mapping each requested stream to the sorted list of maximal missing intervals, each a two-integer array. Include fully covered streams with [] and ignore unrelated streams. Reject inverted input intervals and windows.

Print the JSON decision to stdout. For invalid input return nonzero and write a readable diagnostic to stderr. Use exact JSON types, including rejecting booleans where integers are required. Input ordering must not affect the result. Preserve the inventory CLI.

## Reporting and integration work

Add CSV ingestion with columns stream,first,last, a multi-stream summary with missing-day counts and longest gap, and parity checks against JSON. Use interval arithmetic that handles billion-day ranges without enumerating days. Test adjacent coverage, clipped intervals, empty files and multiple streams. Document the reporting CLI, its input schema, one working example, and failure behavior. Exercise both success and failure paths through subprocess tests. Keep input files read-only. Use deterministic output and temporary paths for tests.

## Estimated implementation session

Allow 40 minutes for input modeling, 90 for the decision algorithm, 65 for the reporting feature, 50 for validation and edge cases, 60 for integration and regression tests, and 30 for documentation and reviewer evidence. Total estimate: 5 hours 35 minutes. Record actual time worked.
