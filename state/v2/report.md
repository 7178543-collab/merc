# v2 shadow report

Turn 13445, 2026-10-21 14:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,494, prestige 3,594 (924 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 92 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 46 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 272 | 264 | 714 | 0 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.8 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 42/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 1.0 turns (holds 87, next step uses 87/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68
- **timber**: build materials for net maker152202386007001 are in (350.6 held, 50 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **net maker152202386007001** 67% (INITIAL), about 4 turns left; still to deliver: labour 66, timber 50, tools 7; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 50 | 350.6 | 0 | off: covered; switch v1's buy off |
| tools | 7 | 199.3 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 17

## Notes

- labour: projection runs 92 over real use lately; planning 714, not 801

## Prestige spending, cheapest coin per prestige first

956 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 3 (pies) | mansion | 8 | 52.9 | 52.9 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 53.4 | 53.4 | thin at home: hop beer, wine |
| hold sermon 2 (candles) | church | 31 | 51.3 | 53.6 | needs a church (build cost 61,393); thin at home: candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 54.7 | 54.7 | thin at home: wine, pies |
| hold sermon 2 | church | 24 | 52.7 | 55.6 | needs a church (build cost 61,393); thin at home: furniture |
| hold prayer 2 | chapel | 13 | 53.1 | 55.9 | needs a chapel (build cost 31,702); thin at home: furniture |
| jousting 1 | arena | 170 | 56.6 | 56.8 | needs a arena (build cost 25,278); thin at home: protection, light armour, arms; needs weaponry skill |
| jousting 3 | arena | 230 | 56.8 | 56.9 | needs a arena (build cost 25,278); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 54.3 | 57.2 | needs a townhouse (build cost 7,100); thin at home: wine |
| hold mass 1 | cathedral | 180 | 55.8 | 57.3 | needs a cathedral (build cost 226,330); thin at home: jewellery, glassware, candles |
| hold banquet 4 | mansion | 17.5 | 57.8 | 57.8 | thin at home: wine, hop beer, ham |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only 10 a turn after crew: ship stays at 0
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn; best orders clear only -0 a turn after crew: ship stays at 0
- best towns now: Clairlond +34, Caillechâtel +32, Chatgnan +23, Boistot +22, Angefont +18
- Clairlond would trade: candles buy 1 @ 73.5, garments sell 16 @ 22.4, pasties buy 2 @ 12.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clairas | 374 | 0.10 | 0.10 (10/turn) | grindstones 1 (306.6->536.75), medicine 1 (105->130.15), ham 1 (65.62->67.45), spirits 1 (18.48->19.19) | gears 3 (61.43->66.5), pasties 2 (11.65->15.1), candles 1 (78.75->83.5), steel ingots 1 (10.24->11.69) | +284 |
| Rotterburg | 1056 | 0.35 | 0.20 (20/turn) | windows 1 (432.6->546.25), nets 4 (37.8->40.66), dye 1 (38.43->45.03), coats 2 (57.75->60.32) | sails 1 (609->712.5), candles 1 (73.5->83.5), pasties 2 (11.13->15.1), gears 1 (60.9->66.5) | +260 |
| Dortgart | 1045 | 0.35 | 0.10 (10/turn) | herbs 1 (30.24->46.55), dye 1 (38.43->46.17), wine 4 (5.72->6.89), belts 1 (23.52->26.6) | sails 1 (567->712.5), gold bars 1 (798->817), gears 1 (57.23->66.5), canvas 2 (24.36->29.07) | +210 |
| Kleinburgh | 1440 | 0.56 | 0.30 (30/turn) | malt 2 (5.25->13.39), looms 1 (510.3->522.5), rope 2 (75->77.9), nets 4 (37.8->39.71) | sails 1 (561.75->712.5), gears 3 (57.23->66.5), candles 1 (74.03->83.5) | +209 |
| Brunnham | 1281 | 0.47 | 0.20 (20/turn) | lathes 1 (145.95->167.2), dye 1 (38.43->45.6), tiles 2 (3.78->11.4), coats 2 (57.75->59.85) | sails 1 (556.5->712.5), candles 1 (71.4->83.5), pasties 2 (12.18->15.1), garments 2 (19.95->20.6) | +204 |

**Best:** Clairas at about +284 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.8 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 264 @ 2.2, stop - |  | uses 714.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 272 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.8 |  |
| pasties | 3 @ 15.8, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.2/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 4 @ min 73.0 | makes 2.2, uses 0.0, holds 18 (keeps 0): sells the surplus + 1/turn of the excess |
| timber |  | 8 @ min 6.85 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 54.0 turns |

## Chain sizing

Mode HOLD, garments sold 20.0/turn (+0.0 exported); plan makes 21.3 garments a turn.
Labour: own 450, everything else 420, chain may buy 350 -> chain allowance 380, chain plan 382 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.45 | 5.43 |
| ret | 3 | 0.97 | 0.97 |
| spin | 4 | 2.00 | 1.99 |
| weave | 3 | 0.83 | 0.83 |
| sew | 2 | 0.53 | 0.52 |

Buffers: flax fibres 49/71, thread 273/210, cloth 0/83
- chain plan needed 529 labour, budget left 380: cut to 380 (sewing capped at 0.52)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
