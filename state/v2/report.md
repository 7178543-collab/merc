# v2 shadow report

Turn 13276, 2026-10-14 13:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,941, prestige 2,818 (148 free, +3.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 312 | 0 | 19 | 0 | 0 | min_holding 60, sell 56, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 147 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 22.8 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 661 | 661 | 959 | 0 | 152 | buy 541, buy @ 2.2 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 64 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 37.8 |
| porterage | 37 | 37 | 25 | 0 | 12 | buy 37, buy @ 0.8 |

**0 risks, 2 waste, 3 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 152 labour expired last turn (~274 coin): holding 661 against a ~50 buffer target -> v2: trim the buy until the stock is near 50
- **linen snake**: linen snake cost 74 coin last turn (crew 0.68) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax plants**: flax plants buffer thin: 1.4 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 503
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (411.1 held, 4 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 92% (EXPANSION), about 1 turns left; still to deliver: labour 21, limestone 5, timber 4; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 5 | 153.0 | 0 | off: covered |
| timber | 4 | 411.1 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 21

## Notes

- labour expiry guard: 152 bought labour expired last turn, buy 541 (not 572) this turn

## Prestige spending, cheapest coin per prestige first

1125 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 55.7 | 55.7 | thin at home: pasties, cheese, pies |
| hold banquet 3 (pies) | mansion | 8 | 56.1 | 56.1 | thin at home: pasties, cheese, pies |
| maintain 1 | park | 0.5 | 54.3 | 58.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 58.4 | 58.4 | thin at home: cheese, pies |
| hold mass 2 (premium) | cathedral | 360 | 58.7 | 59.5 | needs a cathedral (build cost 295,390); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold sermon 2 (candles) | church | 31 | 57.4 | 59.7 | needs a church (build cost 74,834); thin at home: jewellery, furniture |
| jousting 1 | arena | 170 | 60.0 | 60.2 | needs a arena (build cost 28,536); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 | church | 24 | 58.2 | 61.2 | needs a church (build cost 74,834); thin at home: jewellery, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 61.3 | 61.3 | thin at home: cured fish, cheese |
| jousting 3 | arena | 230 | 61.4 | 61.6 | needs a arena (build cost 28,536); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 62.0 | 62.0 | thin at home: cured fish, cheese |
| hold prayer 2 | chapel | 13 | 59.6 | 62.1 | needs a chapel (build cost 35,060); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.10 | 11 | 108202735 | 0 | cheese 8, salt 7 | - | 58 |
| linen snake | 0.1 / 0.68 | 74 | 141901647 | 0.056 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Heilegg: cured meat buy 6 @ 24.4, hop beer buy 1 @ 7.55, nets sell 6 @ 42.2; crew 0.1; est +30 a turn
- **Flax Wyrm** on Toqueque: nothing pays; crew 0.0; est +0 a turn; best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Neuborn +59, Donaunieder +56, Brunnham +53, Dortdorf +45, Nürnnieder +44
- Neuborn would trade: cheese buy 20 @ 5.45, cured meat buy 6 @ 21.8, nets sell 2 @ 42.2, stockfish buy 1 @ 102; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Donaunieder | 985 | 0.35 | 0.20 (22/turn) | nets 6 (20.12->46.93), yarn 7 (5.35->6.84), bricks 1 (4.42->15.67) | cured meat 6 (24.15->27.8), tar 1 (10.45->11.2) | +183 |
| Heidlowe | 662 | 0.20 | 0.20 (22/turn) | nets 7 (20.12->40.47), beer 41 (3.13->4.18), lead bars 2 (11.03->11.69), tar 1 (9.6->10.36) | cured meat 5 (24.99->27.8), wine 7 (5.25->5.7) | +182 |
| Rouhomme | 368 | 0.11 | 0.20 (22/turn) | nets 6 (20.12->42.18), beer 57 (3.13->3.65), lead bars 1 (11.03->21.47), charcoal 2 (2.06->4.8) | casks 1 (3.51->5.94), cured meat 6 (27.3->27.8), lead ore 2 (4.12->5.18), tools 7 (4.91->5.15) | +175 |
| Amsdermund | 1111 | 0.42 | 0.20 (22/turn) | nets 7 (20.12->39.14), dyed cloth 3 (13.55->15.2), lead bars 2 (11.03->11.59) | cured meat 6 (24.36->27.8), candles 1 (73.5->77), slaked lime 1 (8.4->12.35), steel ingots 4 (15.12->16.25) | +158 |
| Fulkirch | 1576 | 0.70 | 0.20 (22/turn) | nets 7 (20.12->40.28), varnish 1 (18.17->21.66), tools 16 (4.76->5.56) | steel ingots 2 (15.23->16.25) | +137 |

**Best:** Donaunieder at about +183 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 55 @ min 3.7 | makes 56.0, uses 19.2, holds 312 (keeps 60): sells the surplus + 18/turn of the excess |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 6 = 1.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 36 @ min 22.0 | makes 30.8, uses 2.1, holds 147 (keeps 30): sells the surplus + 7/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 541 @ 2.2, stop - |  | uses 993.8/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 661 = 1.2 turns |
| limestone |  | 5 @ min 22.0 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 37.8 | makes 6.0, uses 0.0, holds 64 (keeps 40): sells the surplus + 1/turn of the excess |
| porterage | 33 @ 0.8, stop - |  | uses 29.6/turn (observed), makes 0.0, holds 37 = 1.3 turns |
| rope |  | 4 @ min 81.5 |  |
| timber |  | 27 @ min 8.5 | makes 24.0, uses 0.0, holds 411 (keeps 350): sells the surplus + 3/turn of the excess |
| tools | 8 @ 6.2, stop 63 |  | uses 7.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 25.6 turns |

## Self-diagnosis

- R2: quarry 1 blocked by limestone space: 153 held of 153 capacity, we make 5.2 a turn; buy already stops at 100: add a sell order or more capacity for limestone
