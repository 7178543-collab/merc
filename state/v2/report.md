# v2 shadow report

Turn 14281, 2026-11-25 10:02. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,201, prestige 3,719 (599 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 10 | 0 | 12 | 0 | 0 | sell 19, sell @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 530 | 0 | 34 | buy 64, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 34 labour expired last turn (~68 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +5 crew for linen snake (crew 0.10, no projection from the game)
- labour: projection runs 100 over real use lately; planning 530, not 624
- labour expiry guard: 34 bought labour expired last turn, buy 30 (not 30) this turn

## Prestige spending, cheapest coin per prestige first

120 turns left: prestige gained now converts 45.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.4 | 51.4 | needs a arena (build cost 30,644); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.0 | 55.1 | needs a arena (build cost 30,644); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 59.4 | 59.4 | running |
| jousting 3 | arena | 230 | 58.1 | 60.0 | needs a arena (build cost 30,644); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.7 | 60.7 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 61.1 | 61.1 |  |
| hold banquet 2 (pies) | mansion | 7 | 61.2 | 61.2 |  |
| hold banquet 4 (pies) | mansion | 18 | 63.3 | 63.3 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 64.9 | 64.9 | thin at home: hop beer, stockfish, sculptures |
| jousting 2 | arena | 210 | 63.7 | 65.7 | needs a arena (build cost 30,644); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 66.9 | 66.9 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 67.1 | 67.1 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.05 | 6 | 151802239 | 0 | beer 12 | - | 52 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 15.4 (keep 14); best orders clear only 12 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Orlesailles +79, Bordetes +67, Großmühle +51, Heilegg +47, Dortdorf +46
- Orlesailles would trade: cured meat buy 3 @ 24.2, pasties buy 10 @ 9.6; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~125 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.50 (62/turn) | bread 184 (2.75->4.94), charcoal 20 (2.46->6.17), timber 19 (9.03->11.4), beer 8 (3.88->7.17) | fleece 7 (9.35->10.16), premium cheese 1 (28.77->30.4), candles 1 (92.4->93.5), cloth 3 (10.92->11.2) | +558 |
| Amsdermund | 1111 | 0.47 | 0.50 (62/turn) | windows 2 (1050->1140), jewellery 4 (97.12->123.5), leather 8 (29.82->32.3), nets 6 (35.8->38.76) | coats 3 (86.62->97.85), cloth 24 (9.5->11.2), thread 49 (5.25->6), wax 3 (24.15->28.5) | +419 |
| Heilegg | 826 | 0.28 | 0.60 (75/turn) | wrought iron 19 (17.54->27.55), flour 3 (19.64->38), dyed cloth 7 (21.21->27.36), garments 10 (30.2->32.68) | cured meat 3 (24.57->27.8), honey 1 (10.82->11.4) | +357 |
| Pontmont | 341 | 0.11 | 0.60 (75/turn) | timber 35 (9.03->14.82), cookware 5 (29.4->34.39), garments 10 (30.2->31.16), nails 9 (7.51->8.22) | fleece 9 (8.82->10.16), tools 15 (5.62->6.27), bricks 10 (5.25->7.93), chisels 1 (8.19->10.16) | +207 |
| Hofkirchen | 991 | 0.39 | 0.40 (50/turn) | glass ingots 2 (68.78->93.1), jewellery 4 (97.12->109.25), cloth 15 (11.76->13.87), ploughs 3 (83.48->95) | tin ingots 4 (34.86->35.91), candles 1 (92.4->93.5), honey 1 (9.82->11.4), dyed yarn 1 (5.23->5.89) | +156 |

**Best:** Grandgues at about +558 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.8 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.95 | goal planner: sells 2 a turn at 0.95, keeps 219 (no one offered it) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 30) |
| light armour | 1 @ 100, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.4k (cash + stock at home prices); +92/turn over 6 turns, -27/turn over 24 turns.
- Limits: cash flow >= -300/turn, prestige >= -1.24/turn (values are after 200 tax a turn).
- Today's settings: value -169/turn, cash -163/turn, prestige +0.89/turn.
- Plan: value +2/turn, cash +10/turn, prestige -1.24/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -19 vs -156, +118 vs -155, +129 vs -141.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Darmwald: +37/turn
  - ship Flax Wyrm -> Rouhomme: +1/turn
  - mansion 1 1.00 -> 0.49: +149/turn
  - spinnery 1 1.65 -> 1.34: +5/turn
  - retting pit 1 0.91 -> 0.79: +3/turn
  - flax farm 1 4.64 -> 3.97: +9/turn
  - net maker 0.00 -> 0.28: -5/turn
  - sewing shop 1 0.30 -> 0.22: -11/turn
  - weavery 1 0.50 -> 0.35: +7/turn
- Model check over the last 59 turns: predicted -146/turn for the settings we ran, real -24/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 33.26, beer 3.33, timber 3.69, prestige 66.40, cash 0.00
- Orders it would set: bread buy 5 (v2 8); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 30); light armour buy 1 (v2 None); meat buy 0 (v2 None)
- Ship linen snake: Grandgues -> Darmwald (+28/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Rouhomme (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 82/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 10.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.92 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 39 @ 3.98 (ask 3.92, cap 14.4))
- R1: bread slot dry: 5.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.58; our bid is already at/over the ask (sellers too thin)
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
