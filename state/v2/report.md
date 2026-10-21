# v2 shadow report

Turn 13451, 2026-10-21 20:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,175, prestige 3,586 (916 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 174 | 0 | 4 | 0 | 0 | min_holding 60, sell 57, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 41 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 11 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.4 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**2 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 42/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 1.0 turns (holds 87, next step uses 87/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for net maker152202386007001 are in (350.6 held, 22 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **net maker152202386007001** 86% (INITIAL), about 2 turns left; still to deliver: labour 29, timber 22, tools 3; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 22 | 350.6 | 0 | off: covered; switch v1's buy off |
| tools | 3 | 199.7 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 15

## Notes

- labour: projection runs 87 over real use lately; planning 725, not 801

## Prestige spending, cheapest coin per prestige first

950 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.6 | 49.6 | thin at home: pasties, wine, ham, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.8 | 49.8 | thin at home: pasties, pies |
| hold banquet 2 (pies) | mansion | 7 | 52.0 | 52.0 | thin at home: pasties, wine, pies |
| hold banquet 4 | mansion | 17.5 | 53.7 | 53.7 | thin at home: wine, ham, stockfish |
| hold sermon 2 (candles) | church | 31 | 51.7 | 54.1 | needs a church (build cost 63,496); thin at home: jewellery, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |
| hold sermon 2 | church | 24 | 52.3 | 55.3 | needs a church (build cost 63,496); thin at home: jewellery |
| hold prayer 2 | chapel | 13 | 52.9 | 55.6 | needs a chapel (build cost 32,094) |
| hold banquet 3 (fish) | mansion | 7.6 | 56.2 | 56.2 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 57.3 | 57.3 | thin at home: wine, cured fish |
| jousting 3 | arena | 230 | 57.5 | 57.6 | needs a arena (build cost 25,195); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.3 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: furniture buy 20 @ 13.7; crew 0.2; est +234 a turn; stock: furniture 20 @ 13.7 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn
- best towns now: Cobholme +488, Grandgues +458, Fulkirch +421, Bordetes +418, Hofkirchen +415
- Cobholme would trade: beer sell 60 @ 5.45, furniture buy 37 @ 13.2; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Dortdorf | 871 | 0.25 | 0.10 (10/turn) | plate armour 1 (1044.75->1444), herbs 1 (27.09->33.25), pies 1 (12.29->14.54), raw cloth 1 (6.41->7.89) | candles 1 (71.4->76), spirits 1 (16.48->19.95), copper ore 1 (18.79->22.23), hinges 1 (29.61->30.78) | +413 |
| Briclives | 1041 | 0.34 | 0.10 (10/turn) | tapestries 2 (635.25->836), gold ore 1 (129.15->139.65), cheese 9 (8.56->8.98), dyed yarn 1 (6.72->7.36) | lead ore 3 (9.13->11.4), tools 3 (4.28->4.72) | +410 |
| Bordetes | 831 | 0.23 | 0.20 (20/turn) | plate armour 1 (1044.75->1311), limestone 1 (20.58->52.25), dye 2 (50.82->52.25), ham 1 (59.33->61.75) | coats 1 (62.48->68.88), medicine 1 (113.4->119.7), candles 1 (72.45->76), garments 2 (20.16->21) | +304 |
| Kleinburgh | 1440 | 0.55 | 0.60 (60/turn) | gold ore 1 (129.15->212.8), lead ore 7 (13.02->20.33), furniture 12 (11.87->15.58), leather 1 (23.73->29.07) | sails 1 (489.3->636.5), coats 1 (63.53->68.88), candles 1 (72.98->76) | +282 |
| Marmont | 638 | 0.17 | 0.30 (30/turn) | tapestries 1 (635.25->793.25), beer 61 (3.24->4.29), malt 1 (7.35->11.11), dyed yarn 1 (6.72->7.12) | wrought iron 3 (11.97->12.35) | +198 |

**Best:** Dortdorf at about +413 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 57 @ min 3.38 | makes 56.0, uses 4.2, holds 174 (keeps 60): sells the surplus + 5/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.2 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 275 @ 2.2, stop - |  | uses 725.2/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.2 |  |
| pasties | 3 @ 12.6, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.2/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 75.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 54.1 turns |

## Chain sizing

Mode HOLD, garments sold 20.0/turn (+0.0 exported); plan makes 20.9 garments a turn.
Labour: own 450, everything else 418, chain may buy 350 -> chain allowance 382, chain plan 382 (-3 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.45 | 5.49 |
| ret | 3 | 0.97 | 0.98 |
| spin | 4 | 2.00 | 2.01 |
| weave | 3 | 0.83 | 0.82 |
| sew | 2 | 0.53 | 0.51 |

Buffers: flax fibres 48/71, thread 258/209, cloth 0/82
- chain plan needed 532 labour, budget left 382: cut to 382 (sewing capped at 0.51)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
