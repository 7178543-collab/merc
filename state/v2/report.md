# v2 shadow report

Turn 13542, 2026-10-25 15:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,518, prestige 3,582 (462 free, +19.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 0 | 6 | 0 | 0 | buy @ 2.4; sell 1, sell @ 1.76 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 61 | 28 | 29 | 0 | 0 | stop 111, buy 28, buy @ 3.7 |
| labour | 5 | 55 | 527 | 0 | 28 | buy 5, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 13, sell @ 33.6 |
| porterage | 14 | 14 | 13 | 0 | 1 | buy 14, buy @ 1.1 |

**1 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy

## Waste (money lost now)

- **labour**: 28 labour expired last turn (~45 coin): holding 5 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax plants**: flax plants buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 103 over real use lately; planning 548, not 651

## Prestige spending, cheapest coin per prestige first

859 turns left: prestige gained now converts 98.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.1 | 47.1 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.6 | 47.6 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.4 | 48.4 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.4 | 50.4 | thin at home: pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.8 | 50.8 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 50.8 | 50.8 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 51.8 | 51.8 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 51.8 | 51.8 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 52.8 | 52.8 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 52.8 | 52.8 |  |
| jousting 3 | arena | 230 | 53.0 | 53.2 | needs a arena (build cost 23,366); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 51.4 | 54.2 | needs a chapel (build cost 29,200) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Birkeningen | 1006 | 0.32 | 0.20 (19/turn) | grindstones 1 (224.7->334.4), tackles 1 (163.8->178.6), premium ham 1 (306.6->315.4), garments 1 (18.1->18.62) | malt 1 (5.25->6.17) | +115 |
| Magdeach | 667 | 0.17 | 0.10 (10/turn) | grindstones 1 (224.7->279.3), leather 1 (31.29->41.99), steel ingots 1 (15.65->15.86) | pasties 2 (10.08->14.2), malt 4 (5.62->6.17), flax fibres 1 (4.75->5.55), ploughs 2 (69.83->71.72) | +67 |
| Neuborn | 780 | 0.20 | 0.50 (49/turn) | beer 55 (3.14->4.05), nets 3 (34->38), charcoal 11 (1.94->4.16), grindstones 1 (224.7->231.8) | cheese 16 (4.83->5.46), thread 10 (3.97->4.68), flax fibres 9 (4.94->5.55) | +61 |
| Vauxvais | 204 | 0.05 | 0.30 (29/turn) | bread 143 (2.16->2.66), charcoal 11 (1.94->2.39) | candles 1 (64.58->68.5), pasties 2 (12.39->14.2), thread 13 (4.41->4.68), beer 6 (3.17->3.5) | +59 |
| Orlesailles | 1178 | 0.40 | 0.30 (29/turn) | thread 33 (4.66->6.27), nets 3 (34->36.48), cured fish 5 (25.41->26.6) | gears 2 (56.7->59.38), candles 1 (66.67->68.5), pasties 2 (12.6->14.2), silver ore 1 (34.02->36.1) | +50 |

**Best:** Birkeningen at about +115 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.38) |
| candles | 2 @ 70, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 1 @ 29.0, stop 4 |  | uses 0.9/turn (mansion 1), makes 0.0, holds 4 = 4.2 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 0 @ 2.4, stop 13 | 1 @ min 1.77 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 7 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 1 @ min 5.45 | goal planner: trial sale of an idle pile, 1 a turn at 5.45, keeps 82 (8 over) |
| furniture | 2 @ 13.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 27 @ 3.7, stop 107 |  | goal planner: buys 27 a turn for today's rates, keeps up to 107 (v2 had 56) |
| labour | 4 @ 2.2, stop - |  | goal planner: buys 4 for today's rates (v2 had 48) |
| light armour | 1 @ 87.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 13 @ min 33.6 | goal planner: sells 13 at 33.6 (v2 had 13 at 34.0) |
| pasties | 2 @ 14.5, stop 8 |  | goal planner: buys 2 a turn for today's rates, keeps up to 8 (v2 had 6) |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 7) |
| rope |  | 1 @ min 72.0 |  |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| thread |  | 15 @ min 4.5 | goal planner: sells 15 a turn at 4.5, keeps 205 (no one offered it) |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 199 = 74.5 turns |
| varnish | 1 @ 20.4, stop 1 |  | uses 0.2/turn (net maker152202386007001), makes 0.0, holds 0 = 1.6 turns |
| wax | 1 @ 21.2, stop 1 |  | uses 0.2/turn (net maker152202386007001), makes 0.0, holds 1 = 3.5 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.5k (cash + stock at home prices); -48/turn over 6 turns, +31/turn over 24 turns.
- Limits: cash flow >= +20/turn, prestige >= -0.68/turn (values are after 220 tax a turn).
- Today's settings: value +103/turn, cash +58/turn, prestige +19.24/turn.
- Plan: value +525/turn, cash +433/turn, prestige +10.59/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +472 vs +136, -243 vs -48, -44 vs +43.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +9/turn
  - ship Flax Wyrm -> Magdeach: +6/turn
  - mansion 1 0.15 -> 0.00: +28/turn
  - ropewalk 1 0.25 -> 1.00: +27/turn
  - net maker 0.73 -> 0.00: +30/turn
  - net maker [make nets 1] 0.00 -> 0.28: +3/turn
  - park 1 16.00 -> 0.00: +13/turn
  - spinnery 1 1.59 -> 2.60: +127/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 11.38: +33/turn
  - weavery 1 0.13 -> 0.37: +28/turn
- Model check over the last 48 turns: predicted +97/turn for the settings we ran, real +48/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 0.84, thread 2.10, cloth 3.36, flax fibres 2.50, garments 9.71, nets 15.74, beer 2.15, timber 2.92, prestige 0.00, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); flax fibres sell 1 (v2 none); furniture buy 2 (v2 None); grain buy 27 (v2 56); labour buy 4 (v2 48); light armour buy 1 (v2 None); pasties buy 2 (v2 6); porterage buy 14 (v2 7); thread sell 15 (v2 none)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 11.38, worth +0/turn.
- Recipe: retting pit 1 retting 2 -> retting 1 at 2.19, worth +488/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.28, worth +20/turn.
- Ship linen snake: Grandgues -> Vauxvais (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Magdeach (+6/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +42/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~4014 coin: +22/turn, payback 186 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate park 1: +96/turn (tax 96 saved).
- Trim: donate logging camp w/ tool: +20/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 2.3/turn (+0.0 exported); plan makes 32.0 garments a turn.
Labour: own 500, everything else 406, chain may buy 350 -> chain allowance 444, chain plan 441 (+194 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.29 | 5.15 |
| ret | 3 | 1.12 | 0.92 |
| spin | 4 | 1.59 | 1.89 |
| weave | 3 | 0.13 | 1.25 |
| sew | 2 | 0.09 | 0.78 |

Buffers: flax fibres 89/85, thread 827/249, cloth 0/125

## Self-diagnosis

Nothing found this run.
