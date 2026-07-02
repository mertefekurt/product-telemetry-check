# product-telemetry-check

> Validate product telemetry specs for event name, properties, and privacy review.

## CLI contract Overview

Validate product telemetry specs for event name, properties, and privacy review. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 33

Accepts telemetry spec. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 33

```bash
python -m pip install -e ".[dev]"
product-telemetry-check examples/sample.txt
product-telemetry-check examples/sample.txt --json --fail-on medium
python -m product_telemetry_check --help
```

## Rule Surface 33

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-event-name` | high | event name missing |
| `missing-properties` | medium | properties missing |
| `privacy-unchecked` | low | privacy review missing |

## Validation Notes 33

```bash
ruff check .
pytest
python -m product_telemetry_check --help
```

Example risky input:

```text
event name missing properties none privacy unchecked
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
