# v2 shadow report

Turn 14278, 2026-11-25 07:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,741, prestige 3,719 (599 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 94 | 0 | 12 | 0 | 0 | sell 23, sell @ 3.58 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 546 | 0 | 18 | buy 64, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), but the home ask 29.60 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~35 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **cured meat**: home ask 29.60 is above our ceiling 29.00 and last turn bought 3 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 59.1 coin per prestige at mansion, vs 70.6 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 97 over real use lately; planning 549, not 646

## Prestige spending, cheapest coin per prestige first

123 turns left: prestige gained now converts 46.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.3 | 51.3 | needs a arena (build cost 31,410); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.9 | 55.0 | needs a arena (build cost 31,410); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.1 | 59.1 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.1 | 59.1 | thin at home: pies |
| maintain 1 | park | 0.5 | 59.1 | 59.1 | running |
| jousting 3 | arena | 230 | 57.4 | 59.2 | needs a arena (build cost 31,410); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 61.0 | 61.0 |  |
| hold banquet 4 (pies) | mansion | 18 | 62.8 | 62.8 | thin at home: hop beer, stockfish, pies |
| hold banquet 5 | mansion | 22 | 64.4 | 64.4 | thin at home: pies, hop beer, stockfish, sculptures |
| jousting 2 | arena | 210 | 62.9 | 64.8 | needs a arena (build cost 31,410); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 66.4 | 66.4 | thin at home: hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 66.5 | 66.5 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 15 @ 5.85, cured meat buy 3 @ 27.0; crew 0.1; est +20 a turn
- **Flax Wyrm** on Caillechâtel: cured meat buy 3 @ 23.8, pasties buy 3 @ 14.9; crew 0.1; est +17 a turn; stock: pasties 3 @ 14.9 (keep 14)
- best towns now: Orlesailles +84, Heilegg +83, Bordetes +79, Großmühle +60, Friedwerp +54
- Orlesailles would trade: cured meat buy 3 @ 24.2, pasties buy 10 @ 9.6; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~126 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.50 (63/turn) | bread 181 (2.98->4.39), charcoal 19 (2.35->5.65), beer 15 (3.88->6.74), wine 15 (6.77->9.5) | cloth 3 (11.34->13.2), cured meat 3 (27.93->29.6), garments 2 (29.61->30.6), fleece 7 (9.08->9.21) | +455 |
| Heilegg | 826 | 0.29 | 0.50 (63/turn) | wrought iron 26 (17.54->27.55), dyed cloth 9 (19.95->27.36), garments 10 (29.8->32.49), beer 15 (3.88->5.7) | cured meat 3 (24.36->29.6), thread 9 (5.57->6.05), tin ingots 3 (35.07->35.91), honey 1 (11.03->11.69) | +430 |
| Brunnham | 1281 | 0.59 | 0.30 (38/turn) | garments 10 (29.8->34.01), nets 6 (35.8->39.33), dyed cloth 9 (19.95->21.85), rope 1 (83->84.55) | sculptures 1 (2478->2736), cloth 21 (12.29->13.2), cured meat 3 (26.67->29.6), tin ingots 3 (34.65->35.91) | +316 |
| Nürnnieder | 520 | 0.17 | 0.20 (25/turn) | leather 8 (29.82->32.3), limestone 1 (24.78->42.75), tools 14 (7.14->8.07), cloth 1 (12->12.92) | sculptures 1 (2478->2736), cured meat 3 (26.88->29.6), fleece 7 (8.51->9.21), thread 7 (5.41->6.05) | +306 |
| Blanans | 297 | 0.10 | 0.10 (13/turn) | nets 1 (35.8->37.24) | sculptures 1 (2478->2736), beer 11 (3.04->3.9), cloth 6 (11.87->13.2), medicine 1 (151.2->157.7) | +280 |

**Best:** Grandgues at about +455 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 22 @ min 3.78 | makes 19.3, uses 4.2, holds 94 (keeps 0): sells the surplus + 7/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 2 @ 87.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.95 | goal planner: sells 2 a turn at 0.95, keeps 219 (no one offered it) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 49) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.6k (cash + stock at home prices); +117/turn over 6 turns, -41/turn over 24 turns.
- Limits: cash flow >= -281/turn, prestige >= -1.25/turn (values are after 200 tax a turn).
- Today's settings: value -157/turn, cash -141/turn, prestige +1.20/turn.
- Plan: value +27/turn, cash +36/turn, prestige -1.25/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -138 vs -187, -19 vs -156, +118 vs -155.
- Route sales counted at most (what the ships really sold, a turn): beer 2.3, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Heidlowe: +5/turn
  - ship Flax Wyrm -> Blanans: +3/turn
  - mansion 1 1.00 -> 0.42: +165/turn
  - spinnery 1 1.65 -> 1.36: +5/turn
  - retting pit 1 0.91 -> 0.81: +2/turn
  - flax farm 1 4.64 -> 4.02: +8/turn
  - net maker 0.00 -> 0.28: -3/turn
  - sewing shop 1 0.30 -> 0.24: -6/turn
  - weavery 1 0.50 -> 0.39: +12/turn
- Model check over the last 59 turns: predicted -146/turn for the settings we ran, real -14/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 33.23, beer 3.23, timber 3.69, prestige 62.61, cash 0.00
- Orders it would set: bread buy 5 (v2 7); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 49); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Heidlowe (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 82/77, thread 1049/228, cloth 72/128

## Self-diagnosis

- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
