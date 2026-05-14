# Evaluation Rubric

A scoring rubric for AI-generated outputs against the schema. Four axes, each scored 0–3.

The rubric is designed for outputs that purport to be expert-grounded answers, not for casual generation. A creative writing prompt about Greek mythology doesn't need to pass this rubric. A research-assistant answer does.

## Axis 1: Provenance integrity

| Score | Criterion |
|---|---|
| 0 | The output makes claims with no source attribution. |
| 1 | Some claims are sourced; others are presented as unsourced authoritative statements. |
| 2 | Every substantive claim has a source. Citations may be vague (author only, no work). |
| 3 | Every substantive claim has a specific, locatable source citation (work, page or ad-loc reference). |

## Axis 2: Source-class awareness

| Score | Criterion |
|---|---|
| 0 | The output treats scholarly claims, project-curated claims, AI extractions, and unvetted contributions as equivalent. |
| 1 | Source classes are present somewhere, but the prose does not meaningfully distinguish them. |
| 2 | Source classes affect the answer: scholarly or reviewed claims carry more weight, while AI-extracted or unvetted claims are flagged. |
| 3 | Source-class-aware reasoning is explicit: the output distinguishes reviewed scholarship, curator judgment, AI extraction, and unvetted material when explaining confidence or uncertainty. |

## Axis 3: Ambiguity preservation

| Score | Criterion |
|---|---|
| 0 | The output flattens scholarly disagreement into a single confident position. |
| 1 | Disagreement is mentioned in passing but not represented structurally. |
| 2 | Major disagreement is named, with at least one alternative reading explicitly attributed. |
| 3 | All significant readings are named with their communities, periods, and sources. The reader can see *who* believes *what* and *when*. |

## Axis 4: Hard-stop adherence

Hard stops are limits the schema imposes on what each source type permits. For example:

- A literary self-presentation (e.g., a Senecan letter, an apologetic autobiography) does **not** permit biographical inference about the author's actual life.
- A literary fragment quoted only through later citation does **not** permit confident reconstruction of the original context.
- A staged philosophical dialogue does **not** permit treating any speaker's view as the author's own without external corroboration.

| Score | Criterion |
|---|---|
| 0 | The output asserts a claim the source type explicitly does not permit. |
| 1 | The output makes a partial inference that strains a hard stop, without acknowledging it. |
| 2 | The output respects the hard stop and notes the limit in passing. |
| 3 | The output explicitly cites the hard stop as a reason for limiting its claim. |

## Composite scoring

The four axes are not weighted equally. **Hard-stop adherence is a gate**: any score below 2 on Axis 4 fails the output regardless of the other scores, because the schema's whole purpose is to prevent that class of error.

For the other three axes, a sensible threshold is:

- **Total ≥ 7** out of 9 (after passing the hard-stop gate) → accept
- **Total 5–6** → return with feedback for revision
- **Total < 5** → reject and re-generate

A worked example of the rubric applied to a hypothetical AI output is in `examples/evaluation-example.md`.

## What the rubric is for

The rubric isn't an evaluation framework for AI in general. It's specifically for AI outputs that are *meant to read as expert-grounded*. Its job is to make sure such outputs are auditable: that a reader can verify each claim, see who disagrees, and understand what limits the underlying sources impose.

Two patterns the rubric is specifically designed to catch:

- **Confident hallucination**: outputs that read as authoritative but cite nothing. Axis 1 catches these.
- **False consensus**: outputs that smooth over real scholarly disagreement to look more decisive. Axis 3 catches these.

These are the two failure modes that make AI outputs in expert domains worse than the underlying sources.
