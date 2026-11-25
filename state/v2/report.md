# v2 shadow report

Turn 14283, 2026-11-25 12:13. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,230, prestige 3,716 (596 free, -1.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 1 | 0 | 10 | 0 | 0 | sell 15, sell @ 3.84 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 531 | 0 | 33 | buy 64, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12

## Waste (money lost now)

- **labour**: 33 labour expired last turn (~66 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 551, not 651
- labour expiry guard: 33 bought labour expired last turn, buy 32 (not 51) this turn

## Prestige spending, cheapest coin per prestige first

118 turns left: prestige gained now converts 44.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.6 | 51.7 | needs a arena (build cost 31,789); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.3 | 55.4 | needs a arena (build cost 31,789); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 59.7 | 59.7 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 61.1 | 61.1 |  |
| hold banquet 2 (pies) | mansion | 7 | 61.5 | 61.5 | thin at home: pasties |
| hold banquet 1 (fish) | mansion | 4.2 | 61.6 | 61.6 |  |
| jousting 3 | arena | 230 | 60.6 | 62.6 | needs a arena (build cost 31,789); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 64.0 | 64.0 | thin at home: pasties, hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 65.4 | 65.4 | thin at home: pasties, hop beer, stockfish, sculptures |
| hold banquet 4 | mansion | 17.5 | 67.6 | 67.6 | thin at home: hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 67.8 | 67.8 |  |
| hold banquet 4 (premium) | mansion | 20 | 68.1 | 68.1 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 12 | 134102075 | 0 | - | pasties 5 | -76 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.4 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Heidlowe +48, Großmühle +46, Heilegg +36, Darmwald +33, Friedwerp +32
- Heidlowe would trade: cured meat buy 3 @ 23.2, pasties buy 7 @ 12.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~126 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Dortgart | 1045 | 0.43 | 0.30 (38/turn) | nets 6 (35.8->38.19), dyed cloth 5 (21.42->23.37), ploughs 2 (81.9->89.77), glass ingots 3 (70.88->73.62) | sculptures 1 (2436->2736), cloth 19 (9.92->12.2), lathes 1 (220.5->229.9), cured meat 3 (26.04->27.8) | +365 |
| Pontmont | 341 | 0.12 | 0.60 (76/turn) | timber 35 (8.51->15.58), garments 10 (31.6->35.91), paper 14 (27.93->30.4), copper ingots 7 (18.69->18.9) | fleece 7 (9.19->11.78), thread 21 (5.25->5.9), bricks 8 (5.25->8.07), tools 17 (5.83->6.08) | +297 |
| Kirchwerp | 1072 | 0.45 | 0.40 (50/turn) | jewellery 2 (99.75->123.5), canvas 4 (43.68->52.25), casks 11 (6.51->9.36), leather 8 (29.82->32.3) | cloth 24 (7.88->12.2), garments 2 (25.62->31.8), lathes 1 (218.4->229.9), cured meat 3 (25.62->27.8) | +248 |
| Vauxvais | 204 | 0.07 | 0.20 (25/turn) | wool 7 (13.02->20.14), cured fish 7 (24.78->27.93), limestone 2 (22.89->34.39), cookware 4 (30.03->33.44) | cloth 19 (9.45->12.2), thread 11 (3.09->5.9), bricks 6 (4.85->8.07), swords 2 (233.1->237.5) | +242 |
| Heilegg | 826 | 0.29 | 0.40 (50/turn) | wrought iron 11 (18.69->27.55), dyed cloth 5 (21.42->27.36), flour 3 (20.37->31.92), glass ingots 3 (70.88->78.85) | cured meat 3 (24.57->27.8), fleece 10 (10.92->11.78), cheese 9 (5.67->6.37), tin ingots 2 (34.44->35.91) | +240 |

**Best:** Dortgart at about +365 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 17 @ min 3.88 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 1) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 29.0, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.95 | goal planner: sells 2 a turn at 0.95, keeps 219 (no one offered it) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 32) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 84.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.4k (cash + stock at home prices); -28/turn over 6 turns, -0/turn over 24 turns.
- Limits: cash flow >= -301/turn, prestige >= -1.23/turn (values are after 200 tax a turn).
- Today's settings: value -172/turn, cash -162/turn, prestige +0.39/turn.
- Plan: value -30/turn, cash -17/turn, prestige -1.23/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +129 vs -141, -10 vs -162, +40 vs -166.
- Route sales counted at most (what the ships really sold, a turn): beer 1.8, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Darmwald: +18/turn
  - ship Flax Wyrm -> Rouhomme: +5/turn
  - mansion 1 1.00 -> 0.61: +115/turn
  - brewery 1 0.14 -> 0.21: +4/turn
  - net maker 0.00 -> 0.28: +3/turn
  - spinnery 1 1.65 -> 1.31: -5/turn
  - retting pit 1 0.91 -> 0.76: +4/turn
  - flax farm 1 4.64 -> 3.81: +11/turn
  - sewing shop 1 0.30 -> 0.21: -11/turn
  - weavery 1 0.50 -> 0.34: +20/turn
- Model check over the last 59 turns: predicted -145/turn for the settings we ran, real -15/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 33.23, beer 3.25, timber 3.65, prestige 66.39, cash 0.00
- Orders it would set: bread buy 5 (v2 1); cloth sell 1 (v2 none); cured meat buy 4 (v2 12); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 32); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Darmwald (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Rouhomme (+5/turn over staying).
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

Buffers: flax fibres 88/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.8 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 4.26 -> **buy 39 @ 4.34 (ask 4.26, cap 14.4)** (ok)
- R1: bread slot dry: 5.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.58; our bid is already at/over the ask (sellers too thin)
- R1: cured meat slot dry: 3.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 29, home ask 27.8; our bid is already at/over the ask (sellers too thin)
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
