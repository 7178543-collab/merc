# v2 shadow report

Turn 13375, 2026-10-18 16:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,440, prestige 3,300 (630 free, +47.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 398 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 293 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 21.2 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 82 | 110 | 537 | 0 | 23 | buy 98, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 69 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 9 | 0 | 2 | buy 11, buy @ 1.1 |

**0 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 23 labour expired last turn (~37 coin): holding 82 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cloth**: cloth buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 51
- **furniture**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 73 over real use lately; planning 592, not 666

## Prestige spending, cheapest coin per prestige first

1026 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold prayer 2 | chapel | 13 | 54.1 | 56.5 | needs a chapel (build cost 30,524); thin at home: furniture |
| hold feast 2 | townhouse | 2.6 | 53.9 | 56.6 | needs a townhouse (build cost 6,938); thin at home: wine |
| jousting 1 | arena | 170 | 56.5 | 56.6 | needs a arena (build cost 23,930); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 57.3 | 57.3 | thin at home: wine, cured fish |
| hold sermon 2 (candles) | church | 31 | 54.9 | 57.6 | needs a church (build cost 78,548); thin at home: jewellery, candles, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 58.9 | 58.9 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.0 | 59.0 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 55.5 | 59.0 | needs a church (build cost 78,548); thin at home: jewellery, furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 59.3 | 59.3 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 60.8 | 60.8 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 61.9 | 61.9 | thin at home: pasties, hop beer, pies, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.7 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.45 / 0.03 | 3 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 29 @ 14.0, pasties buy 2 @ 12.2; crew 0.1; est +363 a turn; stock: furniture 29 @ 14.0 (keep 140); stock: pasties 2 @ 12.2 (keep 14)
- **Flax Wyrm** on Disscester: furniture buy 11 @ 11.3, pasties buy 4 @ 15.3; crew 0.4; est +141 a turn; stock: furniture 11 @ 11.3 (keep 140); stock: pasties 4 @ 15.3 (keep 14)
- best towns now: Großaue +419, Pontmont +374, Rouhomme +365, Grandgues +363, Heilegg +361
- Großaue would trade: furniture buy 33 @ 12.1, pasties buy 2 @ 16.0; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Chatgnan | 728 | 0.19 | 0.30 (29/turn) | beer 51 (2.99->4.75), nails 6 (5.83->9.12), fleece 1 (7.35->7.55), rope 1 (79.5->80.27) | thread 7 (4.91->5.2), flax fibres 2 (5.67->6.25) | +84 |
| Etallaen | 774 | 0.20 | 0.30 (29/turn) | tools 9 (4.24->6.65), beer 51 (2.99->3.69), cured fish 4 (26.04->29.83), blades 1 (22.05->32.3) | - | +68 |
| Neuborn | 780 | 0.20 | 0.70 (69/turn) | rope 3 (79.5->85.5), seeds 15 (1.78->3.32), beer 51 (2.99->3.7), charcoal 12 (2.52->4.75) | cheese 15 (5.88->6.22), thread 3 (4.7->5.2) | +68 |
| Vauxvais | 204 | 0.05 | 0.10 (10/turn) | cookware 15 (23.31->25.27), rope 3 (79.5->83.6), beer 51 (2.99->3.13), fleece 1 (7.35->7.55) | flax fibres 18 (5.88->6.25), thread 8 (4.66->5.2), dyed yarn 1 (9.03->9.69) | +52 |
| Disscester | 1474 | 0.56 | 0.10 (10/turn) | soap 1 (91.35->148.2), wine 1 (5.67->7.5) | honey 1 (6.77->8.31) | +50 |

**Best:** Chatgnan at about +84 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 50 @ min 3.54 | makes 28.0, uses 4.2, holds 398 (keeps 60): sells the surplus + 26/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| furniture | 1 @ 15.5, stop 2 |  | uses 0.4/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| garments |  | 32 @ min 21.2 | makes 13.1, uses 2.1, holds 293 (keeps 30): sells the surplus + 21/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 142 @ 2.2, stop - |  | uses 592.3/turn (brewery 1, flax farm 1, household), makes 450.0, holds 82 = 0.6 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 13 @ min 37.4 | makes 9.0, uses 0.0, holds 69 (keeps 15): sells the surplus + 4/turn of the excess |
| porterage | 4 @ 1.1, stop - |  | uses 4.2/turn (observed), makes 0.0, holds 11 = 2.6 turns |
| rope |  | 7 @ min 77.5 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 8 @ min 6.7 |  |
| tools | 4 @ 6.2, stop 26 |  | uses 3.2/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 63.1 turns |

## Chain sizing

Mode HOLD, garments sold 6.8/turn (+0.0 exported); plan makes 18.9 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 327 (+64 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.98 | 4.58 |
| ret | 3 | 0.71 | 0.81 |
| spin | 4 | 1.46 | 1.68 |
| weave | 3 | 0.51 | 0.73 |
| sew | 2 | 0.32 | 0.46 |

Buffers: flax fibres 59/68, thread 395/200, cloth 33/73

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 31.2, home ask 24.8; our bid is already at/over the ask (sellers too thin)
- R1: furniture slot dry: 0.0 held, 1.4 a turn (household slot (+0.4 prestige)); our buy 2 @ 15.5, home ask none (no sellers at home)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R4: logging camp w/ tool, ropewalk 1 projected 0: short of labour (~36 needed); labour itself is not raised here
