# v2 shadow report

Turn 13402, 2026-10-19 19:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,768, prestige 3,424 (754 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 312 | 0 | 4 | 0 | 0 | min_holding 60, sell 39, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 175 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 0 | 0 | 428 | 0 | 22 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.6 |
| porterage | 37 | 7 | 7 | 30 | 0 | buy 37, buy @ 1.1 |

**1 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: logging camp w/ tool, quarry 1 ran short of porterage (buy is live (37 @ 1.1), 7 bought last turn); labour need rises ~172/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 9 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Notes

- labour: projection runs 145 over real use lately; planning 510, not 655

## Prestige spending, cheapest coin per prestige first

999 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.2 | 46.2 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 53.6 | 53.6 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 53.7 | 53.7 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.0 | 54.0 | thin at home: cured fish |
| hold prayer 2 | chapel | 13 | 53.1 | 55.8 | needs a chapel (build cost 32,350); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 56.0 | 56.0 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 56.2 | 56.2 | thin at home: wine |
| jousting 1 | arena | 170 | 56.3 | 56.4 | needs a arena (build cost 24,932); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 57.8 | 57.8 |  |
| hold sermon 2 | church | 24 | 54.5 | 58.2 | needs a church (build cost 80,716); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 55.3 | 58.2 | needs a church (build cost 80,716); thin at home: candles, furniture |
| hold banquet 3 (pies) | mansion | 8 | 59.4 | 59.4 | thin at home: pasties |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 120102307 | 0.392 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.392 | - | furniture 1 | -14 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only 12 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Disscester +37, Briclives +31
- Disscester would trade: garments sell 12 @ 22.8, rope sell 1 @ 88.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Friedwerp | 684 | 0.17 | 0.30 (28/turn) | beer 43 (2.73->4.01), nets 3 (35.6->37.43), flax fibres 4 (4.5->5.08), thread 9 (4.66->4.89) | candles 1 (68.78->81.5), flax fibres 11 (5.67->6.6), mouldboards 1 (40.11->46.17), pasties 1 (12.71->18.6) | +88 |
| Hofkirchen | 991 | 0.29 | 0.10 (9/turn) | wrought iron 7 (12.6->17.67), flax fibres 4 (4.5->6.08) | candles 1 (71.4->81.5), paper 8 (20.48->22.04), jewellery 1 (73.5->83.12), medicine 1 (118.65->128.25) | +87 |
| Darmwald | 1022 | 0.31 | 0.40 (37/turn) | bellows 1 (325.5->364.8), tools 16 (4.8->6.32), beer 44 (2.73->3.48), flax fibres 4 (4.5->5.98) | pasties 2 (14.49->18.6), jewellery 1 (77.7->83.12), garments 2 (20.48->20.8) | +79 |
| Briclives | 1041 | 0.32 | 0.40 (37/turn) | beer 44 (2.73->4.89), canvas 1 (30.66->34.01), flax fibres 1 (4.5->5.61) | pasties 2 (15.23->18.6), nails 3 (4.77->5.27), tools 2 (4.35->4.82) | +72 |
| Heilegg | 826 | 0.21 | 0.10 (9/turn) | spinning wheels 1 (258.3->288.8), flax fibres 4 (4.5->5.37), dyed yarn 1 (9.77->10.73) | candles 1 (70.88->81.5), pasties 2 (13.65->18.6), jewellery 1 (78.75->83.12), garments 2 (20.06->20.8) | +53 |

**Best:** Friedwerp at about +88 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 43 @ min 3.38 | makes 28.0, uses 4.2, holds 312 (keeps 60): sells the surplus + 19/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 60 @ 2.2, stop - |  | uses 509.7/turn (brewery 1, flax farm 1, household), makes 450.0, holds 0 = 0.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.6 |  |
| pasties | 3 @ 19.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.8 turns |
| porterage | 14 @ 1.1, stop - |  | uses 14.2/turn (observed), makes 0.0, holds 37 = 2.6 turns |
| rope |  | 4 @ min 74.5 | makes 2.2, uses 0.0, holds 20 (keeps 0): sells the surplus + 1/turn of the excess |
| tools | 6 @ 6.2, stop 45 |  | uses 5.5/turn (retting pit 1), makes 0.0, holds 199 = 36.2 turns |

## Chain sizing

Mode HOLD, garments sold 2.0/turn (+0.0 exported); plan makes 1.2 garments a turn.
Labour: own 450, everything else 512, chain may buy 350 -> chain allowance 350, chain plan 126 (-6 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.58 | 2.61 |
| ret | 3 | 0.48 | 0.46 |
| spin | 4 | 0.98 | 1.02 |
| weave | 3 | 0.09 | 0.03 |
| sew | 2 | 0.06 | 0.03 |

Buffers: flax fibres 57/45, thread 304/132, cloth 13/5

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: ropewalk 1, quarry 1 projected 0: short of labour (~124 needed); labour itself is not raised here
