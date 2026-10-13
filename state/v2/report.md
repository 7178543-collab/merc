# v2 shadow report

Turn 13252, 2026-10-13 13:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 23,416, prestige 2,607 (187 free, +0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 326 | 0 | 19 | 0 | 0 | min_holding 60, sell 68, sell @ 3.7 |
| cured fish | 19 | 6 | 6 | 0 | 0 | stop 20, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 26 | 7 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 336 | 0 | 2 | 0 | 0 | min_holding 30, sell 63, sell @ 22 |
| grain | 130 | 33 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 41 |
| porterage | 37 | 37 | 25 | 0 | 12 | buy 37, buy @ 0.8 |

**0 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Tuning

- **flax plants**: flax plants buffer thin: 1.5 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 464
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (476.6 held, 9 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 79% (EXPANSION), about 3 turns left; still to deliver: labour 55, limestone 13, timber 9; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 13 | 152.2 | 0 | off: covered |
| timber | 9 | 476.6 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 19

## Prestige spending, cheapest coin per prestige first

1149 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 187: ~111 turns at +0.6/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 55.8 | running |
| hold banquet 2 (pies) | mansion | 7 | 57.1 | 57.1 | thin at home: pasties, cheese, pies, candles |
| hold sermon 2 (candles) | church | 31 | 55.3 | 57.5 | needs a church (build cost 73,525); thin at home: jewellery, candles |
| hold banquet 3 (pies) | mansion | 8 | 58.3 | 58.3 | thin at home: pasties, cheese, pies, candles |
| hold prayer 2 | chapel | 13 | 56.2 | 58.7 | needs a chapel (build cost 35,814) |
| hold banquet 4 (pies) | mansion | 18 | 59.0 | 59.0 | thin at home: pasties, cheese, candles |
| hold sermon 2 | church | 24 | 56.3 | 59.2 | needs a church (build cost 73,525); thin at home: jewellery |
| hold banquet 2 (fish) | mansion | 6.8 | 60.1 | 60.1 | thin at home: cured fish, cheese |
| jousting 1 | arena | 170 | 60.0 | 60.1 | needs a arena (build cost 27,750); thin at home: protection, light armour, arms; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 59.4 | 60.2 | needs a cathedral (build cost 292,470); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 3 | arena | 230 | 60.3 | 60.4 | needs a arena (build cost 27,750); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 61.5 | 61.5 | running; thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 88002195 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 159601387 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Clairlond: cured fish buy 5 @ 26.2; crew 0.1; est +16 a turn
- **linen snake** on Kirchwerp: nothing pays; crew 0.0; est +0 a turn; best orders clear only 14 a turn after crew: ship stays at 0
- best towns now: Orlesailles +76, Gotthafen +38, Marmont +35, Karlmoor +29, Arnsreuth +26
- Orlesailles would trade: cured fish buy 5 @ 26.4, garments sell 32 @ 24.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clairlond | 1288 | 0.52 | 0.40 (44/turn) | garments 63 (21.8->23.75), yarn 5 (4.18->5.27) | wool 6 (9.5->13.11), cured fish 5 (27.09->31.4), wax 1 (19.95->21.47) | +129 |
| Orlesailles | 1178 | 0.45 | 0.30 (33/turn) | garments 32 (21.8->24.51), arms 3 (27.3->29.45), yarn 4 (4.18->5.13), glassware 2 (74.03->75.05) | cured fish 5 (27.3->31.4), wool 5 (9.45->13.11), stockfish 1 (104.48->107.35), wax 4 (20.48->21.47) | +115 |
| Vauxvais | 204 | 0.06 | 0.40 (44/turn) | timber 28 (6.55->8.22), beer 60 (3.05->3.42), bricks 1 (4.32->9.79), wheels 1 (20->21.85) | cured fish 4 (27.72->31.4), limestone 2 (12.6->21.2), wool 2 (9.13->13.11), pies 1 (15.75->18.71) | +84 |
| Bordetes | 831 | 0.25 | 1.00 (109/turn) | beer 52 (3.05->4.6), bread 94 (2.48->3.27), grain 7 (2.68->3.61), flax fibres 1 (5.55->6.08) | cured fish 3 (28.14->31.4), wool 1 (8.29->13.11), cloth 5 (8.51->9.26), salt 3 (4.33->4.69) | +83 |
| Großmühle | 751 | 0.22 | 0.10 (11/turn) | nets 1 (42.2->42.94), wheels 1 (20->20.52) | soap 1 (77.7->116.85), wool 10 (9.13->13.11), cured fish 2 (29.82->31.4), canvas 1 (34.02->35.15) | +76 |

**Best:** Clairlond at about +129 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 69 @ min 3.7 | makes 70.0, uses 18.6, holds 326 (keeps 60): sells the surplus + 18/turn of the excess |
| cured fish | 7 @ 26.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 26 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 63 @ min 22.0 | makes 43.1, uses 1.8, holds 336 (keeps 30): sells the surplus + 22/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 604 @ 2.2, stop - |  | uses 1025.1/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 492 = 0.9 turns |
| limestone |  | 5 @ min 23.4 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 6 @ min 41.0 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| timber |  | 33 @ min 8.5 | makes 24.0, uses 0.0, holds 477 (keeps 350): sells the surplus + 9/turn of the excess |
| tools | 8 @ 6.2, stop 61 |  | uses 7.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 26.3 turns |
