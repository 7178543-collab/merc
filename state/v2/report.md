# v2 shadow report

Turn 13480, 2026-10-23 01:47. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,379, prestige 3,620 (500 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 111 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 94 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 212 | 212 | 702 | 0 | 10 | buy 212, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.5 turns (holds 17, next step uses 32/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 180

## Notes

- labour: projection runs 75 over real use lately; planning 702, not 777

## Prestige spending, cheapest coin per prestige first

921 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.5 | 49.5 | thin at home: hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 50.8 | 50.8 | thin at home: hop beer, pies |
| jousting 3 | arena | 230 | 52.2 | 52.3 | needs a arena (build cost 24,713); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.6 | 52.6 | thin at home: wine, hop beer, ham |
| hold banquet 2 (pies) | mansion | 7 | 53.0 | 53.0 | thin at home: wine, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 53.1 | 53.1 | thin at home: hop beer, cured meat |
| hold banquet 3 (fish) | mansion | 7.6 | 53.4 | 53.4 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 51.4 | 53.9 | needs a church (build cost 65,326); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 51.5 | 54.3 | needs a chapel (build cost 31,559); thin at home: furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 54.4 | 54.4 | thin at home: wine, cured meat |
| hold banquet 1 (fish) | mansion | 4.2 | 54.5 | 54.5 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Neuborn | 780 | 0.21 | 1.00 (100/turn) | bread 127 (2.27->3.46), furniture 10 (13.02->15.2), seeds 6 (2.21->3.32), grain 7 (2.58->3.17) | cheese 9 (4.94->5.51), wax 1 (20.06->22.23) | +103 |
| Heilegg | 826 | 0.23 | 0.10 (10/turn) | grindstones 1 (224.7->311.6), ham 1 (60.9->67.45), lead ore 1 (8.93->14.54), yarn 4 (4.14->4.71) | wax 2 (20.48->22.23), salt 4 (4.09->4.54) | +95 |
| Chribruck | 1202 | 0.43 | 0.30 (30/turn) | grindstones 1 (224.7->286.9), lead ore 4 (8.93->19.19), mouldboards 1 (31.71->34.01), coats 1 (74.55->76) | wax 2 (20.68->22.23), flax fibres 3 (4.54->5.5) | +86 |
| Fontaux | 411 | 0.11 | 0.30 (30/turn) | cheese 11 (6.14->9.79), charcoal 13 (2.02->4.6), casks 5 (5.62->9.5), tools 14 (4.68->5.32) | - | +82 |
| Kirchwerp | 1072 | 0.36 | 0.50 (50/turn) | soap 2 (91.88->119.7), grindstones 1 (224.7->247), furniture 12 (13.02->14.82), lead ore 2 (8.93->12.35) | garments 2 (19.32->19.9), wax 2 (21.84->22.23) | +78 |

**Best:** Neuborn at about +103 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 27 @ min 20.0 | makes 16.4, uses 2.1, holds 94 (keeps 30): sells the surplus + 12/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 202 @ 2.2, stop - |  | uses 701.7/turn (brewery 1, flax farm 1, household), makes 500.0, holds 212 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.4 |  |
| pasties | 3 @ 13.1, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.4/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 74.0 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 53.1 turns |

## Goal: business value (shadow)
- Value now 15.8k (cash + stock at home prices); +79/turn over 6 turns, -96/turn over 24 turns.
- Limits: cash flow >= +68/turn, prestige >= -0.83/turn (after 236 tax and crew).
- Today's settings: value +57/turn, cash +62/turn, prestige -1.51/turn - breaks the prestige floor and cash floor.
- Plan: value +111/turn, cash +282/turn, prestige -0.83/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.50 -> 1.00: +23/turn
  - logging camp w/ tool 7.00 -> 3.12: +11/turn
  - ropewalk 1 0.50 -> 0.44: +7/turn
  - quarry 1 0.00 -> 0.08: +4/turn
  - sewing shop 1 0.40 -> 0.18: -16/turn
  - weavery 1 0.67 -> 0.29: +21/turn
  - spinnery 1 2.05 -> 1.66: +25/turn
  - retting pit 1 1.00 -> 0.81: +4/turn
  - flax farm 1 5.61 -> 4.53: +11/turn
  - mansion 1 0.00 -> 0.16: -36/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.61, thread 3.97, cloth 6.39, flax fibres 4.59, garments 18.55, nets 34.60, beer 2.82, timber 5.33, prestige 52.35, cash 0.00
- Investments:
  - Tenants L13 for 500 prestige: +80/turn (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 6.2/turn (+0.0 exported); plan makes 22.6 garments a turn.
Labour: own 500, everything else 415, chain may buy 350 -> chain allowance 435, chain plan 435 (+76 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.61 | 6.44 |
| ret | 3 | 1.00 | 1.14 |
| spin | 4 | 2.05 | 2.36 |
| weave | 3 | 0.67 | 0.89 |
| sew | 2 | 0.40 | 0.55 |

Buffers: flax fibres 46/80, thread 217/236, cloth 17/89
- chain plan needed 508 labour, budget left 435: cut to 435 (sewing capped at 0.55)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
