# v2 shadow report

Turn 13450, 2026-10-21 19:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,098, prestige 3,587 (917 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 179 | 0 | 4 | 0 | 0 | min_holding 60, sell 59, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 42 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.8 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 42/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 1.0 turns (holds 87, next step uses 87/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68
- **timber**: build materials for net maker152202386007001 are in (350.6 held, 25 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **net maker152202386007001** 84% (INITIAL), about 2 turns left; still to deliver: labour 33, timber 25, tools 4; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 25 | 350.6 | 0 | off: covered; switch v1's buy off |
| tools | 4 | 199.3 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 17

## Notes

- labour: projection runs 87 over real use lately; planning 714, not 801

## Prestige spending, cheapest coin per prestige first

951 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.8 | 50.8 |  |
| hold banquet 3 (pies) | mansion | 8 | 51.2 | 51.2 | thin at home: pies |
| hold banquet 2 (pies) | mansion | 7 | 53.1 | 53.1 | thin at home: pies |
| hold sermon 2 (candles) | church | 31 | 51.9 | 54.4 | needs a church (build cost 64,527); thin at home: candles, furniture |
| hold banquet 4 | mansion | 17.5 | 54.9 | 54.9 | thin at home: ham, stockfish |
| hold sermon 2 | church | 24 | 52.5 | 55.6 | needs a church (build cost 64,527); thin at home: furniture |
| hold prayer 2 | chapel | 13 | 53.0 | 55.7 | needs a chapel (build cost 31,204); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 57.4 | 57.4 | thin at home: cured fish |
| jousting 3 | arena | 230 | 57.3 | 57.4 | needs a arena (build cost 24,974); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 1 | cathedral | 180 | 55.9 | 57.6 | needs a cathedral (build cost 252,230); thin at home: jewellery, glassware, candles |
| jousting 1 | arena | 170 | 58.8 | 58.9 | needs a arena (build cost 24,974); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.3 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: furniture buy 34 @ 14.2; crew 0.2; est +395 a turn; stock: furniture 34 @ 14.2 (keep 145)
- **linen snake** on Neuborn: furniture buy 27 @ 13.7; crew 0.3; est +313 a turn; stock: furniture 27 @ 13.7 (keep 145)
- best towns now: Cobholme +479, Grandgues +454, Hofkirchen +415, Bordetes +405, Rouhomme +395
- Cobholme would trade: beer sell 60 @ 5.35, furniture buy 36 @ 13.2; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Dortdorf | 871 | 0.25 | 0.10 (10/turn) | looms 1 (457.8->541.5), plate armour 1 (1044.75->1111.5), dye 1 (41.37->46.36), pies 2 (11.65->14.34) | candles 1 (71.4->85), copper ore 1 (19.21->22.23), hinges 1 (30.24->30.97), pasties 2 (13.02->14) | +179 |
| Cobholme | 1564 | 0.62 | 0.90 (89/turn) | beer 60 (3.24->5.51), bellows 1 (302.4->336.3), malt 2 (6.83->13.59), ham 1 (60.9->69.83) | candles 1 (73.5->85), copper ore 2 (16.8->22.23), gears 1 (50.61->52.72), canvas 1 (27.51->28.88) | +131 |
| Clairas | 374 | 0.10 | 0.10 (10/turn) | looms 1 (457.8->541.5), spirits 1 (10.61->16.81), slaked lime 2 (7.46->9.5), dyed yarn 1 (6.88->7.6) | spinning wheels 1 (208.95->220.4), candles 1 (75.08->85), canvas 1 (26.04->28.88), pasties 2 (12.08->14) | +117 |
| Bordetes | 831 | 0.23 | 0.20 (20/turn) | medicine 1 (128.1->184.3), limestone 1 (20.58->52.25), dye 1 (41.37->52.25), spirits 1 (10.61->19.95) | candles 1 (75.6->85), canvas 1 (26.04->28.88), butter 1 (56.18->57.95), hop beer 1 (6.88->8.12) | +113 |
| Darmwald | 1022 | 0.33 | 0.20 (20/turn) | looms 1 (457.8->517.75), ploughs 1 (72.45->99.75), spirits 1 (10.61->17.48), pies 2 (11.65->14.25) | pasties 2 (10.24->14), candles 1 (79.8->85), cloth 11 (7.67->8.4), canvas 1 (28.14->28.88) | +108 |

**Best:** Dortdorf at about +179 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 57 @ min 3.38 | makes 56.0, uses 4.2, holds 179 (keeps 60): sells the surplus + 6/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 264 @ 2.2, stop - |  | uses 714.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.4 |  |
| pasties | 3 @ 14.7, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.2/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 73.0 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 54.0 turns |

## Chain sizing

Mode HOLD, garments sold 20.0/turn (+0.0 exported); plan makes 20.9 garments a turn.
Labour: own 450, everything else 420, chain may buy 350 -> chain allowance 380, chain plan 380 (-3 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.45 | 5.46 |
| ret | 3 | 0.97 | 0.97 |
| spin | 4 | 2.00 | 2.00 |
| weave | 3 | 0.83 | 0.82 |
| sew | 2 | 0.53 | 0.51 |

Buffers: flax fibres 48/71, thread 263/209, cloth 0/82
- chain plan needed 531 labour, budget left 380: cut to 380 (sewing capped at 0.51)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
