# 03 — State & Outfit Log

*Owns state only: what is clean, what is in the wash, what is away, what was worn when.*

**Default: everything `available` in `02-wardrobe.csv` is wearable, subject to its `ring_fence`.** Only exceptions are listed here.

---

## The wash rule

**Wash day is Thursday, weekly, always.** Laundry is done by someone else, so nothing here simulates a wash cycle. Four lines cover it:

1. **Everything resets on Thursday.** Whatever went in the basket during the week is clean again.
2. **Base layers are single-wear between wash days** — tees, tanks, socks, underwear. **Not a rolling seven days.** The week runs Thursday to Thursday: the same tee can be worn on a Wednesday and again on the Friday, because a wash day fell between them. Inside one Thursday-to-Thursday block, don't put the same one in two outfits.
3. **Anything else, Pavlos says so.** "The olive shirt's dirty" is the only input needed; it goes in the list below until Thursday.
4. **A return is not a wash day.** They are separate events and rarely fall on the same day. **On the return date, everything that came home goes to the dirty list — except the categories that don't get washed.** `Outerwear`, `Footwear`, `Accessories` and `Luggage` go straight back to available; everything else waits for the Thursday. *Derive the split from `category`* — stating the categories rather than the items is what makes it hold for the next trip without being rewritten.

*The no-counter decision is deliberate. A per-item wear counter needs logging almost every day to stay true, and a counter that's two-thirds accurate is worse than none — it recommends things that are in the basket, and then the recommendations stop being trusted.*

## Dirty — unavailable until wash day

**Home from Bournemouth, 2 Sep 2026. In the basket until Thursday 3 Sep:**

#5 · #8 · #10 · #38 · #43 · #47 · #49 · #66 · #69 · #85 · #95 · #97 · #102 · #106 · #117

## Travel

*Holds the away list, and — once a trip has actually started — that trip's packing map. Nothing else.*

*(no trip in progress)*

> **Clear this section on the return date.** An away list that outlives the trip silently removes a third of the wardrobe from every recommendation. If the date has passed and the section is still here, clear it and say so.

**While an away block is open, the away list has two readings and the answer must name the one it used.** Where he is, the suitcase is the wardrobe and the away items are the *only* items — that is the reading for any day type that can happen on the trip. In London, the away items are the ones missing. **The location is inferred from the day type, not asked for.**

**When the requested day type cannot occur at the current location — a client day, an office day or a dinner while he is away — answer for the return date and say so on the first line. The answer is not logged.** See the log boundary below.

### When a packing map enters this document

**A packing map enters here only when the trip starts, and only as part of this section.** Until departure a map is a proposal — it lives in the answer, not in state. Most maps never become trips at all: a request to pack for somewhere is a question, not a booking, and building one commits nothing.

**A packing map never enters the outfit log**, in any form and at any stage. The log is the record of days that happened; a map is a plan for days that have not. Filing a plan there corrupts the 14-day rule and the single-wear rule with days that were never worn — the same failure the away-block rule above exists to prevent.

**On departure:** the map goes under this section with the trip, and the packed items become the away list.

**On the return date, three things happen and they are not the same event:** this section clears · what was actually worn is written to the log · what came home is split between dirty and available by rule 4 of the wash rule. **The wash that follows is the next Thursday, which is usually a later day** — the gap between the two is real and the dirty list has to survive it.

---

## The outfit log

**Worn days only.** One row per day that happened, written after the fact.

| Date | Day type | Items | Notes |
|---|---|---|---|
| 17 Aug 2026 | Office | #169 Frame light olive · #70 Axel Arigato Clean 90 | Bottom half fixed by Pavlos |
| 26 Aug 2026 | Travel (holiday) | #145 Folk olive chore · #106 ARKET cream tee · #49 Frame beige · #70 Axel Arigato · #129 brown belt · #159 elk strap · #160 chain | Mirror-checked twice. #33 olive tee rejected under the open chore jacket — **produced field rule 1 in `00-rules.md`**. Sleeves cuffed at the forearm |

> **The boundary. An entry is written on "picked N", for a day actually worn, and is dated that day.** Never forward-dated, never a plan, never a packing map.
>
> **A planned outfit is a chat answer, not state.** Recommending a look, pre-planning a week and answering for a return date all produce outfits that nothing has yet worn. None of them touch this table. A row for a day that didn't happen makes the 14-day rule and the single-wear rule fire against garments that never left the wardrobe — which is not a harmless surplus, it is a false exclusion that silently narrows every later answer.

---

## Rules for recommending

1. **Only items `available` in the CSV and clean here**, respecting each item's `ring_fence`.
2. **One clearly light piece and one clearly dark**, or full tonal. Never mid-tones head to toe.
3. **The proportion doctrine applies to every outfit.**
4. **Nothing worn in the last 14 days for the same audience.** Vary at least one major piece.
5. **No weather lookup for a London day** — season and judgement are enough. Look it up when travelling, or when Pavlos raises it.
6. **Name items by id, brand, colour and garment — "#145 Folk olive chore jacket", never "#145".** *Set 2 Sep 2026: the id alone is a lookup key, not a name, and an answer he has to decode is an answer he can't act on. The id stays because it is the only unambiguous handle; it is never the whole label.*
7. **Lead with the recommended pick.** Two or three options, short.
8. **Apply the two field rules in `00-rules.md`.**
9. **State which side of the away list the answer is built from** — see the Travel section.

**Preferred source: the locked set in `04-looks.md`.** Generating from scratch is for novel occasions only.

---

## Constraints to work around

*Each one that costs money has a row in `05-buy.md`.*

- **The smart-casual jacket bench is shallow, and thins further by season.** *Derive it from `category`, `formality_rank` and `season`.* **#21 Adam Waite olive cord is made to measure, correct length and the best colour family, and is out of rotation — work it harder.** The biggest structural gap.
- **Client-day trousers are the bottleneck, not the tops.** The eligible bench is shallow, thins further outside summer, and **every trouser in it is light-value** — so the dark half of law 1 can only come from the top, which forces the collar achromatic and compounds the warm-at-the-collar ceiling. *Derive the bench from `season`, `formality_rank` and `ring_fence`; the suit-lock and its one exception are in `flag_notes`.*
- **Warm at the collar is the minority.** *Derive the bench from `temp = WARM` on the `BASE` and `MID` rows.* It caps how many client looks can be warm at the collar.
- **Tobacco above the waist is zero.** Every brown item owned is a shoe, a belt, a jacket, a scarf or a strap — against a man whose second-best colour is tobacco.
- **Black tie cannot be dressed.** Dinner jackets yes; no black dress trousers, no bow tie.
- **Black socks only.** Every charcoal, navy and brown look breaks the sock rule.
- **The blue jeans are damaged** (#174, excluded until assessed).
- **No packable rain shell.** The only waterproof things owned are the backpack and the case.
- **Short-sleeve shirts are effectively absent for summer client wear** — #9 can't be buttoned, #10 is holiday-only.
- **Swim shorts are one deep.**
- **No tennis shoes.** #16 is a running shoe — no lateral support, an injury risk on court.

---

## Open items

- **#173 shade** — the maker lists this roll neck in grey *and* charcoal. Graded STRONG on charcoal. **If it is mid-grey it drops to FAIL at the collar and the lead dinner look needs rebuilding.** Check in daylight.
- **#172** — bottle green, graded OK provisionally. **Also the forest-green shade test from `00-rules.md`.** Wear once, decide.
- **#101 vs #68** — same ribbed tank in S and XS. Wear both; if S is right, #68 retires.
- **#24** — colour is provenance C. Confirm navy in daylight.
- **`fit` and `hem` are UNKNOWN across the outerwear.** *Derive the roster from `hem = UNKNOWN`* — it shrinks by itself as the shots are taken. One session closes it — full-length mirror, phone at chest height, arms down, **do not tilt the phone**, same spot each time, head to knees, wearing the trousers and shoes you'd normally pair with it.
- **#171, #172, #173** — year acquired unknown. Not blocking.

---

## Batched CSV pass — tailor trip, week of 2 Sep 2026

| Item | Edit on completion |
|---|---|
| **#45** NN07 tan chinos | Remove turn-ups, let out the waist → `hem` → OK, `verdict` → KEEP, lift the exclusion |
| **#52** Frame washed black jeans | Under-crotch repair → `condition` → Good, `verdict` → KEEP, lift the exclusion |
| **#174** 7FAM dark blue jeans | Assess the hole — repairable or retire? If not, a replacement goes on the buy plan |
| **#129 / #49** | Take the two garment measurements — they settle the contested body waist |
| **Part B** | The six measurements in `01-pavlos.md §C` |

## Still incoming

**#77** Cavaier black jewellery stack.
