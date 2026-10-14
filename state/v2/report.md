# v2 shadow report

Turn 13271, 2026-10-14 08:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 14,047, prestige 2,813 (143 free, +3.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 370 | 0 | 19 | 0 | 0 | min_holding 60, sell 61, sell @ 3.7 |
| cured fish | 5 | 0 | 6 | 0 | 0 | stop 22, buy 11, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 149 | 0 | 2 | 0 | 0 | min_holding 30, sell 54, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 51 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 40.8 |
| porterage | 37 | 37 | 29 | 0 | 8 | buy 37, buy @ 0.8 |

**0 risks, 2 waste, 4 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 224 labour expired last turn (~414 coin): holding 437 against a ~43 buffer target -> v2: trim the buy until the stock is near 43
- **linen snake**: linen snake cost 11 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **cured fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.4 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 486
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (431.9 held, 10 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 75% (EXPANSION), about 3 turns left; still to deliver: labour 65, limestone 15, timber 10; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 15 | 142.7 | 0 | off: covered |
| timber | 10 | 431.9 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1130 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 55.7 | 55.7 | thin at home: pasties, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 57.7 | 57.7 | thin at home: pasties, pies, candles |
| maintain 1 | park | 0.5 | 55.5 | 59.2 | running |
| jousting 1 | arena | 170 | 59.5 | 59.7 | needs a arena (build cost 28,768); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 59.8 | 59.8 | thin at home: pies, candles |
| hold prayer 2 | chapel | 13 | 57.2 | 59.8 | needs a chapel (build cost 36,149) |
| hold banquet 2 (fish) | mansion | 6.8 | 60.4 | 60.4 | thin at home: cured fish |
| hold sermon 2 (candles) | church | 31 | 58.3 | 60.7 | needs a church (build cost 76,434); thin at home: jewellery, candles |
| hold sermon 2 | church | 24 | 58.3 | 61.3 | needs a church (build cost 76,434); thin at home: jewellery |
| jousting 3 | arena | 230 | 61.3 | 61.5 | needs a arena (build cost 28,768); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 61.4 | 62.2 | needs a cathedral (build cost 301,250); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 1 (fish) | mansion | 4.2 | 62.7 | 62.7 | running; thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 55101678 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 95502502 | 0.024 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Kleinburgh: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Bordetes: nothing pays; crew 0.0; est +0 a turn; best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Boistot +52, Cobholme +52, Dortdorf +40, Orlesailles +26, Nürnnieder +24
- Boistot would trade: cookware buy 4 @ 20.4, hop beer buy 1 @ 6.6, mouldboards buy 1 @ 39.8, soap buy 1 @ 76.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Caillechâtel | 488 | 0.15 | 0.20 (23/turn) | cloth 26 (7.3->11.78), rope 2 (64->79.33), garments 13 (21.2->22.04) | wheels 2 (22.26->23.37), flax fibres 10 (5.83->6.15), flax plants 27 (1.44->1.75), wine 2 (5.3->5.65) | +150 |
| Hofkirchen | 991 | 0.36 | 1.00 (113/turn) | beer 32 (3.11->5.27), rope 2 (64->81.7), bread 71 (2.46->3.89), thread 18 (4.66->5.13) | jewellery 0 (78.75->87.88), cheese 8 (5.93->6.46), hop beer 1 (7.72->9.4), cloth 6 (8.24->8.7) | +124 |
| Heilegg | 826 | 0.26 | 0.40 (45/turn) | rope 5 (64->82.65), cloth 13 (7.3->7.93), beer 62 (3.11->3.69), thread 11 (4.66->5.08) | jewellery 1 (85.05->87.88), hop beer 2 (7.77->9.4), nails 2 (6.2->7.12), garments 2 (21.63->22) | +108 |
| Cobholme | 1564 | 0.71 | 0.10 (11/turn) | rope 4 (64->82.17), varnish 1 (20.06->21.47), pies 1 (16.7->19), tar 2 (9.6->11.11) | medicine 1 (142.8->168.15), butter 1 (59.33->64.12), jewellery 1 (86.1->87.88), nails 2 (5.88->7.12) | +98 |
| Neuborn | 780 | 0.24 | 1.00 (113/turn) | beer 62 (3.11->4.43), timber 16 (6.25->11.4), cloth 10 (7.3->8.03), garments 19 (21.2->21.66) | nails 2 (6.35->7.12) | +89 |

**Best:** Caillechâtel at about +150 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 60 @ min 3.7 | makes 56.0, uses 19.2, holds 370 (keeps 60): sells the surplus + 23/turn of the excess |
| cured fish | 11 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 5 = 0.9 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 4.0 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 19 @ min 22.0 | makes 11.9, uses 2.1, holds 149 (keeps 30): sells the surplus + 9/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 426 @ 2.2, stop - |  | uses 855.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 437 = 1.1 turns |
| limestone |  | 5 @ min 22.4 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 6 @ min 40.6 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| rope |  | 5 @ min 77.5 |  |
| timber |  | 29 @ min 8.5 | makes 24.0, uses 0.0, holds 432 (keeps 350): sells the surplus + 5/turn of the excess |
| tools | 8 @ 6.2, stop 62 |  | uses 7.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 26.0 turns |
