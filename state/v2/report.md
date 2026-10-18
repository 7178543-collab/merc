# v2 shadow report

Turn 13376, 2026-10-18 17:47. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,413, prestige 3,297 (627 free, -2.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 371 | 0 | 4 | 0 | 0 | min_holding 60, sell 50, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 292 | 0 | 2 | 0 | 0 | min_holding 30, sell 32, sell @ 21.2 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 206 | 98 | 548 | 47 | 0 | buy 206, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 65 | 0 | 0 | 0 | 0 | min_holding 15, sell 13, sell @ 37.4 |
| porterage | 4 | 11 | 5 | 0 | 6 | buy 4, buy @ 1.1 |

**1 risks, 2 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: buying 4, short of ~9 needed -> v2: buy 9

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 27 coin last turn (crew 0.27) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: buying 206, need ~145 -> v2: buy 145

## Tuning

- **cloth**: cloth buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 38
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 73 over real use lately; planning 595, not 585

## Prestige spending, cheapest coin per prestige first

1025 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| jousting 1 | arena | 170 | 56.2 | 56.3 | needs a arena (build cost 24,803); thin at home: protection, light armour, arms; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 53.9 | 56.5 | needs a chapel (build cost 32,498); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 53.9 | 56.6 | needs a church (build cost 80,011); thin at home: jewellery, candles, furniture |
| hold feast 2 | townhouse | 2.6 | 54.2 | 57.2 | needs a townhouse (build cost 7,852); thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 57.3 | 57.3 | thin at home: wine, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.1 | 58.1 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 58.5 | 58.5 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 55.4 | 59.0 | needs a church (build cost 80,011); thin at home: jewellery, furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 59.3 | 59.3 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 59.8 | 59.8 | thin at home: pasties, hop beer, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.27 | 26 | - | 0 | - | - | 0 |
| linen snake | 0.1 / 0.33 | 32 | 151802239 | 0.488 | - | furniture 29, pasties 1 | -415 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 21 @ 14.0, nets sell 2 @ 33.8, pasties buy 3 @ 15.3; crew 0.1; est +294 a turn; stock: furniture 21 @ 14.0 (keep 140); stock: pasties 3 @ 15.3 (keep 14)
- best towns now: Fulkirch +491, Heilegg +458, Amsdermund +451, Pontmont +412, Hofkirchen +404
- Fulkirch would trade: furniture buy 26 @ 13.3, nets sell 10 @ 38.6, pasties buy 5 @ 15.4; crew 0.8

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heidlowe | 662 | 0.17 | 0.30 (29/turn) | nets 11 (17.29->34.2), tools 16 (4.24->4.73), wrought iron 7 (13.76->14.44), beer 45 (2.98->3.36) | flax fibres 26 (5.08->6.35), cloth 5 (7.19->7.85) | +219 |
| Fulkirch | 1576 | 0.61 | 0.20 (19/turn) | nets 10 (17.29->37.24), tallow 1 (19.95->23.94), cloth 2 (6.87->7.89) | dyed yarn 1 (8.87->9.69), garments 2 (20.58->21.2) | +188 |
| Marmont | 638 | 0.17 | 0.10 (10/turn) | nets 9 (17.29->36.86), lead ore 1 (7.61->10.45), tools 13 (4.24->4.52) | wrought iron 3 (11.76->12.06) | +174 |
| Amsdermund | 1111 | 0.37 | 0.30 (29/turn) | nets 6 (17.29->39.9), limestone 1 (20.16->45.98), thread 16 (4.66->5.22), wine 9 (5.62->6.32) | cheese 20 (5.67->6.22) | +152 |
| Corstoft | 1496 | 0.57 | 0.20 (19/turn) | nets 7 (17.29->35.53), rope 1 (79->85.97), tallow 1 (19.95->25.08), cloth 2 (6.87->8.12) | flax fibres 10 (5.08->6.35), dyed yarn 1 (8.87->9.69) | +132 |

**Best:** Heidlowe at about +219 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 48 @ min 3.54 | makes 28.0, uses 4.2, holds 371 (keeps 60): sells the surplus + 24/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 29 @ min 21.2 | makes 9.8, uses 2.1, holds 292 (keeps 30): sells the surplus + 21/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 145 @ 2.2, stop - |  | uses 595.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 206 = 1.4 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 12 @ min 34.0 | makes 9.0, uses 0.0, holds 65 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 9 @ 1.1, stop - |  | uses 9.3/turn (observed), makes 0.0, holds 4 = 0.4 turns |
| rope |  | 7 @ min 77.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 8 @ min 6.9 |  |
| tools | 4 @ 6.2, stop 27 |  | uses 3.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 59.2 turns |

## Chain sizing

Mode HOLD, garments sold 7.7/turn (+0.0 exported); plan makes 2.9 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 118 (-149 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.58 | 2.22 |
| ret | 3 | 0.81 | 0.39 |
| spin | 4 | 1.68 | 0.87 |
| weave | 3 | 0.38 | 0.08 |
| sew | 2 | 0.24 | 0.07 |

Buffers: flax fibres 59/47, thread 429/139, cloth 33/12

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R4: logging camp w/ tool projected 0 of 7 (limited by porterage)
