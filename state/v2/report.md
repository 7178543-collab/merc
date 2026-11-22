# v2 shadow report

Turn 14217, 2026-11-22 18:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,271, prestige 3,686 (566 free, +1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 59 | 0 | 19 | 0 | 0 | min_holding 58, sell 10, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 14 | 12 | 7 | 0 | 5 | stop 42, buy 14, buy @ 2.26 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 20 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 547 | 0 | 17 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.70 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 17 labour expired last turn (~29 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 56.5 coin per prestige at mansion, vs 73.8 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.70 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 106 over real use lately; planning 547, not 647

## Prestige spending, cheapest coin per prestige first

184 turns left: prestige gained now converts 60.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.3 | 51.2 | needs a arena (build cost 28,236); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| jousting 2 | arena | 210 | 55.1 | 56.1 | needs a arena (build cost 28,236); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.5 | 56.5 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.5 | 59.5 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 63.0 | 63.0 | thin at home: wine, pies |
| hold banquet 4 (pies) | mansion | 18 | 64.4 | 64.4 | thin at home: wine, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 66.3 | 66.3 | thin at home: wine, stockfish, premium cheese |
| hold mass 2 (premium) | cathedral | 360 | 54.2 | 67.5 | needs a cathedral (build cost 308,160); thin at home: furniture, jewellery, glassware, windows, premium garments |
| hold banquet 4 | mansion | 17.5 | 68.0 | 68.0 | thin at home: wine, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 70.7 | 70.7 |  |
| hold banquet 3 (pies) | mansion | 8 | 71.9 | 71.9 | thin at home: pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.2 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.4 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Donaunieder +68, Briclives +49, Clairas +44, Clairlond +40, Chribruck +38
- Donaunieder would trade: cured meat buy 6 @ 29.2, furniture buy 3 @ 13.5, pasties buy 2 @ 12.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (110/turn) | beer 75 (3.46->7.08), bread 225 (2.52->3.76), firewood 30 (2.46->11.4), timber 32 (8.45->11.69) | bricks 7 (7.93->10.45), cloth 6 (8.56->10), dyed yarn 0 (5.15->5.94), flax plants 3 (1.99->2.39) | +976 |
| Kirchwerp | 1072 | 0.40 | 0.40 (44/turn) | thread 76 (6.15->9.5), glass ingots 1 (63->81.7), nets 6 (37.4->40.28), honey 4 (10.5->13.21) | jewellery 3 (73.5->81.22), tools 17 (4.62->6.17), flax fibres 8 (5.62->7.8), cured meat 6 (31.5->33.6) | +350 |
| Hofkirchen | 991 | 0.35 | 0.80 (88/turn) | beer 83 (3.46->5.32), honey 5 (10.5->15.77), nets 6 (37.4->41.8), thread 30 (6.15->6.98) | jewellery 3 (73.5->81.22), flax fibres 25 (6.41->7.8), tools 17 (5.15->6.17), cured meat 5 (31.5->33.6) | +260 |
| Coburgbaum | 619 | 0.18 | 0.50 (55/turn) | beer 49 (3.46->5.42), charcoal 19 (2.05->5.03), acid 1 (139.65->152), nets 2 (37.4->39.14) | cured meat 6 (31.71->33.6), tools 17 (5.78->6.17), dyed cloth 6 (14.8->15.39), salt 6 (5.08->5.56) | +142 |
| Rouhomme | 368 | 0.11 | 1.00 (110/turn) | bread 112 (2.52->3.48), firewood 20 (2.46->6.17), flour 1 (17.75->25.08), seeds 3 (2.39->3.23) | bricks 10 (4.62->10.45), tools 7 (4.73->6.17), dyed cloth 3 (14.7->15.39), candles 0 (84->85) | +141 |

**Best:** Grandgues at about +976 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 37.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.46, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.0) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 47) |
| light armour | 1 @ 112, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 32.1k (cash + stock at home prices); -44/turn over 6 turns, +63/turn over 24 turns.
- Limits: cash flow >= -428/turn, prestige >= -1.11/turn (values are after 200 tax a turn).
- Today's settings: value -192/turn, cash -192/turn, prestige +1.38/turn.
- Plan: value +7/turn, cash +9/turn, prestige -1.11/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -100 vs -186, -310 vs -171, -254 vs -177.
- Route sales counted at most (what the ships really sold, a turn): beer 1.2.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +3/turn
  - ship Flax Wyrm -> Donaunieder: +14/turn
  - mansion 1 1.00 -> 0.41: +184/turn
  - net maker 0.00 -> 0.29: +4/turn
  - flax farm 1 4.64 -> 4.99: -1/turn
  - retting pit 1 0.91 -> 0.99: +5/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +15/turn
  - ropewalk 1 0.25 -> 0.00: -16/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.35: +18/turn
- Model check over the last 59 turns: predicted -145/turn for the settings we ran, real +107/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.72, thread 4.32, cloth 6.90, flax fibres 5.12, garments 19.97, nets 31.78, beer 3.08, timber 4.23, prestige 73.34, cash 0.00
- Orders it would set: bread buy 5 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 47); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.35, worth +11/turn.
- Ship linen snake: Grandgues -> Angefont (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +86/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1957 coin: +5/turn, payback 402 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 86/77, thread 1057/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1057 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.7 for 3 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
