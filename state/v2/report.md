# v2 shadow report

Turn 14240, 2026-11-23 17:21. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,464, prestige 3,683 (563 free, +1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 62 | 0 | 19 | 0 | 0 | min_holding 58, sell 1, sell @ 3.16 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 9 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 18 | 6 | 6 | 3 | 0 | stop 36, buy 18, buy @ 3.7 |
| labour | 64 | 65 | 563 | 0 | 2 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **grain**: brewery 1 ran short of grain (buy is live (18 @ 3.7), 6 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **labour**: buying 64, short of ~71 needed -> v2: buy 71

## Tuning

- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 54.8 coin per prestige at mansion, vs 65.0 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 98 over real use lately; planning 571, not 669

## Prestige spending, cheapest coin per prestige first

161 turns left: prestige gained now converts 55.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 47.8 | 48.8 | needs a arena (build cost 25,857); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 3 (premium) | arena | 420 | 49.2 | 49.7 | needs a arena (build cost 25,857); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| jousting 2 | arena | 210 | 52.4 | 53.4 | needs a arena (build cost 25,857); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 52.8 | 53.4 | needs a arena (build cost 25,857); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 54.8 | 54.8 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 57.7 | 57.7 |  |
| hold banquet 2 (pies) | mansion | 7 | 61.7 | 61.7 |  |
| hold banquet 4 (pies) | mansion | 18 | 63.1 | 63.1 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 64.2 | 64.2 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 1 (meat) | mansion | 4.2 | 65.0 | 65.0 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 65.5 | 65.5 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | - | cured meat 6, pasties 1 | -138 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 22.2, pasties buy 1 @ 16.4; crew 0.1; est +28 a turn; stock: pasties 1 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 13.3 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Gottweiler +34, Grandgues +28, Kirchwerp +17
- Gottweiler would trade: cured meat buy 6 @ 21.4, pasties buy 1 @ 14.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (83/turn) | firewood 37 (2.18->5.22), charcoal 19 (2.35->4.46), timber 27 (7.56->8.93), glassware 2 (77.7->81.7) | cured meat 6 (22.89->28), bricks 13 (7.04->9.88), thread 22 (5.35->6.1), wool 10 (11.23->11.88) | +212 |
| Brebronn | 862 | 0.26 | 0.60 (63/turn) | tiles 3 (3.38->12.06), flour 1 (16.8->23.56), candles 1 (85.58->86.45), glass ingots 1 (66.67->67.92) | flax plants 72 (0.47->1.93), thread 45 (4.56->6.1), windows 1 (714->745.75), wool 10 (9.55->11.88) | +206 |
| Hofkirchen | 991 | 0.33 | 1.00 (104/turn) | ploughs 6 (80.85->91.2), arms 10 (29.19->32.68), seeds 7 (2.14->6.08), beer 81 (3.28->4.07) | jewellery 2 (74.03->91.2), lathes 1 (202.65->218.5), thread 62 (5.67->6.1), tools 19 (5.04->5.56) | +194 |
| Hanstein | 380 | 0.11 | 1.00 (104/turn) | timber 29 (7.56->11.88), charcoal 14 (2.35->5.27), firewood 12 (2.18->6.65), flour 1 (16.8->18.9) | thread 15 (4.75->6.1), wool 7 (10.08->11.88), cured meat 2 (23.94->28), flax fibres 6 (6.46->7.9) | +186 |
| Pontmont | 341 | 0.10 | 0.90 (94/turn) | timber 39 (7.56->10.92), beer 81 (3.28->3.84), nails 9 (7.67->9.5), wrought iron 3 (18.9->21.47) | thread 27 (5.57->6.1), bricks 11 (7.04->9.88), wool 10 (10.82->11.88), flax fibres 1 (5.78->7.9) | +176 |

**Best:** Grandgues at about +212 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 27 @ 3.26, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 62 = 3.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 7 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 22 = 3.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 6 @ 3.7, stop 22 |  | goal planner: buys 6 a turn for today's rates, keeps up to 22 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 71) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 41.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 83.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.6k (cash + stock at home prices); +58/turn over 6 turns, -50/turn over 24 turns.
- Limits: cash flow >= -394/turn, prestige >= -1.10/turn (values are after 200 tax a turn).
- Today's settings: value -113/turn, cash -113/turn, prestige +1.39/turn.
- Plan: value +49/turn, cash +56/turn, prestige -1.10/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -368 vs -114, -100 vs -123, -52 vs -116.
- Route sales counted at most (what the ships really sold, a turn): beer 2.0, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Kleinburgh: -15/turn
  - ship Flax Wyrm -> Gottweiler: +29/turn
  - mansion 1 1.00 -> 0.41: +134/turn
  - brewery 1 0.14 -> 0.08: +10/turn
  - net maker 0.00 -> 0.20: +7/turn
  - spinnery 1 1.65 -> 1.52: +4/turn
  - flax farm 1 4.64 -> 4.50: -1/turn
  - sewing shop 1 0.30 -> 0.36: -6/turn
  - weavery 1 0.50 -> 0.60: +11/turn
- Model check over the last 58 turns: predicted -157/turn for the settings we ran, real +58/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.66, flax fibres 4.95, garments 19.27, nets 33.60, beer 2.99, timber 3.24, prestige 57.76, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 7); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 18); labour buy 64 (v2 71); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Kleinburgh (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Gottweiler (+12/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 85/77, thread 1050/228, cloth 72/128

## Self-diagnosis

Nothing found this run.
