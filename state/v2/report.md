# v2 shadow report

Turn 14067, 2026-11-16 12:39. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,330, prestige 3,640 (520 free, -3.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 22, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.68 is above our ceiling 2.60 and last turn bought 3 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **candles**: home ask 83.00 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 608

## Prestige spending, cheapest coin per prestige first

334 turns left: prestige gained now converts 81.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.1 | 52.5 | needs a arena (build cost 27,977); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 57.4 | 57.4 | thin at home: cured fish |
| jousting 2 | arena | 210 | 57.1 | 57.5 | needs a arena (build cost 27,977); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.1 | 59.1 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 59.1 | 59.1 |  |
| hold mass 2 (premium) | cathedral | 360 | 58.7 | 62.3 | needs a cathedral (build cost 275,110); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 (pies) | mansion | 18 | 62.5 | 62.5 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 62.7 | 62.7 | thin at home: hop beer |
| hold banquet 1 (meat) | mansion | 4.2 | 63.3 | 63.3 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 63.5 | 63.5 |  |
| hold banquet 4 (premium) | mansion | 20 | 63.6 | 63.6 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 13.0 (keep 145); stock: pasties 3 @ 14.7 (keep 14); best orders clear only 15 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.0 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Chribruck +85, Gosschweig +83, Etallaen +78, Bremcop +70, Clairlond +67
- Chribruck would trade: candles buy 6 @ 78.0, furniture buy 1 @ 13.9, pasties buy 3 @ 14.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (89/turn) | timber 38 (7.72->12.44), firewood 34 (3.11->6.41), charcoal 19 (3.19->5.56), flour 3 (17.96->19.19) | swords 1 (233.1->260.3), tools 8 (4.62->5.94), bricks 10 (7.09->8.41), cloth 4 (8.66->9.6) | +311 |
| Amsdermund | 1111 | 0.42 | 0.30 (33/turn) | flour 3 (17.96->29.64), premium ham 1 (260.4->281.2), wine 4 (6.41->9.97), pasties 8 (16.8->19.38) | cloth 24 (7.98->9.6), swords 1 (235.2->260.3), tools 17 (4.83->5.94), wrought iron 2 (13.55->16.72) | +149 |
| Hofkirchen | 991 | 0.35 | 0.30 (33/turn) | jewellery 11 (96.08->100.7), fleece 4 (8.03->9.36), lead ore 2 (8.72->11.78), wine 3 (6.41->7.46) | cloth 24 (7.82->9.6), swords 1 (231->260.3), tools 17 (5.15->5.94), garments 2 (23.94->27.6) | +137 |
| Heilegg | 826 | 0.25 | 0.50 (56/turn) | charcoal 19 (3.19->6.03), flour 3 (17.96->23.56), malt 3 (7.35->8.84), wine 4 (6.41->7.5) | cloth 24 (7.35->9.6), swords 1 (231->260.3), cookware 6 (23.73->24.7), salt 5 (4.56->5.56) | +128 |
| Vauxvais | 204 | 0.06 | 1.00 (111/turn) | wax 17 (27.3->30.02), firewood 54 (3.11->5.42), charcoal 19 (3.19->4.75), rope 1 (75->83.12) | tools 17 (5.15->5.94), garments 2 (24.36->27.6), flax fibres 6 (5.35->6.3), cloth 18 (9.4->9.6) | +126 |

**Best:** Grandgues at about +311 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 6 = 3.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.2) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34 | goal planner: sells 9 at 34 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 73.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.9k (cash + stock at home prices); -469/turn over 6 turns, -81/turn over 24 turns.
- Limits: cash flow >= -180/turn, prestige >= -0.92/turn (values are after 200 tax a turn).
- Today's settings: value +82/turn, cash +62/turn, prestige -3.32/turn - breaks the prestige floor.
- Plan: value -18/turn, cash -8/turn, prestige -0.92/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -282 vs +45, +331 vs +48, +292 vs +66.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanbrücken: +8/turn
  - ship Flax Wyrm -> Gosschweig: +0/turn
  - net maker 0.00 -> 0.29: +10/turn
  - ropewalk 1 0.25 -> 0.19: +6/turn
  - spinnery 1 1.65 -> 1.51: +4/turn
  - flax farm 1 4.64 -> 4.71: -1/turn
  - sewing shop 1 0.30 -> 0.38: -13/turn
  - weavery 1 0.50 -> 0.62: +18/turn
  - mansion 1 0.00 -> 0.57: -136/turn
- Model check over the last 59 turns: predicted -41/turn for the settings we ran, real -112/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.77, thread 4.45, cloth 7.10, flax fibres 5.27, garments 20.55, nets 32.11, beer 3.32, timber 3.46, prestige 63.32, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Hanbrücken (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Gosschweig (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.9/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 420 (+131 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.18 |
| ret | 3 | 0.91 | 0.84 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 119/78, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.36 -> **buy 9 @ 3.42 (ask 3.36, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
