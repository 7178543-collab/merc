# v2 shadow report

Turn 14231, 2026-11-23 08:16. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,758, prestige 3,690 (570 free, +1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 67 | 0 | 19 | 0 | 0 | min_holding 58, sell 1, sell @ 2.86 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 3 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 8 | 0 | 9 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 564 | 5 | 0 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **grain**: only 0.9 turns of grain left and buying 6 (need 18) -> v2: buy 18

## Tuning

- **cured meat**: home ask 30.40 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.8 coin per prestige at mansion, vs 68.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 112 over real use lately; planning 569, not 636

## Prestige spending, cheapest coin per prestige first

170 turns left: prestige gained now converts 57.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| jousting 3 | arena | 230 | 53.4 | 54.3 | needs a arena (build cost 26,079); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.8 | 57.8 |  |
| jousting 2 | arena | 210 | 58.5 | 59.5 | needs a arena (build cost 26,079); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 62.6 | 62.6 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 65.1 | 65.1 | thin at home: hop beer, wine, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 65.3 | 65.3 | thin at home: wine |
| hold banquet 4 (premium) | mansion | 20 | 67.1 | 67.1 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 | mansion | 17.5 | 68.4 | 68.4 | thin at home: wine, hop beer, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 68.5 | 68.5 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 70.8 | 70.8 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 71.8 | 71.8 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | - | pasties 7 | -98 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 14.2 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Fontaux +39, Heidlowe +27, Großaue +17
- Fontaux would trade: cured meat buy 6 @ 22.6, pasties buy 1 @ 16.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | bread 186 (2.29->3.19), firewood 33 (1.92->6.27), beer 70 (4.03->5.22), cured fish 8 (26.46->31.73) | thread 40 (5.41->5.9), bricks 9 (7.46->9.97), tools 15 (6.04->6.46), garments 1 (29.61->32.2) | +485 |
| Vauxvais | 204 | 0.06 | 0.60 (64/turn) | grain 167 (2.77->3.76), bread 205 (2.29->2.91), garments 10 (30.6->31.16), flax plants 1 (1.29->1.42) | tools 17 (5.78->6.46), bricks 4 (6.83->9.97), flax fibres 7 (6.3->7.3), furniture 1 (9.55->14.7) | +282 |
| Heilegg | 826 | 0.24 | 0.70 (74/turn) | beer 78 (4.03->5.32), dyed cloth 9 (19.01->23.75), arms 12 (30.03->32.3), flour 3 (20.68->26.79) | tools 17 (5.25->6.46), cloth 13 (9.13->10.5), garments 2 (27.3->32.2), tin ingots 5 (33.81->35.91) | +209 |
| Bordetes | 831 | 0.24 | 1.00 (106/turn) | grain 27 (2.77->5.56), bread 33 (2.29->4.8), beer 12 (4.03->7.98), furniture 2 (15.44->18.9) | axes 0 (19.53->23.75), tools 2 (5.99->6.46), garments 0 (31.08->32.2), leather 0 (28.14->30.59) | +200 |
| Fontaux | 411 | 0.12 | 1.00 (106/turn) | beer 24 (4.03->6.22), firewood 11 (1.92->8.88), timber 8 (7.82->12.82), bread 70 (2.29->2.98) | cured meat 2 (23.31->30.4), flax fibres 5 (6.3->7.3), axes 0 (21->23.75), pies 1 (19.95->20.9) | +196 |

**Best:** Grandgues at about +485 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 1 @ min 3.16 | goal planner: trial sale of an idle pile, 1 a turn at 3.16, keeps 58 (9 over) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.8) |
| grain | 6 @ 3.7, stop 23 |  | goal planner: buys 6 a turn for today's rates, keeps up to 23 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 69) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 39.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 74.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 2.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.3k (cash + stock at home prices); -6/turn over 6 turns, +16/turn over 24 turns.
- Limits: cash flow >= -407/turn, prestige >= -1.12/turn (values are after 200 tax a turn).
- Today's settings: value -151/turn, cash -159/turn, prestige +1.36/turn.
- Plan: value +44/turn, cash +51/turn, prestige -1.12/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -305 vs -162, +174 vs -144, +150 vs -139.
- Route sales counted at most (what the ships really sold, a turn): beer 1.6.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Heidlowe: +30/turn
  - ship Flax Wyrm -> Vauxvais: +6/turn
  - mansion 1 1.00 -> 0.41: +168/turn
  - net maker 0.00 -> 0.29: +10/turn
  - spinnery 1 1.65 -> 1.50: +5/turn
  - flax farm 1 4.64 -> 4.57: +0/turn
  - ropewalk 1 0.25 -> 0.00: -4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.22: +11/turn
  - weavery 1 0.50 -> 0.60: -9/turn
  - sewing shop 1 0.30 -> 0.36: +15/turn
- Model check over the last 59 turns: predicted -156/turn for the settings we ran, real +55/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.65, thread 4.15, cloth 6.62, flax fibres 4.92, garments 19.16, nets 30.55, beer 2.86, timber 3.35, prestige 67.40, cash 0.00
- Orders it would set: beer sell 1 (v2 none); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 18); labour buy 64 (v2 69); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.22, worth +9/turn.
- Ship linen snake: Grandgues -> Heidlowe (+18/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+7/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1861 coin: +3/turn, payback 631 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 85/77, thread 1060/228, cloth 72/128

## Self-diagnosis

- R1: cured meat slot dry: 3.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 30.4 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 31 (ask 30.4, cap 42.0))
- R2: spinnery 1 blocked by thread space: 1060 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
