# Example: Applying the Evaluation Rubric

This example takes a hypothetical AI-generated answer and scores it against the rubric in `docs/evaluation-rubric.md`.

## The question

> Did Seneca treat his slaves well?

## The hypothetical AI output

> Yes. In Epistle 47, Seneca writes that he lives on familiar terms with his slaves, treating them as human beings, tent-mates, and humble friends rather than as property. This was an unusually progressive view for his time, and it reflects Seneca's broader Stoic commitment to human equality. Seneca's personal practice was therefore notably more humane than that of his Roman contemporaries.

This output reads confident and well-written. The rubric will show why it is wrong on multiple axes.

## Scoring

### Axis 1: Provenance integrity — Score: 1

The output makes four factual claims:

1. *Seneca wrote in Epistle 47 that he lived on familiar terms with his slaves.* (Verifiable from the passage; effectively cited.)
2. *This was an unusually progressive view for his time.* (No source.)
3. *It reflects Seneca's broader Stoic commitment to human equality.* (No source.)
4. *Seneca's personal practice was therefore notably more humane than that of his Roman contemporaries.* (No source — and this is the load-bearing claim.)

One out of four claims has a citation. Score: 1 (some claims sourced; others presented as authoritative without support).

### Axis 2: Source-class awareness — Score: 0

The output treats all claims as equally weighted and equally confident. The schema would distinguish between the credentialed-scholar / textual claim (what Seneca *wrote*) and the curator-or-extraction inferences (what his practice actually was, how he compared to contemporaries, what his philosophical commitments motivated). The output makes no such distinction.

### Axis 3: Ambiguity preservation — Score: 0

The output flattens scholarly disagreement entirely. Three reception communities (medieval monastic, Renaissance humanist, modern Stoic revival) read Ep. 47 in three different ways and for three different purposes (`interp-seneca-47-*` in the sample data). The output picks one — the modern self-help reading — and presents it as the answer.

### Axis 4: Hard-stop adherence — Score: 0 → **FAIL**

This is the gate axis, and the output fails it.

A claim in the sample data (`claim-seneca-47-not-biographical`) explicitly states:

> Seneca's self-presentation in this letter — implying that he himself treats his slaves well — is literary self-fashioning, not autobiographical evidence. The letters are published philosophical correspondence, not private documents.

The AI output asserts exactly the inference the hard stop prohibits: it treats Seneca's literary self-presentation as evidence about his actual personal practice, then escalates further to a comparative claim about his Roman contemporaries.

## Verdict

**Reject.** The hard-stop failure on Axis 4 alone disqualifies the output, regardless of the other scores. The output looks plausible and reads as authoritative; it commits exactly the class of error the schema is built to prevent.

## A revised answer that would score well

> Seneca's Epistle 47 presents the author as someone who lives on familiar terms with his slaves and rejects the language of slavery in favor of *homines*, *contubernales*, and *amici*. The letter's argumentative move is a triple refutation of the proposition "they are slaves" with progressively more intimate counter-categories.
>
> Whether Seneca *actually* practiced what the letter advocates is a separate question, and the letter itself does not provide evidence for it. The Epistles are published philosophical correspondence, not private documents; the self-presentation is part of the rhetorical work. (Gummere's 1917 Loeb introduction is one place this distinction is made; the project author's notes treat it as a hard-stop case in the schema.)
>
> Three different reception communities have read Ep. 47 differently: medieval monastic readers as moral instruction on the humane treatment of dependents, Renaissance humanists as a model of Latin prose and Stoic ethics, and the modern Stoic revival as portable self-help wisdom. Each of these readings has its own function; none of them resolves the question of Seneca's personal practice, because that question requires evidence the letter does not contain.

This revised output would score 3 / 3 / 3 / 3 on the rubric. It cites a source for each substantive claim, distinguishes credentialed-scholar textual evidence from curator-level inference, surfaces the three reception readings rather than picking one, and explicitly invokes the hard stop on biographical inference from literary self-presentation.

## What this example demonstrates

1. **The rubric catches what the schema is designed to catch.** The original output's failure mode — confident authoritative inference from a source type that doesn't permit it — is exactly the failure mode the hard-stop axis is built around.

2. **Looking right is not being right.** The original output is grammatically clean, well-organized, and rhetorically confident. Without the rubric, it would pass most casual review. The rubric is what makes the difference visible.

3. **Revision is structured.** Each axis the original failed on suggests a specific revision. Axis 1 → cite each claim. Axis 3 → surface the three readings. Axis 4 → respect the hard stop. The revised answer follows the rubric directly.
