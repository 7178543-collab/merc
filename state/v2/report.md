# v2 shadow report

Turn 13454, 2026-10-21 23:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,324, prestige 3,582 (912 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 159 | 0 | 4 | 0 | 0 | min_holding 60, sell 56, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 38 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 283 | 264 | 714 | 12 | 0 | buy 283, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 41/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 71
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 181
- **timber**: build materials for net maker152202386007001 are in (350.3 held, 5 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **net maker152202386007001** 97% (INITIAL), about 1 turns left; still to deliver: labour 7, timber 5, tools 1; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 5 | 350.3 | 0 | off: covered; switch v1's buy off |
| tools | 1 | 199.9 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 7

## Notes

- labour: projection runs 87 over real use lately; planning 726, not 808

## Prestige spending, cheapest coin per prestige first

947 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 3 (pies) | mansion | 8 | 49.5 | 49.5 | thin at home: pasties, pies |
| hold banquet 4 (pies) | mansion | 18 | 50.0 | 50.0 | thin at home: pasties, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.1 | 51.1 | thin at home: pasties, wine, pies |
| hold sermon 2 (candles) | church | 31 | 51.2 | 53.5 | needs a church (build cost 61,909); thin at home: jewellery, candles, furniture |
| hold banquet 4 | mansion | 17.5 | 54.2 | 54.2 | thin at home: wine, ham |
| hold sermon 2 | church | 24 | 51.5 | 54.5 | needs a church (build cost 61,909); thin at home: jewellery, furniture |
| hold prayer 2 | chapel | 13 | 52.0 | 54.8 | needs a chapel (build cost 32,322); thin at home: furniture |
| hold mass 1 | cathedral | 180 | 55.0 | 56.5 | needs a cathedral (build cost 231,160); thin at home: jewellery, glassware, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 |  |
| jousting 3 | arena | 230 | 56.7 | 56.8 | needs a arena (build cost 25,361); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 57.7 | 57.7 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.2 / 0.20 | 19 | 185801747 | 0.32 | - | furniture 15 | -212 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: furniture buy 21 @ 14.0; crew 0.2; est +240 a turn; stock: furniture 21 @ 14.0 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- best towns now: Cobholme +499, Hofkirchen +438, Bordetes +420, Heilegg +363, Blanans +358
- Cobholme would trade: beer sell 59 @ 5.45, furniture buy 38 @ 13.2; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Briclives | 1041 | 0.34 | 0.10 (10/turn) | tapestries 1 (693->1168.5), slaked lime 1 (8.45->10.26), pasties 1 (12->13.21) | candles 1 (76.12->81.5), tools 3 (4.24->5.15), coats 1 (63->64.6) | +478 |
| Hofkirchen | 991 | 0.32 | 0.10 (10/turn) | plate armour 1 (1044.75->1187.5), looms 1 (415.8->532), pies 1 (11.65->15.2), leather 1 (23.94->25.65) | candles 1 (75.6->81.5), spirits 1 (16.91->19.57), tar 4 (10.19->11.4), cloth 9 (8.03->8.5) | +268 |
| Großaue | 1136 | 0.39 | 0.20 (20/turn) | looms 1 (415.8->541.5), glassware 2 (56.7->62.7), malt 2 (7.61->11.88) | gold ore 1 (134.4->175.75), copper ore 3 (16.59->22.8), candles 1 (71.92->81.5), windows 1 (401.1->406.6) | +210 |
| Rouhomme | 368 | 0.10 | 0.70 (70/turn) | looms 1 (415.8->489.25), windows 1 (483->513), bread 142 (2.18->2.62), furniture 12 (13.23->14.15) | candles 1 (72.45->81.5), coats 1 (59.33->64.6), cured fish 12 (22.05->22.61), tallow 1 (14.6->16.81) | +163 |
| Neuborn | 780 | 0.21 | 0.40 (40/turn) | tackles 1 (169.05->233.7), garments 19 (19.02->20.9), seeds 9 (1.78->3.32), charcoal 13 (1.75->3.8) | hop beer 6 (6.98->8.17), candles 1 (77.7->81.5), chisels 1 (11.97->14.44), honey 6 (7.35->7.84) | +136 |

**Best:** Briclives at about +478 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 56 @ min 3.38 | makes 56.0, uses 4.2, holds 159 (keeps 60): sells the surplus + 4/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 19 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 276 @ 2.2, stop - |  | uses 726.4/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 283 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.0 |  |
| pasties | 3 @ ?, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.5/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 78.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.0 turns |

## Chain sizing

Mode HOLD, garments sold 20.0/turn (+0.0 exported); plan makes 21.7 garments a turn.
Labour: own 450, everything else 410, chain may buy 350 -> chain allowance 390, chain plan 390 (-2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.70 | 5.54 |
| ret | 3 | 1.01 | 0.98 |
| spin | 4 | 2.09 | 2.03 |
| weave | 3 | 0.83 | 0.86 |
| sew | 2 | 0.51 | 0.53 |

Buffers: flax fibres 47/72, thread 272/213, cloth 0/86
- chain plan needed 533 labour, budget left 390: cut to 390 (sewing capped at 0.53)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
