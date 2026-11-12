# v2 shadow report

Turn 13964, 2026-11-12 05:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,808, prestige 3,562 (442 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 11 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 35 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 4.18 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 4.18 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.90 x26, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~74 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 506, not 606
- labour expiry guard: 45 bought labour expired last turn, buy 0 (not 6) this turn

## Prestige spending, cheapest coin per prestige first

437 turns left: prestige gained now converts 88.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| jousting 3 | arena | 230 | 55.0 | 55.3 | needs a arena (build cost 25,969); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.6 | 56.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 56.8 | 56.8 | thin at home: wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 58.5 | 58.5 |  |
| hold banquet 4 | mansion | 17.5 | 60.6 | 60.6 | thin at home: wine, ham, stockfish |
| jousting 2 | arena | 210 | 60.3 | 60.6 | needs a arena (build cost 25,969); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.8 | 60.8 | thin at home: wine, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 61.8 | 61.8 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 62.0 | 62.0 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 62.7 | 62.7 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 63.9 | 63.9 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0.344 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.416 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 22 @ 14.6, pasties buy 7 @ 15.5; crew 0.1; est +273 a turn; stock: furniture 22 @ 14.6 (keep 145); stock: pasties 7 @ 15.5 (keep 14)
- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 14.4, pasties buy 2 @ 15.6; crew 0.2; est +225 a turn; stock: furniture 20 @ 14.4 (keep 145); stock: pasties 2 @ 15.6 (keep 14)
- best towns now: Großmühle +303, Bedenis +279, Angefont +273, Grandgues +273, Großaue +268
- Großmühle would trade: furniture buy 22 @ 13.7, pasties buy 12 @ 14.3; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Darmwald | 1022 | 0.35 | 0.80 (85/turn) | beer 85 (3.68->6.08), garments 10 (18.96->25.65), furniture 9 (11.76->16.62), lead ore 2 (9.5->14.25) | - | +260 |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | firewood 44 (4.35->7.03), timber 34 (8.29->9.69), nets 4 (35->39.71), furniture 8 (11.76->13.77) | cloth 9 (8.19->9.05), garments 1 (23.52->23.6), paper 3 (26.67->26.79) | +167 |
| Pontmont | 341 | 0.10 | 0.50 (53/turn) | limestone 6 (16.48->38), garments 10 (18.96->20.9), furniture 9 (11.76->13.96), bricks 6 (8.77->11.78) | tallow 1 (18.17->20.52), flax fibres 1 (5.83->6.65), dyed cloth 10 (10.71->10.83), tools 14 (5.25->5.37) | +165 |
| Arnsreuth | 921 | 0.30 | 0.20 (21/turn) | tapestries 1 (687.75->783.75), garments 10 (18.96->22.04), arms 5 (35.91->40.28), furniture 9 (11.76->13.87) | ploughs 1 (69.3->75.52), paper 2 (25.62->26.79), flour 1 (18.59->21.85), tar 5 (9.66->10.45) | +163 |
| Essenbrucke | 584 | 0.17 | 0.30 (32/turn) | beer 28 (3.68->6.27), garments 10 (18.96->22.23), dyed cloth 13 (12.71->15.2), lead ore 3 (9.5->14.82) | butter 1 (75.08->83.6), charcoal 19 (2.05->3.67), thread 4 (4.47->5.65), cloth 2 (8.35->9.05) | +159 |

**Best:** Darmwald at about +260 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 37.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 89.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.85 | goal planner: sells 2 a turn at 5.85, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| furniture | 2 @ 15.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 111, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.2k (cash + stock at home prices); -38/turn over 6 turns, -138/turn over 24 turns.
- Limits: cash flow >= -242/turn, prestige >= -0.59/turn (values are after 200 tax a turn).
- Today's settings: value +34/turn, cash +105/turn, prestige -2.42/turn - breaks the prestige floor.
- Plan: value -18/turn, cash +108/turn, prestige -0.59/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +47 vs +116, +86 vs +114, +7 vs +83.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +8/turn
  - ship Flax Wyrm -> Großaue: +0/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.03: +20/turn
  - weavery 1 0.50 -> 0.60: -3/turn
  - sewing shop 1 0.30 -> 0.36: +8/turn
  - spinnery 1 1.65 -> 1.31: -4/turn
  - retting pit 1 0.91 -> 0.80: +1/turn
  - flax farm 1 4.64 -> 3.18: -6/turn
- Model check over the last 61 turns: predicted +108/turn for the settings we ran, real +13/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.63, thread 4.09, cloth 6.54, flax fibres 4.85, garments 18.92, nets 29.56, beer 3.15, timber 3.17, prestige 61.10, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Hofkirchen (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Großaue (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 407 (+116 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.54 |
| ret | 3 | 0.91 | 0.71 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 162/77, thread 1064/227, cloth 73/127

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 4.18; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
