# v2 shadow report

Turn 13283, 2026-10-14 20:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,151, prestige 0 (-2,670 free, +0.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 283 | 0 | 19 | 0 | 0 | min_holding 60, sell 52, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 99 | 0 | 2 | 0 | 0 | min_holding 30, sell 18, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 273 | 313 | 656 | 0 | 107 | buy 273, buy @ 2.2 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 52 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 42.6 |
| porterage | 37 | 37 | 25 | 0 | 12 | buy 37, buy @ 0.8 |

**0 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 107 labour expired last turn (~173 coin): holding 273 against a ~34 buffer target -> v2: trim the buy until the stock is near 34

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (447.0 held, 20 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 50% (EXPANSION), about 6 turns left; still to deliver: labour 130, limestone 30, timber 20; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 30 | 114.2 | 0 | off: covered |
| timber | 20 | 447.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1118 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 52.2 | running |
| hold banquet 2 (pies) | mansion | 7 | 54.6 | 54.6 | thin at home: wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 55.5 | 55.5 | thin at home: pies |
| hold prayer 2 | chapel | 13 | 54.2 | 56.7 | needs a chapel (build cost 34,944); thin at home: furniture |
| hold banquet 4 (pies) | mansion | 18 | 57.1 | 57.1 | thin at home: wine, pies |
| jousting 1 | arena | 170 | 57.4 | 57.6 | needs a arena (build cost 26,990); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 56.1 | 58.5 | needs a church (build cost 76,757); thin at home: jewellery, furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 59.0 | 59.0 | thin at home: wine |
| jousting 3 | arena | 230 | 60.2 | 60.4 | needs a arena (build cost 26,990); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 60.7 | 60.7 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 60.9 | 60.9 | running |
| hold banquet 4 | mansion | 17.5 | 61.5 | 61.5 | thin at home: wine, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 108202735 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Toqueque: cheese sell 5 @ 10.3, salt sell 4 @ 8.7, tar buy 1 @ 10.4, wool buy 2 @ 9.7, yarn buy 9 @ 4.16; crew 0.1; est +34 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Kirchwerp +118, Darmwald +80, Großmühle +61, Corstoft +47, Gosschweig +35
- Kirchwerp would trade: acid buy 1 @ 146, medicine buy 1 @ 133, wool buy 2 @ 9.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.36 | 0.50 (51/turn) | beer 55 (3.16->4.33), flax fibres 5 (5.14->6.84) | garments 20 (22.26->25.65), acid 1 (150.15->209), medicine 1 (136.5->181.45), jewellery 1 (87.67->109.25) | +223 |
| Pontmont | 341 | 0.09 | 0.60 (61/turn) | rope 4 (73.5->81.7), beer 55 (3.16->3.76), bread 135 (2.42->2.79), cheese 17 (6.51->6.89) | garments 20 (21.84->25.65), wool 2 (9.92->14.34), nets 1 (35.28->41.61), wheels 3 (21.84->22.23) | +161 |
| Rouhomme | 368 | 0.10 | 0.80 (81/turn) | bread 135 (2.42->3.25), beer 55 (3.16->3.65), charcoal 2 (2.18->3.86), flour 1 (25.62->28.88) | garments 20 (23.31->25.65), wool 1 (8.87->14.34), tools 6 (4.91->5.1), mouldboards 1 (43.26->43.51) | +150 |
| Grandgues | 152 | 0.04 | 0.20 (20/turn) | flax fibres 7 (5.14->8.79), timber 20 (6.31->7.5), rope 1 (73.5->77.42), beer 55 (3.16->3.29) | garments 20 (22.68->25.65), jewellery 1 (80.85->109.25), wool 1 (9.13->14.34), flour 1 (18.48->22.04) | +141 |
| Darmwald | 1022 | 0.34 | 0.20 (20/turn) | tackles 1 (176.4->187.15), rope 2 (73.5->77.42), thread 25 (4.66->5.13) | medicine 1 (123.9->181.45), garments 20 (23.52->25.65), jewellery 1 (93.45->109.25), wool 2 (9.97->14.34) | +135 |

**Best:** Kirchwerp at about +223 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 25.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.7 | makes 56.0, uses 19.2, holds 283 (keeps 60): sells the surplus + 15/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.0 turns |
| cured meat | 6 @ 25.2, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 15 @ min 22.0 | makes 12.3, uses 2.1, holds 99 (keeps 30): sells the surplus + 5/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 237 @ 2.2, stop - |  | uses 675.1/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 273 = 1.2 turns |
| limestone |  | 5 @ min 21.0 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 6 @ min 42.6 |  |
| porterage | 33 @ 0.8, stop - |  | uses 29.6/turn (observed), makes 0.0, holds 37 = 1.3 turns |
| rope |  | 5 @ min 71.5 |  |
| timber |  | 30 @ min 8.5 | makes 24.0, uses 0.0, holds 447 (keeps 350): sells the surplus + 6/turn of the excess |
| tools | 7 @ 6.2, stop 50 |  | uses 6.2/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 32.3 turns |

## Self-diagnosis

Nothing found this run.
