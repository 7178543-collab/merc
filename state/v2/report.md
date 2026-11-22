# v2 shadow report

Turn 14199, 2026-11-22 00:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,152, prestige 3,710 (590 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 103 | 39 | 12 | 0 | 0 | min_holding 58, sell 14, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 33 | 8 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 65 | 524 | 0 | 41 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (12 @ 34), home ask 33.40 x11, yet 0 bought last turn); labour need rises ~35/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 41 labour expired last turn (~83 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 33.40 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 88 over real use lately; planning 524, not 609

## Prestige spending, cheapest coin per prestige first

202 turns left: prestige gained now converts 63.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.6 | 53.4 | needs a arena (build cost 28,576); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.6 | 58.5 | needs a arena (build cost 28,576); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 60.6 | 60.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 61.8 | 61.8 | thin at home: stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 61.8 | 61.8 | thin at home: stockfish |
| hold mass 2 (premium) | cathedral | 360 | 53.7 | 64.0 | needs a cathedral (build cost 306,075); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 66.4 | 66.4 | thin at home: stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 67.8 | 67.8 |  |
| hold banquet 3 (pies) | mansion | 8 | 69.1 | 69.1 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 69.5 | 69.5 | thin at home: cheese |
| jousting 1 | arena | 170 | 70.2 | 71.3 | needs a arena (build cost 28,576); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 75.5 | 75.5 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 12.6 (keep 14); best orders clear only 14 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Orlesailles +44, Kirchwerp +41, Hofkirchen +26, Birkeningen +18, Amsdermund +17
- Orlesailles would trade: cured meat buy 3 @ 30.6, pasties buy 5 @ 9.35; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~129 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (129/turn) | bread 232 (2.9->5.32), firewood 40 (2.84->11.97), charcoal 15 (2.84->8.55), thread 45 (6.7->7.03) | dyed cloth 4 (14.7->17.57), cheese 3 (10.82->13.3), yarn 2 (6.77->8.69), garments 1 (31.71->32.6) | +993 |
| Amsdermund | 1111 | 0.49 | 0.40 (52/turn) | windows 2 (840->883.5), nets 4 (40.2->47.31), hides 1 (13.55->17), lead bars 2 (14.28->14.91) | cloth 24 (7.35->13.3), dyed cloth 5 (9.97->17.57), rope 5 (78.75->83.12), garments 2 (25.2->32.6) | +339 |
| Kirchwerp | 1072 | 0.46 | 0.40 (52/turn) | casks 36 (6.51->9.36), nets 6 (40.2->44.27), butter 1 (79.28->89.3), paper 2 (30.87->34.2) | cloth 24 (10.5->13.3), cured meat 3 (20.27->33.4), rope 5 (78.75->83.12), garments 2 (24.15->32.6) | +297 |
| Rouhomme | 368 | 0.13 | 0.90 (116/turn) | bread 279 (2.9->3.88), honey 7 (9.24->13.49), nets 6 (40.2->41.61), wine 9 (6.56->7.31) | yarn 16 (6.67->8.69), tools 16 (4.73->5.84), cloth 17 (12.71->13.3) | +272 |
| Heilegg | 826 | 0.29 | 1.00 (129/turn) | bread 126 (2.9->5.18), wine 4 (6.56->9.21), beer 5 (4->6.37), nets 2 (40.2->44.65) | cloth 10 (10.4->13.3), dyed cloth 2 (14.7->17.57), garments 0 (26.46->32.6), yarn 13 (8.03->8.69) | +272 |

**Best:** Grandgues at about +993 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 18 @ min 3.88 | makes 19.3, uses 4.2, holds 103 (keeps 58): sells the surplus + 3/turn of the excess |
| bread | 5 @ 2.82, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 80.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 1 @ 29.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 2 @ 15.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 31.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 24) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 39.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.5k (cash + stock at home prices); -25/turn over 6 turns, +126/turn over 24 turns.
- Limits: cash flow >= -381/turn, prestige >= -1.21/turn (values are after 200 tax a turn).
- Today's settings: value -179/turn, cash -162/turn, prestige +0.54/turn.
- Plan: value -9/turn, cash -3/turn, prestige -1.21/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +35 vs -151, -115 vs -150, +93 vs -184.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Kirchwerp: +70/turn
  - ship Flax Wyrm -> Donaunieder: +10/turn
  - mansion 1 1.00 -> 0.58: +138/turn
  - spinnery 1 1.65 -> 1.29: +7/turn
  - retting pit 1 0.91 -> 0.81: +1/turn
  - flax farm 1 4.64 -> 4.09: +6/turn
  - net maker 0.00 -> 0.29: -3/turn
  - sewing shop 1 0.30 -> 0.21: -7/turn
  - weavery 1 0.50 -> 0.35: +14/turn
- Model check over the last 59 turns: predicted -129/turn for the settings we ran, real +26/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.72, beer 3.34, timber 3.76, prestige 74.71, cash 0.00
- Orders it would set: bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 1 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 64 (v2 24); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Kirchwerp (+42/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+10/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2008 coin: +4/turn, payback 491 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 421 (+132 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.28 |
| ret | 3 | 0.91 | 0.86 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 112/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 5.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.82, home ask 2.76; our bid is already at/over the ask (sellers too thin)
- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 12 @ 34, home ask 33.4; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
