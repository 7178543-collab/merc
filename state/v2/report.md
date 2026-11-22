# v2 shadow report

Turn 14207, 2026-11-22 08:24. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,982, prestige 3,697 (577 free, -3.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 111 | 0 | 4 | 0 | 0 | min_holding 58, sell 18, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 21 | 8 | 9 | 0 | 0 | stop 29, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 529 | 0 | 35 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 5 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), but the home ask 33.20 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 4 (need 12) -> v2: buy 12

## Waste (money lost now)

- **labour**: 35 labour expired last turn (~67 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.70 is above our ceiling 2.60 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **cured meat**: home ask 33.20 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 59.4 coin per prestige at mansion, vs 75.9 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 529, not 627
- labour expiry guard: 35 bought labour expired last turn, buy 29 (not 29) this turn

## Prestige spending, cheapest coin per prestige first

194 turns left: prestige gained now converts 62.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.8 | 51.6 | needs a arena (build cost 28,080); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 55.6 | 56.5 | needs a arena (build cost 28,080); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 57.6 | 57.6 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 59.4 | 59.4 |  |
| hold banquet 4 (pies) | mansion | 18 | 63.8 | 63.8 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 53.8 | 64.8 | needs a cathedral (build cost 297,140); thin at home: furniture, jewellery, glassware, windows, premium garments |
| hold banquet 4 (premium) | mansion | 20 | 65.6 | 65.6 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 2 (pies) | mansion | 7 | 67.0 | 67.0 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 68.4 | 68.4 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 68.7 | 68.7 | thin at home: wine, hop beer, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 69.1 | 69.1 | thin at home: wine |
| jousting 1 | arena | 170 | 71.0 | 72.1 | needs a arena (build cost 28,080); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.7 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 12 a turn after crew: ship stays at 0
- best towns now: Bordetes +55, Heidlowe +43, Blanans +37, Clairas +36, Hofkirchen +36
- Bordetes would trade: beer sell 19 @ 6.25, pasties buy 4 @ 13.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~121 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (121/turn) | bread 266 (2.84->4.52), firewood 31 (2.18->11.4), timber 25 (9.29->11.78), beer 17 (3.48->5.03) | bricks 7 (8.03->9.79), garments 1 (28.35->31), cloth 4 (11.03->11.7), cured meat 1 (29.19->30.78) | +818 |
| Rouhomme | 368 | 0.12 | 0.90 (109/turn) | bread 293 (2.84->4.5), nets 6 (36.4->39.33), rope 1 (88->91.2), seeds 4 (3->3.42) | bricks 11 (5.02->9.79), tools 17 (4.73->6.27), cloth 12 (10.92->11.7) | +462 |
| Amsdermund | 1111 | 0.46 | 0.70 (85/turn) | acid 1 (113.4->142.5), furniture 10 (14.6->19), nets 5 (36.4->39.71), varnish 1 (21->24.51) | cloth 24 (10.5->11.7), cured meat 2 (21->30.78), cheese 6 (7.93->11.02), lathes 1 (189->209) | +217 |
| Hanstein | 380 | 0.12 | 0.40 (49/turn) | acid 1 (113.4->139.65), nets 6 (36.4->40.66), charcoal 17 (2.16->4.5), furniture 6 (14.6->17.67) | thread 21 (5.78->6.85), canvas 1 (42.21->53.2), cloth 13 (10.71->11.7), cheese 6 (9.5->11.02) | +173 |
| Brunnham | 1281 | 0.57 | 0.60 (73/turn) | nets 6 (36.4->47.12), cured fish 13 (24.57->27.36), acid 1 (113.4->119.7), rope 1 (88->94.05) | lathes 2 (189->209), cloth 24 (10.08->11.7), thread 43 (5.93->6.85), canvas 3 (51.03->53.2) | +165 |

**Best:** Grandgues at about +818 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 18 @ min 3.38 | makes 19.3, uses 4.2, holds 111 (keeps 58): sells the surplus + 3/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 3) |
| candles | 2 @ 82, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 29.0, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 2 @ 14.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.6) |
| grain | 8 @ 3.7, stop 29 |  | goal planner: buys 8 a turn for today's rates, keeps up to 29 (v2 had 17) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 29) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 85.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.0k (cash + stock at home prices); +60/turn over 6 turns, +89/turn over 24 turns.
- Limits: cash flow >= -416/turn, prestige >= -1.15/turn (values are after 200 tax a turn).
- Today's settings: value -177/turn, cash -156/turn, prestige +0.64/turn.
- Plan: value -22/turn, cash -3/turn, prestige -1.15/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +121 vs -170, +207 vs -150, +355 vs -142.
- Route sales counted at most (what the ships really sold, a turn): beer 0.3.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Chatgnan: +6/turn
  - ship Flax Wyrm -> Blanans: +0/turn
  - mansion 1 1.00 -> 0.57: +135/turn
  - spinnery 1 1.65 -> 1.33: +7/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - flax farm 1 4.64 -> 4.21: +4/turn
  - net maker 0.00 -> 0.29: -4/turn
  - sewing shop 1 0.30 -> 0.23: -12/turn
  - weavery 1 0.50 -> 0.36: +23/turn
- Model check over the last 59 turns: predicted -136/turn for the settings we ran, real +37/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.91, beer 3.31, timber 3.69, prestige 74.33, cash 0.00
- Orders it would set: bread buy 5 (v2 3); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 4 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 17); labour buy 64 (v2 29); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Chatgnan (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1987 coin: +4/turn, payback 492 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 424 (+136 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.46 |
| ret | 3 | 0.91 | 0.89 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 98/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 0.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.7 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 2.76 (ask 2.7, cap 4.3))
- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 29, home ask 33.2 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 33.8 (ask 33.2, cap 42.0))
- R1: prestige rate -3.56 a turn vs 12-turn median +0.44; likely: dry slot: bread, cured meat; mansion 1 projected 0 (cured meat)
- R5: tar buy not filling: bid 11 under the home ask 11.4 for 6 turns, bought 0.0 of 1, 0.2 held (0.8 turns); raise needs Taylor (ceiling 11.0)
