# v2 shadow report

Turn 14229, 2026-11-23 06:05. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,433, prestige 3,687 (567 free, +1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 68 | 0 | 19 | 0 | 0 | min_holding 58, sell 1, sell @ 3.14 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 20 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 551 | 0 | 13 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.10 x16, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **cured meat**: home ask 30.80 is above our ceiling 29.00 and last turn bought 1 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 56.4 coin per prestige at mansion, vs 67.9 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 108 over real use lately; planning 551, not 657

## Prestige spending, cheapest coin per prestige first

172 turns left: prestige gained now converts 58.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| jousting 3 | arena | 230 | 52.8 | 53.7 | needs a arena (build cost 26,144); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.4 | 56.4 |  |
| jousting 2 | arena | 210 | 57.8 | 58.8 | needs a arena (build cost 26,144); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.9 | 59.9 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 64.3 | 64.3 | thin at home: wine, pies |
| hold banquet 4 (pies) | mansion | 18 | 65.1 | 65.1 | thin at home: hop beer, wine, stockfish |
| hold banquet 5 | mansion | 22 | 65.8 | 65.8 | thin at home: hop beer, wine, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 66.6 | 66.6 | thin at home: hop beer, wine, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 67.9 | 67.9 | running |
| hold banquet 4 | mansion | 17.5 | 68.1 | 68.1 | thin at home: wine, hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 68.8 | 68.8 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0 | - | cured meat 5 | -148 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Bedenis +30, Clairlond +27, Friedwerp +22, Magdeach +22, Donaunieder +22
- Bedenis would trade: cured meat buy 6 @ 28.4, pasties buy 6 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (84/turn) | beer 84 (3.21->7.12), firewood 37 (1.97->8.46), timber 29 (7.98->10.92), thread 56 (5.9->7.03) | bricks 10 (6.88->10.07), cloth 6 (6.88->10.2), tools 17 (6.04->6.27), dyed yarn 1 (5.15->5.56) | +751 |
| Rouhomme | 368 | 0.10 | 1.00 (105/turn) | firewood 33 (1.97->7.03), garments 7 (28->29.83), cheese 7 (6.67->7.5), nets 4 (38.4->39.33) | bricks 18 (5.08->10.07), tools 13 (4.73->6.27), cookware 8 (23.94->25.65), flax fibres 7 (6.3->7.7) | +186 |
| Clairas | 374 | 0.10 | 0.90 (94/turn) | firewood 27 (1.97->6.65), garments 10 (28->30.4), nets 4 (38.4->40.28), cheese 6 (6.67->7.41) | thread 36 (5.02->6.25), cloth 24 (8.51->10.2), flax fibres 19 (6.62->7.7), tools 17 (5.62->6.27) | +184 |
| Hofkirchen | 991 | 0.33 | 0.80 (84/turn) | beer 84 (3.21->4.69), nails 14 (7.51->10.83), nets 6 (38.4->43.89), yarn 7 (5.83->6.84) | tools 17 (5.35->6.27), dyed cloth 7 (14.38->15.77), garments 2 (26.25->28.2), lathes 2 (212.1->216.6) | +173 |
| Heilegg | 826 | 0.24 | 0.60 (63/turn) | beer 84 (3.21->4.89), nets 6 (38.4->44.46), tools 17 (7.04->7.6), tiles 4 (3.46->7.03) | cloth 12 (9.24->10.2), hop beer 4 (11.87->14.44), garments 2 (25.41->28.2), thread 18 (5.88->6.25) | +171 |

**Best:** Grandgues at about +751 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 1 @ 2.9, stop 3 | 1 @ min 3.38 | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had None) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 11) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 3 @ 2.4, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.0) |
| grain | 1 @ 3.7, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 17) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 51) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 37.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.3k (cash + stock at home prices); -127/turn over 6 turns, +28/turn over 24 turns.
- Limits: cash flow >= -393/turn, prestige >= -1.11/turn (values are after 200 tax a turn).
- Today's settings: value -145/turn, cash -144/turn, prestige +1.37/turn.
- Plan: value +44/turn, cash +51/turn, prestige -1.11/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +93 vs -184, +11 vs -165, -305 vs -162.
- Route sales counted at most (what the ships really sold, a turn): beer 1.5.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Orlesailles: +11/turn
  - ship Flax Wyrm -> Vauxvais: +7/turn
  - mansion 1 1.00 -> 0.41: +168/turn
  - net maker 0.00 -> 0.29: +9/turn
  - spinnery 1 1.65 -> 1.56: +4/turn
  - brewery 1 0.14 -> 0.01: +2/turn
  - flax farm 1 4.64 -> 4.73: -1/turn
  - sewing shop 1 0.30 -> 0.36: -9/turn
  - weavery 1 0.50 -> 0.60: +15/turn
- Model check over the last 59 turns: predicted -156/turn for the settings we ran, real +61/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.65, thread 4.14, cloth 6.62, flax fibres 4.91, garments 19.15, nets 30.54, beer 2.84, timber 3.40, prestige 67.89, cash 0.00
- Orders it would set: beer buy 1 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 11); firewood buy 3 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 1 (v2 17); labour buy 64 (v2 51); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Orlesailles (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+7/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1865 coin: +3/turn, payback 583 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 86/77, thread 1059/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1059 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
