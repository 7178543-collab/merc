# v2 shadow report

Turn 13860, 2026-11-07 21:29. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,928, prestige 3,356 (236 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 44 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.46 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 31 | 7 | 9 | 0 | 0 | stop 32, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 524 | 0 | 5 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.74 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 12.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 524, not 618

## Prestige spending, cheapest coin per prestige first

541 turns left: prestige gained now converts 93.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 53.7 | 53.7 | thin at home: pasties, wine, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 53.7 | 53.9 | needs a arena (build cost 25,063); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.4 | 55.4 |  |
| hold banquet 4 | mansion | 17.5 | 56.7 | 56.7 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 57.0 | 57.0 |  |
| hold banquet 4 (premium) | mansion | 20 | 57.1 | 57.1 | thin at home: wine, ham, stockfish, premium cheese |
| hold banquet 3 (pies) | mansion | 8 | 58.6 | 58.6 | thin at home: pasties, cheese |
| jousting 2 | arena | 210 | 58.8 | 59.0 | needs a arena (build cost 25,063); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.1 | 59.1 | thin at home: wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 59.1 | 59.1 | thin at home: cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 59.9 | 59.9 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.4 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 16.0 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rotterburg | 1056 | 0.36 | 0.10 (10/turn) | - | tapestries 3 (693->783.75), candles 1 (74.03->85), tackles 2 (170.1->173.85), cheese 3 (7.25->8.31) | +287 |
| Disscester | 1474 | 0.60 | 0.10 (10/turn) | cured meat 3 (22.68->24.32) | tapestries 2 (682.5->783.75), candles 1 (76.12->85), chisels 1 (7.04->11.4), wool 1 (11.55->13.68) | +213 |
| Amsdermund | 1111 | 0.40 | 0.30 (31/turn) | thread 48 (4.66->5.22), cured fish 8 (24.36->25.27) | tapestries 3 (735->783.75), cloth 22 (6.88->9.1), cheese 3 (6.25->8.31), flax fibres 9 (5.17->6.5) | +209 |
| Hofkirchen | 991 | 0.33 | 0.40 (42/turn) | lead ore 8 (13.55->21.09), nets 6 (33.6->36.29), flour 2 (21.84->26.41), glass ingots 1 (66.67->68.4) | tapestries 3 (750.75->783.75), cloth 20 (7.88->9.1), candles 1 (73.5->85), cheese 3 (6.51->8.31) | +203 |
| Brebronn | 862 | 0.26 | 0.10 (10/turn) | - | tapestries 1 (614.25->783.75), candles 1 (75.6->85), cloth 10 (8.19->9.1), casks 7 (5.51->6.65) | +194 |

**Best:** Rotterburg at about +287 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 15 @ min 3.42 |  |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.4) |
| grain | 8 @ 3.7, stop 32 |  | goal planner: buys 8 a turn for today's rates, keeps up to 32 (v2 had 12) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 24) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.7k (cash + stock at home prices); +189/turn over 6 turns, +145/turn over 24 turns.
- Limits: cash flow >= -289/turn, prestige >= +2.65/turn (values are after 200 tax a turn).
- Today's settings: value +70/turn, cash +54/turn, prestige -1.19/turn - breaks the prestige floor.
- Plan: value -111/turn, cash -104/turn, prestige +2.65/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +235 vs +68, +24 vs +68, -1460 vs +63 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - flax farm 1 4.64 -> 4.73: -0/turn
  - sewing shop 1 0.30 -> 0.36: -10/turn
  - weavery 1 0.50 -> 0.61: +12/turn
  - ropewalk 1 0.25 -> 0.00: -14/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.38: +17/turn
  - mansion 1 0.00 -> 0.91: -192/turn
- Model check over the last 61 turns: predicted +104/turn for the settings we ran, real +82/turn.
- Worth of one more unit per turn: labour 1.63, thread 4.09, cloth 6.54, flax fibres 4.85, garments 18.92, nets 29.51, beer 2.98, timber 3.26, prestige 55.08, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 12); labour buy 29 (v2 24); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.38, worth +15/turn.
- Ship linen snake: Grandgues -> Etallaen (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 441 (+152 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.02 |
| ret | 3 | 0.91 | 1.00 |
| spin | 4 | 1.65 | 1.77 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 530/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.5 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
