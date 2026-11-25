# v2 shadow report

Turn 14272, 2026-11-25 01:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,862, prestige 3,722 (602 free, +1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 35 | 0 | 19 | 0 | 0 | sell 3, sell @ 3.5; stop 116, buy 39, buy @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 35, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 560 | 0 | 4 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 114 over real use lately; planning 560, not 652

## Prestige spending, cheapest coin per prestige first

129 turns left: prestige gained now converts 47.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.3 | 51.1 | needs a arena (build cost 30,248); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.0 | 54.9 | needs a arena (build cost 30,248); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 58.4 | 58.4 |  |
| maintain 1 | park | 0.5 | 58.5 | 58.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 61.1 | 61.1 |  |
| hold banquet 2 (pies) | mansion | 7 | 61.2 | 61.2 |  |
| jousting 3 | arena | 230 | 59.6 | 61.2 | needs a arena (build cost 30,248); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 63.6 | 63.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 65.5 | 65.5 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 66.7 | 66.7 | thin at home: hop beer, stockfish, sculptures |
| jousting 2 | arena | 210 | 65.3 | 67.0 | needs a arena (build cost 30,248); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 68.1 | 68.1 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 13.9 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.5 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Orlesailles +48, Darmwald +41, Heidlowe +41, Heilegg +40, Donaunieder +36
- Orlesailles would trade: cured meat buy 6 @ 24.6, pasties buy 4 @ 9.15; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~128 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.46 | 0.30 (38/turn) | glass ingots 4 (70.88->114), garments 10 (29.8->38), canvas 5 (42.63->47.5), leather 4 (27.93->32.3) | cured meat 6 (24.99->28.2), butter 1 (80.85->84.08), tin ingots 1 (34.86->35.91) | +312 |
| Vauxvais | 204 | 0.07 | 0.10 (13/turn) | swords 1 (226.8->332.5), limestone 1 (19.84->34.39), honey 3 (11.23->15.01), flour 2 (19.64->23.75) | cloth 26 (9.92->14.25), tools 16 (5.46->6.46), butter 1 (70.88->84.08), bricks 5 (4.85->7.74) | +295 |
| Dortgart | 1045 | 0.44 | 0.20 (26/turn) | dyed cloth 11 (18.27->22.8), garments 10 (29.8->33.63), glass ingots 1 (70.88->83.12), nets 3 (34.6->38) | cloth 14 (9.92->14.25), silver bars 1 (254.1->294.5), cured meat 6 (24.15->28.2), butter 1 (77.7->84.08) | +219 |
| Rotterburg | 1056 | 0.45 | 0.20 (26/turn) | garments 10 (29.8->30.59), nets 3 (34.6->35.53) | cloth 26 (7.25->14.25), butter 1 (61.43->84.08), cured meat 5 (23.94->28.2), tin ingots 4 (33.6->35.91) | +218 |
| Heilegg | 826 | 0.29 | 0.40 (51/turn) | dyed cloth 11 (18.27->22.8), nets 6 (34.6->42.56), garments 10 (29.8->31.73), arms 7 (32.97->35.72) | cloth 26 (13.02->14.25), cured meat 6 (24.36->28.2) | +206 |

**Best:** Kirchwerp at about +312 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 3 @ min 3.88 | makes 19.3, uses 19.2, holds 35 (keeps 0): sells the surplus + 3/turn of the excess |
| bread | 5 @ 2.72, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 92.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.96 | goal planner: sells 2 a turn at 0.96, keeps 219 (no one offered it) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 60) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.2k (cash + stock at home prices); -36/turn over 6 turns, -40/turn over 24 turns.
- Limits: cash flow >= -286/turn, prestige >= -1.26/turn (values are after 200 tax a turn).
- Today's settings: value -195/turn, cash -196/turn, prestige +1.19/turn.
- Plan: value -1/turn, cash +4/turn, prestige -1.26/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +56 vs -175, +82 vs -191, -103 vs -181.
- Route sales counted at most (what the ships really sold, a turn): beer 2.3, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +28/turn
  - ship Flax Wyrm -> Rouhomme: +5/turn
  - mansion 1 1.00 -> 0.42: +170/turn
  - net maker 0.00 -> 0.28: +7/turn
  - flax farm 1 4.64 -> 4.03: +1/turn
  - spinnery 1 1.65 -> 1.34: -1/turn
  - retting pit 1 0.91 -> 0.81: +10/turn
  - sewing shop 1 0.30 -> 0.25: -2/turn
  - weavery 1 0.50 -> 0.40: +7/turn
- Model check over the last 59 turns: predicted -146/turn for the settings we ran, real -51/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.80, thread 4.57, cloth 7.27, flax fibres 5.48, garments 21.00, nets 33.18, beer 3.36, timber 3.58, prestige 67.29, cash 0.00
- Orders it would set: bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 60)
- Ship linen snake: Grandgues -> Donaunieder (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Rouhomme (+7/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1964 coin: +1/turn, payback 3222 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 85/77, thread 1058/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 34.6 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 39 @ 3.7, home ask 4.04 (held back: acted on beer at turn 14271 (one action per 2 turns))
- R1: cured meat slot dry: 6.5 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 28.2; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1058 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
