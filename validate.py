"""Validate the sample data files against schema/schema.json.

Run:
    pip install jsonschema
    python validate.py

Exits 0 on success, non-zero on first validation failure.
"""
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).parent
schema = json.loads((ROOT / "schema" / "schema.json").read_text())
defs = schema["$defs"]

CHECKS = [
    ("sample-data/passages.json",        "Passage"),
    ("sample-data/sources.json",         "Source"),
    ("sample-data/claims.json",          "Claim"),
    ("sample-data/interpretations.json", "Interpretation"),
    ("sample-data/assertors.json",       "Assertor"),
]

for rel_path, type_name in CHECKS:
    items = json.loads((ROOT / rel_path).read_text())
    for item in items:
        jsonschema.validate(item, defs[type_name])
    print(f"  {rel_path}: {len(items)} items pass {type_name} schema")

print("\nAll sample data validates against schema.")
