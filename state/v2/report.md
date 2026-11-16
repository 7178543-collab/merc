# v2 shadow report

Turn 14068, 2026-11-16 13:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,596, prestige 3,637 (517 free, -3.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 9 | 0 | 0 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 26, buy 9, buy @ 3.42 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 508 | 0 | 21 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.06 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.06 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.90 x4, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 21 labour expired last turn (~38 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 83.00 is above our ceiling 76.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 508, not 604

## Prestige spending, cheapest coin per prestige first

333 turns left: prestige gained now converts 81.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 53.9 | 54.3 | needs a arena (build cost 28,399); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.3 | 54.3 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 57.8 | 57.8 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 59.4 | 59.4 | thin at home: cured fish, cheese |
| hold banquet 2 (pies) | mansion | 7 | 59.4 | 59.4 | thin at home: cheese |
| jousting 2 | arena | 210 | 59.0 | 59.5 | needs a arena (build cost 28,399); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 62.6 | 62.6 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 63.3 | 63.3 | thin at home: hop beer, cheese |
| hold banquet 4 (premium) | mansion | 20 | 63.8 | 63.8 | thin at home: hop beer, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 60.2 | 64.3 | needs a cathedral (build cost 315,720); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 2 (meat) | mansion | 6.8 | 64.4 | 64.4 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 64.6 | 64.6 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.8 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 0 a turn after crew: ship stays at 0
- best towns now: Gosschweig +112, Etallaen +108, Chribruck +103, Bremcop +102, Boistot +49
- Gosschweig would trade: candles buy 8 @ 76.5, pasties buy 4 @ 14.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clairas | 374 | 0.11 | 0.60 (68/turn) | timber 28 (7.72->10.73), tapestries 1 (771.75->793.25), limestone 2 (24.15->32.11), malt 3 (5.67->6.93) | windows 1 (672->840.75), swords 1 (235.2->252.7), cloth 21 (8.77->9.65), dyed cloth 5 (10.5->13.01) | +300 |
| Hofkirchen | 991 | 0.36 | 0.40 (45/turn) | jewellery 12 (93.45->100.7), lead ore 2 (8.66->11.78), wine 3 (6.51->7.65), flax plants 1 (1.46->2.26) | windows 1 (803.25->840.75), cloth 24 (7.82->9.65), swords 1 (231->252.7), tools 17 (5.15->6.65) | +220 |
| Grandgues | 152 | 0.05 | 0.70 (79/turn) | timber 29 (7.72->12.25), firewood 33 (3.17->6.08), thread 12 (5.15->5.56), malt 3 (5.67->6.65) | swords 1 (231->252.7), tools 6 (4.64->6.65), cloth 4 (8.45->9.65), bricks 7 (7.04->8.41) | +219 |
| Calange | 218 | 0.07 | 0.10 (11/turn) | dyed cloth 7 (14.49->16.53), wrought iron 5 (20.16->21.47), malt 3 (5.67->6.89), cheese 3 (7.46->8.17) | windows 1 (693->840.75), swords 1 (231->252.7), candles 1 (73.5->83), garments 2 (25.2->27.2) | +210 |
| Amsdermund | 1111 | 0.43 | 0.30 (34/turn) | wine 10 (6.51->9.97), paper 7 (24.57->27.17), pasties 7 (16.91->19.76), flour 2 (18.79->25.08) | cloth 24 (7.98->9.65), tools 17 (4.83->6.65), swords 1 (231->252.7), garments 2 (26.46->27.2) | +145 |

**Best:** Clairas at about +300 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 3 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 4 = 2.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 21.8) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 8) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34 | goal planner: sells 9 at 34 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.3k (cash + stock at home prices); +217/turn over 6 turns, -53/turn over 24 turns.
- Limits: cash flow >= -192/turn, prestige >= -0.90/turn (values are after 200 tax a turn).
- Today's settings: value +85/turn, cash +81/turn, prestige -3.30/turn - breaks the prestige floor.
- Plan: value -26/turn, cash +1/turn, prestige -0.90/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +331 vs +48, +292 vs +66, +266 vs +62.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +5/turn
  - net maker 0.00 -> 0.28: +9/turn
  - spinnery 1 1.65 -> 1.35: +0/turn
  - retting pit 1 0.91 -> 0.76: -3/turn
  - flax farm 1 4.64 -> 3.83: +8/turn
  - weavery 1 0.50 -> 0.41: -19/turn
  - mansion 1 0.00 -> 0.57: -126/turn
- Model check over the last 59 turns: predicted -33/turn for the settings we ran, real -96/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.79, beer 3.37, timber 3.83, prestige 64.68, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 8); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Gosschweig (+5/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +3/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.8/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 420 (+131 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.21 |
| ret | 3 | 0.91 | 0.84 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 117/77, thread 1055/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.06; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1055 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: candles buy not filling: bid 76 under the home ask 83.0 for 5 turns, bought 1.0 of 2, 4.0 held (2.7 turns)
