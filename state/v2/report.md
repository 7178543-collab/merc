# v2 shadow report

Turn 13445, 2026-10-21 14:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,494, prestige 3,594 (924 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 92 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 46 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 272 | 264 | 714 | 0 | 0 | buy 272, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.8 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 42/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 1.0 turns (holds 87, next step uses 87/turn) -> v2: check the step that makes it

## Tuning

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
| hold sermon 2 (candles) | church | 31 | 51.3 | 53.6 | needs a church (build cost 61,953); thin at home: candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 54.7 | 54.7 | thin at home: wine, pies |
| hold sermon 2 | church | 24 | 52.7 | 55.6 | needs a church (build cost 61,953); thin at home: furniture |
| hold prayer 2 | chapel | 13 | 53.1 | 55.8 | needs a chapel (build cost 31,702); thin at home: furniture |
| jousting 1 | arena | 170 | 56.6 | 56.8 | needs a arena (build cost 25,474); thin at home: protection, light armour, arms; needs weaponry skill |
| jousting 3 | arena | 230 | 56.8 | 56.9 | needs a arena (build cost 25,474); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 54.3 | 57.2 | needs a townhouse (build cost 7,100); thin at home: wine |
| hold mass 1 | cathedral | 180 | 55.8 | 57.3 | needs a cathedral (build cost 227,730); thin at home: jewellery, glassware, candles |
| hold banquet 4 | mansion | 17.5 | 57.8 | 57.8 | thin at home: wine, hop beer, ham |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only 8 a turn after crew: ship stays at 0
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn; best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Clairlond +39, Bedenis +32, Essenbrucke +25, Grandgues +25, Boistot +23
- Clairlond would trade: candles buy 1 @ 72.5, garments sell 16 @ 22.4, pasties buy 2 @ 11.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clairas | 374 | 0.10 | 0.30 (30/turn) | grindstones 1 (308.7->457.9), yarn 4 (4.64->6.08), coats 2 (57.75->59.38), ham 1 (67.2->68.4) | beer 82 (3.13->3.86), candles 1 (73.5->84.5), pasties 2 (11.55->15.3), grain 26 (2.6->2.96) | +229 |
| Magdeach | 667 | 0.18 | 0.50 (50/turn) | pies 1 (13.55->27.74), rope 1 (74->85.97), scythes 1 (20.37->25.84), wrought iron 3 (13.44->15.01) | beer 113 (3.13->3.86), cheese 17 (7.19->8.31), candles 1 (74.03->84.5), gears 1 (53.03->62.7) | +122 |
| Unterhufe | 595 | 0.16 | 0.50 (50/turn) | tackles 1 (160.65->195.7), scythes 1 (20.37->22.8), tallow 1 (17.32->19.76), pies 2 (13.55->14.44) | beer 113 (3.15->3.86), candles 1 (73.5->84.5), lead ore 2 (6.67->11.4), cheese 10 (7.51->8.31) | +109 |
| Großmühle | 751 | 0.20 | 0.10 (10/turn) | nets 1 (37.8->41.04), scythes 1 (20.37->23.56), pickaxes 1 (8.72->9.97), pies 2 (13.55->14.54) | bellows 2 (212.1->237.5), cheese 12 (6.41->8.31), candles 1 (74.55->84.5), pasties 1 (9.55->15.3) | +97 |
| Rotterburg | 1056 | 0.35 | 0.20 (20/turn) | looms 1 (520.8->570), nets 5 (37.8->40.66), dye 1 (39.27->49.4), belts 1 (24.15->26.79) | candles 1 (74.03->84.5), pasties 2 (11.45->15.3), lead ore 3 (9.24->11.4) | +92 |

**Best:** Clairas at about +229 coin a turn.

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

Mode HOLD, garments sold 20.2/turn (+0.0 exported); plan makes 21.3 garments a turn.
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
