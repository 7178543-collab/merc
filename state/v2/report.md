# v2 shadow report

Turn 13457, 2026-10-22 02:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,783, prestige 3,578 (908 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 147 | 0 | 4 | 0 | 0 | min_holding 60, sell 55, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 40 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 276 | 274 | 724 | 2 | 0 | buy 276, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.8 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 1, next step uses 42/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 176
- **pasties**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 87 over real use lately; planning 726, not 801

## Prestige spending, cheapest coin per prestige first

944 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.9 | 49.9 | thin at home: pasties, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 51.7 | 51.7 | thin at home: pasties, pies |
| hold banquet 2 (pies) | mansion | 7 | 52.2 | 52.2 | thin at home: pasties, wine, pies |
| hold banquet 4 | mansion | 17.5 | 53.5 | 53.5 | thin at home: wine, ham |
| hold sermon 2 (candles) | church | 31 | 51.3 | 53.7 | needs a church (build cost 64,876); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 51.7 | 54.8 | needs a church (build cost 64,876); thin at home: jewellery, furniture |
| hold prayer 2 | chapel | 13 | 52.3 | 55.2 | needs a chapel (build cost 33,612); thin at home: furniture |
| hold feast 2 | townhouse | 2.6 | 52.2 | 55.3 | needs a townhouse (build cost 7,394); thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 55.6 | 55.6 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 55.8 | 55.8 | thin at home: wine |
| jousting 1 | arena | 170 | 55.7 | 55.8 | needs a arena (build cost 26,336); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.2 / 0.20 | 19 | 185801747 | 0.368 | garments 9 | furniture 22 | -260 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: garments sell 10 @ 22.4, pasties buy 2 @ 14.4; crew 0.1; est +19 a turn; stock: pasties 2 @ 14.4 (keep 14)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.1 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +419, Grandgues +409, Heilegg +382, Bordetes +379, Clairlond +376
- Hofkirchen would trade: furniture buy 35 @ 13.0; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Chribruck | 1202 | 0.43 | 0.10 (10/turn) | plate armour 1 (1044.75->1425), tapestries 1 (635.25->646), leather 1 (24.15->26.98), pies 1 (11.03->14.25) | spinning wheels 1 (214.2->231.8), jewellery 1 (58.28->68.4), tar 2 (10.13->11.4), pasties 1 (14.07->15.39) | +418 |
| Bedenis | 566 | 0.15 | 0.10 (10/turn) | plate armour 1 (1044.75->1254), tapestries 1 (635.25->693.5), pies 1 (11.03->13.39), scythes 1 (20.37->20.71) | slaked lime 4 (6.83->10.54), coats 1 (53.55->60.32), candles 1 (72.45->77), canvas 1 (24.36->27.55) | +295 |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | plate armour 1 (1044.75->1178), scythes 1 (20.37->24.7), wine 5 (5.46->6.65), pies 1 (11.03->15.01) | candles 1 (71.4->77), pasties 2 (13.55->15.39), tar 3 (10.24->11.4) | +157 |
| Darmwald | 1022 | 0.33 | 0.20 (20/turn) | gold ore 1 (175.35->285), nets 3 (37.8->43.13), pies 1 (11.03->15.67), scythes 1 (20.37->23.56) | candles 1 (70.35->77), cloth 31 (7.67->8.2), pasties 1 (9.19->15.39), canvas 1 (23.73->27.55) | +155 |
| Birkeningen | 1006 | 0.33 | 0.20 (20/turn) | lathes 1 (111.3->176.7), scythes 1 (20.37->24.51), flax plants 3 (1.45->2.75), pies 1 (11.03->13.11) | cheese 20 (4.41->6.98), candles 1 (73.5->77), chisels 1 (11.45->14.44), pasties 2 (13.55->15.39) | +124 |

**Best:** Chribruck at about +418 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 55 @ min 3.38 | makes 56.0, uses 4.2, holds 147 (keeps 60): sells the surplus + 3/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 10 @ min 20.0 | sell; ships offer 10 a turn abroad, so home sells 10 (was 20) |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 276 @ 2.2, stop - |  | uses 726.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 276 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.8 |  |
| pasties | 4 @ ?, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 11 = 4.1 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.3/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 79.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 53.7 turns |

## Chain sizing

Mode HOLD, garments sold 19.8/turn (+0.0 exported); plan makes 22.6 garments a turn.
Labour: own 450, everything else 403, chain may buy 350 -> chain allowance 397, chain plan 398 (+7 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.54 | 5.63 |
| ret | 3 | 0.98 | 1.00 |
| spin | 4 | 2.03 | 2.06 |
| weave | 3 | 0.86 | 0.87 |
| sew | 2 | 0.53 | 0.55 |

Buffers: flax fibres 46/73, thread 265/214, cloth 1/87
- chain plan needed 532 labour, budget left 397: cut to 397 (sewing capped at 0.55)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R3: net maker152202386007001 (net maker) finished but idle 2 turns (no recipe) (held back: failsafe level 1: reduce-only, would start make nets 1 at 0.5 (storehouse provider))
