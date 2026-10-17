# v2 shadow report

Turn 13337, 2026-10-17 02:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 15,401, prestige 3,241 (571 free, +0.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 205 | 0 | 19 | 0 | 0 | min_holding 60, sell 21, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 19, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 274 | 271 | 721 | 0 | 0 | buy 274, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 45 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 10 | 11 | 11 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 3, next step uses 31/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 76
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 198

## Notes

- labour: projection runs 73 over real use lately; planning 721, not 790

## Prestige spending, cheapest coin per prestige first

1064 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 57.4 | 57.4 | thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 57.7 | 57.7 | thin at home: wine, cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 57.9 | 57.9 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 58.1 | 58.1 | thin at home: cured fish |
| jousting 1 | arena | 170 | 58.4 | 58.5 | needs a arena (build cost 23,803); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 59.3 | 59.3 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 59.7 | 59.7 | running |
| hold prayer 2 | chapel | 13 | 57.7 | 60.0 | needs a chapel (build cost 30,546); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 57.7 | 60.3 | needs a church (build cost 77,122); thin at home: jewellery, candles, furniture |
| hold feast 2 | townhouse | 2.6 | 58.3 | 60.9 | needs a townhouse (build cost 7,136); thin at home: wine |
| hold sermon 2 | church | 24 | 57.7 | 61.0 | needs a church (build cost 77,122); thin at home: jewellery, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 5 | -109 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Caillechâtel +31, Clarfranche +21, Fulkirch +18, Marmont +17, Etallaen +17
- Caillechâtel would trade: nets sell 10 @ 38.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.70 (69/turn) | bread 142 (2.31->3.08), thread 25 (4.66->6.13), charcoal 13 (1.8->4.37), axes 1 (18.06->36.67) | flax plants 2 (0.66->1.61), tools 3 (4.91->5.15) | +167 |
| Brebronn | 862 | 0.24 | 0.20 (20/turn) | wrought iron 9 (14.07->26.22), beer 20 (2.96->5.75), nets 1 (34.2->40.85) | cloth 20 (8.35->8.8), wool 1 (8.82->10.07) | +162 |
| Caillechâtel | 488 | 0.13 | 0.10 (10/turn) | nets 10 (34.2->37.24), garments 10 (19.77->20.9), beer 20 (2.96->3.57), canvas 1 (31.29->33.44) | rope 2 (70.88->75.52), cloth 8 (8.45->8.8), wool 1 (8.35->10.07) | +60 |
| Unterhufe | 595 | 0.16 | 0.10 (10/turn) | garments 13 (19.77->22.42), yarn 6 (5.41->7.89), paper 1 (21->23.18), tools 9 (4.5->4.84) | beer 19 (3.11->3.7) | +55 |
| Orlesailles | 1178 | 0.41 | 0.20 (20/turn) | garments 13 (19.77->22.61), thread 15 (4.66->6.27), glassware 1 (50.19->52.25), nets 1 (34.2->36.29) | cloth 6 (8.24->8.8), pies 2 (17.32->18.9) | +53 |

**Best:** Rouhomme at about +167 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 20 @ min 3.7 | makes 28.0, uses 19.2, holds 205 (keeps 60): sells the surplus + 11/turn of the excess |
| cured meat | 7 @ 24.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 23 = 3.8 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 271 @ 2.2, stop - |  | uses 721.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 274 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 | makes 9.0, uses 0.0, holds 45 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 11 @ 1.1, stop - |  | uses 11.0/turn (observed), makes 0.0, holds 10 = 0.9 turns |
| rope |  | 6 @ min 77.5 | makes 4.5, uses 0.0, holds 17 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 9 = 9.3 turns |
| timber |  | 27 @ min 6.7 | makes 8.4, uses 0.0, holds 585 (keeps 350): sells the surplus + 19/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 50.5 turns |

## Chain sizing

Mode HOLD, garments sold 19.5/turn (+0.0 exported); plan makes 17.6 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 390 (+6 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.18 | 6.20 |
| ret | 3 | 1.10 | 1.10 |
| spin | 4 | 2.26 | 2.27 |
| weave | 3 | 0.69 | 0.68 |
| sew | 2 | 0.39 | 0.43 |

Buffers: flax fibres 57/85, thread 389/250, cloth 3/68
- chain plan needed 583 labour, budget left 389: cut to 389 (sewing capped at 0.43)

## Self-diagnosis

- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
