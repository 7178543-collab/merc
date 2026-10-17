# v2 shadow report

Turn 13354, 2026-10-17 19:45. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,481, prestige 3,279 (609 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 144 | 0 | 4 | 0 | 0 | min_holding 60, sell 28, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 132 | 0 | 2 | 0 | 0 | min_holding 30, sell 31, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 274 | 274 | 724 | 27 | 0 | buy 274, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.6 |
| porterage | 11 | 11 | 8 | 0 | 3 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.4 turns (holds 24, next step uses 54/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 51 coin last turn (crew 0.50) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 71
- **grain**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 73 over real use lately; planning 751, not 825

## Prestige spending, cheapest coin per prestige first

1047 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 57.9 | 57.9 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 58.5 | 58.5 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 58.8 | 58.8 |  |
| hold prayer 2 | chapel | 13 | 56.3 | 58.8 | needs a chapel (build cost 31,934); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 59.1 | 59.1 | thin at home: wine, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.6 | 59.6 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 59.6 | 59.6 | thin at home: cured fish |
| jousting 1 | arena | 170 | 59.8 | 60.0 | needs a arena (build cost 24,630); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 58.8 | 61.5 | needs a church (build cost 81,177); thin at home: jewellery, candles, furniture |
| hold feast 2 | townhouse | 2.6 | 58.2 | 61.6 | needs a townhouse (build cost 8,946); thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 63.4 | 63.4 | thin at home: wine, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.5 / 0.50 | 51 | - | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Disscester +74, Cobholme +33, Caillechâtel +32
- Disscester would trade: garments sell 33 @ 25.0; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Disscester | 1474 | 0.58 | 0.30 (30/turn) | garments 33 (19.8->32.87), tools 16 (4.5->5.22) | - | +412 |
| Cobholme | 1564 | 0.63 | 0.50 (50/turn) | beer 30 (2.91->6.51), light armour 2 (86.1->95.95), rope 2 (75.5->77.9) | ploughs 1 (55.65->70.77), cloth 16 (8.19->9.2), fleece 1 (6.98->7.69), salt 3 (4.81->5.56) | +103 |
| Caillechâtel | 488 | 0.13 | 0.10 (10/turn) | beer 17 (2.91->7.12), garments 10 (19.8->20.14), tools 4 (4.5->4.8) | cloth 14 (8.29->9.2), bricks 1 (5.46->12.25), cheese 7 (5.72->6.37), wheels 1 (16.07->18.52) | +92 |
| Rouhomme | 368 | 0.10 | 0.10 (10/turn) | beer 30 (2.91->3.65), cured meat 2 (21.68->26.41), cheese 9 (7.25->8.07), nails 2 (5.78->7.31) | spinning wheels 1 (220.5->258.4), bricks 1 (5.15->12.25), dyed yarn 1 (8.4->9.4), cloth 5 (9.03->9.2) | +80 |
| Heilegg | 826 | 0.23 | 0.20 (20/turn) | tackles 2 (172.2->190), beer 30 (2.91->3.65), nets 6 (38.8->40.47), slaked lime 1 (6.41->9.5) | salt 8 (4.05->5.56), pies 2 (16.38->19.95), cloth 7 (8.24->9.2), fleece 1 (6.51->7.69) | +74 |

**Best:** Disscester at about +412 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 29 @ min 3.7 | makes 28.0, uses 4.2, holds 144 (keeps 60): sells the surplus + 5/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 32 @ min 22.0 | makes 27.5, uses 2.1, holds 132 (keeps 30): sells the surplus + 6/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 301 @ 2.2, stop - |  | uses 751.4/turn (brewery 1, flax farm 1, household), makes 450.0, holds 274 = 0.9 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.8 |  |
| porterage | 8 @ 1.1, stop - |  | uses 8.2/turn (observed), makes 0.0, holds 11 = 1.3 turns |
| rope |  | 7 @ min 73.5 | makes 2.2, uses 0.0, holds 58 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 22 @ min 7.2 | makes 8.4, uses 0.0, holds 519 (keeps 350): sells the surplus + 13/turn of the excess |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 52.3 turns |

## Chain sizing

Mode HOLD, garments sold 11.7/turn (+0.0 exported); plan makes 27.9 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 439 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.77 | 5.76 |
| ret | 3 | 1.03 | 1.02 |
| spin | 4 | 2.11 | 2.11 |
| weave | 3 | 1.08 | 1.08 |
| sew | 2 | 0.67 | 0.68 |

Buffers: flax fibres 58/80, thread 381/235, cloth 24/108
- chain plan needed 438 labour, budget left 438: cut to 438 (sewing capped at 0.68)

## Self-diagnosis

- R1: prestige rate -1.30 a turn vs 12-turn median +2.95; likely: no slot, building or contract cause found: check the impacts
- R3: mansion 1 (mansion) finished but idle 4 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R4: ropewalk 1 projected 0: short of labour (~14 needed); labour itself is not raised here
