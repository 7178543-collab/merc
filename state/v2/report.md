# v2 shadow report

Turn 14216, 2026-11-22 17:39. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,525, prestige 3,684 (564 free, +1.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 58 | 0 | 19 | 0 | 0 | min_holding 58, sell 10, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 12 | 3 | 3 | 0 | 0 | stop 42, buy 14, buy @ 2.26 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 20 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 564 | 5 | 0 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**0 risks, 0 waste, 5 tuning** where v2 would act differently from v1.

## Tuning

- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 60.2 coin per prestige at mansion, vs 77.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 62.6 coin per prestige at mansion, vs 77.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (pies)**: hold banquet 2 (pies) costs 64.5 coin per prestige at mansion, vs 77.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 106 over real use lately; planning 569, not 651

## Prestige spending, cheapest coin per prestige first

185 turns left: prestige gained now converts 60.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.7 | 50.2 | needs a arena (build cost 27,419); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| jousting 3 | arena | 230 | 51.2 | 52.0 | needs a arena (build cost 27,419); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.5 | 54.0 | needs a arena (build cost 27,419); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 56.0 | 57.0 | needs a arena (build cost 27,419); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 60.2 | 60.2 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 62.6 | 62.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 63.2 | 63.2 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 63.9 | 63.9 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 2 (pies) | mansion | 7 | 64.5 | 64.5 |  |
| hold banquet 4 (premium) | mansion | 20 | 65.0 | 65.0 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 67.2 | 67.2 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | - | cured meat 5, pasties 4 | -220 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.4 (keep 14); best orders clear only 8 a turn after crew: ship stays at 0
- best towns now: Blanans +66, Donaunieder +57, Clairas +50, Dortgart +48, Briclives +48
- Blanans would trade: cured meat buy 6 @ 31.2, furniture buy 3 @ 11.9, pasties buy 1 @ 11.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (110/turn) | bread 245 (2.54->4.2), firewood 30 (2.01->11.4), beer 74 (4.24->6.74), timber 32 (8.51->12.16) | bricks 9 (7.93->10.45), tools 11 (5.99->6.93), cured meat 5 (33.81->35.2), canvas 0 (54.6->61.27) | +1015 |
| Hofkirchen | 991 | 0.35 | 0.80 (88/turn) | beer 82 (4.24->5.22), nets 6 (37.4->41.99), honey 5 (10.5->14.63), wine 8 (6.56->7.65) | flax fibres 27 (5.62->8.95), tools 17 (5.15->6.93), cured meat 5 (31.5->35.2), jewellery 2 (73.5->81.22) | +249 |
| Kirchwerp | 1072 | 0.40 | 0.30 (33/turn) | glassware 4 (79.8->89.77), nets 6 (37.4->40.47), leather 1 (27.51->32.3), lead ore 2 (6.14->8.98) | tools 17 (4.41->6.93), flax fibres 11 (5.62->8.95), cured meat 6 (31.29->35.2), jewellery 2 (73.5->81.22) | +183 |
| Heidlowe | 662 | 0.19 | 0.30 (33/turn) | nets 6 (37.4->41.23), wine 7 (6.56->8.17), fleece 3 (7.35->7.84), lead ore 3 (6.14->7.36) | flax fibres 19 (6.46->8.95), cured meat 6 (31.08->35.2), thread 40 (6.04->6.75), tools 17 (5.62->6.93) | +162 |
| Rouhomme | 368 | 0.11 | 1.00 (110/turn) | bread 122 (2.54->3.53), firewood 20 (2.01->6.03), flour 1 (20.06->25.84), seeds 3 (2.46->3.27) | bricks 8 (5.02->10.45), tools 7 (4.73->6.93), canvas 0 (53.55->61.27), dyed cloth 4 (14.7->15.39) | +159 |

**Best:** Grandgues at about +1015 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 37.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.48, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 13 = 2.2 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.4) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 9) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 69) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 85.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 32.9k (cash + stock at home prices); +132/turn over 6 turns, +111/turn over 24 turns.
- Limits: cash flow >= -439/turn, prestige >= -1.10/turn (values are after 200 tax a turn).
- Today's settings: value -181/turn, cash -177/turn, prestige +1.09/turn.
- Plan: value +15/turn, cash -37/turn, prestige -1.10/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -44 vs -176, -100 vs -186, -310 vs -171.
- Route sales counted at most (what the ships really sold, a turn): beer 1.2.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gottweiler: +22/turn
  - ship Flax Wyrm -> Vauxvais: +5/turn
  - mansion 1 1.00 -> 0.48: +167/turn
  - net maker 0.00 -> 0.29: +4/turn
  - flax farm 1 4.64 -> 7.26: +2/turn
  - retting pit 1 0.91 -> 1.00: +13/turn
  - weavery 1 0.50 -> 0.61: -9/turn
  - sewing shop 1 0.30 -> 0.36: +14/turn
  - ropewalk 1 0.25 -> 0.00: -17/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.35: +19/turn
- Model check over the last 59 turns: predicted -144/turn for the settings we ran, real +34/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.72, thread 4.32, cloth 6.90, flax fibres 5.12, garments 19.97, nets 31.76, beer 3.05, timber 3.65, prestige 74.09, cash 0.00
- Orders it would set: bread buy 5 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); garments sell 11 (v2 10); labour buy 64 (v2 69); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.35, worth +12/turn.
- Ship linen snake: Grandgues -> Gottweiler (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +86/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1905 coin: +5/turn, payback 363 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 83/77, thread 1059/228, cloth 73/128

## Self-diagnosis

- R1: fish slot dry: 12.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy 14 @ 2.26, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1059 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: cured meat buy not filling: bid 33.6 under the home ask 35.2 for 3 turns, bought 6.0 of 12, 13.0 held (2.2 turns); raise needs Taylor (ceiling 29.0)
