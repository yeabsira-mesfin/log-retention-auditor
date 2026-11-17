"""Domain validation for catalog evidence envelopes."""

from evidence_catalog.validation import (
    ValidationError, boolean, fields, identifier, integer, text,
)

PROJECT = 'log-retention-auditor'


def validate_payload(payload):

    fields(payload, ("stream", "first", "last"))
    identifier(payload["stream"], "stream")
    integer(payload["first"], "first day")
    integer(payload["last"], "last day")
    if payload["first"] > payload["last"]:
        raise ValidationError("first day must not follow last day")


def example_payload():
    return {'stream': 'auth', 'first': 1, 'last': 30}
