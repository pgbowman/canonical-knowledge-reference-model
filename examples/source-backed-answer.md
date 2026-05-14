# Example: A Source-Backed Answer

This example shows how the schema supports a question whose answer requires both primary-source evidence and an explicit account of what the primary source *does not* say.

## Question

> Where does the detail about Achilles's heel come from?

## Retrieval

The system retrieves all data attached to passages where Achilles appears in the corpus. In the sample data, that's `homer-iliad-1-1-7` (the proem).

Attached to that passage:

- **One claim** stating that the *Iliad's* text does not mention Achilles's heel (`claim-iliad-1-no-heel`).
- **One claim** stating that the proem announces μῆνις, not invulnerability, as the principal subject (`claim-iliad-1-menis`, sourced to Leaf 1900).
- **Three interpretations**: an archaic Greek heroic reading (heroic paradigm), a later mythographic reading (bodily vulnerability — the heel), and a modern popular reading (shorthand idiom).

## Answer

> The detail about Achilles's heel does **not** appear in the *Iliad* itself. The proem and Achilles's later speeches in the poem define his heroic identity through μῆνις (wrath) and τιμή (honor), with mortality as the implicit vulnerability — Walter Leaf's standard 1900 commentary frames the proem as programmatic in this sense (Leaf 1900, ad loc. 1.1).
>
> The heel motif enters the tradition through the later mythographers — Pseudo-Apollodorus, *Bibliotheca* 3.13.6, and Statius, *Achilleid* 1.269–270 — who rationalize Achilles's eventual death by attributing it to a localized bodily defect produced when his mother's attempt to make him immortal was interrupted. This is a reception event, not a Homeric one: the detail appears centuries after the *Iliad*.
>
> In modern popular use, "Achilles heel" has become a detached idiom for fatal weakness, often used without reference to Homer or even to Achilles as a character. This is a third reception step, in which the difference between the Iliadic Achilles and the later mythographic Achilles is flattened into a single popular image.

## Sources cited in the answer

| Citation | Type | Source class |
|---|---|---|
| *Iliad* 1.1–7 | Primary text (in A.T. Murray's 1924 public-domain translation) | n/a |
| Leaf, *Commentary on the Iliad* (1900), ad loc. 1.1 | Secondary commentary | credentialed_scholar |
| Pseudo-Apollodorus, *Bibliotheca* 3.13.6 | Primary text (later antiquity) | n/a |
| Statius, *Achilleid* 1.269–270 | Primary text (later antiquity) | n/a |
| Project-curator paraphrase of scholarly consensus on the post-Homeric origin of the heel motif | Curator paraphrase | project_curator |

## What this example demonstrates

Three things:

1. **The system can answer a negative question structurally.** "The *Iliad* does not say X" is a real claim, with its own provenance (you have to read the *Iliad* in full to make it), and the schema accommodates it as a primary claim by the project author.

2. **The system distinguishes the layers of reception.** The Iliadic Achilles, the mythographic Achilles, and the popular-idiom "Achilles heel" are three different things, attached to the same passage but representing different communities at different periods. The answer reflects all three rather than collapsing them.

3. **The source classes are visible.** The Leaf citation is classified as credentialed scholarship; the paraphrase of consensus on the post-Homeric heel is classified as curator judgment; an AI extraction, if it had contributed, would be marked separately and flagged for review. A reader can see at a glance where each piece of the answer comes from.
