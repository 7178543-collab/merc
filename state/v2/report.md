# v2 shadow report

Turn 13334, 2026-10-16 23:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,438, prestige 3,249 (579 free, -4.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 223 | 0 | 4 | 0 | 0 | min_holding 60, sell 35, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 34 | 0 | 2 | 0 | 0 | min_holding 30, sell 19, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 286 | 286 | 720 | 0 | 16 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 56 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 42/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 16 labour expired last turn (~26 coin): holding 286 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 80
- **flax plants**: flax plants buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 73 over real use lately; planning 721, not 794

## Prestige spending, cheapest coin per prestige first

1067 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 56.1 | 56.1 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.8 | 56.8 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.1 | 58.1 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 58.3 | 58.3 | thin at home: pasties, hop beer, wine, stockfish |
| hold banquet 3 (meat) | mansion | 7.6 | 58.6 | 58.6 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 59.8 | 59.8 | thin at home: hop beer, wine, stockfish, premium cheese, premium ham |
| hold prayer 2 | chapel | 13 | 57.7 | 60.2 | needs a chapel (build cost 32,484); thin at home: furniture |
| hold feast 2 | townhouse | 2.6 | 57.6 | 60.3 | needs a townhouse (build cost 7,204); thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 57.9 | 60.5 | needs a church (build cost 80,211); thin at home: jewellery, candles, furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 60.6 | 60.6 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Darmwald +24, Marmont +17
- Darmwald would trade: nets sell 5 @ 41.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Orlesailles | 1178 | 0.41 | 0.30 (30/turn) | garments 18 (19.99->22.61), thread 34 (4.68->6.27), nets 2 (34.2->40.85), canvas 1 (31.5->36.1) | swords 1 (197.4->355.3), pies 2 (17.22->18.62) | +250 |
| Rouhomme | 368 | 0.10 | 0.60 (60/turn) | thread 23 (4.68->6.27), charcoal 13 (1.85->4.43), beer 37 (2.97->3.69), canvas 1 (31.5->36.29) | swords 1 (210->355.3), garments 2 (21->22.8), flax plants 2 (0.78->1.65), tools 3 (4.91->5.15) | +232 |
| Großmühle | 751 | 0.20 | 0.10 (10/turn) | garments 16 (19.99->25.08), canvas 1 (31.5->33.82), casks 3 (5.62->6.32), nets 2 (34.2->34.96) | swords 1 (218.4->355.3), cured meat 4 (21.21->22.23), flax fibres 5 (5.57->6.05), honey 2 (7.88->8.17) | +220 |
| Friedwerp | 684 | 0.18 | 0.10 (10/turn) | garments 18 (19.99->21.28), casks 3 (5.62->7.74), nets 2 (34.2->36.29), varnish 1 (18.17->20.14) | swords 1 (203.7->355.3), cloth 17 (7.77->8.65), yarn 6 (3.28->4.03), flax fibres 7 (5.35->6.05) | +200 |
| Clarfranche | 1484 | 0.58 | 0.20 (20/turn) | paper 2 (22.26->32.49), garments 18 (19.99->21.09), nets 2 (34.2->37.24) | swords 1 (210->355.3), cloth 24 (7.61->8.65), axes 1 (14.7->15.67) | +187 |

**Best:** Orlesailles at about +250 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 35 @ min 3.7 | makes 28.0, uses 4.2, holds 223 (keeps 60): sells the surplus + 12/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 19 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 271 @ 2.2, stop - |  | uses 721.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 12 @ min 34.0 | makes 9.0, uses 0.0, holds 56 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 11 @ 1.1, stop - |  | uses 11.2/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 5 @ min 77.5 |  |
| timber |  | 29 @ min 6.7 | makes 8.4, uses 0.0, holds 611 (keeps 350): sells the surplus + 21/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 50.0 turns |

## Chain sizing

Mode HOLD, garments sold 20.2/turn (+0.0 exported); plan makes 20.9 garments a turn.
Labour: own 450, everything else 376, chain may buy 350 -> chain allowance 424, chain plan 425 (+3 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.44 | 6.50 |
| ret | 3 | 1.12 | 1.16 |
| spin | 4 | 2.36 | 2.38 |
| weave | 3 | 0.80 | 0.81 |
| sew | 2 | 0.52 | 0.51 |

Buffers: flax fibres 59/89, thread 413/263, cloth 0/81
- chain plan needed 578 labour, budget left 424: cut to 424 (sewing capped at 0.51)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 81.5 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
