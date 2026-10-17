# v2 shadow report

Turn 13350, 2026-10-17 15:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,369, prestige 3,280 (610 free, +2.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 121 | 0 | 19 | 0 | 0 | min_holding 60, sell 14, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 73 | 0 | 2 | 0 | 0 | min_holding 30, sell 24, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 276 | 281 | 731 | 0 | 0 | buy 276, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.2 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.5 turns (holds 23, next step uses 50/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 65

## Notes

- labour: projection runs 73 over real use lately; planning 731, not 804

## Prestige spending, cheapest coin per prestige first

1051 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 57.3 | 57.3 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 57.8 | 57.8 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.5 | 58.5 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 58.9 | 58.9 |  |
| hold prayer 2 | chapel | 13 | 56.7 | 59.2 | needs a chapel (build cost 32,286); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 57.4 | 60.0 | needs a church (build cost 80,152); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 57.1 | 60.6 | needs a church (build cost 80,152); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 58.5 | 61.5 | needs a townhouse (build cost 8,242); thin at home: wine |
| hold mass 2 (premium) | cathedral | 360 | 62.2 | 63.3 | needs a cathedral (build cost 354,961); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 (pies) | mansion | 18 | 63.6 | 63.6 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 64.0 | 64.0 | thin at home: pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 110801910 | 0.036 | rope 1 | cured meat 4 | -60 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 5 | -108 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Karlmoor: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Fulkirch +28, Neuborn +25, Hofkirchen +19
- Fulkirch would trade: candles buy 1 @ 70.5, rope sell 5 @ 79.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.32 | 0.70 (71/turn) | tackles 2 (169.05->185.25), thread 13 (4.66->5.13), flax fibres 4 (5.4->6.17), resin 2 (2.48->3.72) | beer 79 (3.28->5.42), cured meat 6 (21->23.2), candles 1 (73.5->81.5), bricks 1 (4.64->12.16) | +171 |
| Magdeach | 667 | 0.18 | 0.40 (41/turn) | garments 17 (19.58->20.33), tools 8 (4.5->5.13) | beer 79 (3.19->5.42), bricks 1 (6.09->12.16), cheese 8 (5.67->6.08), cured meat 6 (22.47->23.2) | +167 |
| Vauxvais | 204 | 0.06 | 0.10 (10/turn) | rope 3 (74->78.38), soap 2 (81.9->85.02), garments 23 (19.58->19.76), nets 5 (37.4->37.81) | beer 69 (3.4->5.42), grain 13 (3.13->3.32) | +155 |
| Grandgues | 152 | 0.04 | 0.30 (30/turn) | bread 152 (2.27->2.41), tools 8 (4.5->4.73), charcoal 12 (2.37->2.81), firewood 1 (1.61->4.01) | beer 79 (3.99->5.42), pies 2 (16.28->20.33), bricks 1 (7.35->12.16), cloth 6 (7.3->7.9) | +132 |
| Blanans | 297 | 0.08 | 0.20 (20/turn) | salt 4 (4.75->6.79), thread 9 (4.66->4.94), soap 1 (81.9->82.65), resin 2 (2.48->2.74) | beer 78 (3.82->5.42), bricks 1 (5.83->12.16), grain 13 (2.94->3.32), candles 1 (80.33->81.5) | +131 |

**Best:** Hofkirchen at about +171 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 13 @ min 5.55 | makes 28.0, uses 19.2, holds 121 (keeps 60): sells the surplus + 4/turn of the excess |
| cured meat | 9 @ 24.2, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 19 = 3.2 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 25 @ min 22.0 | makes 25.4, uses 2.1, holds 73 (keeps 30): sells the surplus + 2/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 281 @ 2.2, stop - |  | uses 731.1/turn (brewery 1, flax farm 1, household), makes 450.0, holds 276 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.4 |  |
| porterage | 10 @ 1.1, stop - |  | uses 10.0/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 6 @ min 72.0 | makes 2.2, uses 0.0, holds 52 (keeps 0): sells the surplus + 4/turn of the excess |
| timber |  | 26 @ min 6.7 | makes 8.4, uses 0.0, holds 572 (keeps 350): sells the surplus + 18/turn of the excess |
| tools | 4 @ 6.2, stop 30 |  | uses 3.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 55.1 turns |

## Chain sizing

Mode HOLD, garments sold 13.3/turn (+0.0 exported); plan makes 25.0 garments a turn.
Labour: own 450, everything else 397, chain may buy 350 -> chain allowance 403, chain plan 404 (+2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.30 | 5.39 |
| ret | 3 | 0.94 | 0.96 |
| spin | 4 | 1.94 | 1.97 |
| weave | 3 | 0.99 | 0.97 |
| sew | 2 | 0.62 | 0.61 |

Buffers: flax fibres 57/76, thread 386/224, cloth 23/97
- chain plan needed 477 labour, budget left 403: cut to 403 (sewing capped at 0.61)

## Self-diagnosis

- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
