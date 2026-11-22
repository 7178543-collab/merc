# v2 shadow report

Turn 14209, 2026-11-22 10:35. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,396, prestige 3,690 (570 free, -3.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 86 | 0 | 4 | 0 | 0 | min_holding 58, sell 18, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 19 | 8 | 9 | 0 | 0 | stop 31, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 531 | 0 | 33 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), but the home ask 31.80 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 4 (need 12) -> v2: buy 12

## Waste (money lost now)

- **labour**: 33 labour expired last turn (~62 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 31.80 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.6 coin per prestige at mansion, vs 73.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 100 over real use lately; planning 534, not 634
- labour expiry guard: 33 bought labour expired last turn, buy 31 (not 34) this turn

## Prestige spending, cheapest coin per prestige first

192 turns left: prestige gained now converts 61.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.1 | 51.0 | needs a arena (build cost 28,140); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.9 | 55.8 | needs a arena (build cost 28,140); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 56.7 | 56.7 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 57.6 | 57.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 63.6 | 63.6 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 63.7 | 63.7 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 65.5 | 65.5 | thin at home: hop beer, stockfish, premium cheese |
| hold mass 2 (premium) | cathedral | 360 | 54.2 | 66.0 | needs a cathedral (build cost 308,300); thin at home: furniture, jewellery, glassware, premium garments |
| hold banquet 2 (pies) | mansion | 7 | 66.5 | 66.5 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 67.5 | 67.5 |  |
| hold banquet 4 | mansion | 17.5 | 68.5 | 68.5 | thin at home: hop beer, stockfish |
| hold mass 3 | cathedral | 460 | 59.2 | 68.5 | needs a cathedral (build cost 308,300); thin at home: coats, jewellery, glassware, candles, sculptures, furniture, tapestries, books |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0 | beer 19 | pasties 6 | -56 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 17 @ 5.4, pasties buy 7 @ 16.4; crew 0.1; est +32 a turn; stock: pasties 7 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 14.2 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Bordetes +60, Fontaux +48, Grandgues +32, Blanans +25, Clairas +24
- Bordetes would trade: beer sell 17 @ 6.75, pasties buy 4 @ 13.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~119 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (119/turn) | bread 256 (2.67->4.31), firewood 36 (2.14->11.4), timber 22 (9.29->11.78), beer 13 (3.46->5.42) | bricks 6 (7.4->10.64), dyed cloth 5 (14.7->16.81), garments 1 (28.35->31.4), wool 3 (11.87->11.97) | +801 |
| Rouhomme | 368 | 0.12 | 1.00 (119/turn) | bread 303 (2.67->4.14), yarn 12 (5.08->5.89), nets 5 (37.4->39.14), grain 0 (3.22->5.18) | bricks 7 (4.96->10.64), tools 15 (4.73->5.79), cheese 5 (9.92->11.02), garments 1 (30.45->31.4) | +414 |
| Heilegg | 826 | 0.27 | 0.30 (36/turn) | wrought iron 12 (17.01->27.55), nets 6 (37.4->44.65), butter 2 (65.62->83.12), cured fish 10 (23.94->26.98) | cloth 24 (10.5->11.5), dyed cloth 8 (14.7->16.81), thread 32 (6.2->6.95), cheese 6 (8.56->11.02) | +343 |
| Hofkirchen | 991 | 0.38 | 0.50 (60/turn) | yarn 58 (5.08->6.84), nets 6 (37.4->44.27), cured fish 17 (23.94->25.65), butter 2 (65.62->70.77) | lathes 2 (189->209), jewellery 3 (73.5->81.22), cheese 6 (7.35->11.02), cloth 24 (10.5->11.5) | +292 |
| Kirchwerp | 1072 | 0.43 | 0.30 (36/turn) | windows 2 (866.25->902.5), cloth 20 (12.08->14.25), arms 6 (34.02->40.28), varnish 1 (21.21->26.6) | jewellery 3 (73.5->81.22), lathes 1 (189->209), tools 17 (4.41->5.79), garments 2 (24.15->31.4) | +230 |

**Best:** Grandgues at about +801 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 11 @ min 3.38 | makes 19.3, uses 4.2, holds 86 (keeps 58): sells the surplus + 1/turn of the excess; ships offer 17 a turn abroad, so home sells 11 (was 16) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 29.0, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.2) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 31) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 85.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.7k (cash + stock at home prices); +248/turn over 6 turns, +112/turn over 24 turns.
- Limits: cash flow >= -433/turn, prestige >= -1.13/turn (values are after 200 tax a turn).
- Today's settings: value -170/turn, cash -157/turn, prestige +0.63/turn.
- Plan: value -21/turn, cash -9/turn, prestige -1.13/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +355 vs -142, +221 vs -156, +193 vs -163.
- Route sales counted at most (what the ships really sold, a turn): beer 0.3.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +16/turn
  - ship Flax Wyrm -> Calange: +9/turn
  - mansion 1 1.00 -> 0.58: +129/turn
  - spinnery 1 1.65 -> 1.32: +8/turn
  - retting pit 1 0.91 -> 0.83: +0/turn
  - flax farm 1 4.64 -> 4.18: +4/turn
  - net maker 0.00 -> 0.29: -4/turn
  - sewing shop 1 0.30 -> 0.22: -14/turn
  - weavery 1 0.50 -> 0.35: +25/turn
- Model check over the last 59 turns: predicted -137/turn for the settings we ran, real +23/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.89, beer 3.30, timber 3.69, prestige 72.29, cash 0.00
- Orders it would set: bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 4 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 31); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Gosschweig (+16/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Calange (+9/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1979 coin: +3/turn, payback 656 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 426 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.53 |
| ret | 3 | 0.91 | 0.91 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 93/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: bread slot dry: 5.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.54; our bid is already at/over the ask (sellers too thin)
- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 29, home ask 31.8 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 32.4 (ask 31.8, cap 42.0))
- R1: prestige rate -3.57 a turn vs 12-turn median -1.55; likely: dry slot: bread, cured meat; mansion 1 projected 0 (cured meat)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
