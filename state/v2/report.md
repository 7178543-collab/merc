# v2 shadow report

Turn 13767, 2026-11-04 00:38. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,153, prestige 3,181 (61 free, -0.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 29, short of ~40 needed -> v2: buy 40
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.80 x2, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Notes

- labour: projection runs 100 over real use lately; planning 540, not 640

## Prestige spending, cheapest coin per prestige first

634 turns left: prestige gained now converts 95.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.3 | 51.3 | thin at home: hop beer, stockfish, candles |
| jousting 3 | arena | 230 | 53.1 | 53.3 | needs a arena (build cost 24,649); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 54.1 | 54.1 | thin at home: hop beer, ham, stockfish, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |
| hold banquet 4 (premium) | mansion | 20 | 54.5 | 54.5 | thin at home: hop beer, stockfish, candles |
| hold banquet 3 (pies) | mansion | 8 | 55.2 | 55.2 | thin at home: hop beer, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 56.7 | 56.7 | thin at home: cheese, pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 57.2 | 57.2 | thin at home: hop beer, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 57.6 | 57.6 | thin at home: cheese |
| jousting 2 | arena | 210 | 58.1 | 58.3 | needs a arena (build cost 24,649); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 1 | arena | 170 | 58.3 | 58.5 | needs a arena (build cost 24,649); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0.344 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.072 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 30 @ 12.9, pasties buy 5 @ 13.9; crew 0.2; est +410 a turn; stock: furniture 30 @ 12.9 (keep 145); stock: pasties 5 @ 13.9 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 14.0 (keep 14); best orders clear only 14 a turn after crew: ship stays at 0
- best towns now: Chatgnan +530, Amsdermund +508, Bordetes +487, Hofkirchen +469, Caillechâtel +410
- Chatgnan would trade: furniture buy 46 @ 14.0; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.06 | 0.30 (31/turn) | wax 9 (22.89->27.17), acid 1 (106.05->127.3), limestone 1 (19.64->24.7), tiles 3 (2.23->3.32) | bricks 8 (4.85->8.26), cloth 12 (7.61->8.65), cookware 4 (24.36->26.22), wine 23 (6.04->6.41) | +128 |
| Grandgues | 152 | 0.04 | 0.50 (51/turn) | charcoal 19 (2.12->4.45), timber 25 (7.04->8.88), bread 149 (2.23->2.43), acid 1 (106.05->114.95) | bricks 8 (6.67->8.26), cloth 5 (8.29->8.65), beer 4 (3.36->3.8), casks 1 (5.72->6.65) | +110 |
| Neuborn | 780 | 0.21 | 0.40 (41/turn) | charcoal 19 (2.12->5.7), acid 1 (106.05->133), yarn 2 (3.63->3.91) | cloth 13 (6.62->8.65), cookware 4 (22.47->26.22), garments 2 (20.37->23.4), thread 15 (4.3->4.72) | +110 |
| Heilegg | 826 | 0.23 | 0.60 (61/turn) | cured fish 5 (22.68->27.93), acid 1 (106.05->123.5), wrought iron 11 (14.49->15.58), grindstones 1 (247.8->262.2) | cloth 22 (7.56->8.65), cookware 4 (22.89->26.22), garments 2 (20.06->23.4), mouldboards 2 (40.32->40.85) | +104 |
| Blanans | 297 | 0.08 | 0.90 (92/turn) | bread 149 (2.23->2.58), charcoal 19 (2.12->3.29), timber 25 (7.04->8.64), firewood 1 (1.7->5.7) | cloth 24 (7.3->8.65), garments 2 (20.37->23.4), mouldboards 2 (38.22->40.85), cookware 4 (25.2->26.22) | +93 |

**Best:** Vauxvais at about +128 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 79, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.1 | goal planner: sells 1 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 1 @ min 1.35 | goal planner: trial sale of an idle pile, 1 a turn at 1.35, keeps 219 (8 over) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 22.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 40) |
| light armour | 1 @ 86, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.5/turn (observed), makes 0.0, holds 1 = 2.2 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.1k (cash + stock at home prices); +128/turn over 6 turns, +153/turn over 24 turns.
- Limits: cash flow >= -173/turn, prestige >= +9.94/turn (values are after 200 tax a turn).
- Today's settings: value +111/turn, cash +111/turn, prestige -0.31/turn - breaks the prestige floor.
- Plan: value -130/turn, cash -126/turn, prestige +3.89/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +101 vs +101, -36 vs +102, +82 vs +112.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Caillechâtel: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +4/turn
  - flax farm 1 4.64 -> 4.48: +1/turn
  - spinnery 1 1.65 -> 1.59: +0/turn
  - sewing shop 1 0.30 -> 0.37: -8/turn
  - weavery 1 0.50 -> 0.61: +10/turn
  - ropewalk 1 0.25 -> 0.00: -14/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.31: +15/turn
  - brewery 1 0.14 -> 0.27: -17/turn
- Model check over the last 59 turns: predicted +70/turn for the settings we ran, real +96/turn.
- Worth of one more unit per turn: labour 1.62, thread 4.07, cloth 6.50, flax fibres 4.82, garments 18.80, nets 29.25, beer 2.78, timber 3.02, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 1 (v2 none); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 40); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.31, worth +14/turn.
- Ship linen snake: Grandgues -> Caillechâtel (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.3/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 505 (+216 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.45 |
| ret | 3 | 0.91 | 1.29 |
| spin | 4 | 1.65 | 2.28 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 271/228, cloth 81/128

## Self-diagnosis

Nothing found this run.
