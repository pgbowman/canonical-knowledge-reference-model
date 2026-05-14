# Architecture

The reference model is built around four interlocking layers. Each layer is small. The composition is the point.

## 1. Schema layer

The schema defines what *kinds* of things exist in the knowledge system and how they relate. The model uses five node types:

| Node | What it represents |
|---|---|
| `Passage` | A textual unit — a primary-source quotation with reference, language, original text, translation. |
| `Source` | A secondary work — commentary, monograph, edition, handbook. |
| `Claim` | An assertion about a passage, carrying provenance. |
| `Interpretation` | A community's reading of a passage at a specific period (a reception event). |
| `Assertor` | An entity that makes claims, with a source class. |

And four edge types:

| Edge | Meaning |
|---|---|
| `(Claim)-[:ABOUT]->(Passage)` | What the claim is about |
| `(Claim)-[:ASSERTED_BY]->(Assertor)` | Who made the claim |
| `(Claim)-[:SOURCED_BY]->(Source)` | Which secondary work supports the claim |
| `(Interpretation)-[:OF]->(Passage)` | Which passage a given community reading interprets |

That's the entire shape. The full definition is in `schema/schema.md` (human-readable) and `schema/schema.json` (machine-readable).

## 2. Provenance layer

Every node and edge in the graph carries provenance metadata. The fields that matter:

- `asserted_by` — the assertor's identifier
- `assertion_type` — `primary` (the assertor's own judgment) or `reported` (the assertor relaying another expert)
- `research_status` — `stub` / `draft` / `reviewed` / `verified`
- `confidence` — optional numeric confidence value
- `source` — for reported claims, the secondary work being relayed
- `source_location` — page number, paragraph, or ad-loc reference

This is the layer that makes every output traceable to its origin.

Two distinctions do most of the work:

- **Primary vs reported**: an AI extraction that says *"Aeneid 1.1 echoes Iliad 1.1"* (its own judgment) is verified differently from an extraction that says *"Conington (1863, ad loc. 1.1) argues Aeneid 1.1 echoes Iliad 1.1"* (relaying a scholar). The first needs full review; the second only needs a citation check.
- **Source class**: a claim from a credentialed scholar, a project curator, an AI extraction, or an unvetted contributor should be handled differently. The evaluation layer preserves these distinctions rather than flattening them into a single pool of claims.

## 3. Retrieval layer

A query against the schema returns not just the answer but the provenance trail. A question like *"What did Achilles's heel mean to ancient Greek audiences?"* returns:

- The passages where the heel detail appears (which, in the *Iliad*, it does not)
- The claims about those passages, with source citations
- The interpretations attached to each passage, by community and period
- An ambiguity map when claims or interpretations disagree

Three concrete worked examples live in the `examples/` directory.

## 4. Evaluation layer

A scoring rubric for AI outputs against the schema. It scores on four axes:

| Axis | What it asks |
|---|---|
| Provenance integrity | Does every claim trace back to a source? |
| Source-class awareness | Does the output distinguish reviewed scholarship, curator judgment, AI extraction, and unvetted material when explaining confidence or uncertainty? |
| Ambiguity preservation | When sources disagree, does the output report the disagreement? |
| Hard-stop adherence | Does the output respect source-type limits (e.g., not asserting biographical fact from literary self-presentation)? |

The full rubric is in `docs/evaluation-rubric.md`.

## How the layers compose

```
Question
   │
   ▼
Retrieval over Schema + Provenance layers
   │
   ▼
Candidate answer (with cited claims, by community, by source class)
   │
   ▼
Evaluation against Rubric
   │
   ▼
Final output (with confidence, sources, and surfaced disagreement)
```

A diagram is in `diagrams/architecture.mmd`.

## What the model deliberately does *not* do

- It does not produce a single canonical answer. A passage like Plato's cave allegory has many legitimate community readings; the system holds them in parallel rather than picking one.
- It does not flatten AI extractions into the same class as reviewed scholarly claims. An LLM extraction stays clearly marked as such until a human reviewer promotes or revises it.
- It does not invent provenance. A claim with no source is `assertion_type='primary'` and is treated accordingly.
- It does not optimize for retrieval speed. The whole architecture is about *what* gets retrieved and *with what trail*; performance is downstream of getting the shape right.
