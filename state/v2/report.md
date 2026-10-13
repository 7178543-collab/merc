# v2 shadow report

Turn 13245, 2026-10-13 06:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 23,508, prestige 2,582 (162 free, +4.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 185 | 0 | 19 | 0 | 0 | min_holding 60, sell 58, sell @ 3.7 |
| cured fish | 20 | 0 | 6 | 0 | 0 | stop 20, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 25 | 3 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 425 | 0 | 2 | 0 | 0 | min_holding 30, sell 71, sell @ 24 |
| grain | 130 | 0 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 52 | 0 | 0 | 0 | 0 | min_holding 40, sell 10, sell @ 36 |
| porterage | 37 | 26 | 26 | 7 | 0 | buy 37, buy @ 0.8 |

**1 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: quarry 1 ran short of porterage (buy is live (37 @ 0.8), 26 bought last turn); labour need rises ~44/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Waste (money lost now)

- **labour**: 81 labour expired last turn (~141 coin): holding 936 against a ~66 buffer target -> v2: trim the buy until the stock is near 66

## Tuning

- **cloth**: cloth buffer thin: 1.1 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 451
- **cured fish**: home ask 26.40 is above our ceiling 26.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax plants**: flax plants buffer thin: 1.1 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 619
- **timber**: build materials for park 1 are in (422.3 held, 32 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 20% (EXPANSION), about 10 turns left; still to deliver: labour 208, limestone 48, timber 32; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 48 | 152.1 | 0 | off: covered |
| timber | 32 | 422.3 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 21

## Prestige spending, cheapest coin per prestige first

1156 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 162: ~21 turns at +4.2/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 55.5 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.4 | 56.4 | thin at home: pasties, pies, candles |
| jousting 1 | arena | 170 | 57.6 | 57.8 | needs a arena (build cost 26,315); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 57.9 | 57.9 | thin at home: pasties, pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 58.3 | 58.3 | thin at home: cured fish, cheese |
| hold banquet 4 (pies) | mansion | 18 | 58.9 | 58.9 | thin at home: pasties, candles |
| hold sermon 2 (candles) | church | 31 | 57.4 | 59.5 | needs a church (build cost 70,860); thin at home: jewellery, candles, furniture |
| jousting 3 | arena | 230 | 59.5 | 59.6 | needs a arena (build cost 26,315); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 60.2 | 60.2 | running; thin at home: cured fish |
| hold mass 2 (premium) | cathedral | 360 | 59.8 | 60.6 | needs a cathedral (build cost 283,520); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 60.7 | 60.7 | thin at home: cured fish, cheese |
| hold feast 2 | townhouse | 2.6 | 58.4 | 60.7 | needs a townhouse (build cost 6,772) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 117401698 | 0 | - | - | 0 |
| linen snake | 0.6 / 0.60 | 62 | 109102068 | 0.144 | garments 6 | - | 79 |

## Ship plans (this turn's world prices)

- **linen snake** on Etallaen: garments sell 24 @ 29.4, nets sell 6 @ 43.8; crew 0.6; est +69 a turn
- **Flax Wyrm** on Brebronn: nothing pays; crew 0.0; est +0 a turn
- best towns now: Etallaen +69, Hanbrücken +58, Hanstein +38, Vauxvais +34, Neuborn +31

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.22 | 0.10 (11/turn) | garments 24 (24.6->28.5), nets 6 (31.18->42.37), cloth 7 (7.2->8.07), wax 1 (25.2->25.46) | flax plants 2 (1.6->2.75), resin 1 (1.25->2.18) | +158 |
| Vauxvais | 204 | 0.06 | 0.40 (43/turn) | nets 4 (31.18->41.8), timber 25 (6.6->8.22), beer 57 (2.98->3.23), bricks 1 (4.26->9.79) | limestone 2 (12.6->19.6), flax fibres 6 (5.67->6.65), yarn 6 (3.65->4.5), flax plants 1 (1.58->2.75) | +98 |
| Hanstein | 380 | 0.11 | 0.20 (21/turn) | nets 6 (31.18->42.18), timber 8 (6.6->9.69), lead bars 2 (10.45->12.44), cloth 15 (7.2->7.41) | thread 70 (5.02->5.25), flax plants 2 (1.4->2.75), seeds 3 (1.91->2.32), pies 1 (17.32->18.14) | +96 |
| Hanbrücken | 531 | 0.15 | 0.60 (64/turn) | timber 25 (6.6->10.92), nets 2 (31.18->41.99), tar 1 (9.5->23.75), cloth 6 (7.2->7.84) | flax plants 2 (2.12->2.75), flax fibres 1 (6.25->6.65) | +89 |
| Neuborn | 780 | 0.22 | 0.70 (75/turn) | nets 3 (31.18->40.85), timber 16 (6.6->11.4), grindstones 1 (346.5->368.6), bricks 1 (4.26->9.5) | stockfish 1 (94.5->102.6), cloth 3 (6.93->7.9), flax fibres 5 (5.72->6.65), garments 1 (23.94->25.8) | +84 |

**Best:** Etallaen at about +158 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 24.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 58 @ min 3.7 | makes 70.0, uses 18.6, holds 185 (keeps 60): sells the surplus + 6/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 7 = 4.7 turns |
| cured fish | 7 @ 26.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 25 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 60 @ min 22.0 | makes 57.8, uses 1.8, holds 425 (keeps 30): sells the surplus + 28/turn of the excess; ships offer 24 a turn abroad, so home sells 60 (was 84) |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 908 @ 2.2, stop - |  | uses 1314.2/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 936 = 1.1 turns |
| light armour | 1 @ 112, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 1 = 5.0 turns |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 10 @ min 36.0 | sell; ships offer 6 a turn abroad, so home sells 10 (was 6) |
| porterage | 37 @ 0.8, stop - |  | uses 32.9/turn (observed), makes 0.0, holds 37 = 1.1 turns |
| timber |  | 28 @ min 8.5 | makes 24.0, uses 0.0, holds 422 (keeps 350): sells the surplus + 4/turn of the excess |
| tools | 9 @ 6.2, stop 72 |  | uses 8.9/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 22.5 turns |
