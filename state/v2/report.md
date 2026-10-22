# v2 shadow report

Turn 13472, 2026-10-22 17:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,633, prestige 3,632 (512 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 120 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 449 | 459 | 712 | 0 | 197 | buy 273, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.2 turns (holds 6, next step uses 32/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 197 labour expired last turn (~322 coin): holding 449 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 180

## Notes

- labour: projection runs 84 over real use lately; planning 712, not 777

## Prestige spending, cheapest coin per prestige first

929 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 4 (pies) | mansion | 18 | 49.2 | 49.2 | thin at home: pasties, hop beer, wine |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 2 (pies) | mansion | 7 | 50.1 | 50.1 | thin at home: pasties, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 50.1 | 50.1 | thin at home: pasties, hop beer, pies |
| jousting 3 | arena | 230 | 52.3 | 52.4 | needs a arena (build cost 25,780); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.7 | 52.7 | thin at home: wine, hop beer, ham |
| hold banquet 2 (fish) | mansion | 6.8 | 53.0 | 53.0 | thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 51.2 | 53.7 | needs a church (build cost 65,123); thin at home: jewellery, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 53.9 | 53.9 | thin at home: hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 54.6 | 54.6 |  |
| hold prayer 2 | chapel | 13 | 51.7 | 54.6 | needs a chapel (build cost 33,004) |
| jousting 1 | arena | 170 | 55.2 | 55.4 | needs a arena (build cost 25,780); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.04 | rope 1 | - | 12 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Clairlond +26, Chribruck +18, Karlmoor +18, Friedwerp +18, Bremcop +17
- Clairlond would trade: candles buy 1 @ 67.5, pasties buy 2 @ 12.0, rope sell 2 @ 84.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Brunnham | 1281 | 0.47 | 0.20 (20/turn) | lead ore 2 (9.5->18.71), nets 11 (35.6->37.62), lead bars 3 (13.97->17.1), leather 1 (25.2->29.45) | looms 1 (593.25->717.25), medicine 3 (123.9->138.7), lathes 1 (185.85->218.5), acid 1 (134.4->144.4) | +250 |
| Clarfranche | 1484 | 0.58 | 0.30 (30/turn) | lead bars 4 (13.97->17.67), chisels 1 (12.39->16.05), leather 1 (25.2->29.45), flax plants 7 (1.42->2.79) | looms 1 (561.75->717.25), premium ham 1 (296.1->317.3), lathes 1 (198.45->218.5), copper ingots 3 (12.92->16.62) | +225 |
| Amsdermund | 1111 | 0.38 | 0.30 (30/turn) | herbs 2 (35.28->38), malt 2 (6.46->8.03), lead bars 1 (13.97->15.01), lead ore 2 (9.5->11.88) | premium ham 1 (206.85->317.3), looms 1 (661.5->717.25), candles 1 (69.3->78), copper ingots 3 (14.38->16.62) | +191 |
| Gosschweig | 1099 | 0.38 | 0.30 (30/turn) | flour 2 (20.27->27.93), lead bars 3 (13.97->16.25), nets 3 (35.6->37.24), lead ore 2 (9.5->12.44) | looms 1 (645.75->717.25), medicine 3 (115.5->138.7), candles 1 (69.3->78), pasties 2 (13.02->15.4) | +172 |
| Heilegg | 826 | 0.23 | 0.20 (20/turn) | grindstones 1 (285.6->347.7), lead ore 2 (9.5->13.96), lead bars 4 (13.97->15.39), rope 2 (74->76) | looms 1 (666.75->717.25), medicine 2 (120.75->138.7), candles 1 (74.03->78), pasties 2 (12.71->15.4) | +168 |

**Best:** Brunnham at about +250 coin a turn.

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
| labour | 262 @ 2.2, stop - |  | uses 712.5/turn (brewery 1, flax farm 1, household), makes 450.0, holds 449 = 1.7 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.6 |  |
| pasties | 3 @ 16.1, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.8 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.4/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 72.0 |  |
| timber |  | 8 @ min 6.65 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.3 turns |

## Chain sizing

Mode HOLD, garments sold 13.0/turn (+0.8 exported); plan makes 18.4 garments a turn.
Labour: own 450, everything else 415, chain may buy 350 -> chain allowance 385, chain plan 385 (+26 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.61 | 5.97 |
| ret | 3 | 1.00 | 1.06 |
| spin | 4 | 2.05 | 2.18 |
| weave | 3 | 0.67 | 0.71 |
| sew | 2 | 0.40 | 0.45 |

Buffers: flax fibres 44/74, thread 253/218, cloth 6/71
- chain plan needed 564 labour, budget left 385: cut to 385 (sewing capped at 0.45)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
