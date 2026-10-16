# v2 shadow report

Turn 13318, 2026-10-16 07:11. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,212, prestige 3,238 (568 free, +50.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 298 | 0 | 4 | 0 | 0 | min_holding 60, sell 43, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 13 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 22 |
| grain | 68 | 0 | 9 | 0 | 0 | stop 52, buy 13, buy @ 3.7 |
| labour | 255 | 163 | 613 | 113 | 0 | buy 255, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 40 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 36.8 |
| porterage | 21 | 21 | 6 | 0 | 15 | buy 21, buy @ 1.1 |

**1 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.3 turns (holds 9, next step uses 38/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68
- **flax plants**: flax plants buffer thin: 2.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 174
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 147 over real use lately; planning 726, not 799

## Prestige spending, cheapest coin per prestige first

1083 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.6 | 56.6 | thin at home: pasties, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 57.6 | 57.6 | thin at home: cheese |
| hold banquet 4 (pies) | mansion | 18 | 58.1 | 58.1 | thin at home: pasties, hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 58.6 | 58.6 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 58.8 | 58.8 | thin at home: pasties, hop beer, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 59.2 | 59.2 |  |
| hold sermon 2 (candles) | church | 31 | 57.3 | 59.5 | needs a church (build cost 69,282); thin at home: jewellery, candles, furniture |
| hold feast 2 | townhouse | 2.6 | 57.5 | 60.0 | needs a townhouse (build cost 6,857) |
| hold mass 2 (premium) | cathedral | 360 | 59.4 | 60.2 | needs a cathedral (build cost 279,060); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 60.9 | 60.9 | thin at home: hop beer, cheese |
| hold prayer 2 | chapel | 13 | 58.6 | 61.1 | needs a chapel (build cost 32,086); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Calange | 218 | 0.06 | 0.10 (11/turn) | garments 17 (23->26.98), varnish 1 (18.17->19.19) | grain 9 (2.71->3.14) | +63 |
| Angefont | 686 | 0.20 | 0.10 (11/turn) | garments 17 (23->26.41), cookware 11 (23.52->24.13), cured meat 2 (23.2->24.7) | - | +58 |
| Hofkirchen | 991 | 0.34 | 0.20 (21/turn) | lead bars 7 (11.97->14.34), hop beer 3 (11.03->13.87), steel ingots 3 (14.18->16.81), tools 16 (5.1->5.65) | wrought iron 5 (11.55->12.82), acid 1 (157.5->161.5), garments 2 (22.68->24.8), dyed cloth 2 (12.08->13.59) | +48 |
| Vauxvais | 204 | 0.06 | 0.10 (11/turn) | garments 17 (23->26.03), cloth 1 (8->8.46), flax plants 1 (1.32->1.58), pasties 1 (15.96->16.15) | limestone 1 (12.6->15.2) | +44 |
| Kirchwerp | 1072 | 0.38 | 0.20 (21/turn) | wine 18 (6.09->7.65), lead bars 7 (11.97->13.3), steel ingots 3 (14.18->15.48), flax fibres 5 (4.92->6.17) | garments 2 (22.47->24.8), gears 1 (70.35->73.62), jewellery 1 (78.75->82.17), dyed cloth 2 (11.97->13.59) | +42 |

**Best:** Calange at about +63 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 42 @ min 3.7 | makes 28.0, uses 4.2, holds 298 (keeps 60): sells the surplus + 18/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 17 @ min 22.4 |  |
| grain | 13 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 68 = 5.2 turns |
| labour | 276 @ 2.2, stop - |  | uses 725.6/turn (brewery 1, flax farm 1, household), makes 450.0, holds 255 = 0.9 turns |
| limestone |  | 5 @ min 17.4 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 39.2 | makes 9.0, uses 0.0, holds 40 (keeps 15): sells the surplus + 1/turn of the excess |
| porterage | 21 @ 1.1, stop - |  | uses 20.8/turn (observed), makes 0.0, holds 21 = 1.0 turns |
| rope |  | 4 @ min 74.5 |  |
| tar | 1 @ 11.0, stop 4 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 5 = 5.0 turns |
| timber |  | 38 @ min 8.5 | makes 12.0, uses 0.0, holds 676 (keeps 350): sells the surplus + 26/turn of the excess |
| tools | 5 @ 6.2, stop 36 |  | uses 4.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 44.8 turns |

## Chain sizing

Mode HOLD, garments sold 0.5/turn (+0.0 exported); plan makes 19.7 garments a turn.
Labour: own 450, everything else 429, chain may buy 350 -> chain allowance 371, chain plan 371 (-1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.49 | 5.44 |
| ret | 3 | 0.97 | 0.97 |
| spin | 4 | 2.00 | 1.99 |
| weave | 3 | 0.76 | 0.77 |
| sew | 2 | 0.47 | 0.48 |

Buffers: flax fibres 64/88, thread 661/259, cloth 9/77
- chain plan needed 742 labour, budget left 371: cut to 371 (sewing capped at 0.48)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 77.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
