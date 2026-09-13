# 02a — Schema & Method

*Companion to `02-wardrobe.csv`. Schema v3.*

**The CSV lives as a project doc, never as an upload — an upload cannot be edited in place.** If a CSV ever appears as a file again, it is a stale copy and the doc wins.

---

## The governing rule

> **A document may state a fact it owns, and may point at facts it doesn't. It may never restate them.**

| Owner | Owns |
|---|---|
| **`02-wardrobe.csv`** | What exists, and every attribute of it — including ring-fences and availability |
| **`03-state.md`** | State: clean, in wash, away, worn when |
| **`05-buy.md`** | What to buy, ranked, each entry naming the look it unblocks |
| **`00-rules.md`** | The rules |
| **`04-looks.md`** | The locked set |
| Everything else | Derived — a pointer, never a restatement |

**No typed counts anywhere.** Censuses, bench depths, record totals: derived from the CSV when asked, never written into prose. **A constraint is still worth stating — state it, then name the derivation** *("derive the bench from `temp` and `layer`")*, never the number and never the roster. A roster is a count with the receipts attached and goes stale the same way.

> **One exemption: `99-archive.md`.** Its numbers are dated evidence — what was true at the moment a lesson was learned — not live facts about the wardrobe, and re-deriving them would destroy the lesson rather than update it. The file carries its own guard: *never quote a number from this file.* **A sweep leaves it alone.**

---

## Columns — 32

**Identity** · `id` *(unique; gaps are deliberate)* · `category` · `subcategory` · `brand` · `pattern` · `formality` · `season`

`formality` is the human-readable register (Casual · Smart casual · Smart · Formal · Formal (evening) · Sport · Loungewear · Occasion · All · n/a); `formality_rank` is the number the logic uses.

### Colour — five decidable attributes, not one string

| Column | Values | Drives |
|---|---|---|
| `colour` | free text | **Display only. Never used by logic** |
| `hue` | black · charcoal · grey · navy · blue · olive · green · brown · tan · cream · white · rust · burgundy · purple · red · orange · silver · gold · n/a | Palette matching |
| `value` | **L · M · D** | **The one-light-one-dark rule. The most-used field** |
| `chroma` | NEUTRAL · MUTED · SATURATED | The no-loud-colour rule |
| `temp` | WARM · COOL · NEUTRAL | Warm-at-the-collar |
| `hex` | `#rrggbb` | Swatch rendering |

> ⚠️ **A slash means unresolved only when the garment is one colour and the string can't say which.** *"Dark grey / faded black"* on a solid trouser hides which family the thing belongs to; resolve it to one word before deriving anything, because taking the first half is how a run of items ended up in the wrong colour family.
>
> **A genuinely two-coloured object is not unresolved.** Tortoise sunglasses, a palm-print swim short, a striped tie, a colour-block trainer: both words are true, the object really is two colours, and `hue` carries the ground or the dominant one. Nothing needs deciding.
>
> **The test is the object, not the punctuation.** Read `pattern` and read the garment. If two names are competing to describe one ground colour, it fires; if they are naming two colours that are both there, it doesn't.

### Fabric & construction

| Column | Values | Drives |
|---|---|---|
| `fabric` | cotton · linen · wool · merino · lambswool · cashmere · knit · jersey · loopback · denim · corduroy · velvet · suede · leather · shearling · technical · silk · other · **UNKNOWN** | Warmth, formality, care |
| `texture` | **FLAT · TEXTURED · PILE** · **UNKNOWN** | **The black-at-the-face rule.** Black + FLAT is barred outside evening; black + PILE is permitted; a melange or marl earns the same exemption |

**`UNKNOWN` on both means not yet established — never write a value for something merely unexamined, and never `other`.** `other` is a fabric that has been identified and doesn't fit the list; `UNKNOWN` is a label that hasn't been read. The two must not collapse into each other, because only one of them is a job.

> ⚠️ **`texture = UNKNOWN` blocks the black-at-the-face rule, and only that rule.** It therefore bites on **`hue = black` alone**: a black row with UNKNOWN texture is ineligible at the collar until the label is read, because it may turn out to be FLAT. **Every other hue is unaffected** — charcoal, navy, olive and the rest are fine at the collar flat, so UNKNOWN texture costs them nothing.

### Layering & role

| Column | Values | Drives |
|---|---|---|
| `layer` | BASE · MID · OUTER · BOTTOM · SHOE · N/A | Slot assignment. **MID and BASE are the face garments — the ones that sit at the collar** |
| `needs_base` | Y · N | Knit outers require a tee beneath, never another knit |
| `formality_rank` | 1 loungewear → 6 black tie | Mode eligibility, shoe-to-bottom matching |
| `warmth` | 1–5 | Weather-driven recommendation |

**Overshirts sit at OUTER, not MID** — a garment worn open over something else competes with jackets, and a relaxed cut on one is correct rather than off-brief.

### Fit & proportion

| Column | Values | Drives |
|---|---|---|
| `fit_cut` | SKINNY · SLIM · REGULAR · RELAXED | The tailored-silhouette brief |
| `hem` | PLAIN · TURNUP · TAILOR · CHECK · **UNKNOWN** · OK · N/A | **No-turn-ups.** TURNUP and TAILOR are excluded from generated looks until altered. **UNKNOWN means not yet established — never write N/A for something merely unmeasured** |
| `fit` | free text | **Derived or reported, never asked as a judgement** |

### Grading, restriction & provenance

| Column | Values |
|---|---|
| `palette` | STRONG · OK · WEAK · FAIL · N/A |
| `silhouette` | OK · OFF-BRIEF · CHECK |
| **`ring_fence`** | **NONE · CASUAL · HOME · GYM · HOLIDAY-EVE · OCCASION · LAYER** |
| `provenance` | E · A · C · B · D |

**`ring_fence` — where an item may NOT go:**

| Value | Meaning |
|---|---|
| `NONE` | No restriction |
| `CASUAL` | Casual and weekend only — never office, never client-facing |
| `HOME` | Home and private only |
| `GYM` | Gym and sport only |
| `HOLIDAY-EVE` | Holiday evenings only |
| `OCCASION` | Specific occasions only |
| `LAYER` | Solo is fine casually; layer it where register matters |

**Check this column before building any outfit or packing list.** A rule that can't be read by the thing applying it isn't a rule. **And once it is a column, it is not also a paragraph** — prose repeating a ring-fence beside a rule that already says to read the column is redundant machinery that can drift. See `99-archive.md`.

### State & disposition

`condition` · `acquired` · `availability` *(available · incoming · retired)* · `verdict` *(KEEP · CHECK · TAILOR · RETIRE · BUY)* · `flag_notes` · `open_question`

**`availability` is disposition — does this garment exist and is it in the wardrobe.** It changes rarely. **Day-to-day state lives in `03-state.md`.** Both must pass: `retired` or `incoming` never enters an outfit; `available` can still be unavailable today because it's away or dirty.

**There is no per-item wear counter, by design.** Laundry runs weekly and is handled by someone else, so the wardrobe cannot observe its own wash state — a counter would drift out of sync and start recommending things that are in the basket. `03-state.md` holds the wash rule instead.

---

## Queued — agreed, not yet in the CSV

### `separates` — Y · N · blank

**Add on the next CSV pass, after the tailor edits in `03-state.md` are applied.** Bump this file's column count and the schema version when it lands.

| Value | Meaning |
|---|---|
| `Y` | Part of a set, but **works as an odd piece** — eligible for generated looks on its own |
| `N` | **Suit-locked.** Comes out with its set or not at all; never an odd-piece option |
| *blank* | Not a set piece. The column doesn't apply |

**Why:** the suit-lock is currently prose in `flag_notes`, so every look that touches a set piece depends on the generator reading a sentence and interpreting it correctly. That is the same failure mode `ring_fence` was created to end — *a rule that can't be read by the thing applying it isn't a rule.* One enum column makes it mechanical.

**Seeding, so no roster is needed here:** every row whose `flag_notes` says SUIT-LOCKED takes `N` · the row flagged as the exception that works as separates takes `Y` · everything not part of a set stays blank.

**Then strip the rule clause from `flag_notes`, and only that clause.** The eligibility sentence — *"NOT an odd-trouser option"* and its equivalents — becomes a restatement the moment the column exists, and the two can drift apart. **The pairing stays** — *"with 12"*, *"with 81"* — because it says which garments belong together, which the column does not carry and nothing else records.

**If the pairing ever needs to be mechanical too, it is a `set_with` column holding the partner `id` — not more prose.** Not queued; noted so the answer isn't re-litigated.

**Check on landing:** the suit-locked pieces drop out of odd-trouser selection, the summer exception survives it, and every partner id that was in `flag_notes` before the pass is still there after.

---

## Provenance

**Ranked. Higher beats lower, always, without discussion.**

| Rank | Code | Meaning |
|---|---|---|
| **1** | **E** | **In hand** — held and looked at in daylight, label read, tape used |
| 2 | **A** | Primary document — order email, brand product page |
| 3 | **C** | Stated from memory |
| 4 | **B** | Photograph only — never handled |
| — | **D** | Specification for a recommended purchase, not owned |

**The supersession rule:** whatever is established with the garment in hand is the truth, and overwrites everything else without being queried.

**E does not require a camera.** Colour needs daylight and thirty seconds.

**What breaks E:** confirming an auto-derived field without examining the thing. A guess promoted to *confirmed* is worse than a guess that admits it, because nothing will flag it again.

**Three ways this file has actually been wrong, all still live risks:** derivation from a two-part colour string · photo reads under artificial light *(a single-look photo read is provenance B and never overwrites anything)* · inference from a brand catalogue *(what a brand's range contains is not evidence about a specific object)*.

---

## Where the logic lives

**Attributes drive the RULES:** contrast (`value`) · warm-at-collar (`temp`) · black-at-face (`hue` + `texture`) · layering (`layer`, `needs_base`) · shoe-to-bottom (`formality_rank`, `category`) · turn-up exclusion (`hem`) · restriction (`ring_fence`).

**Curated pools drive the SELECTION.** A purely attribute-driven pool was tested and produced worse looks. **Attributes for rules, curation for pools.**

---

## Maintenance

- **"bought [item]"** → new row, `provenance = C` (or **A** from an order email), all attributes populated before the row is accepted
- **In-hand beats everything** → `provenance = E`, overwrites without a query
- **Correcting a colour** → update `colour` **and** re-derive `hue`, `value`, `chroma`, `temp`, `hex`. Never one without the others
- **"retire [item]"** → `availability = retired`. **Never delete a row**
- **Unknown is not N/A, and never empty.** If a field is merely unmeasured, write UNKNOWN — or `TBC` for a brand — so it stays visible. An empty cell reads as *nothing to do*; UNKNOWN reads as *a job*
- **Nuance goes in `flag_notes`**, never into an enum column — and **never a count**. `flag_notes` is prose inside the CSV, so the no-typed-counts rule applies to it exactly as it does to a document
- **After any change here, regenerate the looks and republish the artifacts**

---

## Known weaknesses

| Weakness | Severity | Status |
|---|---|---|
| **`fabric` is auto-derived and demonstrably wrong** | **HIGH** | **OPEN — the largest weakness.** Almost no fabrics were read off a label; two material errors were found by eye alone. It drives `texture`, which drives the black-at-the-face rule. **The fix is reading care labels, not photographing them** |
| **Suit-lock is prose, not a column** | Medium | **Queued above** — `separates`, next CSV pass |
| `fit` empty on most rows | Medium | Needs the worn shots |
| `hem` UNKNOWN across the outerwear | Medium | The one outstanding capture job |
| Garment chest measurements unreliable | Medium | Two jackets read narrower than their own waists |
| #171, #172, #173 graded on a single unverified statement | Medium | **#173 especially** — the maker lists it in grey *and* charcoal, and the grade swings STRONG → FAIL on which it is |
| `brand = TBC` on a tail of rows | Low | Mostly ties — derive the roster from the CSV |
| Tie records are provenance B | Low | **Accepted permanently.** Low stakes, out of scope |
