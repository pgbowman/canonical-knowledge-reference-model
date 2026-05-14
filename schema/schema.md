# Schema

Five node types, four edge types, common provenance properties. The full machine-readable definition is in `schema.json`.

## Node types

### `Passage`

A textual unit — a primary-source quotation.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | Stable identifier (e.g., `homer-iliad-1.1-7`) |
| `work` | object | yes | `{author, title, language}` |
| `reference` | string | yes | Canonical reference (e.g., `1.1-7`, `47.1-4`, `514a-517a`) |
| `label` | string | yes | Human-readable label |
| `original_text` | string | yes | Source-language text |
| `translation` | string | no | English translation |
| `translation_attribution` | string | no | Translator + year + public-domain note |
| `source_url` | string | no | Link to a public-domain edition |
| `key_terms` | array | no | Lemmatized key terms with parsing |

### `Source`

A secondary work — commentary, monograph, edition, handbook.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | Stable identifier (e.g., `leaf-1900`) |
| `author` | string | yes | |
| `title` | string | yes | |
| `year` | integer | yes | First-edition year |
| `publisher` | string | no | |
| `source_type` | string | yes | `commentary` / `monograph` / `handbook` / `translation` / `critical_edition` |
| `consensus` | string | no | `standard` / `influential` / `contested` / `fringe` |
| `public_domain` | boolean | no | |
| `url` | string | no | Link to public-domain copy if applicable |

### `Claim`

An assertion about a passage, carrying provenance.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | |
| `passage` | string | yes | Reference to a `Passage.id` |
| `statement` | string | yes | The claim, in plain prose |
| `assertor` | string | yes | Reference to an `Assertor.id` |
| `assertion_type` | string | yes | `primary` (assertor's own) or `reported` (relaying a source) |
| `research_status` | string | yes | `stub` / `draft` / `reviewed` / `verified` |
| `confidence` | number | no | 0.0 – 1.0 |
| `source` | string | no | Reference to a `Source.id` (required if `assertion_type='reported'`) |
| `source_location` | string | no | Page or ad-loc reference within the source |
| `notes` | string | no | |

### `Interpretation`

A community's reading of a passage at a specific period (a reception event).

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | |
| `passage` | string | yes | Reference to a `Passage.id` |
| `community` | string | yes | Identifier of the reading community |
| `period` | string | yes | Date range or period label |
| `medium` | string | no | `manuscript` / `print_edition` / `oral_performance` / `digital` / etc. |
| `function` | string | yes | What the community used the passage *for* (e.g., `moral_instruction`, `rhetorical_model`, `metaphysical_allegory`) |
| `reading` | string | yes | Prose description of the interpretation |
| `asserted_by` | string | yes | Reference to an `Assertor.id` |
| `assertion_type` | string | yes | `primary` / `reported` / `paraphrase` |
| `research_status` | string | yes | |
| `source` | string | no | Source supporting this interpretation, if any |
| `notes` | string | no | |

### `Assertor`

An entity that makes claims, with a source class.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | |
| `name` | string | yes | |
| `source_class` | string | yes | `credentialed_scholar` / `project_curator` / `ai_extraction` / `unvetted_contributor` |
| `credentials` | string | no | Affiliation or qualification |

**On source classes.** Source classes are not a hierarchy of correctness. They identify where a claim came from and how it should be handled in review. A credentialed scholar can still be wrong; an AI extraction can still be useful. The source class simply tells the workflow how much review, caution, and attribution a claim requires before it is used in generated output.

## Edge types

| Edge | From | To | Notes |
|---|---|---|---|
| `ABOUT` | `Claim` | `Passage` | The passage the claim is about |
| `ASSERTED_BY` | `Claim` or `Interpretation` | `Assertor` | Who made it |
| `SOURCED_BY` | `Claim` or `Interpretation` | `Source` | Which secondary work supports it |
| `OF` | `Interpretation` | `Passage` | The passage being interpreted |

The sample data files encode these relationships as foreign-key string references (`passage`, `assertor`, `source`, etc.) on each entity. A graph-database implementation would materialize them as edges; a relational implementation would use join tables. The schema doesn't dictate the storage model.

## Common conventions

- All IDs are kebab-case, ASCII-safe, and stable.
- `research_status` is the workflow gate: a claim moves through `stub → draft → reviewed → verified` as humans validate it.
- `assertion_type='primary'` means *the assertor's own judgment*. `'reported'` means *the assertor is relaying another scholar*. The distinction matters for evaluation: reported claims only need citation-checking; primary claims need substantive review.
- Source classes are categorical, not a quality ranking — they describe the origin and review status of a claim, not its correctness.
- **Verification caution.** No claim should be marked `research_status='verified'` unless the cited source has been checked directly and the location is exact. Claims marked `'reviewed'` should have been examined by a human reviewer but may still require fuller verification. Draft, extracted, or inferred claims should remain clearly marked until reviewed.
