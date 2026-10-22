# v2 shadow report

Turn 13465, 2026-10-22 10:02. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,941, prestige 3,568 (898 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 129 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 63 | 0 | 2 | 0 | 0 | min_holding 30, sell 24, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 290 | 285 | 732 | 0 | 3 | buy 290, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 34.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 45/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 176

## Notes

- labour: projection runs 75 over real use lately; planning 732, not 805

## Prestige spending, cheapest coin per prestige first

936 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 47.9 | 47.9 | thin at home: wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 48.2 | 48.2 | thin at home: pies |
| hold banquet 2 (pies) | mansion | 7 | 48.3 | 48.3 | thin at home: wine, pies |
| hold sermon 2 (candles) | church | 31 | 48.8 | 51.3 | needs a church (build cost 65,903); thin at home: jewellery, candles, furniture |
| hold banquet 4 | mansion | 17.5 | 51.8 | 51.8 | thin at home: wine, ham |
| jousting 3 | arena | 230 | 52.6 | 52.7 | needs a arena (build cost 25,892); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 53.4 | 53.4 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 54.0 | 54.0 |  |
| hold sermon 2 | church | 24 | 50.9 | 54.1 | needs a church (build cost 65,903); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 51.4 | 54.2 | needs a townhouse (build cost 6,730); thin at home: wine |
| hold prayer 2 | chapel | 13 | 51.3 | 54.2 | needs a chapel (build cost 32,687); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.188 | nets 1, rope 1 | furniture 9 | -87 |
| linen snake | 0.1 / 0.06 | 6 | 185801747 | 0.048 | - | furniture 1 | -14 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: furniture buy 2 @ 14.6, garments sell 23 @ 21.8; crew 0.1; est +47 a turn; stock: furniture 2 @ 14.6 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Cobholme +69, Neuborn +47, Chribruck +46, Disscester +45, Marmont +44
- Cobholme would trade: beer sell 56 @ 5.55, furniture buy 2 @ 13.2, rope sell 2 @ 79.5; crew 0.8

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bordetes | 831 | 0.22 | 0.10 (10/turn) | plate armour 1 (1044.75->1216), rope 2 (68->73.15), tackles 1 (168->171.95), chisels 1 (15.02->15.77) | spinning wheels 1 (231->248.9), steel ingots 3 (15.54->18.9), canvas 2 (24.99->28.12), tallow 1 (14.8->16.53) | +213 |
| Heilegg | 826 | 0.22 | 0.30 (29/turn) | grindstones 1 (277.2->347.7), casks 5 (5.72->9.17), sails 1 (614.25->627), rope 2 (68->71.72) | gold bars 1 (782.25->817), steel ingots 4 (16.38->18.9), cheese 16 (6.2->6.6), pasties 2 (12.18->13.9) | +154 |
| Marmont | 638 | 0.17 | 0.20 (20/turn) | beer 51 (3.18->4.22), rope 2 (68->78.85), blades 1 (12.5->13.49), chisels 1 (15.02->16.15) | acid 1 (104.48->133.95), steel ingots 2 (13.02->18.9), pasties 2 (12.92->13.9), glassware 1 (47.25->47.5) | +100 |
| Clairlond | 1288 | 0.46 | 0.20 (20/turn) | rope 2 (68->75.05), hides 1 (12.5->18.14), nets 2 (35.6->37.24), chisels 1 (15.02->15.86) | looms 1 (530.25->579.5), steel ingots 5 (14.28->18.9), cheese 9 (5.25->6.6), pasties 2 (12.5->13.9) | +92 |
| Cobholme | 1564 | 0.61 | 0.80 (78/turn) | beer 56 (3.18->5.37), rope 2 (68->76.95), lead bars 3 (16.7->19.95), wheels 1 (20.06->21.28) | gears 1 (50.61->58.9), steel ingots 1 (15.44->18.9), wax 1 (20.16->22.8) | +87 |

**Best:** Bordetes at about +213 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 3.38 | makes 56.0, uses 4.2, holds 129 (keeps 60): sells the surplus + 1/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 10 @ min 20.0 | makes 23.0, uses 2.1, holds 63 (keeps 30): sells the surplus + 3/turn of the excess; ships offer 23 a turn abroad, so home sells 10 (was 24) |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 282 @ 2.2, stop - |  | uses 731.9/turn (brewery 1, flax farm 1, household), makes 450.0, holds 290 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.6 |  |
| pasties | 3 @ 13.6, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.3/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 71.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.8 turns |

## Chain sizing

Mode HOLD, garments sold 14.0/turn (+2.3 exported); plan makes 22.6 garments a turn.
Labour: own 450, everything else 403, chain may buy 350 -> chain allowance 397, chain plan 397 (+1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.54 | 5.59 |
| ret | 3 | 0.98 | 0.99 |
| spin | 4 | 2.03 | 2.04 |
| weave | 3 | 0.90 | 0.89 |
| sew | 2 | 0.56 | 0.55 |

Buffers: flax fibres 44/73, thread 282/216, cloth 0/89
- chain plan needed 612 labour, budget left 397: cut to 397 (sewing capped at 0.55)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R3: net maker152202386007001 (net maker) finished but idle 6 turns (no recipe) (held back: failsafe level 1: reduce-only, would start make nets 1 at 0.5 (storehouse provider))
