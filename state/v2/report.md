# v2 shadow report

Turn 13348, 2026-10-17 13:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,396, prestige 3,274 (604 free, +2.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 131 | 0 | 19 | 0 | 0 | min_holding 60, sell 14, sell @ 5.1 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 47 | 0 | 2 | 0 | 0 | min_holding 30, sell 16, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 290 | 282 | 731 | 0 | 1 | buy 290, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 35.6 |
| porterage | 11 | 11 | 10 | 0 | 1 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.5 turns (holds 24, next step uses 50/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 65

## Notes

- labour: projection runs 73 over real use lately; planning 731, not 805

## Prestige spending, cheapest coin per prestige first

1053 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 57.4 | 57.4 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 58.0 | 58.0 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.5 | 58.5 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 58.8 | 58.8 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 58.9 | 58.9 |  |
| hold prayer 2 | chapel | 13 | 56.5 | 58.9 | needs a chapel (build cost 32,192); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 57.2 | 59.8 | needs a church (build cost 79,945); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 56.9 | 60.3 | needs a church (build cost 79,945); thin at home: jewellery, furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 60.8 | 60.8 | running |
| hold feast 2 | townhouse | 2.6 | 58.2 | 61.3 | needs a townhouse (build cost 8,204); thin at home: wine |
| hold mass 2 (premium) | cathedral | 360 | 62.2 | 63.2 | needs a cathedral (build cost 354,161); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 110801910 | 0.08 | nets 2, rope 4 | cured meat 1 | 122 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 5 | -108 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Karlmoor: nothing pays; crew 0.0; est +0 a turn; best orders clear only 0 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Neuborn +39, Brunnham +30, Hofkirchen +20, Grandgues +19, Bordetes +16
- Neuborn would trade: candles buy 1 @ 74.0, cured meat buy 6 @ 20.4, rope sell 2 @ 85.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clairas | 374 | 0.10 | 0.20 (20/turn) | tools 16 (4.5->6.03), garments 24 (19.46->19.76), rope 3 (74->75.05), firewood 1 (1.62->5.27) | beer 78 (3.28->5.37), flax fibres 10 (5.83->6.9), candles 1 (77.7->81.5), arms 4 (28.98->29.83) | +197 |
| Grandgues | 152 | 0.04 | 0.20 (20/turn) | rope 2 (74->80.27), wheels 2 (17.12->20.52), garments 24 (19.46->19.76), charcoal 12 (1.73->2.3) | beer 82 (3.99->5.37), flax fibres 6 (5.41->6.9), arms 4 (28.35->29.83), grain 13 (2.81->3.34) | +173 |
| Karlmoor | 787 | 0.21 | 0.40 (40/turn) | nets 4 (37.2->50.35), tackles 1 (169.05->185.25), wheels 1 (17.12->22.8), flax plants 1 (1.26->1.92) | beer 78 (3.91->5.37), candles 1 (74.55->81.5), grain 13 (2.65->3.34) | +163 |
| Gosschweig | 1099 | 0.38 | 0.70 (70/turn) | nets 1 (37.2->43.13), wheels 2 (17.12->20.52), thread 15 (4.66->5.22), garments 22 (19.46->19.95) | beer 82 (2.96->5.37), candles 1 (73.5->81.5), tar 2 (10.4->11.4) | +162 |
| Pontmont | 341 | 0.09 | 0.30 (30/turn) | cheese 18 (6.67->9.26), wheels 2 (17.12->19.38), tools 16 (4.5->4.71), cloth 1 (7.3->7.65) | beer 82 (3.99->5.37), arms 4 (28.35->29.83), bricks 1 (5.62->11.97), potash 1 (13.65->16.05) | +160 |

**Best:** Clairas at about +197 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ ?, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 14 @ min 3.7 | makes 28.0, uses 19.2, holds 131 (keeps 60): sells the surplus + 5/turn of the excess |
| cured meat | 10 @ 24.4, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 16 = 2.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 23 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 281 @ 2.2, stop - |  | uses 731.3/turn (brewery 1, flax farm 1, household), makes 450.0, holds 290 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.2 |  |
| porterage | 10 @ 1.1, stop - |  | uses 10.0/turn (observed), makes 0.0, holds 11 = 1.1 turns |
| rope |  | 6 @ min 72.0 | makes 2.2, uses 0.0, holds 48 (keeps 0): sells the surplus + 4/turn of the excess |
| timber |  | 28 @ min 6.7 | makes 8.4, uses 0.0, holds 595 (keeps 350): sells the surplus + 20/turn of the excess |
| tools | 4 @ 6.2, stop 30 |  | uses 3.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 54.9 turns |

## Chain sizing

Mode HOLD, garments sold 14.6/turn (+0.0 exported); plan makes 25.4 garments a turn.
Labour: own 450, everything else 397, chain may buy 350 -> chain allowance 403, chain plan 404 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.30 | 5.33 |
| ret | 3 | 0.94 | 0.95 |
| spin | 4 | 1.94 | 1.95 |
| weave | 3 | 0.99 | 0.99 |
| sew | 2 | 0.62 | 0.62 |

Buffers: flax fibres 58/77, thread 409/226, cloth 24/99
- chain plan needed 491 labour, budget left 403: cut to 403 (sewing capped at 0.62)

## Self-diagnosis

- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
