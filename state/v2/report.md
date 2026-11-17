# v2 shadow report

Turn 14097, 2026-11-17 18:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,005, prestige 3,607 (487 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 504 | 0 | 25 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 25 labour expired last turn (~46 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

304 turns left: prestige gained now converts 78.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.6 | 52.1 | needs a arena (build cost 28,971); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.3 | 54.3 | running |
| jousting 2 | arena | 210 | 56.5 | 57.0 | needs a arena (build cost 28,971); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 58.2 | 58.2 | thin at home: hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 58.9 | 58.9 |  |
| hold banquet 2 (pies) | mansion | 7 | 60.6 | 60.6 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 60.7 | 60.7 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 61.4 | 61.4 | thin at home: cured fish |
| hold banquet 4 (premium) | mansion | 20 | 61.8 | 61.8 | thin at home: hop beer, ham, stockfish, premium cheese, premium ham |
| hold banquet 1 (meat) | mansion | 4.2 | 62.0 | 62.0 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 62.4 | 62.4 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 63.0 | 63.0 | thin at home: hop beer, ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.3 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +697, Hofkirchen +432, Clairlond +269, Cobholme +266, Fulkirch +259
- Amsdermund would trade: furniture buy 64 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (104/turn) | timber 29 (8.4->12.82), firewood 31 (3.09->6.6), bread 162 (2.52->2.83), charcoal 19 (2.88->4.54) | furniture 9 (18.48->20.14), bricks 2 (7.88->11.3), medicine 1 (152.25->157.7), tools 3 (4.62->5.98) | +272 |
| Fontaux | 411 | 0.13 | 0.80 (93/turn) | beer 69 (3.93->5.27), tapestries 1 (782.25->836), timber 32 (8.4->11.69), garments 10 (27.6->31.54) | cloth 7 (10.92->11.5), cheese 8 (6.72->6.89) | +243 |
| Amsdermund | 1111 | 0.44 | 0.40 (46/turn) | chisels 4 (12.5->17.1), wine 10 (7.3->9.36), nets 4 (34.2->35.91), slaked lime 2 (8.66->11.4) | cloth 24 (6.67->11.5), furniture 9 (14.18->20.14), premium cheese 3 (20.58->32.68), dyed cloth 9 (13.65->14.72) | +240 |
| Großmühle | 751 | 0.23 | 0.20 (23/turn) | tapestries 2 (782.25->821.75), raw cloth 17 (10.5->13.77), nets 5 (34.2->35.34), dyed yarn 1 (5.21->5.65) | furniture 9 (12.81->20.14), cloth 8 (10.24->11.5), cheese 8 (5.99->6.89), bricks 2 (5.99->11.3) | +204 |
| Birkeningen | 1006 | 0.38 | 0.60 (70/turn) | tapestries 2 (782.25->840.75), nets 4 (34.2->38.76), wine 9 (7.3->8.55), charcoal 18 (2.88->6.22) | cloth 20 (10.03->11.5), medicine 1 (147->157.7), furniture 9 (17.75->20.14), ham 1 (113.4->115.9) | +185 |

**Best:** Grandgues at about +272 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.92, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 82, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 76.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.5k (cash + stock at home prices); +90/turn over 6 turns, +78/turn over 24 turns.
- Limits: cash flow >= -292/turn, prestige >= -0.78/turn (values are after 200 tax a turn).
- Today's settings: value +91/turn, cash +70/turn, prestige -2.65/turn - breaks the prestige floor.
- Plan: value +16/turn, cash +23/turn, prestige -0.78/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -274 vs +84, +227 vs +67, +230 vs +82.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Großmühle: +3/turn
  - ship Flax Wyrm -> Clairlond: +0/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.38: +4/turn
  - net maker 0.00 -> 0.28: +1/turn
  - retting pit 1 0.91 -> 0.83: +1/turn
  - flax farm 1 4.64 -> 4.17: +4/turn
  - sewing shop 1 0.30 -> 0.25: -24/turn
  - weavery 1 0.50 -> 0.40: -5/turn
  - mansion 1 0.00 -> 0.45: -74/turn
- Model check over the last 60 turns: predicted +118/turn for the settings we ran, real +27/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.72, beer 3.38, timber 3.89, prestige 60.99, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Großmühle (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Clairlond (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 84/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
