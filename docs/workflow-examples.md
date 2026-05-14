# Workflow Examples

Three workflows the schema is designed to support. Each appears in worked form in the `examples/` directory.

## 1. Source-backed answer

The most common workflow. A question comes in; the system returns an answer with the specific sources that ground each claim.

**Question:** *Where does the detail about Achilles's heel come from?*

**Process:**

1. Retrieve all passages where "Achilles" appears in the corpus
2. Filter to those mentioning vulnerability or the heel motif
3. Return claims about each, with source citations, ordered by:
   - Primary-source claims first (passages whose own text says it)
   - Reported claims next, with their secondary-source citations
   - Interpretations (community readings) last, by period

**Output shape:**

> The detail does not appear in the *Iliad* itself: the proem and Achilles's later speeches define his heroic identity through μῆνις (wrath) and τιμή (honor), with mortality as the implicit vulnerability. The heel motif enters the tradition through later mythographers (Pseudo-Apollodorus, *Bibliotheca* 3.13.6; Statius, *Achilleid* 1.269–270). The shift from "Achilles as mortal hero" to "Achilles as bodily invulnerable except in the heel" is a reception event, not a Homeric one.
>
> **Sources:** *Iliad* 1.1–7 (primary), Leaf, *Commentary on the Iliad* (1900, ad loc.), the mythographic tradition as preserved in Pseudo-Apollodorus and Statius.

A full version is in `examples/source-backed-answer.md`.

## 2. Ambiguity map

When a question has multiple legitimate scholarly readings, the system returns all of them with their respective communities, periods, and sources rather than averaging them into one.

**Question:** *What is the philosophical function of Plato's cave allegory?*

**Process:**

1. Retrieve the passage (*Republic* 514a–517a)
2. Retrieve all interpretations attached to it
3. Group by community / period / function
4. Return the parallel readings, each with its provenance

**Output shape:** a table with rows like *"Neoplatonic — metaphysical_allegory — the cave as the sensible world, the ascent as the soul's return to the One"*, *"Christian medieval — soul_pilgrimage — the cave as the fallen world, the ascent as conversion"*, *"Modern epistemology — theory_of_knowledge — the cave as everyday belief, the ascent as the disciplined acquisition of knowledge"* — each with its source citation.

The point of the ambiguity map is that the system reports *which* reading belongs to *which* community, rather than presenting one as the default. The Christian medieval reading is real; so is the modern epistemological one; some readings coexist because they answer different questions, while others genuinely compete — the schema lets both kinds of relation remain visible.

A full version is in `examples/ambiguity-map.md`.

## 3. Evaluation pass

After an AI generates an output, an evaluation pass scores it against the rubric. Each scored axis can route the output:

- High score on all axes → publish or accept
- Low score on provenance integrity → reject and re-prompt requiring source citation
- Low score on ambiguity preservation → reject and re-prompt requiring multi-reading output
- Low score on source-class awareness → reject and re-prompt requiring explicit source-class markers
- Low score on hard-stop adherence → reject hard (the output asserted something the schema says is not assertable from this source type)

The interesting case is **systematic low scores on a single axis**: that's a sign the prompt or the source corpus has a structural problem the schema can help diagnose.

A full version is in `examples/evaluation-example.md`.
