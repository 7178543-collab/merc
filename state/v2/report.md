# v2 shadow report

Turn 13441, 2026-10-21 10:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,267, prestige 3,600 (930 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 48 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.4 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 1, next step uses 42/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 65
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 167
- **timber**: build materials for net maker152202386007001 are in (346.4 held, 54 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **net maker152202386007001** 64% (INITIAL), about 5 turns left; still to deliver: labour 72, timber 54, tools 8; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 54 | 346.4 | 0 | off: covered; switch v1's buy off |
| tools | 8 | 199.7 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 15

## Notes

- labour: projection runs 92 over real use lately; planning 714, not 806

## Prestige spending, cheapest coin per prestige first

960 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 3 (pies) | mansion | 8 | 52.7 | 52.7 | thin at home: hop beer, pies |
| hold sermon 2 (candles) | church | 31 | 51.3 | 53.7 | needs a church (build cost 64,748); thin at home: candles, furniture |
| hold banquet 4 (pies) | mansion | 18 | 54.6 | 54.6 | thin at home: hop beer, wine, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 55.7 | 55.7 |  |
| hold sermon 2 | church | 24 | 53.0 | 56.1 | needs a church (build cost 64,748); thin at home: furniture |
| hold prayer 2 | chapel | 13 | 53.5 | 56.3 | needs a chapel (build cost 32,900); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 57.8 | 57.8 | thin at home: wine, pies |
| hold mass 1 | cathedral | 180 | 56.3 | 57.9 | needs a cathedral (build cost 238,080); thin at home: jewellery, glassware, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 58.4 | 58.4 | thin at home: hop beer, cured fish |
| jousting 3 | arena | 230 | 58.3 | 58.4 | needs a arena (build cost 26,582); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 59.2 | 59.2 | thin at home: wine, hop beer, ham |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.092 | - | furniture 4 | -57 |
| linen snake | 0.1 / 0.10 | 10 | 185801747 | 0.08 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn
- best towns now: Etallaen +58, Bedenis +19, Fulkirch +18, Calange +18, Brunnham +16
- Etallaen would trade: garments sell 17 @ 23.8, rope sell 2 @ 83.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.21 | 0.30 (31/turn) | garments 21 (20.6->26.6), beer 51 (3.14->4.8), silver bars 1 (170.1->228), rope 2 (74->80.75) | glass ingots 1 (43.47->52.25), axes 5 (15.96->16.25) | +265 |
| Chribruck | 1202 | 0.44 | 0.10 (10/turn) | silver bars 1 (170.1->368.6), dye 1 (42->47.97), dyed cloth 1 (12.92->13.87), dyed yarn 1 (7.09->8.41) | cheese 12 (8.19->8.98), lead ore 2 (8.14->11.02) | +212 |
| Gottweiler | 1135 | 0.41 | 0.20 (21/turn) | silver bars 1 (170.1->294.5), coats 1 (58.8->68.4), nets 7 (37.8->39.71), lead bars 6 (17.85->19.19) | cheese 19 (6.77->8.98), dyed cloth 3 (9.87->10.54), fleece 1 (5.67->6.27), garments 2 (20.16->20.8) | +193 |
| Fulkirch | 1576 | 0.65 | 0.40 (41/turn) | silver bars 1 (170.1->285), rope 5 (74->78.85), coats 2 (58.8->65.08), dye 1 (42->47.97) | cheese 32 (7.56->8.98), garments 2 (19.32->20.8), lead ore 4 (7.72->11.02) | +177 |
| Kirchwerp | 1072 | 0.37 | 0.20 (21/turn) | gold ore 1 (122.85->143.45), lathes 1 (159.6->179.55), medicine 1 (107.1->115.9), wine 6 (7.09->8.55) | cheese 32 (6.25->8.98), garments 2 (20.16->20.8), gears 1 (61.95->63.65), slaked lime 1 (8.4->10.92) | +151 |

**Best:** Etallaen at about +265 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 264 @ 2.2, stop - |  | uses 714.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.8 |  |
| pasties | 3 @ 15.2, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.0/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 5 @ min 72.0 | makes 2.2, uses 0.0, holds 33 (keeps 0): sells the surplus + 3/turn of the excess |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 29 |  | uses 3.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 55.3 turns |

## Chain sizing

Mode HOLD, garments sold 20.7/turn (+0.0 exported); plan makes 21.7 garments a turn.
Labour: own 450, everything else 418, chain may buy 350 -> chain allowance 382, chain plan 383 (+7 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.24 | 5.41 |
| ret | 3 | 0.93 | 0.96 |
| spin | 4 | 1.92 | 1.98 |
| weave | 3 | 0.85 | 0.84 |
| sew | 2 | 0.53 | 0.53 |

Buffers: flax fibres 50/72, thread 289/211, cloth 1/84
- chain plan needed 529 labour, budget left 382: cut to 382 (sewing capped at 0.53)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
