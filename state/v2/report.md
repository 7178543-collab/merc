# v2 shadow report

Turn 13481, 2026-10-23 02:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,105, prestige 3,619 (499 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 110 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 108 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 212 | 212 | 677 | 0 | 35 | buy 187, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 2 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.6 turns (holds 18, next step uses 32/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 35 labour expired last turn (~57 coin): holding 212 against a ~0 buffer target -> v2: trim the buy until the stock is near 0
- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 180

## Notes

- labour: projection runs 75 over real use lately; planning 702, not 777
- labour expiry guard: 35 bought labour expired last turn, buy 177 (not 202) this turn

## Prestige spending, cheapest coin per prestige first

920 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 3 (pies) | mansion | 8 | 48.6 | 48.6 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 49.4 | 49.4 | thin at home: hop beer, wine |
| hold banquet 3 (fish) | mansion | 7.6 | 51.2 | 51.2 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 51.2 | 51.2 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 52.5 | 52.5 | thin at home: wine, hop beer, ham |
| jousting 3 | arena | 230 | 52.6 | 52.7 | needs a arena (build cost 24,711); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 51.2 | 53.7 | needs a church (build cost 64,666); thin at home: candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 54.5 | 54.5 |  |
| hold prayer 2 | chapel | 13 | 51.7 | 54.5 | needs a chapel (build cost 31,432); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 54.7 | 54.7 | thin at home: wine, pies |
| hold banquet 1 (meat) | mansion | 4.2 | 55.1 | 55.1 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.23 | 0.50 (50/turn) | grindstones 1 (237.3->347.7), furniture 12 (11.87->13.68), beer 55 (3.18->3.78), lead ore 1 (8.82->18.24) | - | +140 |
| Neuborn | 780 | 0.21 | 1.00 (101/turn) | bread 128 (2.25->3.4), furniture 10 (11.87->15.29), grain 7 (2.58->3.38), lead ore 0 (8.82->11.4) | cheese 9 (4.94->5.65) | +106 |
| Hofkirchen | 991 | 0.32 | 0.60 (60/turn) | acid 1 (158.55->193.8), glass ingots 2 (55.12->68.4), beer 55 (3.18->4.26), grindstones 1 (237.3->248.9) | blades 2 (11.97->12.63), garments 2 (19.32->19.9) | +87 |
| Essenbrucke | 584 | 0.16 | 0.10 (10/turn) | rope 2 (78->84.08), copper ore 1 (19.32->22.04), ham 1 (60.38->62.7), lead ore 1 (8.82->11.3) | spinning wheels 1 (171.15->222.3), pasties 2 (11.34->12.4), resin 1 (1.04->1.86), wine 2 (5.78->6.65) | +73 |
| Clarfranche | 1484 | 0.59 | 0.30 (30/turn) | harnesses 1 (77.7->97.85), grindstones 1 (237.3->267.9), ham 1 (60.38->69.83), lead ore 3 (8.82->14.06) | chisels 2 (7.46->13.59), wine 12 (5.67->6.65) | +64 |

**Best:** Heilegg at about +140 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 30 @ min 20.0 | makes 16.4, uses 2.1, holds 108 (keeps 30): sells the surplus + 16/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 177 @ 2.2, stop - |  | uses 701.7/turn (brewery 1, flax farm 1, household), makes 500.0, holds 212 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 13.0, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.4/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 76.0 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.2 turns |

## Goal: business value (shadow)
- Value now 15.7k (cash + stock at home prices); +44/turn over 6 turns, -100/turn over 24 turns.
- Limits: cash flow >= +79/turn, prestige >= -0.83/turn (after 236 tax and crew).
- Today's settings: value +35/turn, cash +25/turn, prestige -1.50/turn - breaks the prestige floor and cash floor.
- Plan: value +98/turn, cash +283/turn, prestige -0.83/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.50 -> 1.00: +23/turn
  - logging camp w/ tool 7.00 -> 2.92: +12/turn
  - ropewalk 1 0.50 -> 0.44: +6/turn
  - quarry 1 0.00 -> 0.08: +4/turn
  - sewing shop 1 0.40 -> 0.13: -12/turn
  - weavery 1 0.67 -> 0.21: +17/turn
  - spinnery 1 2.05 -> 1.58: +30/turn
  - retting pit 1 1.00 -> 0.77: +3/turn
  - flax farm 1 5.61 -> 4.32: +14/turn
  - mansion 1 0.00 -> 0.16: -36/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.61, thread 3.97, cloth 6.39, flax fibres 4.58, garments 18.55, nets 34.60, beer 2.83, timber 5.33, prestige 52.65, cash 0.00
- Orders it would set (dry run): beer sell 54 (v2 52); labour buy 174 (v2 177); porterage buy 11 (v2 10)
- Investments:
  - Tenants L13 for 500 prestige: +80/turn (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.7/turn (+0.0 exported); plan makes 22.6 garments a turn.
Labour: own 500, everything else 415, chain may buy 350 -> chain allowance 435, chain plan 435 (+76 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.61 | 6.44 |
| ret | 3 | 1.00 | 1.14 |
| spin | 4 | 2.05 | 2.36 |
| weave | 3 | 0.67 | 0.89 |
| sew | 2 | 0.40 | 0.55 |

Buffers: flax fibres 46/80, thread 225/236, cloth 18/89
- chain plan needed 497 labour, budget left 435: cut to 435 (sewing capped at 0.55)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
