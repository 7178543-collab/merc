# v2 shadow report

Turn 13417, 2026-10-20 10:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,267, prestige 3,409 (739 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 131 | 0 | 4 | 0 | 0 | min_holding 60, sell 28, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 149 | 0 | 2 | 0 | 0 | min_holding 30, sell 30, sell @ 20 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 0 | 6 | 440 | 0 | 16 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36 |
| porterage | 8 | 37 | 8 | 0 | 29 | buy 8, buy @ 1.1 |

**0 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Tuning

- **cloth**: cloth buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 7

## Notes

- labour: projection runs 75 over real use lately; planning 440, not 514

## Prestige spending, cheapest coin per prestige first

984 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 2 (pies) | mansion | 7 | 53.9 | 53.9 | thin at home: pasties, wine, cheese, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 54.1 | 54.1 | thin at home: wine, cured fish, cheese |
| hold sermon 2 (candles) | church | 31 | 51.9 | 54.4 | needs a church (build cost 68,008); thin at home: candles, furniture |
| hold banquet 3 (pies) | mansion | 8 | 54.5 | 54.5 | thin at home: pasties, cheese, pies |
| hold prayer 2 | chapel | 13 | 52.3 | 54.8 | needs a chapel (build cost 30,786); thin at home: furniture |
| hold feast 2 | townhouse | 2.6 | 52.3 | 55.0 | needs a townhouse (build cost 6,660); thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 55.2 | 55.2 |  |
| hold sermon 2 | church | 24 | 52.2 | 55.3 | needs a church (build cost 68,008); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 56.0 | 56.0 | thin at home: cured fish, cheese |
| hold banquet 4 (pies) | mansion | 18 | 56.5 | 56.5 | thin at home: pasties, wine, cheese |
| jousting 1 | arena | 170 | 56.3 | 56.5 | needs a arena (build cost 24,854); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.032 | - | furniture 1 | -14 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.032 | - | furniture 2 | -27 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Pontmont +28, Brunnham +24, Fulkirch +21, Essenbrucke +20, Hanstein +19
- Pontmont would trade: rope sell 3 @ 81.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kleinburgh | 1440 | 0.55 | 0.20 (20/turn) | rope 2 (68->76.95), tools 16 (4.26->5.84), varnish 2 (17.64->19.38), lead bars 1 (13.97->14.72) | bellows 1 (228.9->281.2), candles 1 (72.45->80.5), flax fibres 2 (4.64->5.85) | +91 |
| Arnsreuth | 921 | 0.28 | 0.30 (30/turn) | beer 29 (2.81->4.6), rope 2 (68->73.62), tools 16 (4.26->4.66), wine 4 (5.46->6.17) | bellows 1 (254.1->281.2), cheese 3 (6.09->6.93), glassware 1 (56.7->57) | +79 |
| Fontaux | 411 | 0.11 | 0.40 (40/turn) | beer 29 (2.81->3.97), timber 15 (6.2->8.55), tools 15 (4.26->4.64), butter 1 (90.83->93.57) | cheese 14 (5.72->6.93), tackles 1 (176.4->190), candles 1 (74.55->80.5) | +78 |
| Hofkirchen | 991 | 0.31 | 0.10 (10/turn) | lead bars 10 (13.97->16.53), rope 3 (68->71.72), potash 2 (17.32->18.05), varnish 1 (17.64->18.34) | medicine 2 (120.75->127.3), candles 1 (71.4->80.5), acid 1 (132.3->140.6), cheese 17 (6.14->6.93) | +69 |
| Rouhomme | 368 | 0.10 | 0.10 (10/turn) | beer 29 (2.81->3.55), firewood 1 (1.6->5.56), tar 1 (10.82->12.25), wine 4 (5.46->5.65) | bellows 1 (254.1->281.2), cheese 14 (6.51->6.93), lead bars 14 (12.08->12.54), glassware 1 (52.5->57) | +62 |

**Best:** Kleinburgh at about +91 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 28 @ min 3.42 | makes 28.0, uses 4.2, holds 131 (keeps 60): sells the surplus + 4/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 30 @ min 20.0 | makes 1.8, uses 2.1, holds 149 (keeps 30): sells the surplus + 30/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 440.3/turn (brewery 1, flax farm 1, household), makes 450.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.0 |  |
| pasties | 3 @ 14.2, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.8 turns |
| porterage | 8 @ 1.1, stop - |  | uses 7.5/turn (observed), makes 0.0, holds 8 = 1.1 turns |
| rope |  | 3 @ min 66.0 |  |
| timber |  | 15 @ min 6.5 | makes 8.4, uses 0.0, holds 432 (keeps 350): sells the surplus + 6/turn of the excess |
| tools | 3 @ 6.2, stop 24 |  | uses 2.9/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 68.4 turns |

## Chain sizing

Mode HOLD, garments sold 0.4/turn (+0.0 exported); plan makes 0.8 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 135 (-7 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.92 | 2.89 |
| ret | 3 | 0.52 | 0.51 |
| spin | 4 | 1.12 | 1.10 |
| weave | 3 | 0.04 | 0.02 |
| sew | 2 | 0.04 | 0.02 |

Buffers: flax fibres 53/44, thread 242/130, cloth 7/3

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 2 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
