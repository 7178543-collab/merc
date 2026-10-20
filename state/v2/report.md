# v2 shadow report

Turn 13427, 2026-10-20 20:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,988, prestige 3,396 (726 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 55 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.2 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 5 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 6, next step uses 46/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 63
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 162
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1, net maker152202386007001 are in (279.3 held, 99 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 40% (EXPANSION), about 8 turns left; still to deliver: labour 156, limestone 36, timber 24; ready for labour
- **net maker152202386007001** 50% (INITIAL), about 6 turns left; still to deliver: labour 100, timber 75, tools 10; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 36 | 75.7 | 0 | off: covered |
| timber | 99 | 279.3 | 0 | off: covered; switch v1's buy off |
| tools | 10 | 199.9 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 37

## Notes

- labour: projection runs 88 over real use lately; planning 722, not 811

## Prestige spending, cheapest coin per prestige first

974 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 53.9 | running |
| hold banquet 3 (pies) | mansion | 8 | 54.0 | 54.0 | thin at home: pasties, hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 54.9 | 54.9 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 54.9 | 54.9 | thin at home: hop beer, cured fish |
| hold prayer 2 | chapel | 13 | 52.6 | 55.5 | needs a chapel (build cost 33,830); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 53.0 | 55.6 | needs a church (build cost 72,184); thin at home: candles, furniture |
| hold mass 2 (premium) | cathedral | 360 | 55.2 | 56.2 | needs a cathedral (build cost 287,530); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold sermon 2 | church | 24 | 52.9 | 56.3 | needs a church (build cost 72,184); thin at home: furniture |
| jousting 3 | arena | 230 | 57.5 | 57.6 | needs a arena (build cost 26,994); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 57.7 | 57.7 | thin at home: wine, cured fish |
| jousting 1 | arena | 170 | 57.6 | 57.7 | needs a arena (build cost 26,994); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 57.8 | 57.8 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.1 | - | furniture 5 | -71 |
| linen snake | 0.0 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 14.2 (keep 145); best orders clear only 6 a turn after crew: ship stays at 0
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- best towns now: Bedenis +32, Birkeningen +32, Bordetes +29, Calange +28, Bremcop +27
- Bedenis would trade: furniture buy 1 @ 12.3, rope sell 3 @ 82.5, tools buy 5 @ 4.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Caillechâtel | 488 | 0.13 | 0.20 (20/turn) | beer 45 (3.14->5.51), hides 1 (14.38->17.2), leather 1 (19.21->19.57) | grain 26 (2.52->3.14), lead ore 3 (7.72->8.88), cloth 16 (7.4->7.6), flour 2 (13.55->15.2) | +111 |
| Neuborn | 780 | 0.21 | 0.50 (51/turn) | beer 51 (3.14->4.54), arms 3 (26.25->29.26), leather 1 (19.21->25.27), harnesses 1 (52.5->55.1) | stockfish 1 (111.3->126.35), tin ingots 1 (33.81->36.48), candles 1 (76.12->77), tools 5 (4.83->5.25) | +81 |
| Birkeningen | 1006 | 0.33 | 0.20 (20/turn) | garments 20 (20->22.04), acid 1 (112.35->120.65), glass ingots 2 (51.03->55.57), leather 1 (19.21->26.03) | stockfish 1 (112.35->126.35), candles 1 (75.6->77) | +72 |
| Arnsreuth | 921 | 0.28 | 0.30 (31/turn) | beer 41 (3.14->4.45), lead ore 1 (10.13->13.3), axes 1 (15.44->16.34), steel ingots 1 (14.49->16.05) | stockfish 2 (113.4->126.35), candles 1 (69.3->77), cheese 7 (5.78->7.12) | +71 |
| Hanstein | 380 | 0.10 | 0.20 (20/turn) | rope 2 (74->77.9), charcoal 12 (1.81->2.77), steel ingots 1 (14.49->14.72) | stockfish 1 (96.08->126.35), jewellery 2 (63->75.05), grain 26 (2.69->3.14), lead bars 1 (13.12->13.77) | +68 |

**Best:** Caillechâtel at about +111 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 22 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 272 @ 2.2, stop - |  | uses 722.3/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.2 |  |
| pasties | 3 @ 15.3, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.8 turns |
| porterage | 10 @ 1.1, stop - |  | uses 9.8/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 4 @ min 72.0 | makes 2.2, uses 0.0, holds 20 (keeps 0): sells the surplus + 1/turn of the excess |
| timber |  | 8 @ min 6.5 |  |
| tools | 6 @ 6.2, stop 45 |  | uses 5.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 36.0 turns |

## Chain sizing

Mode HOLD, garments sold 17.2/turn (+0.0 exported); plan makes 22.6 garments a turn.
Labour: own 450, everything else 425, chain may buy 350 -> chain allowance 375, chain plan 375 (-2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.08 | 5.09 |
| ret | 3 | 0.90 | 0.91 |
| spin | 4 | 1.86 | 1.86 |
| weave | 3 | 0.90 | 0.88 |
| sew | 2 | 0.57 | 0.55 |

Buffers: flax fibres 52/73, thread 389/215, cloth 6/88
- chain plan needed 493 labour, budget left 375: cut to 375 (sewing capped at 0.55)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
