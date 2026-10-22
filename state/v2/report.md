# v2 shadow report

Turn 13474, 2026-10-22 19:07. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,361, prestige 3,629 (509 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 118 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 43 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 212 | 273 | 702 | 0 | 71 | buy 212, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 2 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.3 turns (holds 9, next step uses 32/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 71 labour expired last turn (~118 coin): holding 212 against a ~0 buffer target -> v2: trim the buy until the stock is near 0
- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 180

## Notes

- labour: projection runs 84 over real use lately; planning 702, not 777
- labour expiry guard: 71 bought labour expired last turn, buy 202 (not 202) this turn

## Prestige spending, cheapest coin per prestige first

927 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 48.8 | 48.8 | thin at home: wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 48.9 | 48.9 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 49.3 | 49.3 | thin at home: hop beer, wine |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| jousting 3 | arena | 230 | 52.6 | 52.8 | needs a arena (build cost 26,018); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 | thin at home: wine |
| hold banquet 4 | mansion | 17.5 | 53.1 | 53.1 | thin at home: wine, hop beer, ham |
| hold banquet 3 (fish) | mansion | 7.6 | 53.6 | 53.6 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 51.5 | 54.1 | needs a church (build cost 65,616); thin at home: candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 54.7 | 54.7 |  |
| hold prayer 2 | chapel | 13 | 51.9 | 54.9 | needs a chapel (build cost 33,250); thin at home: furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 55.3 | 55.3 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 11 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Clairlond +30, Amsdermund +24, Gosschweig +22, Briclives +18
- Clairlond would trade: candles buy 1 @ 60.0, rope sell 2 @ 84.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clarfranche | 1484 | 0.59 | 0.30 (30/turn) | garments 15 (19.8->23.18), rope 2 (64.33->72.67), lead bars 7 (15.54->17.67), flax plants 4 (1.29->3.15) | gold ore 2 (156.45->166.25), candles 1 (70.88->80.5), copper ingots 2 (13.02->13.68), tools 3 (4.45->5.15) | +99 |
| Toqueque | 642 | 0.17 | 0.10 (10/turn) | tackles 1 (169.05->237.5), rope 2 (64.33->76), lead ore 3 (9.97->11.3), malt 1 (5.88->7.6) | candles 1 (74.55->80.5), beer 4 (3.07->3.5) | +95 |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | jewellery 4 (92.4->99.75), rope 2 (64.33->71.72), tackles 1 (169.05->177.65), herbs 1 (35.91->41.8) | premium ham 1 (206.85->239.4), candles 1 (71.4->80.5), blades 2 (12.29->12.63), garments 2 (19.53->20) | +93 |
| Rouhomme | 368 | 0.10 | 0.30 (30/turn) | rope 2 (64.33->72.67), charcoal 13 (2.01->3.46), copper ore 1 (24.99->34.58), honey 3 (7.98->9.69) | chisels 5 (9.35->12.35), candles 1 (70.88->80.5), spinning wheels 1 (222.6->228), tools 3 (4.51->5.15) | +85 |
| Magdeach | 667 | 0.18 | 0.20 (20/turn) | grindstones 1 (283.5->315.4), rope 2 (64.33->75.05), nets 4 (35.6->40.66), malt 5 (5.88->6.7) | candles 1 (73.5->80.5), cheese 11 (5.3->5.61), salt 6 (4.03->4.37), chisels 1 (11.76->12.35) | +78 |

**Best:** Clarfranche at about +99 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 202 @ 2.2, stop - |  | uses 701.7/turn (brewery 1, flax farm 1, household), makes 500.0, holds 212 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.6 |  |
| pasties | 3 @ 13.1, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.4/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 3 @ min 73.0 |  |
| timber |  | 8 @ min 6.75 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.3 turns |

## Chain sizing

Mode HOLD, garments sold 12.2/turn (+0.0 exported); plan makes 22.6 garments a turn.
Labour: own 500, everything else 415, chain may buy 350 -> chain allowance 435, chain plan 435 (+76 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.61 | 6.44 |
| ret | 3 | 1.00 | 1.14 |
| spin | 4 | 2.05 | 2.36 |
| weave | 3 | 0.67 | 0.89 |
| sew | 2 | 0.40 | 0.55 |

Buffers: flax fibres 45/80, thread 244/236, cloth 9/89
- chain plan needed 545 labour, budget left 435: cut to 435 (sewing capped at 0.55)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
