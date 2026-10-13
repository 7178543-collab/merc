# v2 shadow report

Turn 13246, 2026-10-13 07:13. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 23,309, prestige 2,587 (167 free, +4.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 202 | 0 | 19 | 0 | 0 | min_holding 60, sell 59, sell @ 3.7 |
| cured fish | 19 | 6 | 6 | 0 | 0 | stop 20, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 26 | 6 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 426 | 0 | 2 | 0 | 0 | min_holding 30, sell 79, sell @ 22 |
| grain | 130 | 33 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 40, sell 10, sell @ 38.4 |
| porterage | 37 | 37 | 32 | 0 | 5 | buy 37, buy @ 0.8 |

**0 risks, 2 waste, 5 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 173 labour expired last turn (~301 coin): holding 787 against a ~61 buffer target -> v2: trim the buy until the stock is near 61
- **linen snake**: linen snake cost 63 coin last turn (crew 0.60) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **candles**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **cloth**: cloth buffer thin: 1.3 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 409
- **flax plants**: flax plants buffer thin: 1.3 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 529
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (431.1 held, 29 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 28% (EXPANSION), about 9 turns left; still to deliver: labour 188, limestone 44, timber 29; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 44 | 152.3 | 0 | off: covered |
| timber | 29 | 431.1 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 21

## Prestige spending, cheapest coin per prestige first

1155 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 167: ~20 turns at +4.2/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 55.4 | running |
| hold banquet 2 (pies) | mansion | 7 | 57.9 | 57.9 | thin at home: pasties, cheese, pies, candles |
| hold sermon 2 (candles) | church | 31 | 56.2 | 58.4 | needs a church (build cost 70,896); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 56.8 | 59.1 | needs a chapel (build cost 33,257) |
| hold banquet 3 (pies) | mansion | 8 | 59.2 | 59.2 | thin at home: pasties, cheese, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 59.2 | 59.2 | thin at home: pasties, candles |
| jousting 1 | arena | 170 | 59.1 | 59.2 | needs a arena (build cost 26,524); thin at home: protection, light armour, arms; needs weaponry skill |
| jousting 3 | arena | 230 | 59.4 | 59.5 | needs a arena (build cost 26,524); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 | church | 24 | 56.9 | 59.7 | needs a church (build cost 70,896); thin at home: jewellery, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 60.1 | 60.1 | thin at home: cured fish, cheese |
| hold mass 2 (premium) | cathedral | 360 | 59.6 | 60.3 | needs a cathedral (build cost 284,445); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 1 (fish) | mansion | 4.2 | 60.7 | 60.7 | running; thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 117401698 | 0 | - | - | 0 |
| linen snake | 0.5 / 0.60 | 63 | - | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brebronn: nothing pays; crew 0.0; est +0 a turn
- best towns now: Kirchwerp +36, Vauxvais +31, Hanstein +23, Neuborn +21, Etallaen +16
- Kirchwerp would trade: beer sell 4 @ 4.72, timber sell 18 @ 14.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.22 | 0.50 (54/turn) | cloth 20 (7.35->13.3), nets 6 (39.4->40.66), timber 5 (6.6->10.92), yarn 3 (4.98->6.22) | hop beer 5 (7.51->9.59), resin 1 (1.13->2.18), mouldboards 1 (40.74->41.04) | +135 |
| Vauxvais | 204 | 0.06 | 0.40 (43/turn) | timber 26 (6.6->8.22), nets 5 (39.4->42.75), beer 57 (3->3.23), cloth 11 (7.35->8.03) | thread 13 (3.09->5.1), limestone 2 (12.6->18.3), hides 1 (10.71->12.25), yarn 2 (4.05->4.48) | +87 |
| Nürnnieder | 520 | 0.15 | 0.30 (32/turn) | garments 17 (21.8->23.94), thread 59 (4.86->5.13), beer 45 (3->3.4), honey 5 (8.72->9.17) | hop beer 4 (7.88->9.59), flax fibres 11 (5.83->6.4), leather 1 (23.52->24.89) | +61 |
| Kirchwerp | 1072 | 0.39 | 1.00 (107/turn) | beer 33 (3->4.56), timber 13 (6.6->14.25), lead bars 1 (9.4->12.25), tar 1 (9.9->11.4) | hop beer 1 (7.46->9.59), jewellery 0 (78.75->79.8) | +60 |
| Neuborn | 780 | 0.22 | 0.80 (86/turn) | garments 30 (21.8->22.8), timber 16 (6.6->11.4), nets 3 (39.4->40.85), lead bars 1 (9.4->11.49) | cheese 27 (6.3->6.6), cloth 3 (7.77->8.25), flax fibres 4 (5.67->6.4), pies 1 (16.48->18.24) | +57 |

**Best:** Etallaen at about +135 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 59 @ min 3.7 | makes 70.0, uses 18.6, holds 202 (keeps 60): sells the surplus + 8/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 6 = 3.7 turns |
| cured fish | 7 @ 26.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 26 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 79 @ min 22.0 | makes 52.5, uses 1.8, holds 426 (keeps 30): sells the surplus + 29/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 802 @ 2.2, stop - |  | uses 1213.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 787 = 1.0 turns |
| light armour | 1 @ 112, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 1 = 4.0 turns |
| limestone |  | 5 @ min 24.6 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 6 @ min 38.4 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| timber |  | 29 @ min 8.5 | makes 24.0, uses 0.0, holds 431 (keeps 350): sells the surplus + 5/turn of the excess |
| tools | 9 @ 6.2, stop 68 |  | uses 8.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 23.6 turns |
