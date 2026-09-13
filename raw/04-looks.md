# 04 — The Looks

*The operating set. Ten looks each for Client day, Dinner, Casual day, Off duty and Holiday.*

**The Fifty Looks:** https://claude.ai/code/artifact/db4aac4a-7e6c-4db3-8c07-0efdab3d07c3
**Wardrobe Index:** https://claude.ai/code/artifact/5b413adc-319e-4f09-8bfc-c2314e366e59
**Recovery copy:** `04b-the-fifty-looks.html`

*Both regenerated 30 Aug 2026 against the corrected wardrobe. The pre-audit versions — looks at `3050c409…`, index at `601ff535…` — are superseded and should not be used.*

---

## Method

Only items `available` in `02-wardrobe.csv` and clean in `03-state.md`. **Every `ring_fence` respected.** Excluded: #45 and #52 (need work), #174 (damaged), #58 (retired), and the RETIRE-verdict items.

**Verified mechanically, zero violations:** the value step on every look · no mid-tone-only look · ring-fences honoured per mode · no TURNUP or TAILOR hem · `needs_base` items layered · `LAYER` items covered · the closure rule (no open layer over its own hue) · a jacket in every client and dinner look · no suit-locked trouser in a client look · no brown belt on black shoes · no belt in a holiday look.

**Two rules the generator applies that aren't in `00-rules.md` and should be:**

1. **A rank-2 base or mid is fine at a client day under a jacket** — it is not fine at the collar with nothing over it. Without this the warm-collar bench is unusable, because **every warm-at-the-collar piece owned is rank 2.** *That is itself the finding — derive the bench from `temp = WARM` on the `BASE` and `MID` rows and check the rank. The tobacco merino crew on the buy plan would be the first that isn't.*
2. **Holiday permits a light-tonal look** — all pieces L or M with at least one L, no dark required. This is the summer exception already in `00-rules.md`; it needed stating as a rule the generator could apply.

## Outstanding against the set

**#176 white pocket square — recorded 30 Aug 2026, after the fifty were generated.** The client-day mode rule in `00-rules.md` asks for a watch and a white pocket square, and no look in this file could meet it because the square wasn't in the CSV. **It is a constant, not a variable: it goes into every client look and every dinner look, and changes nothing else** — a folded square is too small to move a value step, and every look in both modes already has a jacket to carry it. No look is rebuilt.

**One place it earns a check rather than an assumption:** the looks led by #83 Sandro sand linen. White in a sand breast pocket is a near-miss in the same plane — the miniature of field rule 1. Look at it before those go to the try-on gate. **The artifact and the recovery copy still show the client and dinner cards without it; they need a regeneration, not an edit.**

## On each card

The garment swatches in recorded colour · the value strip (L/M/D) for the visible stack · every item by id, brand and colour · a one-line note on why the look works.

---

## Lock protocol

> **sense check on paper → try on → tick both → LOCKED**

A rejected look is replaced by the next-best candidate and goes through both gates again. **When all five modes are locked, daily styling becomes picking from this file.**

**This table is the record of record.** The gate boxes on the artifact are deliberately inert — a tick in a browser doesn't survive a change of device.

| Mode | Sense check | Tried on | Locked |
|---|---|---|---|
| Client day | ⬜ | ⬜ | ⬜ |
| Dinner | ⬜ | ⬜ | ⬜ |
| Casual day | ⬜ | ⬜ | ⬜ |
| Off duty | ⬜ | ⬜ | ⬜ |
| Holiday | ⬜ | ⬜ | ⬜ |

---

## What binds the generator

*Wardrobe findings, not styling choices. Each has a row in `05-buy.md`.*

1. **Client-day bottoms.** The binding constraint, and worse in winter — the light-value problem in `05-buy.md`.
2. **Warm at the collar.** A minority bench, and every piece in it is rank 2. It caps how many client looks can be warm at the collar, and forces the rest achromatic. *Derive the bench from `temp` and `layer`.*
3. **Office-register jackets are a shallow bench.** *Derive it from `category`, `formality_rank` and `season`.* #21 Adam Waite olive cord does real work in the client set here, having been out of rotation entirely.
4. **Socks are black only.** Every charcoal, navy and brown look breaks the sock rule.

## The one look that cannot be built

**DN10, black tie.** Dinner jackets are owned; **black dress trousers are not**, and neither is a bow tie. It is in the set marked INCOMPLETE, with navy trousers and a business shirt standing in, **because the gap is the finding.** Two purchases, neither expensive. *#176 covers the square that look also needs.*
