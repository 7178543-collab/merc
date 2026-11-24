# v2 shadow report

Turn 14249, 2026-11-24 02:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,406, prestige 3,695 (575 free, +1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 21 | 0 | 19 | 0 | 0 | stop 116, buy 39, buy @ 3.82 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 12 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 7 | 7 | 7 | 2 | 0 | stop 25, buy 7, buy @ 3.7 |
| labour | 65 | 64 | 564 | 6 | 0 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **grain**: brewery 1 ran short of grain (buy is live (7 @ 3.7), 7 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.8 turns of grain left and buying 7 (need 18) -> v2: buy 18

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **cured meat**: home ask 30.40 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 56.9 coin per prestige at mansion, vs 71.1 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 110 over real use lately; planning 570, not 653

## Prestige spending, cheapest coin per prestige first

152 turns left: prestige gained now converts 53.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 47.2 | 48.3 | needs a arena (build cost 26,661); thin at home: swords, protection, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| jousting 2 | arena | 210 | 51.7 | 52.9 | needs a arena (build cost 26,661); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 56.9 | 56.9 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 57.2 | 57.2 | thin at home: beer |
| hold banquet 2 (pies) | mansion | 7 | 60.8 | 60.8 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 63.7 | 63.7 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 64.9 | 64.9 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 66.5 | 66.5 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 67.3 | 67.3 | thin at home: hop beer, stockfish |
| jousting 1 | arena | 170 | 65.9 | 67.4 | needs a arena (build cost 26,661); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 67.8 | 67.8 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0 | - | cured meat 2, pasties 6 | -137 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | beer 2 | cured meat 6 | -135 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 1 @ 5.7, cured meat buy 6 @ 25.0; crew 0.1; est +24 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.5 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Darmwald +49, Rotterburg +44, Donaunieder +41, Hofkirchen +38, Gotthafen +33
- Darmwald would trade: cured meat buy 6 @ 21.4, pasties buy 2 @ 16.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Marmont | 638 | 0.18 | 0.30 (32/turn) | garments 10 (26.4->27.93), tallow 1 (26.88->31.92), malt 2 (7.88->10.45), cloth 15 (9.97->10.26) | sculptures 1 (2205->2660), cured meat 3 (21.42->30.4), flax fibres 6 (5.88->6.55), bricks 5 (6.2->9.88) | +502 |
| Rouhomme | 368 | 0.10 | 1.00 (106/turn) | garments 10 (26.4->37.05), grain 145 (2.94->3.69), yarn 13 (6.51->8.22), cloth 12 (9.97->11.49) | bricks 22 (5.21->9.88), cured meat 4 (26.88->30.4), thread 30 (5.57->6.1), tools 32 (6.09->6.6) | +354 |
| Pontmont | 341 | 0.10 | 0.80 (85/turn) | timber 41 (7.98->13.87), tiles 5 (3.19->7.22), nails 9 (8.35->9.5), tackles 1 (154.35->163.4) | bricks 13 (5.88->9.88), tools 32 (5.78->6.6), thread 28 (5.57->6.1), cured meat 6 (28.98->30.4) | +314 |
| Kirchwerp | 1072 | 0.38 | 0.50 (53/turn) | glassware 5 (81.38->100.7), canvas 6 (42->57), casks 11 (6.51->9.36), wine 16 (6.41->7.84) | cheese 17 (5.1->6.6), nails 5 (5.62->6.7), garments 2 (25.2->26.8), hop beer 1 (13.55->14.44) | +276 |
| Grandgues | 152 | 0.04 | 0.50 (53/turn) | garments 10 (26.4->36.67), bread 176 (2.52->3), nets 3 (37->41.61), wine 9 (6.41->8.03) | cured meat 6 (25.83->30.4), bricks 8 (7.3->9.88), tools 9 (5->6.6), casks 3 (5.02->5.84) | +271 |

**Best:** Marmont at about +502 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 39 @ ?, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 21 = 1.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 9 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 19 = 3.2 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 7 @ 3.7, stop 25 |  | goal planner: buys 7 a turn for today's rates, keeps up to 25 (v2 had 18) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 70) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.1k (cash + stock at home prices); -62/turn over 6 turns, -9/turn over 24 turns.
- Limits: cash flow >= -350/turn, prestige >= -1.15/turn (values are after 200 tax a turn).
- Today's settings: value -140/turn, cash -141/turn, prestige +1.33/turn.
- Plan: value +32/turn, cash +36/turn, prestige -1.15/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +40 vs -117, -369 vs -132, -243 vs -120.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Darmwald: +16/turn
  - ship Flax Wyrm -> Grandgues: +3/turn
  - mansion 1 1.00 -> 0.41: +150/turn
  - net maker [make nets 2] 0.00 -> 0.33: +5/turn
  - spinnery 1 1.65 -> 1.57: +3/turn
  - flax farm 1 4.64 -> 4.55: +0/turn
  - sewing shop 1 0.30 -> 0.36: -8/turn
  - weavery 1 0.50 -> 0.60: +10/turn
- Model check over the last 59 turns: predicted -155/turn for the settings we ran, real +18/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.71, thread 4.30, cloth 6.86, flax fibres 5.09, garments 19.85, nets 32.16, beer 3.01, timber 3.26, prestige 62.44, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 6); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 7 (v2 18); labour buy 65 (v2 70); light armour buy 1 (v2 None)
- Recipe: net maker make nets 3 -> make nets 2 at 0.33, worth +2/turn.
- Ship linen snake: Grandgues -> Darmwald (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+5/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +86/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 86/77, thread 1062/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 21.4 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 39 @ 3.82, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1062 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
