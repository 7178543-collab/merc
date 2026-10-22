# v2 shadow report

Turn 13470, 2026-10-22 15:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,820, prestige 3,637 (517 free, +75.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 123 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 1 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 459 | 418 | 868 | 0 | 0 | buy 459, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 11 | 10 | 0 | 1 | buy 10, buy @ 1.1 |

**1 risks, 2 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 3, next step uses 32/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 55 coin last turn (crew 0.56) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **linen snake**: linen snake cost 49 coin last turn (crew 0.50) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 180
- **timber**: build materials for farmstead 1 are in (275.2 held, 9 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **farmstead 1** 56% (EXPANSION), about 2 turns left; still to deliver: labour 44, timber 9; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 9 | 275.2 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Notes

- labour: +20 crew for Flax Wyrm (crew 0.40, no projection from the game)
- labour: projection runs 81 over real use lately; planning 922, not 1004

## Prestige spending, cheapest coin per prestige first

931 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.1 | 49.1 | thin at home: pasties, hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 49.7 | 49.7 | thin at home: pasties, hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 49.8 | 49.8 | thin at home: pasties, wine, pies |
| jousting 3 | arena | 230 | 52.1 | 52.2 | needs a arena (build cost 25,889); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.7 | 52.7 | thin at home: wine, hop beer, ham |
| hold banquet 2 (fish) | mansion | 6.8 | 53.2 | 53.2 | thin at home: wine, cured fish |
| hold sermon 2 (candles) | church | 31 | 51.3 | 53.8 | needs a church (build cost 66,446); thin at home: jewellery, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 54.0 | 54.0 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.4 | 54.4 | thin at home: cured fish |
| hold prayer 2 | chapel | 13 | 51.6 | 54.5 | needs a chapel (build cost 32,980) |
| jousting 1 | arena | 170 | 55.2 | 55.4 | needs a arena (build cost 25,889); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.56 | 55 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.50 | 49 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 1 @ 68.5, pasties buy 2 @ 11.8, rope sell 2 @ 75.0, tools buy 3 @ 4.52; crew 0.1; est +25 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- best towns now: Etallaen +38, Brebronn +37, Chatgnan +33, Cobholme +33, Clairas +32
- Etallaen would trade: candles buy 1 @ 62.0, pasties buy 2 @ 12.5, rope sell 2 @ 78.5, tools buy 3 @ 4.44; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clairlond | 1288 | 0.47 | 0.20 (20/turn) | tackles 2 (189->228), lead bars 4 (14.07->16.72), coats 1 (68.25->76.95), hides 1 (12.39->17.86) | looms 1 (561.75->731.5), wax 2 (16.17->20.14), candles 1 (72.45->78), pasties 2 (12.5->15.9) | +290 |
| Hanbrücken | 531 | 0.14 | 0.20 (20/turn) | rope 2 (67->73.62), wool 4 (8.66->11.97), lead bars 1 (14.07->14.72), charcoal 13 (1.92->3.06) | looms 1 (546->731.5), flax fibres 20 (5.35->6.5), pasties 2 (13.55->15.9), candles 1 (76.12->78) | +234 |
| Heilegg | 826 | 0.23 | 0.30 (30/turn) | grindstones 1 (287.7->347.7), wrought iron 11 (13.65->16.25), lead bars 7 (14.07->16.53), lead ore 6 (11.03->13.77) | looms 1 (666.75->731.5), candles 1 (71.4->78), pasties 2 (12.18->15.9), flax fibres 8 (5.83->6.5) | +207 |
| Brunnham | 1281 | 0.47 | 0.20 (20/turn) | nets 11 (35.6->38.57), premium ham 1 (262.5->273.6), rope 2 (67->71.72), paper 5 (19.53->21.28) | looms 1 (593.25->731.5), candles 1 (69.3->78), pasties 2 (13.33->15.9), raw cloth 1 (5.51->6.41) | +192 |
| Bordetes | 831 | 0.23 | 0.30 (30/turn) | premium ham 1 (262.5->317.3), glass ingots 2 (57.23->84.08), lead ore 10 (11.03->14.44), rope 2 (67->74.58) | candles 1 (71.92->78), looms 1 (724.5->731.5), tools 3 (4.43->5.2), slaked lime 1 (6.83->7.84) | +192 |

**Best:** Clairlond at about +290 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 472 @ 2.2, stop - |  | uses 922.5/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 459 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.6 |  |
| pasties | 3 @ 16.6, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.4/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 65.0 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 10 = 9.6 turns |
| timber |  | 8 @ min 6.75 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 53.1 turns |

## Chain sizing

Mode HOLD, garments sold 14.2/turn (+1.6 exported); plan makes 17.2 garments a turn.
Labour: own 450, everything else 437, chain may buy 350 -> chain allowance 363, chain plan 362 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.61 | 5.63 |
| ret | 3 | 1.00 | 1.00 |
| spin | 4 | 2.05 | 2.06 |
| weave | 3 | 0.67 | 0.67 |
| sew | 2 | 0.40 | 0.42 |

Buffers: flax fibres 44/73, thread 262/214, cloth 3/67
- chain plan needed 575 labour, budget left 363: cut to 363 (sewing capped at 0.42)

## Self-diagnosis

- R1: garments slot dry: 1.0 held, 2.1 a turn (clothing slot (+1.2 prestige)); our buy none, home ask 20.0 (held back: failsafe level 2: reduce-only, would buy 5 @ 20.4 (ask 20.0, cap 34.3))
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
