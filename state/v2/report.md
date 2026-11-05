# v2 shadow report

Turn 13813, 2026-11-05 22:09. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,560, prestige 3,292 (172 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 1 | 0 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 530, not 630

## Prestige spending, cheapest coin per prestige first

588 turns left: prestige gained now converts 94.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.0 | 54.0 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 54.8 | 54.8 | thin at home: hop beer, wine, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 54.9 | 55.1 | needs a arena (build cost 25,228); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 56.1 | 56.1 | thin at home: wine, cured fish, cheese |
| hold banquet 2 (pies) | mansion | 7 | 56.6 | 56.6 | thin at home: wine, cheese |
| hold banquet 4 | mansion | 17.5 | 58.0 | 58.0 | thin at home: wine, hop beer, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 58.4 | 58.4 | thin at home: hop beer, wine, ham, stockfish, premium cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 58.8 | 58.8 |  |
| hold sermon 2 (candles) | church | 31 | 55.0 | 59.2 | needs a church (build cost 65,000); thin at home: candles, furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 59.5 | 59.5 | thin at home: wine, cheese |
| jousting 2 | arena | 210 | 60.1 | 60.3 | needs a arena (build cost 25,228); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.072 | - | pasties 3 | -44 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 14.9 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.1 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Bedenis +58, Angefont +33, Donaunieder +30, Brunnham +30, Orlesailles +27
- Bedenis would trade: pasties buy 8 @ 10.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Briclives | 1041 | 0.35 | 0.20 (20/turn) | garments 10 (22.6->25.65), beer 15 (3.3->4.27), salt 5 (5.57->6.65), nails 6 (6.51->6.93) | looms 1 (405.3->598.5), candles 1 (78.75->84), wool 1 (9.08->9.88) | +230 |
| Bedenis | 566 | 0.15 | 0.80 (82/turn) | bread 159 (2.25->3.23) | cloth 15 (7.35->8), garments 18 (21->21.47), cheese 4 (6.83->7.22), pasties 1 (10.71->12.63) | +99 |
| Grandgues | 152 | 0.04 | 0.40 (41/turn) | limestone 7 (16.17->21.47), bellows 1 (218.4->231.8), bread 159 (2.25->2.45), logs 1 (3.95->11.11) | garments 18 (20.79->21.47), candles 1 (79.28->84), bricks 3 (7.46->9.21), cheese 4 (6.56->7.22) | +84 |
| Blanans | 297 | 0.08 | 0.70 (72/turn) | limestone 7 (16.17->23.75), bread 159 (2.25->2.56), firewood 1 (1.83->6.46), nets 1 (37.4->39.14) | cloth 22 (7.35->8), garments 18 (21->21.47), candles 1 (77.7->84), flax plants 11 (1.41->1.68) | +75 |
| Dedlowe | 1146 | 0.41 | 0.20 (20/turn) | yarn 14 (4.98->5.56) | looms 1 (567->598.5), candles 1 (64.58->84), ploughs 1 (64.05->74.1), rope 1 (75.6->81.22) | +60 |

**Best:** Briclives at about +230 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 30) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 83.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 1.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.5k (cash + stock at home prices); +190/turn over 6 turns, +146/turn over 24 turns.
- Limits: cash flow >= -273/turn, prestige >= +5.31/turn (values are after 200 tax a turn).
- Today's settings: value +104/turn, cash +109/turn, prestige -0.87/turn - breaks the prestige floor.
- Plan: value -128/turn, cash -122/turn, prestige +3.33/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -146 vs +105, +55 vs +96, +82 vs +102 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bremcop: +2/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - sewing shop 1 0.30 -> 0.36: -5/turn
  - weavery 1 0.50 -> 0.60: +7/turn
  - ropewalk 1 0.25 -> 0.00: -15/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.35: +18/turn
  - brewery 1 0.14 -> 0.27: -19/turn
  - mansion 1 0.00 -> 1.00: -221/turn
- Model check over the last 62 turns: predicted +97/turn for the settings we ran, real +69/turn.
- Worth of one more unit per turn: labour 1.65, thread 4.14, cloth 6.62, flax fibres 4.91, garments 19.15, nets 29.82, beer 2.85, timber 3.06, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 30); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.35, worth +14/turn.
- Ship linen snake: Grandgues -> Bremcop (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 484 (+196 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.99 |
| ret | 3 | 0.91 | 1.20 |
| spin | 4 | 1.65 | 2.12 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 325/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.45 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
- R5: tar buy not filling: bid 11 under the home ask 11.1 for 3 turns, bought 0.0 of 1, 0.2 held (1.0 turns); raise needs Taylor (ceiling 11.0)
