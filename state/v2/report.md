# v2 shadow report

Turn 14121, 2026-11-18 18:36. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,447, prestige 3,594 (474 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 5 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 496 | 0 | 33 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.80 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.80 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 33 labour expired last turn (~66 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 83.50 is above our ceiling 76.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611
- labour expiry guard: 33 bought labour expired last turn, buy 0 (not 11) this turn

## Prestige spending, cheapest coin per prestige first

280 turns left: prestige gained now converts 75.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 54.4 | 54.9 | needs a arena (build cost 27,450); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 58.5 | 58.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 58.9 | 58.9 |  |
| jousting 2 | arena | 210 | 59.5 | 60.1 | needs a arena (build cost 27,450); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 55.4 | 60.5 | needs a cathedral (build cost 296,000); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 61.8 | 61.8 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 63.2 | 63.2 |  |
| hold banquet 4 (pies) | mansion | 18 | 63.9 | 63.9 | thin at home: stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 64.2 | 64.2 | thin at home: stockfish, premium ham |
| hold banquet 2 (meat) | mansion | 6.8 | 64.9 | 64.9 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 64.9 | 64.9 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 65.8 | 65.8 | thin at home: cheese, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: candles 1 @ 77.5 (keep 12); best orders clear only 0 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.0 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Amsdermund +621, Hofkirchen +435, Vauxvais +361, Cobholme +332, Clairlond +286
- Amsdermund would trade: furniture buy 57 @ 13.7, pasties buy 2 @ 15.4; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~122 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.70 (86/turn) | firewood 31 (2.94->6.84), timber 28 (9.03->12.35), charcoal 18 (2.39->5.61), limestone 3 (16.17->24.7) | garments 2 (30.66->41), premium ham 1 (275.1->286.9), cloth 5 (10.45->11.2), yarn 3 (6.3->7.41) | +291 |
| Heilegg | 826 | 0.28 | 0.20 (24/turn) | wrought iron 8 (19.95->27.55), jewellery 5 (96.6->102.6), nets 6 (35.4->39.33), lathes 1 (182.7->197.6) | cloth 20 (8.51->11.2), garments 2 (28.77->41), premium ham 1 (275.1->286.9), cookware 5 (22.89->24.13) | +237 |
| Amsdermund | 1111 | 0.47 | 0.50 (61/turn) | jewellery 5 (96.6->104.5), tackles 1 (151.2->190), leather 1 (25.2->29.26) | cloth 24 (7.35->11.2), garments 2 (26.25->41), paper 7 (21->24.32), cookware 5 (21.63->24.13) | +229 |
| Gottweiler | 1135 | 0.48 | 0.30 (37/turn) | nets 6 (35.4->41.23), tackles 1 (151.2->176.7), jewellery 3 (96.6->99.75), furniture 8 (14.07->16.91) | premium ham 1 (231->286.9), cloth 24 (8.82->11.2), cookware 5 (21.63->24.13), cheese 2 (6.09->8.26) | +198 |
| Kirchwerp | 1072 | 0.44 | 0.50 (61/turn) | jewellery 5 (96.6->104.5), thread 81 (5->5.7), tackles 1 (151.2->168.15), wine 23 (6.88->7.84) | garments 2 (28.35->41), cookware 5 (19.43->24.13), cloth 16 (9.55->11.2), tools 21 (5.02->5.89) | +179 |

**Best:** Grandgues at about +291 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.98, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| candles | 1 @ 76.0, stop 61 |  | goal planner: buys 1 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 13.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 10 @ min 21 | goal planner: sells 10 at 21 (v2 had 10 at 38.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 82.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.9k (cash + stock at home prices); +302/turn over 6 turns, +99/turn over 24 turns.
- Limits: cash flow >= -435/turn, prestige >= -0.72/turn (values are after 200 tax a turn).
- Today's settings: value +112/turn, cash +78/turn, prestige -2.58/turn - breaks the prestige floor.
- Plan: value +41/turn, cash +51/turn, prestige -0.72/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +447 vs +50, +183 vs +49, +287 vs +60.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Dortgart: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.28: +3/turn
  - ropewalk 1 0.25 -> 0.31: +2/turn
  - flax farm 1 4.64 -> 4.01: -3/turn
  - retting pit 1 0.91 -> 0.80: +4/turn
  - spinnery 1 1.65 -> 1.41: +7/turn
  - sewing shop 1 0.30 -> 0.25: -21/turn
  - weavery 1 0.50 -> 0.40: -3/turn
- Model check over the last 60 turns: predicted +127/turn for the settings we ran, real +117/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.80, beer 3.24, timber 3.58, prestige 60.21, cash 0.00
- Orders it would set: bread buy 5 (v2 8); candles buy 1 (v2 2); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Dortgart (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 7.5/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 426 (+136 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.72 |
| ret | 3 | 0.91 | 0.94 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 75/77, thread 1050/227, cloth 72/127

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.8; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R7 stale ask: limestone ask 16.4 over the market for 6 turns: the town trades ~4 a turn at 15.4, we sold 0 with 46 over what we keep; floor 21.73 (config sell_floor / unit cost) is at or over the market: Taylor's call
