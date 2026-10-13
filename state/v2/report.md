# v2 shadow report

Turn 13244, 2026-10-13 05:10. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 24,284, prestige 2,578 (158 free, -5.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 169 | 0 | 4 | 0 | 0 | min_holding 60, sell 10, sell @ 3.7 |
| cured fish | 19 | 5 | 0 | 0 | 0 | stop 20, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 26 | 0 | 2 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 407 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 22 |
| grain | 130 | 32 | 0 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 46 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 36 |
| porterage | 26 | 26 | 11 | 0 | 15 | buy 26, buy @ 0.8 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 115, next step uses 160/turn) -> v2: check the step that makes it
- **flax plants**: retting pit 1 ran short of flax plants (buy is live (no volume cap @ 2.04), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~50/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (420.4 held, 36 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 11% (EXPANSION), about 11 turns left; still to deliver: labour 232, limestone 54, timber 36; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 54 | 152.0 | 0 | off: covered |
| timber | 36 | 420.4 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1157 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 158 and prestige income is not positive

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 1 | arena | 170 | 55.0 | 55.1 | needs a arena (build cost 28,138); thin at home: protection, light armour, arms; needs weaponry skill |
| maintain 1 | park | 0.5 | 51.3 | 55.3 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.3 | 56.3 | thin at home: pasties, cheese, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 56.8 | 56.8 | thin at home: pasties, hop beer, pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 57.4 | 57.4 | thin at home: cheese |
| hold banquet 4 (pies) | mansion | 18 | 58.2 | 58.2 | thin at home: pasties, hop beer, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 58.9 | 58.9 | thin at home: hop beer, cheese |
| hold feast 2 | townhouse | 2.6 | 57.0 | 59.3 | needs a townhouse (build cost 6,688) |
| hold banquet 1 (fish) | mansion | 4.2 | 59.4 | 59.4 | running |
| jousting 3 | arena | 230 | 59.9 | 60.0 | needs a arena (build cost 28,138); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 59.8 | 60.6 | needs a cathedral (build cost 300,220); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 62.4 | 62.4 | thin at home: hop beer, stockfish, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.4 / 0.52 | 51 | 117401698 | 0.548 | beer 30, garments 22 | - | 221 |
| linen snake | 0.1 / 0.00 | 0 | 109102068 | 0.136 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Etallaen: garments sell 50 @ 33.2; crew 0.6; est +306 a turn
- **Flax Wyrm** on Brebronn: nothing pays; crew 0.0; est +0 a turn
- best towns now: Etallaen +306

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.22 | 0.20 (21/turn) | garments 50 (25.8->32.11), nets 6 (31.18->42.75), arms 2 (18.06->22.42), beer 9 (2.98->4.08) | hop beer 2 (7.46->8.74), flax fibres 1 (6.09->7.65), resin 1 (1.44->2.18) | +392 |
| Bordetes | 831 | 0.24 | 0.20 (21/turn) | nets 4 (31.18->43.13), arms 2 (18.06->24.13), cheese 13 (7.14->8.07), cured fish 1 (24.4->25.65) | garments 41 (22.47->24.51), cloth 6 (7.67->8.8), tools 2 (4.7->5.15) | +143 |
| Bedenis | 566 | 0.16 | 0.20 (21/turn) | nets 3 (31.18->40.85), cheese 14 (7.14->8.03), arms 1 (18.06->24.51), varnish 2 (18.17->19.57) | garments 38 (22.47->24.51), cloth 20 (7.88->8.8), flax fibres 2 (6.3->7.65), thread 6 (5.19->5.35) | +128 |
| Hofkirchen | 991 | 0.34 | 0.40 (43/turn) | flax plants 30 (1.94->3.89), arms 2 (18.06->23.18), wine 12 (5.99->6.79), grain 10 (2.26->3.46) | garments 41 (22.89->24.51), cloth 9 (7.56->8.8), canvas 1 (32.34->35.15), stockfish 1 (104.48->107.35) | +127 |
| Amsdermund | 1111 | 0.41 | 0.30 (32/turn) | nets 3 (31.18->44.65), arms 2 (18.06->23.56), lead bars 1 (12.5->16.53), wine 13 (5.99->6.55) | garments 41 (22.89->24.51), cloth 23 (7.56->8.8), flax fibres 5 (6.77->7.65), resin 1 (1.33->2.18) | +123 |

**Best:** Etallaen at about +392 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 56 @ min 3.7 | makes 70.0, uses 18.6, holds 169 (keeps 60): sells the surplus + 5/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.7 turns |
| cured fish | 7 @ 26.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 26 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 55 @ min 22.0 | makes 82.0, uses 1.8, holds 407 (keeps 30): sells the surplus + 25/turn of the excess; ships offer 50 a turn abroad, so home sells 55 (was 105) |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 975 @ 2.2, stop - |  | uses 1378.5/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 945 = 1.0 turns |
| light armour | 1 @ 112, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 1 = 6.0 turns |
| limestone |  | 5 @ min 25.0 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 26 = 1.1 turns |
| timber |  | 28 @ min 8.5 | makes 24.0, uses 0.0, holds 420 (keeps 350): sells the surplus + 4/turn of the excess |
| tools | 5 @ 6.2, stop 40 |  | uses 5.0/turn (logging camp w/ tool), makes 0.0, holds 199 = 39.9 turns |
