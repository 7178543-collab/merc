# v2 shadow report

Turn 13345, 2026-10-17 10:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,235, prestige 3,265 (595 free, +3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 150 | 0 | 19 | 0 | 0 | min_holding 60, sell 16, sell @ 4.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 299 | 274 | 724 | 33 | 0 | buy 299, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 27 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 35.6 |
| porterage | 11 | 11 | 10 | 0 | 1 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.8 turns (holds 25, next step uses 31/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 64 coin last turn (crew 0.66) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 78
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 73 over real use lately; planning 757, not 830

## Prestige spending, cheapest coin per prestige first

1056 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 57.9 | 57.9 | thin at home: wine, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.1 | 58.1 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 56.1 | 58.3 | needs a chapel (build cost 28,586); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 58.4 | 58.4 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 58.6 | 58.6 |  |
| jousting 1 | arena | 170 | 59.0 | 59.1 | needs a arena (build cost 22,620); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 56.8 | 59.3 | needs a church (build cost 74,392); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 56.5 | 59.7 | needs a church (build cost 74,392); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 57.8 | 60.9 | needs a townhouse (build cost 8,128); thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 62.5 | 62.5 | thin at home: wine |
| hold mass 2 (premium) | cathedral | 360 | 61.5 | 62.5 | needs a cathedral (build cost 336,961); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.66 / 0.66 | 64 | 110801910 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Karlmoor: nets sell 8 @ 47.4; crew 0.1; est +74 a turn
- **linen snake** on Heilegg: candles buy 1 @ 74.0, cured meat buy 6 @ 19.5; crew 0.1; est +21 a turn
- best towns now: Karlmoor +74, Heilegg +29, Donaunieder +19, Neuborn +17
- Karlmoor would trade: nets sell 8 @ 47.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Karlmoor | 787 | 0.21 | 0.10 (10/turn) | nets 8 (36.6->49.88), stockfish 1 (109.2->133), garments 13 (19.4->21.09), tackles 1 (168->183.35) | grain 13 (2.65->3.36) | +169 |
| Vauxvais | 204 | 0.05 | 0.30 (29/turn) | soap 2 (75.6->85.02), garments 13 (19.4->20.71), bread 149 (2.31->2.56), rope 3 (73->76.47) | beer 61 (3.44->4.46), grain 13 (3.19->3.36), yarn 3 (4.3->4.46) | +120 |
| Gosschweig | 1099 | 0.37 | 0.50 (49/turn) | soap 1 (75.6->110.2), glassware 2 (54.6->58.9), garments 13 (19.4->19.95), thread 9 (4.66->5.22) | beer 61 (2.96->4.46), candles 1 (73.5->81), tools 3 (3.63->4.98), hop beer 1 (7.88->8.74) | +105 |
| Fontaux | 411 | 0.11 | 0.30 (29/turn) | salt 11 (4.07->7.79), garments 13 (19.4->20.71), flax fibres 4 (4.72->6.08), limestone 1 (11.45->20.71) | beer 49 (3.86->4.46), flax plants 7 (0.72->1.58), grain 13 (2.86->3.36), candles 1 (78.75->81) | +105 |
| Coburgbaum | 619 | 0.16 | 0.40 (39/turn) | garments 13 (19.4->23.37), nets 2 (36.6->41.42), tools 12 (4.5->5.42), soap 1 (75.6->83.6) | beer 46 (3.84->4.46), grain 13 (2.86->3.36), candles 1 (79.8->81) | +100 |

**Best:** Karlmoor at about +169 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ ?, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 16 @ min 4.56 | makes 28.0, uses 19.2, holds 150 (keeps 60): sells the surplus + 7/turn of the excess |
| cured meat | 12 @ 24.4, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 10 = 1.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 307 @ 2.2, stop - |  | uses 757.1/turn (brewery 1, flax farm 1, household), makes 450.0, holds 299 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 35.6 | sell; ships offer 8 a turn abroad, so home sells 10 (was 9) |
| porterage | 11 @ 1.1, stop - |  | uses 11.1/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 8 @ min 71.0 | makes 4.5, uses 0.0, holds 41 (keeps 0): sells the surplus + 3/turn of the excess |
| timber |  | 30 @ min 6.7 | makes 8.4, uses 0.0, holds 612 (keeps 350): sells the surplus + 21/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 50.0 turns |

## Chain sizing

Mode HOLD, garments sold 15.8/turn (+0.0 exported); plan makes 18.4 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 390 (+3 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.30 | 6.07 |
| ret | 3 | 1.12 | 1.08 |
| spin | 4 | 2.31 | 2.22 |
| weave | 3 | 0.66 | 0.72 |
| sew | 2 | 0.39 | 0.45 |

Buffers: flax fibres 58/86, thread 442/254, cloth 25/72
- chain plan needed 573 labour, budget left 389: cut to 389 (sewing capped at 0.45)

## Self-diagnosis

- R1: cured meat slot dry: 10.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 6 @ 29, home ask 23.4; our bid is already at/over the ask (sellers too thin)
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
