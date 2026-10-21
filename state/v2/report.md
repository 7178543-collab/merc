# v2 shadow report

Turn 13453, 2026-10-21 22:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,561, prestige 3,583 (913 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 163 | 0 | 4 | 0 | 0 | min_holding 60, sell 57, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 39 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 275 | 725 | 0 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 42/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 1.0 turns (holds 87, next step uses 87/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68
- **timber**: build materials for net maker152202386007001 are in (350.7 held, 5 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **net maker152202386007001** 97% (INITIAL), about 1 turns left; still to deliver: labour 7, timber 5, tools 1; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 5 | 350.7 | 0 | off: covered; switch v1's buy off |
| tools | 1 | 199.4 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 7

## Notes

- labour: projection runs 87 over real use lately; planning 725, not 790

## Prestige spending, cheapest coin per prestige first

948 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.7 | 50.7 | thin at home: pasties, ham, pies |
| hold banquet 3 (pies) | mansion | 8 | 52.0 | 52.0 | thin at home: pasties, pies |
| hold banquet 2 (pies) | mansion | 7 | 53.9 | 53.9 | thin at home: pasties, pies |
| hold banquet 4 | mansion | 17.5 | 54.3 | 54.3 | thin at home: ham |
| hold sermon 2 (candles) | church | 31 | 52.1 | 54.6 | needs a church (build cost 65,018); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 52.0 | 54.9 | needs a chapel (build cost 33,383); thin at home: furniture |
| hold sermon 2 | church | 24 | 52.8 | 55.9 | needs a church (build cost 65,018); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 56.0 | 56.0 |  |
| jousting 3 | arena | 230 | 56.9 | 57.1 | needs a arena (build cost 26,195); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 57.3 | 57.3 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.1 | 58.1 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.2 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: furniture buy 20 @ 13.7; crew 0.2; est +234 a turn; stock: furniture 20 @ 13.7 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn
- best towns now: Cobholme +506, Bordetes +442, Hofkirchen +434, Orlesailles +379, Heilegg +373
- Cobholme would trade: beer sell 59 @ 5.35, furniture buy 39 @ 13.2; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Briclives | 1041 | 0.34 | 0.10 (10/turn) | tapestries 2 (603.75->1016.5), cheese 9 (8.29->8.98), pasties 1 (13.7->14.82) | candles 1 (75.6->83.5), blades 1 (11.13->13.77), canvas 2 (26.25->26.98), tools 3 (4.24->4.64) | +835 |
| Hanstein | 380 | 0.10 | 0.20 (20/turn) | looms 1 (426.3->698.25), lathes 1 (123.9->154.85), timber 8 (6.7->8.79), flax fibres 4 (4.61->5.37) | candles 1 (71.92->83.5), lead ore 1 (8.77->11.4), pasties 2 (13.97->14.9), tar 3 (10.71->11.4) | +324 |
| Marmont | 638 | 0.17 | 0.30 (30/turn) | tapestries 1 (603.75->788.5), beer 60 (3.22->4.75), yarn 6 (4.77->5.84), flax fibres 3 (4.61->5.22) | candles 1 (74.03->83.5), herbs 1 (31.08->38.19), tar 3 (9.82->11.4), wine 10 (5.02->5.61) | +289 |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | plate armour 1 (1044.75->1187.5), jewellery 2 (88.73->99.75), thread 6 (4.08->4.89), leather 1 (23.94->25.27) | candles 1 (75.6->83.5), tar 6 (10.13->11.4), cloth 8 (8.03->8.5), hinges 2 (30.87->31.92) | +181 |
| Bordees | 1112 | 0.38 | 0.10 (10/turn) | looms 1 (426.3->551), nets 2 (38->39.9) | herbs 1 (27.51->38.19), candles 1 (76.65->83.5), cloth 18 (7.88->8.5), jewellery 1 (77.17->78.38) | +145 |

**Best:** Briclives at about +835 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 56 @ min 3.38 | makes 56.0, uses 4.2, holds 163 (keeps 60): sells the surplus + 4/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 275 @ 2.2, stop - |  | uses 725.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.0 |  |
| pasties | 3 @ 15.6, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.2/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 77.0 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 54.0 turns |

## Chain sizing

Mode HOLD, garments sold 20.0/turn (+0.0 exported); plan makes 20.9 garments a turn.
Labour: own 450, everything else 410, chain may buy 350 -> chain allowance 390, chain plan 391 (+8 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.45 | 5.70 |
| ret | 3 | 0.97 | 1.01 |
| spin | 4 | 2.00 | 2.09 |
| weave | 3 | 0.83 | 0.82 |
| sew | 2 | 0.53 | 0.51 |

Buffers: flax fibres 48/71, thread 248/209, cloth 0/82
- chain plan needed 533 labour, budget left 390: cut to 390 (sewing capped at 0.51)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
