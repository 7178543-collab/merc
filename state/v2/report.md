# v2 shadow report

Turn 13552, 2026-10-26 01:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,192, prestige 3,567 (447 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 6 | 0 | 6 | 0 | 0 | buy @ 2.4; sell 1, sell @ 1.73 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 58 | 21 | 26 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 458 | 0 | 42 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 33.6 |
| porterage | 14 | 14 | 13 | 0 | 1 | buy 14, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy

## Tuning

- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187

## Notes

- labour: projection runs 121 over real use lately; planning 458, not 562

## Prestige spending, cheapest coin per prestige first

849 turns left: prestige gained now converts 98.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.6 | 45.6 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.1 | 47.1 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.9 | 48.9 | thin at home: hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 49.4 | 49.4 | thin at home: hop beer, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 49.6 | 49.6 | thin at home: pies |
| hold banquet 3 (meat) | mansion | 7.6 | 50.4 | 50.4 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 51.2 | 51.2 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 52.4 | 52.4 |  |
| hold banquet 4 | mansion | 17.5 | 52.5 | 52.5 | thin at home: hop beer, stockfish |
| jousting 3 | arena | 230 | 52.7 | 52.8 | needs a arena (build cost 23,366); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 53.5 | 53.5 |  |
| hold prayer 2 | chapel | 13 | 51.1 | 54.0 | needs a chapel (build cost 29,642) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~95 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.21 | 0.10 (9/turn) | glass ingots 3 (57.75->63.65), tackles 1 (159.6->167.2), varnish 3 (18.48->20.9), yarn 5 (4.12->5.08) | premium ham 1 (241.5->260.3), tin ingots 1 (27.51->36.48), candles 1 (67.2->75), premium cheese 1 (26.25->28.5) | +74 |
| Fontaux | 411 | 0.10 | 0.20 (19/turn) | salt 17 (4.77->7.79), charcoal 11 (1.9->3.88), glass ingots 3 (57.75->59.85), garments 1 (18.1->19) | candles 1 (68.25->75) | +70 |
| Gotthafen | 964 | 0.29 | 0.10 (9/turn) | tackles 1 (159.6->203.3), glass ingots 2 (57.75->60.8), garments 1 (18.1->18.9) | ploughs 2 (65.62->70.77), candles 1 (71.4->75), premium cheese 1 (26.04->28.5), pasties 1 (11.45->13.3) | +60 |
| Bordees | 1112 | 0.36 | 0.20 (19/turn) | tackles 1 (159.6->166.25) | looms 1 (516.6->551), ploughs 3 (65.1->70.77), candles 1 (70.35->75), tools 2 (4.7->5.1) | +44 |
| Briclives | 1041 | 0.33 | 0.10 (9/turn) | tackles 1 (159.6->185.25), cured meat 3 (22.68->26.22), stockfish 1 (129.15->134.9), cheese 9 (5.88->6.41) | candles 1 (72.45->75), tools 2 (4.28->5.1), mouldboards 2 (32.34->32.68) | +44 |

**Best:** Heilegg at about +74 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.38) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 0 @ 2.4, stop 13 | 1 @ min 1.73 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 6 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 1 @ min 4.82 | goal planner: sells 1 a turn at 4.82, keeps 82 (no one offered it) |
| grain | 29 @ 3.7, stop 115 |  | goal planner: buys 29 a turn for today's rates, keeps up to 115 (v2 had 57) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 10 @ min 33.6 | goal planner: sells 10 at 33.6 (v2 had 10 at 36.0) |
| pasties | 4 @ 14.5, stop 8 |  | uses 2.0/turn (household upkeep), makes 0.0, holds 2 = 1.0 turns |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 13) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 71.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 2.0 turns |
| thread |  | 19 @ min 4.26 | goal planner: sells 19 a turn at 4.26, keeps 180 (no one offered it) |
| tools | 3 @ 6.2, stop 18 |  | uses 2.2/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 89.9 turns |
| varnish | 1 @ 18.4, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 5.2 turns |
| wax | 1 @ 23.0, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 11.2 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.2k (cash + stock at home prices); -7/turn over 6 turns, -4/turn over 24 turns.
- Limits: cash flow >= +117/turn, prestige >= -0.61/turn (values are after 220 tax a turn).
- Today's settings: value +92/turn, cash +27/turn, prestige -1.93/turn - breaks the prestige floor and cash floor.
- Plan: value +112/turn, cash +117/turn, prestige -0.61/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -337 vs +55, -252 vs +27, -200 vs +41 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +1/turn
  - ship Flax Wyrm -> Grandgues: +3/turn
  - ropewalk 1 0.25 -> 0.70: +43/turn
  - spinnery 1 1.59 -> 1.94: +21/turn
  - net maker 0.23 -> 0.00: +15/turn
  - retting pit 1 1.04 -> 0.97: +2/turn
  - flax farm 1 5.88 -> 5.50: +3/turn
  - logging camp w/ tool 5.00 -> 4.87: +0/turn
  - weavery 1 0.13 -> 0.20: -4/turn
  - mansion 1 0.15 -> 0.47: -65/turn
- Model check over the last 58 turns: predicted +109/turn for the settings we ran, real +34/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.03, cloth 6.49, flax fibres 4.64, garments 18.84, nets 16.65, beer 2.89, timber 3.26, prestige 57.13, cash 0.08
- Orders it would set: cured meat buy 1 (v2 2); flax fibres sell 1 (v2 none); furniture buy 2 (v2 None); grain buy 29 (v2 57); light armour buy 1 (v2 None); porterage buy 14 (v2 13); rope sell 2 (v2 1); thread sell 19 (v2 none)
- Ship linen snake: Grandgues -> Vauxvais (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+3/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +75/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate logging camp w/ tool: +18/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 1.2/turn (+0.0 exported); plan makes 6.6 garments a turn.
Labour: own 500, everything else 394, chain may buy 0 -> chain allowance 106, chain plan 105 (-135 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.39 |
| ret | 3 | 1.04 | 0.07 |
| spin | 4 | 1.59 | 0.73 |
| weave | 3 | 0.13 | 0.26 |
| sew | 2 | 0.09 | 0.16 |

Buffers: flax fibres 249/45, thread 1048/133, cloth 0/26
- chain plan needed 393 labour, budget left 106: cut to 106 (sewing capped at 0.16)

## Self-diagnosis

- R1: firewood slot dry: 5.5 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask 1.81 (held back: failsafe level 3: reduce-only, would buy 6 @ 1.84 (ask 1.81, cap 2.1))
- R2: spinnery 1 blocked by thread space: 1048 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
