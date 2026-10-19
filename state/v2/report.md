# v2 shadow report

Turn 13405, 2026-10-19 22:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,961, prestige 3,421 (751 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 221 | 0 | 4 | 0 | 0 | min_holding 60, sell 36, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 152 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 110 | 116 | 508 | 0 | 58 | buy 110, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 37 | 37 | 25 | 0 | 12 | buy 37, buy @ 1.1 |

**0 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 58 labour expired last turn (~91 coin): holding 110 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5

## Notes

- labour: projection runs 150 over real use lately; planning 508, not 539

## Prestige spending, cheapest coin per prestige first

996 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 52.1 | 52.1 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 54.1 | 54.1 | thin at home: cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 54.4 | 54.4 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 54.7 | 54.7 | thin at home: cheese |
| hold feast 2 | townhouse | 2.6 | 52.2 | 55.2 | needs a townhouse (build cost 7,616) |
| hold banquet 2 (pies) | mansion | 7 | 55.3 | 55.3 | thin at home: pasties |
| hold prayer 2 | chapel | 13 | 53.4 | 56.2 | needs a chapel (build cost 34,114); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 56.4 | 56.4 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 56.4 | 56.4 | thin at home: pasties |
| hold sermon 2 | church | 24 | 53.1 | 56.8 | needs a church (build cost 81,151); thin at home: jewellery, furniture |
| hold sermon 2 (candles) | church | 31 | 54.4 | 57.3 | needs a church (build cost 81,151); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.032 | - | furniture 2 | -28 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 14.2 (keep 145); best orders clear only 3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 14.2 (keep 145); best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Briclives +19, Disscester +15
- Briclives would trade: beer sell 37 @ 4.64, furniture buy 1 @ 13.1; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Friedwerp | 684 | 0.17 | 0.20 (19/turn) | beer 37 (2.73->3.78), nets 2 (35->41.04), flax fibres 4 (4.52->5.27), dyed yarn 1 (9.87->10.36) | candles 1 (69.83->82.5), mouldboards 1 (39.27->46.55), grain 13 (2.79->3.26), iron ore 1 (3.51->4.64) | +61 |
| Briclives | 1041 | 0.33 | 0.40 (38/turn) | beer 37 (2.73->4.73), canvas 1 (30.87->34.2), tar 1 (9.97->11.88), flax fibres 1 (4.52->5.61) | slaked lime 1 (7.35->13.01) | +51 |
| Vauxvais | 204 | 0.05 | 0.10 (10/turn) | beer 37 (2.73->3.21), canvas 1 (30.87->35.72), flax fibres 4 (4.52->5.56), grain 4 (2.56->3.02) | thread 18 (4.22->4.72), candles 1 (77.7->82.5), wrought iron 5 (11.87->12.54), slaked lime 1 (11.13->13.01) | +44 |
| Chatgnan | 728 | 0.19 | 0.20 (19/turn) | cheese 9 (5.62->7.74), beer 37 (2.73->3.48), canvas 1 (30.87->31.92), varnish 1 (17.64->18.34) | candles 1 (75.08->82.5), grain 13 (2.81->3.26), garments 2 (20.48->20.8) | +42 |
| Unterhufe | 595 | 0.15 | 0.10 (10/turn) | nets 6 (35->39.14), cheese 7 (5.62->8.41), butter 2 (77.7->78.38), flax fibres 3 (4.52->4.99) | candles 1 (78.75->82.5), resin 2 (1.69->2.09) | +41 |

**Best:** Friedwerp at about +61 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 35 @ min 3.38 | makes 28.0, uses 4.2, holds 221 (keeps 60): sells the surplus + 11/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 58 @ 2.2, stop - |  | uses 508.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 110 = 1.9 turns |
| limestone |  | 5 @ min 17.1 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.0 |  |
| pasties | 3 @ 13.6, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 16 @ 1.1, stop - |  | uses 15.9/turn (observed), makes 0.0, holds 37 = 2.3 turns |
| rope |  | 2 @ min 74.5 |  |
| timber |  | 11 @ min 6.7 | makes 8.4, uses 0.0, holds 391 (keeps 350): sells the surplus + 3/turn of the excess |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 73.7 turns |

## Chain sizing

Mode HOLD, garments sold 3.0/turn (+0.0 exported); plan makes 1.6 garments a turn.
Labour: own 450, everything else 406, chain may buy 350 -> chain allowance 394, chain plan 128 (+2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.58 | 2.58 |
| ret | 3 | 0.48 | 0.46 |
| spin | 4 | 0.98 | 1.01 |
| weave | 3 | 0.07 | 0.05 |
| sew | 2 | 0.04 | 0.04 |

Buffers: flax fibres 58/45, thread 319/133, cloth 12/6

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
