from __future__ import annotations

from product_telemetry_check.models import Rule

PROJECT_NAME = 'product-telemetry-check'
SUMMARY = 'Validate product telemetry specs for event name, properties, and privacy review.'
SAMPLE_RISK = 'event name missing properties none privacy unchecked'
SAMPLE_CLEAN = 'event name checkout_completed properties plan,region privacy reviewed'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='missing-event-name',
        severity='high',
        pattern='event name\\s+(missing|none|unknown)',
        message='event name missing',
        recommendation='define stable event name',
    ),
    Rule(
        code='missing-properties',
        severity='medium',
        pattern='properties\\s+(none|missing|unknown)',
        message='properties missing',
        recommendation='declare event properties',
    ),
    Rule(
        code='privacy-unchecked',
        severity='low',
        pattern='privacy\\s+unchecked',
        message='privacy review missing',
        recommendation='review privacy impact',
    ),
)
