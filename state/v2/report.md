# v2 shadow report

Turn 14230, 2026-11-23 07:10. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,607, prestige 3,688 (568 free, +1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 68 | 0 | 19 | 0 | 0 | min_holding 58, sell 1, sell @ 3.38; stop 3, buy 1, buy @ 2.9 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 12, buy 3, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 11 | 9 | 9 | 0 | 0 | stop 2, buy 1, buy @ 3.7 |
| labour | 64 | 64 | 552 | 0 | 12 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**0 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Tuning

- **beer**: floor 3.38 vs home bid 2.88: barely selling (0 of 0)
- **cured meat**: home ask 30.40 is above our ceiling 29.00 and last turn bought 1 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 56.8 coin per prestige at mansion, vs 67.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 108 over real use lately; planning 556, not 664

## Prestige spending, cheapest coin per prestige first

171 turns left: prestige gained now converts 57.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| jousting 3 | arena | 230 | 52.7 | 53.6 | needs a arena (build cost 26,051); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 |  |
| jousting 2 | arena | 210 | 57.7 | 58.7 | needs a arena (build cost 26,051); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.4 | 60.4 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 63.5 | 63.5 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 65.0 | 65.0 | thin at home: hop beer, wine, stockfish |
| hold banquet 5 | mansion | 22 | 65.7 | 65.7 | thin at home: hop beer, wine, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 67.0 | 67.0 | thin at home: hop beer, wine, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 67.5 | 67.5 | running |
| hold banquet 4 | mansion | 17.5 | 68.1 | 68.1 | thin at home: wine, hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 68.6 | 68.6 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 7 @ 14.7; crew 0.1; est +19 a turn; stock: pasties 7 @ 14.7 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.4 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Heidlowe +57, Fontaux +54, Clairlond +34, Großaue +33, Heilegg +32
- Heidlowe would trade: cured meat buy 6 @ 21.0, pasties buy 4 @ 16.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (84/turn) | beer 80 (3.04->7.03), firewood 37 (1.94->7.84), garments 10 (29.8->34.39), timber 28 (7.88->9.88) | bricks 10 (6.83->9.97), lathes 2 (205.8->216.6), tools 17 (6.04->6.46) | +685 |
| Gotthafen | 964 | 0.32 | 0.70 (74/turn) | arms 14 (30.03->40.28), nets 6 (40.4->46.36), beer 80 (3.04->3.8), glass ingots 2 (65.1->67.45) | cloth 9 (7.51->10.1), garments 2 (26.46->30.8), tin ingots 2 (34.23->35.91), thread 4 (5.62->6.35) | +213 |
| Heilegg | 826 | 0.24 | 0.60 (63/turn) | beer 80 (3.04->5.18), tiles 8 (3.46->7.55), nets 4 (40.4->43.7), hides 1 (14.07->15.86) | tools 17 (5.25->6.46), cloth 13 (9.19->10.1), garments 2 (26.46->30.8), thread 20 (5.83->6.35) | +210 |
| Fontaux | 411 | 0.12 | 1.00 (105/turn) | beer 22 (3.04->5.89), firewood 12 (1.94->8.69), timber 8 (7.88->12.92), bread 71 (2.58->3.17) | cured meat 2 (23.31->30.4), thread 21 (5.78->6.35), windows 0 (876.75->888.25), pies 1 (19.43->22.61) | +206 |
| Rouhomme | 368 | 0.10 | 1.00 (105/turn) | firewood 30 (1.94->7.03), garments 7 (29.8->35.34), cheese 7 (6.51->7.5), furniture 13 (15.23->16.15) | bricks 16 (4.6->9.97), tools 12 (4.73->6.46), thread 20 (5.93->6.35), flax fibres 5 (6.3->7.3) | +198 |

**Best:** Grandgues at about +685 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 1 @ min 2.86 | goal planner: trial sale of an idle pile, 1 a turn at 2.86, keeps 58 (10 over) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 14.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.0) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 56) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 39.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.3k (cash + stock at home prices); -29/turn over 6 turns, +26/turn over 24 turns.
- Limits: cash flow >= -400/turn, prestige >= -1.12/turn (values are after 200 tax a turn).
- Today's settings: value -137/turn, cash -139/turn, prestige +1.37/turn.
- Plan: value +49/turn, cash +54/turn, prestige -1.12/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +11 vs -165, -305 vs -162, +174 vs -144.
- Route sales counted at most (what the ships really sold, a turn): beer 1.5.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Heidlowe: +43/turn
  - ship Flax Wyrm -> Vauxvais: +6/turn
  - mansion 1 1.00 -> 0.41: +167/turn
  - net maker 0.00 -> 0.29: +9/turn
  - spinnery 1 1.65 -> 1.55: +4/turn
  - brewery 1 0.14 -> 0.08: +0/turn
  - flax farm 1 4.64 -> 4.71: -0/turn
  - weavery 1 0.50 -> 0.60: -9/turn
  - sewing shop 1 0.30 -> 0.36: +15/turn
- Model check over the last 59 turns: predicted -156/turn for the settings we ran, real +60/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.65, thread 4.15, cloth 6.62, flax fibres 4.92, garments 19.16, nets 30.59, beer 2.88, timber 3.38, prestige 67.47, cash 0.00
- Orders it would set: arms buy 1 (v2 None); beer sell 1 (v2 none); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 18); labour buy 64 (v2 56)
- Ship linen snake: Grandgues -> Heidlowe (+15/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1863 coin: +3/turn, payback 624 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 86/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 9.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 30.4 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 31 (ask 30.4, cap 42.0))
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
