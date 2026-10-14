# v2 shadow report

Turn 13270, 2026-10-14 07:12. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 14,454, prestige 2,809 (139 free, +3.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 386 | 0 | 19 | 0 | 0 | min_holding 60, sell 61, sell @ 3.7 |
| cured fish | 10 | 1 | 6 | 0 | 0 | stop 22, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 196 | 0 | 2 | 0 | 0 | min_holding 30, sell 54, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 51 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 40.6 |
| porterage | 37 | 37 | 28 | 0 | 9 | buy 37, buy @ 0.8 |

**0 risks, 0 waste, 5 tuning** where v2 would act differently from v1.

## Tuning

- **cured fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.6 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 428
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **rope**: floor 80.00 vs home bid 64.00: barely selling (0 of 4)
- **timber**: build materials for park 1 are in (427.9 held, 14 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 67% (EXPANSION), about 4 turns left; still to deliver: labour 86, limestone 20, timber 14; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 20 | 137.5 | 0 | off: covered |
| timber | 14 | 427.9 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1131 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 56.5 | 56.5 | thin at home: pasties, cheese, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 57.1 | 57.1 | thin at home: pasties, cheese, pies, candles |
| maintain 1 | park | 0.5 | 54.0 | 57.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 59.4 | 59.4 | thin at home: pasties, cheese, pies, candles |
| hold prayer 2 | chapel | 13 | 57.0 | 59.6 | needs a chapel (build cost 35,980); thin at home: furniture |
| jousting 1 | arena | 170 | 59.8 | 59.9 | needs a arena (build cost 28,661); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 58.2 | 60.6 | needs a church (build cost 76,162); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 58.1 | 61.2 | needs a church (build cost 76,162); thin at home: jewellery, furniture |
| jousting 3 | arena | 230 | 61.1 | 61.2 | needs a arena (build cost 28,661); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 61.3 | 61.3 | thin at home: cured fish, cheese |
| hold mass 2 (premium) | cathedral | 360 | 61.4 | 62.2 | needs a cathedral (build cost 300,310); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 1 (fish) | mansion | 4.2 | 62.3 | 62.3 | running; thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 55101678 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 95502502 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Bordetes: resin sell 1 @ 3.14, rope sell 2 @ 86.0; crew 0.1; est +22 a turn
- **Flax Wyrm** on Kleinburgh: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Boistot +67, Cobholme +63, Orlesailles +58, Dortdorf +50, Nürnnieder +34
- Boistot would trade: cookware buy 4 @ 20.4, hop beer buy 1 @ 6.6, mouldboards buy 1 @ 39.8, rope sell 2 @ 77.5, soap buy 1 @ 76.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Caillechâtel | 488 | 0.14 | 0.20 (22/turn) | cloth 37 (7.3->11.78), rope 2 (64->79.33), garments 13 (21.2->22.04) | wheels 2 (22.26->23.37), flax plants 27 (1.44->1.75), flax fibres 10 (5.83->6.15), wine 2 (5.3->5.65) | +199 |
| Hofkirchen | 991 | 0.35 | 1.00 (111/turn) | beer 33 (3.1->5.27), bread 71 (2.46->3.89), rope 1 (64->81.7), thread 18 (4.66->5.13) | jewellery 0 (78.75->87.88), cheese 8 (5.93->6.46), hop beer 1 (7.72->9.4), cloth 6 (8.24->8.7) | +119 |
| Neuborn | 780 | 0.23 | 1.00 (111/turn) | beer 63 (3.1->4.43), timber 16 (6.25->11.4), garments 32 (21.2->21.66), cloth 10 (7.3->8.03) | nails 2 (6.35->7.12) | +98 |
| Vauxvais | 204 | 0.06 | 0.40 (44/turn) | timber 29 (6.25->8.36), rope 2 (64->74.58), beer 60 (3.1->3.42), cloth 9 (7.3->7.69) | thread 32 (4.79->5.3), hides 1 (10.5->12.73), limestone 1 (12.6->16.53), logs 1 (3.38->5.42) | +90 |
| Birkeningen | 1006 | 0.36 | 0.60 (66/turn) | beer 50 (3.1->4.73), rope 1 (64->85.5), garments 19 (21.2->22.23), furniture 9 (13.97->16.34) | steel ingots 1 (12.92->14.06) | +86 |

**Best:** Caillechâtel at about +199 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 61 @ min 3.7 | makes 56.0, uses 19.2, holds 386 (keeps 60): sells the surplus + 24/turn of the excess |
| cured fish | 11 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 10 = 1.9 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 4.0 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 54 @ min 22.0 | makes 45.5, uses 2.1, holds 196 (keeps 30): sells the surplus + 10/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 653 @ 2.2, stop - |  | uses 1071.7/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 584 = 0.9 turns |
| limestone |  | 5 @ min 22.6 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 6 @ min 40.8 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| rope |  | 10 @ min 71.5 | sell; ships offer 2 a turn abroad, so home sells 10 (was 4) |
| timber |  | 28 @ min 8.5 | makes 24.0, uses 0.0, holds 428 (keeps 350): sells the surplus + 4/turn of the excess |
| tools | 8 @ 6.2, stop 60 |  | uses 7.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 27.1 turns |
