# v2 shadow report

Turn 14063, 2026-11-16 08:13. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,148, prestige 3,654 (534 free, -3.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 521 | 0 | 8 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.0/turn) but there is NO buy order, stock 0.0 -> v2: add buy 8
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.96 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.96 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Notes

- labour: projection runs 117 over real use lately; planning 521, not 618

## Prestige spending, cheapest coin per prestige first

338 turns left: prestige gained now converts 81.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.2 | 50.6 | needs a arena (build cost 27,625); thin at home: swords, protection, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| jousting 2 | arena | 210 | 55.0 | 55.4 | needs a arena (build cost 27,625); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.0 | 59.0 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 59.5 | 59.5 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 59.6 | 59.6 | thin at home: beer, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 61.3 | 61.3 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 62.3 | 62.3 | thin at home: hop beer, wine, stockfish, glassware |
| hold banquet 3 (pies) | mansion | 8 | 62.7 | 62.7 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 63.0 | 63.0 | thin at home: hop beer, wine, stockfish, glassware |
| hold banquet 1 (meat) | mansion | 4.2 | 63.1 | 63.1 | thin at home: beer |
| hold mass 2 (premium) | cathedral | 360 | 59.9 | 63.9 | needs a cathedral (build cost 311,365); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 134102075 | 0.384 | - | candles 2, furniture 19, pasties 2 | -449 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 14.6, pasties buy 1 @ 15.5; crew 0.2; est +230 a turn; stock: furniture 21 @ 14.6 (keep 145); stock: pasties 1 @ 15.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.2 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Chatgnan +474, Vauxvais +392, Boistot +362, Essenbrucke +299, Blanans +299
- Chatgnan would trade: furniture buy 41 @ 13.8; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (96/turn) | timber 48 (8.09->12.54), firewood 35 (3.11->6.32), charcoal 19 (2.84->5.42), rope 1 (72.5->76) | premium cheese 2 (23.1->34.58), beer 4 (3.4->4.28), cloth 4 (8.66->9.3), salt 6 (5.25->5.56) | +320 |
| Kirchwerp | 1072 | 0.38 | 0.50 (53/turn) | steel ingots 10 (19.74->25.84), lead ore 10 (8.14->10.45), wine 5 (6.67->7.5), rope 1 (72.5->74.1) | cloth 24 (7.51->9.3), ploughs 2 (73.5->83.12), salt 9 (3.89->5.56), garments 2 (21.63->24.2) | +137 |
| Pontmont | 341 | 0.10 | 1.00 (107/turn) | firewood 31 (3.11->8.07), tiles 4 (3.26->7.27), candles 1 (76.12->85.02), rope 0 (72.5->84.08) | ploughs 2 (76.12->83.12), logs 1 (4.2->7.22), beer 2 (3.91->4.28) | +121 |
| Gotthafen | 964 | 0.32 | 0.40 (43/turn) | garments 10 (22.8->28.31), lead ore 10 (8.14->13.59), casks 20 (5.83->7.27), tiles 1 (3.26->10.64) | salt 7 (4.75->5.56), cheese 10 (6.41->6.84), wrought iron 2 (16.28->16.62) | +117 |
| Amsdermund | 1111 | 0.41 | 0.30 (32/turn) | garments 10 (22.8->25.08), wine 5 (6.67->9.79), flour 3 (21.21->28.31), candles 3 (76.12->79.33) | cloth 24 (7.35->9.3), tools 16 (4.83->6.08), salt 5 (4.83->5.56), flax fibres 14 (5.78->6.65) | +112 |

**Best:** Grandgues at about +320 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 8 @ 4.48, stop 16 |  | uses 4.0/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| candles | 2 @ 76.0, stop 6 |  | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 3) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 22.2) |
| grain | 0 @ 3.7, stop 21 |  | goal planner: buys 0 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 21) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 70.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 0.7 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.0k (cash + stock at home prices); -540/turn over 6 turns, -123/turn over 24 turns.
- Limits: cash flow >= -173/turn, prestige >= -0.97/turn (values are after 200 tax a turn).
- Today's settings: value +71/turn, cash +33/turn, prestige -3.29/turn - breaks the prestige floor.
- Plan: value -7/turn, cash +1/turn, prestige -0.97/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -328 vs +30, -22 vs +39, -268 vs +28 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bordetes: +0/turn
  - ship Flax Wyrm -> Pontmont: +0/turn
  - ropewalk 1 0.25 -> 0.10: +14/turn
  - net maker 0.00 -> 0.29: +15/turn
  - spinnery 1 1.65 -> 1.43: +4/turn
  - flax farm 1 4.64 -> 4.49: -0/turn
  - sewing shop 1 0.30 -> 0.39: -11/turn
  - weavery 1 0.50 -> 0.64: +18/turn
  - mansion 1 0.00 -> 0.55: -129/turn
- Model check over the last 59 turns: predicted -67/turn for the settings we ran, real -142/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.69, thread 4.29, cloth 6.82, flax fibres 5.15, garments 19.70, nets 30.88, beer 3.16, timber 3.31, prestige 60.36, cash 0.00
- Orders it would set: candles buy 2 (v2 3); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 21); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Bordetes (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Pontmont (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +84/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 11.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 417 (+128 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.05 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 129/78, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 4.28 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 4.36 (ask 4.28, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.96; ask over the cap 2.1 (60 coin per prestige)
