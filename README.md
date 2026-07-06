# Product Telemetry Check

> A small command-line review pass for product analytics.

![Product Telemetry Check cover](assets/readme-cover.svg)

Validate product telemetry specs for event name, properties, and privacy review. This repo keeps the work close to the terminal: clear input, predictable output, and no service to babysit.

## Signals in plain English

- `missing-event-name` (high): event name missing. Fix: define stable event name.
- `missing-properties` (medium): properties missing. Fix: declare event properties.
- `privacy-unchecked` (low): privacy review missing. Fix: review privacy impact.

## Input and report

The reader accepts text, JSON, JSONL, or CSV. The default report is readable in a terminal or pull request; `--json` keeps the same findings available to automation.

## Demo

```bash
git clone https://github.com/mertefekurt/product-telemetry-check.git
cd product-telemetry-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
product-telemetry-check examples/sample.txt
product-telemetry-check examples/sample.txt --json
```

## Sanity checks

```bash
ruff check .
pytest
python -m product_telemetry_check --help
```
