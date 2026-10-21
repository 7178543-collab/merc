# v2 shadow report

Turn 13432, 2026-10-21 01:10. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,525, prestige 3,516 (846 free, +125.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 51 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.2 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 3, next step uses 46/turn) -> v2: check the step that makes it

## Tuning

- **candles**: home ask 71.50 is above our ceiling 70.00 and last turn bought 4 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 63
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 162
- **timber**: build materials for park 1, net maker152202386007001 are in (271.3 held, 71 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 79% (EXPANSION), about 3 turns left; still to deliver: labour 55, limestone 13, timber 9; ready for labour
- **net maker152202386007001** 59% (INITIAL), about 5 turns left; still to deliver: labour 82, timber 62, tools 9; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 13 | 60.7 | 0 | off: covered |
| timber | 71 | 271.3 | 0 | off: covered; switch v1's buy off |
| tools | 9 | 199.2 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 36

## Notes

- labour: projection runs 96 over real use lately; planning 714, not 806

## Prestige spending, cheapest coin per prestige first

969 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 54.4 | 54.4 | thin at home: hop beer, pies |
| hold sermon 2 (candles) | church | 31 | 52.2 | 54.8 | needs a church (build cost 71,073); thin at home: jewellery, furniture |
| maintain 1 | park | 0.5 | 51.0 | 55.0 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.5 | 55.5 |  |
| hold prayer 2 | chapel | 13 | 52.8 | 55.7 | needs a chapel (build cost 33,598); thin at home: furniture |
| hold sermon 2 | church | 24 | 52.6 | 56.0 | needs a church (build cost 71,073); thin at home: jewellery, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 56.3 | 56.3 | thin at home: hop beer, cured fish |
| hold banquet 4 (pies) | mansion | 18 | 57.0 | 57.0 | thin at home: hop beer, wine |
| jousting 3 | arena | 230 | 58.2 | 58.4 | needs a arena (build cost 26,749); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 1 | cathedral | 180 | 56.6 | 58.5 | needs a cathedral (build cost 284,900); thin at home: jewellery, glassware, candles |
| hold banquet 2 (pies) | mansion | 7 | 59.6 | 59.6 | thin at home: wine, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 59.9 | 59.9 | thin at home: wine, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: candles buy 4 @ 73.5, furniture buy 4 @ 13.7; crew 0.1; est +106 a turn; stock: candles 4 @ 73.5 (keep 12); stock: furniture 4 @ 13.7 (keep 145)
- **Flax Wyrm** on Rouhomme: candles buy 4 @ 75.0, furniture buy 4 @ 14.2, tools buy 3 @ 4.48; crew 0.1; est +99 a turn; stock: candles 4 @ 75.0 (keep 12); stock: furniture 4 @ 14.2 (keep 145)
- best towns now: Corstoft +150, Brunnham +134, Gosschweig +132, Karlmoor +130, Disscester +129
- Corstoft would trade: candles buy 4 @ 59.0, furniture buy 4 @ 14.6; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Caillechâtel | 488 | 0.14 | 0.20 (21/turn) | beer 26 (3.18->6.22), blades 1 (13.65->14.06), dyed cloth 1 (8.98->9.26) | butter 2 (53.03->60.8), hinges 2 (32.76->37.05), tapestries 1 (582.75->589), flax fibres 13 (5.78->6.4) | +120 |
| Karlmoor | 787 | 0.22 | 0.10 (10/turn) | garments 22 (19.8->23.18), rope 2 (73.5->86.92), dyed cloth 1 (8.98->10.83), resin 1 (2.21->2.87) | hinges 2 (31.5->37.05), acid 1 (114.45->115.9), nails 6 (5.3->5.65), wax 1 (19.21->20.33) | +110 |
| Chatgnan | 728 | 0.20 | 0.30 (31/turn) | beer 51 (3.18->4.05), rope 3 (73.5->76), glass ingots 2 (45.78->48.92), nets 2 (38.4->40.85) | tapestries 1 (561.75->589), ploughs 2 (64.05->71.25), wine 8 (5.41->6.37), harnesses 1 (45.15->50.82) | +95 |
| Bedenis | 566 | 0.16 | 0.20 (21/turn) | rope 4 (73.5->80.75), dye 1 (40.95->52.25), axes 1 (13.86->15.39), dyed cloth 1 (8.98->10.16) | tapestries 1 (540.75->589), canvas 2 (27.51->29.64), flax fibres 7 (5.57->6.4), lead ore 1 (6.77->10.16) | +93 |
| Hofkirchen | 991 | 0.33 | 0.40 (42/turn) | nets 5 (38.4->43.7), seeds 8 (1.78->4.27), dye 1 (40.95->49.88), hides 2 (10.71->12.35) | cheese 24 (6.3->7.79), flax fibres 15 (5.12->6.4), cured meat 13 (22.26->23.18), beer 4 (2.62->3.5) | +93 |

**Best:** Caillechâtel at about +120 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| candles | 3 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 2 = 1.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 21 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 264 @ 2.2, stop - |  | uses 714.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.4 |  |
| pasties | 3 @ 15.3, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.8 turns |
| porterage | 10 @ 1.1, stop - |  | uses 9.8/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 4 @ min 71.5 | makes 2.2, uses 0.0, holds 29 (keeps 0): sells the surplus + 2/turn of the excess |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 29 |  | uses 3.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 56.1 turns |

## Chain sizing

Mode HOLD, garments sold 22.0/turn (+0.0 exported); plan makes 21.7 garments a turn.
Labour: own 450, everything else 424, chain may buy 350 -> chain allowance 376, chain plan 376 (-3 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.08 | 5.24 |
| ret | 3 | 0.90 | 0.93 |
| spin | 4 | 1.86 | 1.92 |
| weave | 3 | 0.90 | 0.85 |
| sew | 2 | 0.57 | 0.53 |

Buffers: flax fibres 51/72, thread 336/212, cloth 3/85
- chain plan needed 512 labour, budget left 376: cut to 376 (sewing capped at 0.53)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
