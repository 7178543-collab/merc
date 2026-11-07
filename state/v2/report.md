# v2 shadow report

Turn 13858, 2026-11-07 19:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,364, prestige 3,359 (239 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 14 | 6 | 4 | 0 | 0 | min_holding 60, sell 3, sell @ 3.06; stop 17, buy 8, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 2 | 2 | 1 | 0 | stop 13, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 31, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 512 | 0 | 17 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (4 @ 2.4), 2 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 17 labour expired last turn (~28 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 530, not 630

## Prestige spending, cheapest coin per prestige first

543 turns left: prestige gained now converts 93.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 53.4 | 53.4 | thin at home: wine, ham, stockfish, cheese, candles |
| jousting 3 | arena | 230 | 53.6 | 53.9 | needs a arena (build cost 24,963); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.1 | 55.1 | thin at home: beer |
| hold banquet 2 (fish) | mansion | 6.8 | 55.3 | 55.3 | thin at home: wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 56.0 | 56.0 | thin at home: cheese |
| hold banquet 4 | mansion | 17.5 | 56.2 | 56.2 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 56.7 | 56.7 | thin at home: wine, cheese |
| hold banquet 3 (pies) | mansion | 8 | 56.9 | 56.9 | thin at home: pasties, cheese, candles |
| hold banquet 4 (premium) | mansion | 20 | 56.9 | 56.9 | thin at home: wine, ham, stockfish, candles, premium cheese |
| hold banquet 3 (meat) | mansion | 7.6 | 57.3 | 57.3 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 57.4 | 57.4 | thin at home: beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.108 | - | pasties 5 | -80 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.1 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Großmühle | 751 | 0.21 | 0.10 (10/turn) | dyed cloth 31 (13.65->18.05), spirits 2 (11.87->13.01), rope 1 (80->80.75) | medicine 1 (116.55->129.2) | +141 |
| Bordetes | 831 | 0.24 | 0.20 (21/turn) | dyed cloth 31 (13.65->16.34), flour 2 (21.84->31.73), cured meat 7 (23.1->25.46), pasties 2 (16.8->21.66) | cloth 11 (8.4->9.25), tackles 1 (177.45->183.35), axes 1 (14.38->14.91) | +137 |
| Hofkirchen | 991 | 0.33 | 1.00 (104/turn) | bread 85 (2.31->4.24), lead ore 5 (13.86->21.47), flour 1 (21.84->29.64), blades 1 (15.02->17.1) | flax fibres 15 (5.17->6.4), cheese 1 (5.78->6.41), garments 1 (24.36->25.4), dyed cloth 3 (10.92->11.3) | +133 |
| Hanstein | 380 | 0.11 | 0.50 (52/turn) | timber 15 (7.19->11.21), tallow 1 (17.96->23.18), charcoal 18 (2.35->3.34), salt 9 (4.37->4.58) | thread 43 (4.51->5.3), cloth 11 (7.09->9.25), flax fibres 17 (5.88->6.4), seeds 13 (1.84->2.32) | +108 |
| Heilegg | 826 | 0.24 | 0.20 (21/turn) | lead ore 10 (13.86->18.81), nets 6 (33.6->36.29), wrought iron 7 (14.28->15.58), tallow 1 (17.96->20.33) | cloth 24 (8.45->9.25), garments 2 (23.1->25.4), flax fibres 14 (5.72->6.4), dyed cloth 7 (11.03->11.3) | +80 |

**Best:** Großmühle at about +141 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 6 @ 3.9, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 14 = 3.3 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 74.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 13 |  | goal planner: buys 4 a turn for today's rates, keeps up to 13 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.6) |
| grain | 8 @ 3.7, stop 32 |  | goal planner: buys 8 a turn for today's rates, keeps up to 32 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 30) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.2k (cash + stock at home prices); +178/turn over 6 turns, +129/turn over 24 turns.
- Limits: cash flow >= -348/turn, prestige >= +2.55/turn (values are after 200 tax a turn).
- Today's settings: value +84/turn, cash +68/turn, prestige -1.33/turn - breaks the prestige floor.
- Plan: value -103/turn, cash +23/turn, prestige +2.55/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +158 vs +61, +124 vs +62, +235 vs +68.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +1/turn
  - ship Flax Wyrm -> Calange: +1/turn
  - net maker 0.00 -> 0.29: +3/turn
  - ropewalk 1 0.25 -> 0.33: +3/turn
  - sewing shop 1 0.30 -> 0.36: -11/turn
  - weavery 1 0.50 -> 0.60: +12/turn
  - spinnery 1 1.65 -> 1.07: -17/turn
  - retting pit 1 0.91 -> 0.61: +7/turn
  - flax farm 1 4.64 -> 3.08: -12/turn
  - mansion 1 0.00 -> 0.92: -173/turn
- Model check over the last 61 turns: predicted +104/turn for the settings we ran, real +79/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.66, flax fibres 4.94, garments 19.27, nets 29.81, beer 2.98, timber 3.08, prestige 55.90, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 7); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 11); labour buy 29 (v2 30); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Brunnham (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Calange (+1/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/77, thread 533/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 4.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 4 @ 2.4, home ask 2.22; our bid is already at/over the ask (sellers too thin)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.4 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
