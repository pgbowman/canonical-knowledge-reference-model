# Example: An Ambiguity Map

This example shows how the schema represents legitimate scholarly disagreement structurally, rather than picking one reading or averaging them.

## Question

> What is the philosophical function of Plato's cave allegory in *Republic* VII?

## What the system does *not* do

It does not return a single confident answer. The cave allegory has been read in radically different ways by different communities at different periods, and each reading is defensible within its own framework. A system that picks one reading as the canonical answer is misleading — not because any of the readings is wrong, but because the question itself doesn't have a single answer.

## What the system does

It returns an ambiguity map: parallel readings, each with its community, period, function, and source.

## Retrieval

The system pulls the passage (`plato-republic-514a-517a`) and all interpretations attached to it. In the sample data, that's three:

| ID | Community | Period | Function |
|---|---|---|---|
| `interp-plato-cave-neoplatonic` | Neoplatonic | 3c–6c CE | metaphysical_allegory |
| `interp-plato-cave-christian-medieval` | Christian medieval | 4c–14c CE | soul_pilgrimage |
| `interp-plato-cave-modern-epistemology` | Modern epistemology | 19c–present | theory_of_knowledge |

Plus the primary claim, sourced to Jowett 1871, that the allegory represents *"the soul's progress from sensory perception to intellectual understanding."* That claim is itself one reading in the broader landscape — the canonical Anglophone 19th-century reception.

## Answer

> Plato's cave allegory has been read in at least three substantially different ways by different communities, each of which is internally coherent and well-attested.
>
> **The Neoplatonic reading (3c–6c CE)** treats the cave as a metaphysical allegory of the soul's descent into the sensible world and its return to the One. The ascent is not (or not only) educational; it is metaphysical, a structural ascent through the levels of being. Plotinus and the later Neoplatonists provide the canonical exposition of this reading.
>
> **The Christian medieval reading (4c–14c CE)** recodes the cave as the fallen world, the prisoners as souls in sin, the ascent as conversion, and the sun as the divine. The allegory becomes a model of the soul's pilgrimage. Augustine and later medieval authors provide the canonical Christian recodings; the function shifts from metaphysical itinerary to spiritual conversion.
>
> **The modern epistemological reading (19c–present)** treats the cave as a theory of knowledge: the prisoners' shadows as everyday opinion, the released prisoner's progress as the disciplined acquisition of knowledge, the sun as the form of the Good. The metaphysical and religious recodings are bracketed. This is the reading most common in contemporary Anglophone philosophy textbooks; Jowett's 1871 introduction (*Dialogues of Plato*, vol. III) is an early representative.
>
> Some of these readings compete; others coexist because they answer different questions. They look most directly in competition when a reader imposes the question *"what did Plato actually mean?"* on a text that three reception communities have read for three different purposes. The schema represents all three rather than averaging them, letting both kinds of relation — competition and coexistence — remain visible.

## What this example demonstrates

1. **Disagreement is data.** The fact that three communities have read the cave allegory in three different ways is itself useful information about the text. A system that flattens it produces a worse answer than one that surfaces it.

2. **Communities have functions.** Each reading is attached to a community and a function (metaphysical_allegory, soul_pilgrimage, theory_of_knowledge). The function makes it clear *what kind of question* each reading is answering, which is what makes the three readings non-competitive.

3. **The schema makes the ambiguity queryable.** A more sophisticated query — *"for every passage in the corpus, return the count of distinct community readings"* — would produce a map of where in the corpus disagreement is densest. Those passages are typically the most analytically interesting.
