# Canonical Knowledge Systems: A Reference Model for AI Workflows

A small, public, reference repository demonstrating how structured knowledge, source tracking, and explicit handling of disagreement can support more source-aware, reviewable AI-assisted content generation.

The sample domain is public-domain classical Greek and Latin literature, but the pattern may be relevant to other domains where AI-generated answers benefit from source tracking, reviewability, and explicit handling of disagreement.

Here, "canonical" does not mean forcing a single correct interpretation. It means maintaining a stable, reviewable structure for sources, claims, interpretations, and evaluation.

## What this is

A reference artifact — a polished sketch of a way of organizing AI knowledge workflows. Five core ideas, demonstrated with a small dataset and a few worked examples.

## What this isn't

- A product or production system
- A SaaS service
- A working backend or API
- A finished agent framework
- A complete knowledge base

The point is the *shape* of the thing, not a deployment.

## Design problem

AI systems working in interpretive or expert domains tend to flatten distinctions a domain specialist wouldn't flatten. An AI summary of a contested interpretive tradition may collapse opposing readings into a single confident position. An AI gloss on a classical passage assumes the most-cited interpretation is the only one. The default behavior of any retrieval-and-generation system that treats its knowledge domain as a flat surface is to look authoritative while hiding ambiguity.

This reference model treats four things as first-class structural concerns rather than as post-hoc annotations:

1. **Provenance** — every claim records who asserted it, on what authority, and from which source.
2. **Source-backed retrieval** — generated outputs cite the specific source that grounds each claim.
3. **Ambiguity preservation** — when sources disagree, the disagreement is stored, not averaged away.
4. **Source-class-aware evaluation** — every claim carries a source class (credentialed scholar / project curator / AI extraction / unvetted contributor), and evaluation respects the distinction rather than flattening it into a single pool.

A fifth idea sits underneath those: **disagreement is data**. In any interpretive domain, the points where experts disagree are often the most analytically valuable. A system that hides that disagreement, or treats it as noise to be averaged out, is producing worse output than it appears to be.

## Structure

```
README.md
docs/
  architecture.md            — the four-layer model and how it composes
  workflow-examples.md       — three example workflows in narrative form
  evaluation-rubric.md       — scoring criteria for AI outputs against the schema
schema/
  schema.md                  — human-readable schema description
  schema.json                — JSON Schema for validating the sample data
sample-data/
  passages.json              — three public-domain classical passages
  sources.json               — three public-domain secondary works (commentaries, translations)
  claims.json                — claims about each passage, with provenance
  interpretations.json       — community readings of each passage (reception events)
examples/
  source-backed-answer.md    — a worked Q&A with full provenance trail
  ambiguity-map.md           — how the system surfaces scholarly disagreement
  evaluation-example.md      — applying the rubric to a hypothetical AI output
diagrams/
  architecture.mmd           — Mermaid diagram of the four layers
validate.py                  — small script that checks the sample data against the schema
LICENSE
```

## Why classical texts as the demo

Three practical reasons:

- The material is based on ancient texts and older scholarly materials, reducing IP friction for a public demonstration repo.
- Centuries of commentary provide rich verification data, with disagreement well-documented.
- The texts are short, which makes the worked examples concrete and readable.

The schema in this repo is not tied to classical content. The same `Passage` / `Source` / `Claim` / `Interpretation` shape may be adaptable to other source-heavy domains, especially where multiple expert readings or review workflows matter.

## How to read it

If you have ten minutes: start with `docs/architecture.md`, then look at one worked example in `examples/`.

If you have an hour: read the architecture doc, then all three worked examples, then skim the schema. A companion essay may be added later.

If you want to validate the sample data against the schema: run `python validate.py` after `pip install jsonschema`. The script checks every sample data file against its definition in `schema/schema.json` and exits non-zero on the first failure.

## License

This repository is released under the MIT License.

The sample data is based on public-domain classical texts and older scholarly materials. Before reusing quoted translations or commentary excerpts, verify copyright status in your jurisdiction.

## Verification caution

No claim should be marked `research_status='verified'` unless the cited source has been checked directly and the location is exact. Claims marked `'reviewed'` should have been examined by a human reviewer but may still require fuller verification. Draft, extracted, or inferred claims should remain clearly marked until reviewed.

## Independence

This is an independent personal-research artifact. It is not affiliated with, sponsored by, or representative of the author's employer, past or present. It uses public-domain classical material as a neutral demonstration domain.
