# v2 shadow report

Turn 13881, 2026-11-08 18:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,089, prestige 3,541 (421 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 8 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 9 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.52 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

520 turns left: prestige gained now converts 92.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.3 | 55.3 | thin at home: pasties, ham, stockfish |
| jousting 3 | arena | 230 | 56.0 | 56.2 | needs a arena (build cost 26,246); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.2 | 57.2 |  |
| hold banquet 4 (premium) | mansion | 20 | 57.6 | 57.6 | thin at home: ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.9 | 57.9 | thin at home: ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 60.7 | 60.7 | thin at home: cured meat |
| hold banquet 3 (pies) | mansion | 8 | 61.1 | 61.1 | thin at home: pasties |
| hold banquet 3 (fish) | mansion | 7.6 | 61.5 | 61.5 |  |
| jousting 2 | arena | 210 | 61.3 | 61.6 | needs a arena (build cost 26,246); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 63.4 | 63.4 |  |
| hold sermon 2 (candles) | church | 31 | 58.5 | 63.5 | needs a church (build cost 67,030); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Gotthafen +362, Essenbrucke +311, Brebronn +293, Brunnham +284, Großaue +284
- Gotthafen would trade: furniture buy 32 @ 13.8, pasties buy 1 @ 15.7; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (99/turn) | firewood 33 (2.65->6.46), timber 32 (7.67->10.45), charcoal 19 (2.69->5.13), cured fish 6 (25.41->30.97) | spinning wheels 1 (201.6->214.7), cheese 4 (7.4->8.41), salt 1 (5.19->5.56) | +311 |
| Rouhomme | 368 | 0.11 | 1.00 (110/turn) | grain 118 (3.17->3.84), bread 155 (2.39->3.04), garments 10 (19.64->23.75), charcoal 19 (2.69->4.69) | flax fibres 6 (4.94->6), salt 7 (5.1->5.56), cheese 4 (8.03->8.41), dyed cloth 6 (13.65->13.96) | +194 |
| Kirchwerp | 1072 | 0.40 | 0.60 (66/turn) | thread 79 (4.46->5.7), wine 24 (7.19->9.5), garments 10 (19.64->22.04), casks 7 (6.98->8.31) | cloth 24 (7.56->8.7), dyed cloth 6 (12.6->13.96), cheese 4 (7.19->8.41), candles 1 (76.65->79) | +172 |
| Pontmont | 341 | 0.10 | 0.70 (77/turn) | garments 10 (19.64->29.26), bread 155 (2.39->2.85), charcoal 19 (2.69->4.75), rope 4 (82.95->85.02) | malt 5 (7.4->8.5) | +156 |
| Corstoft | 1496 | 0.64 | 0.50 (55/turn) | garments 10 (19.64->29.64), nets 6 (33.8->38), wine 24 (7.19->8.46), beer 15 (3.26->5.03) | candles 1 (69.83->79), butter 1 (87.15->93.1), raw cloth 1 (6.2->6.98) | +145 |

**Best:** Grandgues at about +311 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 81, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.6) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 106, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.3k (cash + stock at home prices); +71/turn over 6 turns, -119/turn over 24 turns.
- Limits: cash flow >= -295/turn, prestige >= -0.51/turn (values are after 200 tax a turn).
- Today's settings: value +52/turn, cash +24/turn, prestige -2.12/turn - breaks the prestige floor.
- Plan: value -5/turn, cash +56/turn, prestige -0.51/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +2 vs +57, +59 vs +57, +312 vs +39.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +8/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +10/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.09: +11/turn
  - brewery 1 0.14 -> 0.20: -9/turn
  - sewing shop 1 0.30 -> 0.36: -10/turn
  - weavery 1 0.50 -> 0.60: +9/turn
  - spinnery 1 1.65 -> 1.07: -10/turn
  - retting pit 1 0.91 -> 0.61: +8/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real -33/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.60, thread 4.01, cloth 6.41, flax fibres 4.76, garments 18.55, nets 28.89, beer 3.03, timber 3.29, prestige 60.13, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.09, worth +4/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 766/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.0 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
