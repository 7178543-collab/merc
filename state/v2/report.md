# v2 shadow report

Turn 13394, 2026-10-19 11:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,771, prestige 3,382 (712 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 238 | 0 | 4 | 0 | 0 | min_holding 60, sell 38, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 187 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 0 | 0 | 419 | 0 | 31 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 23 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.6 |
| porterage | 7 | 7 | 7 | 30 | 0 | buy 7, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: logging camp w/ tool, quarry 1 ran short of porterage (buy is live (7 @ 1.1), 7 bought last turn); labour need rises ~172/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 7, short of ~37 needed -> v2: buy 37

## Notes

- labour: projection runs 134 over real use lately; planning 424, not 559

## Prestige spending, cheapest coin per prestige first

1007 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.2 | 46.2 | running |
| hold feast 2 | townhouse | 2.6 | 53.0 | 55.7 | needs a townhouse (build cost 6,904); thin at home: wine |
| hold prayer 2 | chapel | 13 | 53.1 | 55.7 | needs a chapel (build cost 31,958); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 53.0 | 55.8 | needs a church (build cost 80,446); thin at home: candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 56.3 | 56.3 | thin at home: wine, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 56.4 | 56.4 | thin at home: wine |
| hold sermon 2 | church | 24 | 53.7 | 57.4 | needs a church (build cost 80,446); thin at home: furniture |
| jousting 1 | arena | 170 | 57.6 | 57.7 | needs a arena (build cost 24,968); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.8 | 57.8 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 57.8 | 57.8 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 57.9 | 57.9 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 58.8 | 58.8 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 120102307 | 0.312 | beer 39 | furniture 1 | 22 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 2 @ 14.2; crew 0.1; est +15 a turn; stock: furniture 2 @ 14.2 (keep 140)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Disscester +62, Karlmoor +54, Chatgnan +49, Briclives +44, Heilegg +37
- Disscester would trade: furniture buy 2 @ 14.1, garments sell 14 @ 22.8, rope sell 1 @ 84.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~93 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.10 | 0.30 (28/turn) | cheese 19 (5.35->5.84), timber 10 (6.2->8.07), beer 38 (2.77->3), fleece 1 (5.17->5.89) | thread 64 (4.64->5.55), flax fibres 14 (5.35->6.95), bellows 1 (256.2->275.5), pasties 2 (13.65->18.8) | +128 |
| Rouhomme | 368 | 0.09 | 0.80 (75/turn) | bread 150 (2.07->2.83), beer 38 (2.77->3.42), cheese 14 (5.35->6.08), timber 11 (6.2->7.98) | pasties 2 (14.6->18.8), lead bars 10 (12.08->12.82), flax fibres 2 (5.57->6.95), tiles 1 (3.76->5.42) | +125 |
| Vauxvais | 204 | 0.05 | 0.30 (28/turn) | bread 150 (2.07->2.66), tools 16 (4.12->4.69), beer 38 (2.77->2.96), cheese 5 (5.35->5.84) | flax fibres 12 (5.57->6.95), thread 17 (4.83->5.55), pasties 2 (14.6->18.8), tiles 2 (3.36->5.42) | +119 |
| Fontaux | 411 | 0.10 | 0.30 (28/turn) | casks 9 (5.51->9.5), cheese 15 (5.35->6.93), nails 1 (6.41->8.12), timber 11 (6.2->7.93) | bellows 1 (252->275.5), flax fibres 7 (5.83->6.95), thread 64 (5.35->5.55), hides 1 (9.71->12.44) | +101 |
| Hofkirchen | 991 | 0.29 | 0.30 (28/turn) | seeds 7 (1.98->4.27), tools 16 (4.12->4.62), tallow 1 (21.84->24.51) | bellows 1 (243.6->275.5), flax fibres 14 (5.51->6.95), pasties 2 (13.65->18.8), medicine 1 (122.85->125.4) | +71 |

**Best:** Hanstein at about +128 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 37 @ min 3.54 | makes 28.0, uses 4.2, holds 238 (keeps 60): sells the surplus + 13/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 20.8 | makes 3.3, uses 2.1, holds 187 (keeps 30): sells the surplus + 13/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 424.3/turn (brewery 1, flax farm 1, household), makes 450.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.6 |  |
| pasties | 3 @ 19.7, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 37 @ 1.1, stop - |  | uses 36.9/turn (observed), makes 0.0, holds 7 = 0.2 turns |
| rope |  | 6 @ min 74.5 | makes 2.2, uses 0.0, holds 48 (keeps 0): sells the surplus + 4/turn of the excess |
| tools | 3 @ 6.2, stop 22 |  | uses 2.6/turn (retting pit 1), makes 0.0, holds 199 = 75.9 turns |

## Chain sizing

Mode HOLD, garments sold 9.2/turn (+0.0 exported); plan makes 3.3 garments a turn.
Labour: own 450, everything else 512, chain may buy 350 -> chain allowance 350, chain plan 129 (+2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.40 | 2.35 |
| ret | 3 | 0.43 | 0.42 |
| spin | 4 | 0.88 | 0.91 |
| weave | 3 | 0.12 | 0.13 |
| sew | 2 | 0.08 | 0.08 |

Buffers: flax fibres 57/48, thread 433/140, cloth 18/13

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 1 (limited by porterage)
