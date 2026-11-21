# v2 shadow report

Turn 14182, 2026-11-21 07:01. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,473, prestige 3,726 (606 free, -3.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 59 | 0 | 4 | 0 | 0 | min_holding 58, sell 15, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 9 | 9 | 0 | 0 | stop 36, buy 10, buy @ 3.7 |
| labour | 64 | 64 | 502 | 0 | 62 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), home ask 28.80 x14, yet 0 bought last turn); labour need rises ~35/turn when they restart -> v2: find out why the buy isn't filling
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: home ask 2.64 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.70 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 62 labour expired last turn (~130 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.70 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +3 crew for Flax Wyrm (crew 0.05, no projection from the game)
- labour: projection runs 100 over real use lately; planning 522, not 622
- labour expiry guard: 62 bought labour expired last turn, buy 2 (not 22) this turn

## Prestige spending, cheapest coin per prestige first

219 turns left: prestige gained now converts 66.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.8 | 53.5 | needs a arena (build cost 29,434); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.8 | 58.6 | needs a arena (build cost 29,434); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 61.2 | 61.2 | thin at home: hop beer, stockfish, candles |
| hold banquet 4 (pies) | mansion | 18 | 61.3 | 61.3 | thin at home: hop beer, stockfish, cheese, candles |
| maintain 1 | park | 0.5 | 61.8 | 61.8 | running |
| hold mass 2 (premium) | cathedral | 360 | 54.8 | 63.6 | needs a cathedral (build cost 316,615); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 65.1 | 65.1 | thin at home: hop beer, cheese, candles |
| hold banquet 4 | mansion | 17.5 | 66.3 | 66.3 | thin at home: hop beer, stockfish, cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 66.9 | 66.9 | thin at home: cheese, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 72.6 | 72.6 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 73.9 | 73.9 |  |
| jousting 1 | arena | 170 | 74.8 | 75.9 | needs a arena (build cost 29,434); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 14 @ 16.0; crew 0.1; est +28 a turn; stock: pasties 14 @ 16.0 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -12 a turn after crew: ship stays at 0
- best towns now: Blanans +210, Vauxvais +167, Großmühle +154, Angefont +151, Heidlowe +146
- Blanans would trade: furniture buy 13 @ 12.7, grain buy 8 @ 2.66, pasties buy 13 @ 16.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~129 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (129/turn) | firewood 43 (2.77->6.17), charcoal 19 (2.79->6.03), bread 257 (2.86->3.19), thread 92 (6.65->7.03) | cheese 8 (11.45->12.35), wrought iron 3 (17.01->17.86), cloth 4 (11.13->11.5), wool 2 (12.08->12.44) | +249 |
| Hanstein | 380 | 0.13 | 0.70 (90/turn) | butter 1 (68.78->71.25), firewood 18 (2.77->6.79), charcoal 18 (2.79->3.88), cloth 1 (9.9->10.36) | cheese 8 (7.88->12.35), wool 13 (10.45->12.44), dyed cloth 7 (15.86->17.86), tackles 1 (151.2->164.35) | +113 |
| Amsdermund | 1111 | 0.49 | 0.30 (39/turn) | butter 1 (68.78->72.67), hides 1 (13.33->14.72) | cloth 24 (7.35->11.5), cured meat 3 (24.78->27.55), chisels 4 (8.4->9.88), nails 5 (5.46->6.7) | +109 |
| Clairas | 374 | 0.13 | 0.20 (26/turn) | - | cloth 24 (10.13->11.5), cheese 7 (8.61->12.35), thread 35 (6.25->6.9), wool 6 (10.61->12.44) | +87 |
| Clarfranche | 1484 | 0.75 | 0.20 (26/turn) | garments 10 (31.4->35.15), dyed cloth 3 (19.84->21.66), cloth 1 (9.9->12.06) | cheese 8 (7.93->12.35), chisels 4 (6.56->9.88), tallow 1 (28.77->34.77), cured meat 3 (24.78->27.55) | +82 |

**Best:** Grandgues at about +249 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.88 |  |
| bread | 5 @ 2.98, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 29.0, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| furniture | 2 @ 17.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.4) |
| grain | 10 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 35 = 3.9 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 2) |
| light armour | 1 @ 111, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 44.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.3k (cash + stock at home prices); +140/turn over 6 turns, -108/turn over 24 turns.
- Limits: cash flow >= -311/turn, prestige >= -1.28/turn (values are after 200 tax a turn).
- Today's settings: value -174/turn, cash -198/turn, prestige +0.45/turn.
- Plan: value +10/turn, cash +15/turn, prestige -1.28/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -65 vs -185, +114 vs -187, +86 vs -188.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Blanans: +8/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.59: +125/turn
  - ropewalk 1 0.25 -> 0.07: +7/turn
  - spinnery 1 1.65 -> 1.19: +30/turn
  - retting pit 1 0.91 -> 0.76: +3/turn
  - net maker 0.00 -> 0.29: +2/turn
  - flax farm 1 4.64 -> 3.81: +10/turn
  - brewery 1 0.14 -> 0.19: +0/turn
  - weavery 1 0.50 -> 0.44: -3/turn
- Model check over the last 59 turns: predicted -121/turn for the settings we ran, real -2/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.61, beer 3.57, timber 3.76, prestige 68.96, cash 0.00
- Orders it would set: bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 4 (v2 12); firewood buy 4 (v2 8); fish buy 0 (v2 None); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 2); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Blanans (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1991 coin: +1/turn, payback 1477 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 417 (+128 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.01 |
| ret | 3 | 0.91 | 0.80 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 131/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 0.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.98, home ask 2.92; our bid is already at/over the ask (sellers too thin)
- R1: cured meat slot dry: 3.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 29, home ask 28.8; our bid is already at/over the ask (sellers too thin)
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R1: prestige rate -3.75 a turn vs 12-turn median -0.99; likely: dry slot: bread, cured meat, fish
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
