# v2 shadow report

Turn 13442, 2026-10-21 11:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,546, prestige 3,598 (928 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 48 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.4 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 1, next step uses 42/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 65
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 167
- **timber**: build materials for net maker152202386007001 are in (350.8 held, 54 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **net maker152202386007001** 64% (INITIAL), about 5 turns left; still to deliver: labour 72, timber 54, tools 8; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 54 | 350.8 | 0 | off: covered; switch v1's buy off |
| tools | 8 | 199.1 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 15

## Notes

- labour: projection runs 92 over real use lately; planning 714, not 806

## Prestige spending, cheapest coin per prestige first

959 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold sermon 2 (candles) | church | 31 | 50.7 | 53.1 | needs a church (build cost 64,812); thin at home: candles, furniture |
| hold banquet 3 (pies) | mansion | 8 | 53.4 | 53.4 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 54.6 | 54.6 | thin at home: hop beer, pies |
| hold prayer 2 | chapel | 13 | 52.5 | 55.3 | needs a chapel (build cost 32,716); thin at home: furniture |
| hold sermon 2 | church | 24 | 52.3 | 55.4 | needs a church (build cost 64,812); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 56.3 | 56.3 |  |
| hold mass 1 | cathedral | 180 | 55.6 | 57.2 | needs a cathedral (build cost 238,190); thin at home: jewellery, glassware, candles |
| jousting 3 | arena | 230 | 58.0 | 58.1 | needs a arena (build cost 26,619); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.7 | 58.7 | thin at home: pies |
| hold banquet 3 (fish) | mansion | 7.6 | 59.2 | 59.2 | thin at home: hop beer, cured fish |
| hold banquet 4 | mansion | 17.5 | 59.2 | 59.2 | thin at home: hop beer, ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.092 | - | furniture 4 | -57 |
| linen snake | 0.1 / 0.10 | 10 | 185801747 | 0.08 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only 5 a turn after crew: ship stays at 0
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn; best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Brunnham +39, Karlmoor +37, Bedenis +32, Clairas +24, Calange +24
- Brunnham would trade: candles buy 1 @ 69.0, pasties buy 2 @ 11.8, rope sell 4 @ 82.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.30 (31/turn) | windows 1 (443.1->522.5), charcoal 12 (2.1->4.48), beer 51 (3.14->3.59), chisels 1 (15.23->22.61) | candles 1 (73.5->85.5), lead ore 3 (9.82->11.4), flax fibres 7 (5.57->6), wine 15 (6.35->6.51) | +151 |
| Hofkirchen | 991 | 0.32 | 0.30 (31/turn) | plate armour 1 (1291.5->1349), dye 1 (40.95->47.97), tools 16 (4.46->5.03), chisels 1 (15.23->18.52) | cheese 17 (7.61->8.74), candles 1 (72.98->85.5), garments 2 (19.32->20.2), pasties 2 (13.55->14.8) | +112 |
| Hanstein | 380 | 0.10 | 0.30 (31/turn) | medicine 1 (104.48->142.5), timber 8 (6.5->8.55), chisels 1 (15.23->17), scythes 1 (21.21->22.99) | cheese 17 (7.46->8.74), flax plants 83 (1.16->1.53), candles 1 (72.98->85.5), grain 26 (2.56->2.96) | +108 |
| Kirchwerp | 1072 | 0.37 | 0.20 (21/turn) | lathes 1 (155.4->179.55), wine 15 (7.25->8.55), dye 1 (40.95->47.97), coats 1 (57.75->62.22) | cheese 17 (6.25->8.74), candles 1 (71.92->85.5) | +104 |
| Friedwerp | 684 | 0.19 | 0.30 (31/turn) | beer 49 (3.14->3.84), gears 1 (61.43->70.77), casks 7 (6.2->7.74), dye 1 (40.95->47.97) | cheese 17 (6.35->8.74), candles 1 (73.5->85.5), pasties 2 (12.71->14.8), flax fibres 15 (5.62->6) | +100 |

**Best:** Rouhomme at about +151 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 264 @ 2.2, stop - |  | uses 714.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.8 |  |
| pasties | 3 @ 15.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.8 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.0/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 5 @ min 73.0 | makes 2.2, uses 0.0, holds 30 (keeps 0): sells the surplus + 2/turn of the excess |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 29 |  | uses 3.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 55.2 turns |

## Chain sizing

Mode HOLD, garments sold 20.5/turn (+0.0 exported); plan makes 21.3 garments a turn.
Labour: own 450, everything else 418, chain may buy 350 -> chain allowance 382, chain plan 382 (+8 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.24 | 5.43 |
| ret | 3 | 0.93 | 0.96 |
| spin | 4 | 1.92 | 1.99 |
| weave | 3 | 0.85 | 0.84 |
| sew | 2 | 0.53 | 0.52 |

Buffers: flax fibres 50/72, thread 284/211, cloth 1/84
- chain plan needed 529 labour, budget left 382: cut to 382 (sewing capped at 0.52)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
