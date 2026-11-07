# v2 shadow report

Turn 13853, 2026-11-07 14:31. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,719, prestige 3,366 (246 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 9 | 9 | 4 | 0 | 0 | min_holding 60, sell 3, sell @ 3.06; stop 26, buy 9, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 507 | 0 | 22 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.48 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.48 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~36 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 607

## Prestige spending, cheapest coin per prestige first

548 turns left: prestige gained now converts 93.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.2 | 54.2 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.3 | 55.3 |  |
| jousting 3 | arena | 230 | 55.0 | 55.3 | needs a arena (build cost 25,725); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 57.0 | 57.0 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.3 | 57.3 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 59.7 | 59.7 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.7 | 59.7 | thin at home: wine, cheese |
| hold banquet 3 (pies) | mansion | 8 | 59.7 | 59.7 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 | thin at home: cheese |
| jousting 2 | arena | 210 | 60.3 | 60.5 | needs a arena (build cost 25,725); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 61.6 | 61.6 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 9 @ 15.7; crew 0.1; est +18 a turn; stock: pasties 9 @ 15.7 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.1 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Rouhomme +28, Hanstein +23, Chatgnan +22, Orlesailles +21, Grandgues +18
- Rouhomme would trade: pasties buy 9 @ 14.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.11 | 0.30 (32/turn) | garments 10 (18.88->23.18), timber 15 (7.3->11.49), nets 2 (33.6->35.72), axes 1 (15.12->15.86) | cloth 24 (7.4->9.5), cheese 5 (6.88->9.17), seeds 12 (1.84->2.32), candles 1 (82.42->84.5) | +153 |
| Etallaen | 774 | 0.22 | 0.10 (11/turn) | garments 10 (18.88->25.65), cured fish 7 (24.57->28.88), nets 6 (33.6->38.38), honey 2 (8.14->12.06) | cloth 7 (8.14->9.5), candles 1 (78.23->84.5), flax fibres 5 (5.46->6.1), gears 1 (69.83->71.72) | +148 |
| Fontaux | 411 | 0.12 | 1.00 (106/turn) | timber 19 (7.3->11.78), garments 7 (18.88->23.75), firewood 16 (2.6->7.5), charcoal 13 (2.54->4.14) | cloth 4 (8.35->9.5), gears 0 (68.78->71.72), chisels 0 (7.67->8.6), flax plants 2 (1.02->1.57) | +145 |
| Amsdermund | 1111 | 0.41 | 0.40 (43/turn) | garments 10 (18.88->21.85), hop beer 12 (10.92->12.54), paper 4 (22.68->25.08), glass ingots 1 (52.29->60.32) | looms 1 (556.5->603.25), cheese 5 (6.77->9.17), candles 1 (75.08->84.5), jewellery 3 (84->86.92) | +144 |
| Vauxvais | 204 | 0.06 | 0.20 (21/turn) | beer 61 (3.82->4.6), garments 10 (18.88->22.23), glass ingots 1 (52.29->56.52), logs 1 (4.03->5.7) | bricks 8 (4.85->9.03), cheese 5 (6.88->9.17), cloth 10 (8.45->9.5), candles 1 (77.7->84.5) | +139 |

**Best:** Hanstein at about +153 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 9 @ 3.82, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 9 = 2.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 3 @ min 1.21 | goal planner: sells 3 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.8) |
| grain | 8 @ 3.7, stop 31 |  | goal planner: buys 8 a turn for today's rates, keeps up to 31 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.5k (cash + stock at home prices); +179/turn over 6 turns, -57/turn over 24 turns.
- Limits: cash flow >= -322/turn, prestige >= +2.27/turn (values are after 200 tax a turn).
- Today's settings: value +77/turn, cash +61/turn, prestige -1.44/turn - breaks the prestige floor.
- Plan: value -105/turn, cash -98/turn, prestige +2.27/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +132 vs +69, +6 vs +67, +70 vs +66.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +5/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - ropewalk 1 0.25 -> 0.33: +3/turn
  - spinnery 1 1.65 -> 1.36: -8/turn
  - retting pit 1 0.91 -> 0.77: +3/turn
  - flax farm 1 4.64 -> 3.81: +7/turn
  - weavery 1 0.50 -> 0.32: -41/turn
  - sewing shop 1 0.30 -> 0.18: -6/turn
  - mansion 1 0.00 -> 0.88: -146/turn
- Model check over the last 61 turns: predicted +103/turn for the settings we ran, real +73/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.05, beer 3.00, timber 3.13, prestige 57.41, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 3 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Brunnham (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 439 (+150 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.97 |
| ret | 3 | 0.91 | 0.99 |
| spin | 4 | 1.65 | 1.75 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 543/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.48; ask over the cap 2.1 (60 coin per prestige)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.1 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
