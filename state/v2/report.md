# v2 shadow report

Turn 13952, 2026-11-11 17:31. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,695, prestige 3,592 (472 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 23 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.44 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 33 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~77 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +7 crew for Flax Wyrm (crew 0.13, no projection from the game)
- labour: projection runs 100 over real use lately; planning 490, not 590

## Prestige spending, cheapest coin per prestige first

449 turns left: prestige gained now converts 89.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.7 | 54.7 | thin at home: ham, stockfish, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 57.0 | 57.0 |  |
| jousting 3 | arena | 230 | 56.7 | 57.0 | needs a arena (build cost 28,150); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 57.1 | 57.1 | thin at home: ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 58.1 | 58.1 | thin at home: ham, stockfish, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 60.3 | 60.3 |  |
| hold banquet 3 (pies) | mansion | 8 | 61.2 | 61.2 | thin at home: cheese, pies |
| jousting 2 | arena | 210 | 62.1 | 62.4 | needs a arena (build cost 28,150); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 58.5 | 65.1 | needs a church (build cost 73,487); thin at home: candles, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 65.7 | 65.7 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 65.9 | 65.9 | thin at home: cheese, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 19 @ 13.5, pasties buy 9 @ 15.1; crew 0.2; est +257 a turn; stock: furniture 19 @ 13.5 (keep 145); stock: pasties 9 @ 15.1 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.0 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Angefont +310, Heidlowe +310, Marmont +300, Amsdermund +291, Gotthafen +288
- Angefont would trade: furniture buy 27 @ 14.6, pasties buy 7 @ 15.4; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Unterhufe | 595 | 0.17 | 0.10 (11/turn) | dyed cloth 21 (12.81->16.91) | cloth 24 (6.67->10.9), cheese 15 (9.24->11.69), resin 5 (2.44->3.19), garments 2 (24.36->25) | +216 |
| Amsdermund | 1111 | 0.42 | 0.30 (33/turn) | cured fish 7 (24.57->33.25), acid 1 (115.5->120.65), canvas 2 (41.58->43.7), grain 2 (2.66->4.6) | cloth 21 (7.56->10.9), cheese 15 (7.93->11.69), garments 2 (22.89->25), hop beer 5 (7.25->8.64) | +183 |
| Rotterburg | 1056 | 0.39 | 0.50 (55/turn) | garments 10 (24.8->26.79), beer 52 (3.57->4.54), nets 6 (38.2->40.28), wine 4 (6.98->7.74) | cloth 24 (7.19->10.9), cheese 15 (8.98->11.69), salt 4 (4.26->4.75) | +150 |
| Kirchwerp | 1072 | 0.40 | 0.50 (55/turn) | thread 92 (4.66->5.42), jewellery 2 (106.05->122.55), honey 2 (10.08->11.3), arms 5 (35.91->36.86) | cloth 24 (7.56->10.9), garments 2 (23.1->25), blades 1 (14.7->16.43), nails 1 (6.98->7.55) | +144 |
| Grandgues | 152 | 0.04 | 0.40 (44/turn) | bread 162 (2.44->2.85), timber 26 (7.67->8.74), thread 8 (4.66->5.27), flour 2 (23.94->24.51) | cloth 11 (7.67->10.9), cheese 15 (9.5->11.69), windows 1 (577.5->584.25), slaked lime 4 (9.24->10.07) | +143 |

**Best:** Unterhufe at about +216 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.56, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 23 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 88, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 3 @ min 7.15 | goal planner: sells 3 a turn at 7.15, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.2) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 112, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.3k (cash + stock at home prices); -729/turn over 6 turns, -213/turn over 24 turns.
- Limits: cash flow >= -196/turn, prestige >= -0.72/turn (values are after 200 tax a turn).
- Today's settings: value +38/turn, cash +116/turn, prestige -2.57/turn - breaks the prestige floor.
- Plan: value -10/turn, cash +117/turn, prestige -0.72/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +115 vs +57, +778 vs +90, +6 vs +76.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: +18/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: +8/turn
  - spinnery 1 1.65 -> 1.25: -1/turn
  - retting pit 1 0.91 -> 0.78: -5/turn
  - flax farm 1 4.64 -> 3.90: -9/turn
  - mansion 1 0.00 -> 0.44: -75/turn
- HAND-OVER: goal planner: model check failed 3 runs in a row, rates handed back to the old rules.
- Model check over the last 60 turns: predicted +108/turn for the settings we ran, real +26/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.21, beer 3.01, timber 3.29, prestige 59.76, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 3 (v2 none); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> Calange (+18/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +1/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 417 (+126 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.07 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 126/77, thread 1064/227, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
