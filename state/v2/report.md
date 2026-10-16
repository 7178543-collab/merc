# v2 shadow report

Turn 13315, 2026-10-16 04:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,128, prestige 3,200 (530 free, +100.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 314 | 0 | 4 | 0 | 0 | min_holding 60, sell 46, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 0 | 3 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 64 | 0 | 2 | 0 | 0 | min_holding 80, sell 10, sell @ 22 |
| grain | 103 | 0 | 0 | 0 | 0 | stop 52, buy 13, buy @ 3.7 |
| labour | 257 | 54 | 504 | 165 | 0 | buy 229, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 47 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 39.8 |
| porterage | 6 | 21 | 6 | 0 | 15 | buy 6, buy @ 1.1 |

**2 risks, 0 waste, 5 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.4 turns (holds 9, next step uses 24/turn) -> v2: check the step that makes it
- **porterage**: buying 6, short of ~21 needed -> v2: buy 21

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 181
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 55 over real use lately; planning 669, not 682

## Prestige spending, cheapest coin per prestige first

1086 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 58.1 | 58.1 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 58.3 | 58.3 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 58.5 | 58.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 58.6 | 58.6 | thin at home: pasties, pies |
| hold sermon 2 (candles) | church | 31 | 56.4 | 58.7 | needs a church (build cost 69,690); thin at home: jewellery, candles, furniture |
| hold banquet 3 (pies) | mansion | 8 | 59.3 | 59.3 | thin at home: pasties, hop beer, pies |
| hold prayer 2 | chapel | 13 | 57.0 | 59.4 | needs a chapel (build cost 32,265); thin at home: furniture |
| hold mass 2 (premium) | cathedral | 360 | 59.2 | 60.0 | needs a cathedral (build cost 280,625); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 | thin at home: hop beer |
| hold sermon 2 | church | 24 | 57.5 | 60.4 | needs a church (build cost 69,690); thin at home: jewellery, furniture |
| jousting 3 | arena | 230 | 60.8 | 60.9 | needs a arena (build cost 25,633); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.33 | 0.30 (31/turn) | hop beer 5 (11.03->19.38), steel ingots 8 (14.18->15.2), grain 8 (2.58->3.72), soap 1 (98.17->98.8) | cheese 60 (5.88->6.55), acid 2 (163.8->172.9), jewellery 2 (81.38->84.55), pasties 3 (12.81->14.91) | +97 |
| Neuborn | 780 | 0.22 | 0.20 (21/turn) | grain 8 (2.58->3.42), charcoal 2 (1.92->4.01), flax fibres 5 (4.84->5.46), steel ingots 1 (14.18->15.86) | cheese 66 (5.3->6.55), pasties 3 (14.18->14.91) | +74 |
| Kleinburgh | 1440 | 0.58 | 0.10 (10/turn) | light armour 1 (77.7->89.77), tallow 2 (30.45->33.25), varnish 1 (18.17->21.85) | candles 3 (60.38->70.3), jewellery 2 (76.12->84.55), hop beer 1 (8.14->9.59) | +58 |
| Brunnham | 1281 | 0.49 | 0.10 (10/turn) | soap 1 (98.17->103.55), lead bars 9 (12.81->13.59), light armour 1 (77.7->81.22) | acid 1 (136.5->172.9), wheels 8 (21.84->23.18), hop beer 1 (7.46->9.59) | +50 |
| Kirchwerp | 1072 | 0.37 | 0.20 (21/turn) | wine 19 (6.83->8.31), soap 1 (98.17->104.5), flax fibres 5 (4.84->6.17), steel ingots 2 (14.18->15.2) | jewellery 2 (78.75->84.55), dyed cloth 1 (11.97->12.92), gears 1 (71.4->73.62) | +44 |

**Best:** Hofkirchen at about +97 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 43 @ min 3.7 | makes 28.0, uses 4.2, holds 314 (keeps 60): sells the surplus + 19/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 10 @ min 22.0 |  |
| grain | 13 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 103 = 7.9 turns |
| labour | 219 @ 2.2, stop - |  | uses 668.6/turn (brewery 1, flax farm 1, household), makes 450.0, holds 257 = 1.2 turns |
| limestone |  | 5 @ min 17.4 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 37.8 | makes 9.0, uses 0.0, holds 47 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 21 @ 1.1, stop - |  | uses 21.0/turn (observed), makes 0.0, holds 6 = 0.3 turns |
| rope |  | 4 @ min 79.5 |  |
| tar | 1 @ 11.0, stop 4 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 4 = 4.0 turns |
| timber |  | 38 @ min 8.5 | makes 12.0, uses 0.0, holds 673 (keeps 350): sells the surplus + 26/turn of the excess |
| tools | 5 @ 6.2, stop 37 |  | uses 4.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 44.1 turns |

## Chain sizing

Mode HOLD, garments sold 1.0/turn (+0.0 exported); plan makes 19.7 garments a turn.
Labour: own 450, everything else 429, chain may buy 350 -> chain allowance 371, chain plan 371 (+43 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.61 | 5.46 |
| ret | 3 | 1.01 | 0.97 |
| spin | 4 | 2.05 | 2.00 |
| weave | 3 | 0.47 | 0.76 |
| sew | 2 | 0.30 | 0.48 |

Buffers: flax fibres 64/88, thread 609/258, cloth 9/76
- chain plan needed 591 labour, budget left 371: cut to 371 (sewing capped at 0.48)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 76.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 0.4 (limited by porterage)
