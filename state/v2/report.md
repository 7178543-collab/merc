# v2 shadow report

Turn 14069, 2026-11-16 14:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,012, prestige 3,634 (514 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 5 | 9 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 26, buy 9, buy @ 3.42 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 504 | 0 | 25 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 25 labour expired last turn (~46 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **candles**: home ask 82.00 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

332 turns left: prestige gained now converts 81.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.6 | 50.1 | needs a arena (build cost 28,103); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.6 | 54.6 | running |
| jousting 2 | arena | 210 | 54.4 | 54.8 | needs a arena (build cost 28,103); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.9 | 58.9 | thin at home: beer, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 60.7 | 60.7 | thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 60.8 | 60.8 | thin at home: wine, cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 62.5 | 62.5 | thin at home: beer |
| hold banquet 2 (meat) | mansion | 6.8 | 63.2 | 63.2 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 63.6 | 63.6 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 63.9 | 63.9 | thin at home: hop beer, wine, stockfish, premium ham |
| hold banquet 3 (pies) | mansion | 8 | 64.2 | 64.2 | thin at home: hop beer |
| hold mass 2 (premium) | cathedral | 360 | 60.5 | 64.6 | needs a cathedral (build cost 313,500); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 4 @ 78.0, pasties buy 5 @ 16.0; crew 0.1; est +51 a turn; stock: candles 4 @ 78.0 (keep 12); stock: pasties 5 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: furniture buy 2 @ 13.3, pasties buy 2 @ 16.4; crew 0.1; est +20 a turn; stock: furniture 2 @ 13.3 (keep 145); stock: pasties 2 @ 16.4 (keep 14)
- best towns now: Gosschweig +135, Brunnham +115, Chribruck +108, Bedenis +108, Clairlond +82
- Gosschweig would trade: candles buy 9 @ 76.5, furniture buy 2 @ 13.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~112 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.70 (79/turn) | timber 29 (7.77->12.25), charcoal 19 (2.54->6.46), firewood 33 (3.11->6.37), medicine 1 (135.45->148.2) | acid 1 (137.55->149.15), tools 6 (4.89->6.84), cloth 4 (7.88->9.75), coats 1 (72.45->74.1) | +292 |
| Amsdermund | 1111 | 0.43 | 0.30 (34/turn) | premium ham 1 (247.8->281.2), wine 10 (6.51->9.97), paper 7 (24.57->28.69), medicine 1 (135.45->142.5) | cloth 24 (7.98->9.75), tools 16 (4.83->6.84), acid 1 (137.55->149.15), garments 2 (27.3->29.8) | +189 |
| Vauxvais | 204 | 0.06 | 1.00 (112/turn) | wax 13 (27.09->30.02), charcoal 17 (2.54->4.75), firewood 49 (3.11->5.51), medicine 0 (135.45->155.8) | tools 14 (5.15->6.84), cloth 12 (8.98->9.75), garments 1 (24.78->29.8), flax fibres 5 (5.83->6.3) | +162 |
| Pontmont | 341 | 0.10 | 1.00 (112/turn) | firewood 25 (3.11->9.5), premium ham 0 (247.8->290.7), bread 74 (2.52->3.1), charcoal 9 (2.54->4.45) | tools 7 (6.2->6.84), cloth 2 (8.87->9.75), belts 1 (33.6->34.58), iron ore 0 (5.25->6.93) | +161 |
| Heilegg | 826 | 0.26 | 0.50 (56/turn) | charcoal 19 (2.54->6.03), medicine 1 (135.45->149.15), wine 10 (6.51->7.46), nets 6 (34.6->36.1) | cloth 24 (7.35->9.75), acid 1 (136.5->149.15), cheese 7 (6.3->7.27), salt 6 (4.73->5.56) | +136 |

**Best:** Grandgues at about +292 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 9 @ 4.36, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 5 = 1.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 3) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.4) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 75.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.1k (cash + stock at home prices); +369/turn over 6 turns, -20/turn over 24 turns.
- Limits: cash flow >= -209/turn, prestige >= -0.89/turn (values are after 200 tax a turn).
- Today's settings: value +92/turn, cash +76/turn, prestige -2.78/turn - breaks the prestige floor.
- Plan: value +16/turn, cash +23/turn, prestige -0.89/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +292 vs +66, +266 vs +62, +416 vs +81.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanbrücken: +11/turn
  - ship Flax Wyrm -> Gosschweig: +0/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - net maker 0.00 -> 0.28: +6/turn
  - spinnery 1 1.65 -> 1.36: +2/turn
  - retting pit 1 0.91 -> 0.85: +1/turn
  - flax farm 1 4.64 -> 4.30: +3/turn
  - weavery 1 0.50 -> 0.39: -24/turn
  - sewing shop 1 0.30 -> 0.24: -5/turn
  - mansion 1 0.00 -> 0.45: -76/turn
- Model check over the last 59 turns: predicted -27/turn for the settings we ran, real -85/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.76, beer 3.37, timber 3.78, prestige 61.52, cash 0.00
- Orders it would set: candles buy 2 (v2 3); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Hanbrücken (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Gosschweig (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.7/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 421 (+132 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.23 |
| ret | 3 | 0.91 | 0.85 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.29 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 115/78, thread 1050/228, cloth 73/129

## Self-diagnosis

- R1: candles slot dry: 2.5 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 2 @ 76, home ask 82.0 -> **buy 3 @ 83.5 (ask 82.0, cap 120.0)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
