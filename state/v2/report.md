# v2 shadow report

Turn 13247, 2026-10-13 08:07. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 23,318, prestige 2,591 (171 free, +4.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 225 | 0 | 19 | 0 | 0 | min_holding 60, sell 53, sell @ 3.98 |
| cured fish | 20 | 5 | 6 | 0 | 0 | stop 20, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 26 | 7 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 410 | 0 | 2 | 0 | 0 | min_holding 30, sell 73, sell @ 22 |
| grain | 130 | 32 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 38.4 |
| porterage | 37 | 37 | 32 | 0 | 5 | buy 37, buy @ 0.8 |

**0 risks, 1 waste, 5 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 96 labour expired last turn (~167 coin): holding 773 against a ~58 buffer target -> v2: trim the buy until the stock is near 58

## Tuning

- **candles**: home ask 77.00 is above our ceiling 70.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **cloth**: cloth buffer thin: 1.6 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 358
- **flax plants**: flax plants buffer thin: 1.1 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 619
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (423.9 held, 26 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 36% (EXPANSION), about 8 turns left; still to deliver: labour 167, limestone 39, timber 26; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 39 | 152.5 | 0 | off: covered |
| timber | 26 | 423.9 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 21

## Prestige spending, cheapest coin per prestige first

1154 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 171: ~20 turns at +4.2/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 55.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 58.1 | 58.1 | thin at home: pasties, cheese |
| hold sermon 2 (candles) | church | 31 | 56.1 | 58.2 | needs a church (build cost 69,692); thin at home: jewellery, candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 58.3 | 58.3 | thin at home: pasties, cheese, pies |
| hold banquet 3 (pies) | mansion | 8 | 59.2 | 59.2 | thin at home: pasties, cheese, pies |
| hold prayer 2 | chapel | 13 | 56.9 | 59.2 | needs a chapel (build cost 32,510) |
| hold mass 2 (premium) | cathedral | 360 | 58.6 | 59.3 | needs a cathedral (build cost 280,895); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold sermon 2 | church | 24 | 57.0 | 59.7 | needs a church (build cost 69,692); thin at home: jewellery, furniture |
| jousting 1 | arena | 170 | 59.7 | 59.9 | needs a arena (build cost 25,876); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.1 | 60.1 | thin at home: cured fish, cheese |
| jousting 3 | arena | 230 | 60.0 | 60.1 | needs a arena (build cost 25,876); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 60.7 | 60.7 | running; thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 117401698 | 0 | - | - | 0 |
| linen snake | 1.0 / 1.00 | 104 | 159601387 | 1.112 | beer 4, timber 13 | - | 77 |

## Ship plans (this turn's world prices)

- **linen snake** on Kirchwerp: beer sell 65 @ 5.05, candles buy 1 @ 73.0; crew 0.5; est +40 a turn
- **Flax Wyrm** on Brebronn: nothing pays; crew 0.0; est +0 a turn; best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Clairlond +222, Kirchwerp +40, Fontaux +30, Bremcop +28, Neuborn +23
- Clairlond would trade: garments sell 42 @ 27.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clairlond | 1288 | 0.50 | 0.30 (32/turn) | garments 42 (21.8->26.79), glassware 1 (56.18->67.45), cloth 6 (7.45->8.12), varnish 1 (18.17->19.76) | yarn 5 (3.59->4.48), salt 6 (4.24->4.84) | +204 |
| Kirchwerp | 1072 | 0.38 | 0.50 (53/turn) | beer 65 (3.01->4.89), glassware 1 (56.18->61.75), lead bars 3 (12.29->13.3), tar 2 (10->11.02) | candles 1 (75.6->77), hop beer 1 (7.46->8.74), hides 1 (11.23->12.25), salt 11 (4.45->4.84) | +83 |
| Friedwerp | 684 | 0.19 | 0.10 (11/turn) | glassware 1 (56.18->105.45), light armour 1 (82.95->95.95), cloth 3 (7.45->9.79), nets 2 (42.8->44.46) | cheese 17 (6.35->6.74), pies 1 (17.54->18.34) | +76 |
| Etallaen | 774 | 0.22 | 0.10 (11/turn) | cloth 15 (7.45->11.21), glassware 1 (56.18->66.5), flax plants 1 (1.36->2.01) | hop beer 5 (7.51->8.74), candles 1 (76.65->77), yarn 1 (4.12->4.48) | +63 |
| Neuborn | 780 | 0.22 | 0.90 (95/turn) | timber 18 (6.6->11.4), glassware 1 (56.18->65.08), fleece 2 (6.3->9.88), limestone 2 (17.54->28.5) | cheese 17 (6.3->6.74), yarn 4 (3.63->4.48), wax 1 (22.47->23.75), grindstones 1 (226.8->233.7) | +57 |

**Best:** Clairlond at about +204 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 10 @ min 3.7 | makes 70.0, uses 18.6, holds 225 (keeps 60): sells the surplus + 10/turn of the excess; ships offer 65 a turn abroad, so home sells 10 (was 61) |
| candles | 3 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 4 = 2.7 turns |
| cured fish | 7 @ 26.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 26 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 72 @ min 22.0 | makes 45.9, uses 1.8, holds 410 (keeps 30): sells the surplus + 28/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 740 @ 2.2, stop - |  | uses 1153.9/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 773 = 1.1 turns |
| light armour | 1 @ 112, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 1 = 3.0 turns |
| limestone |  | 5 @ min 24.4 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 6 @ min 41.6 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| timber |  | 28 @ min 8.5 | makes 24.0, uses 0.0, holds 424 (keeps 350): sells the surplus + 4/turn of the excess |
| tools | 9 @ 6.2, stop 68 |  | uses 8.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 23.7 turns |
