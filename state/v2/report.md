# v2 shadow report

Turn 14174, 2026-11-20 23:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,970, prestige 3,737 (617 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 123 | 0 | 12 | 0 | 0 | min_holding 58, sell 4, sell @ 4 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 16 | 18 | 9 | 0 | 0 | stop 26, buy 7, buy @ 3.7 |
| labour | 64 | 64 | 519 | 0 | 45 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.70 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~93 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.78 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.70 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 520, not 620
- labour expiry guard: 45 bought labour expired last turn, buy 20 (not 20) this turn

## Prestige spending, cheapest coin per prestige first

227 turns left: prestige gained now converts 68.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.0 | 52.7 | needs a arena (build cost 28,979); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.0 | 57.7 | needs a arena (build cost 28,979); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 57.8 | 57.8 | thin at home: wine, stockfish, candles |
| hold banquet 4 (premium) | mansion | 20 | 60.2 | 60.2 | thin at home: wine, stockfish, candles |
| hold banquet 4 | mansion | 17.5 | 61.6 | 61.6 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 3 (pies) | mansion | 8 | 61.9 | 61.9 | thin at home: cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 62.2 | 62.2 | thin at home: wine, cheese, candles |
| maintain 1 | park | 0.5 | 62.4 | 62.4 | running |
| hold mass 2 (premium) | cathedral | 360 | 54.7 | 62.9 | needs a cathedral (build cost 315,010); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 1 (meat) | mansion | 4.2 | 68.6 | 68.6 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 68.7 | 68.7 | thin at home: wine, cheese |
| hold banquet 3 (meat) | mansion | 7.6 | 69.9 | 69.9 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 13 @ 4.9, pasties buy 14 @ 16.0; crew 0.1; est +35 a turn; stock: pasties 14 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: pasties buy 9 @ 14.9; crew 0.1; est +23 a turn; stock: pasties 9 @ 14.9 (keep 14)
- best towns now: Blanans +220, Clairlond +219, Cobholme +198, Chatgnan +192, Brunnham +179
- Blanans would trade: furniture buy 14 @ 12.4, pasties buy 13 @ 16.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~133 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Großaue | 1136 | 0.52 | 0.50 (67/turn) | - | windows 1 (698.25->817), cloth 24 (10.03->13.3), thread 47 (5.93->7.05), premium ham 1 (218.4->228) | +230 |
| Grandgues | 152 | 0.05 | 0.50 (67/turn) | thread 92 (6.5->7.03), charcoal 19 (2.71->5.27), firewood 30 (2.79->5.7), dyed cloth 5 (19.21->21.47) | cloth 4 (12.18->13.3), malt 2 (8.4->10.26), bread 4 (2.6->2.78), cured meat 3 (25.83->26) | +156 |
| Fontaux | 411 | 0.15 | 0.40 (53/turn) | nets 6 (43->50.82), thread 63 (6.5->7.27), garments 10 (31.2->34.2), flour 3 (21.63->26.6) | cloth 3 (13.02->13.3) | +139 |
| Birkeningen | 1006 | 0.43 | 0.20 (27/turn) | - | windows 1 (719.25->817), cloth 20 (11.55->13.3), tallow 1 (24.99->30.59), dyed cloth 5 (15.54->16.62) | +123 |
| Caillechâtel | 488 | 0.17 | 0.20 (27/turn) | nets 2 (43->43.89) | cloth 24 (8.93->13.3), thread 20 (6.09->7.05), seeds 8 (2.14->2.58), grain 8 (3.07->3.42) | +108 |

**Best:** Großaue at about +230 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 19 @ min 3.88 | makes 19.3, uses 4.2, holds 123 (keeps 58): sells the surplus + 4/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 7 @ 3.7, stop 26 |  | goal planner: buys 7 a turn for today's rates, keeps up to 26 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 20) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 41.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.5k (cash + stock at home prices); -50/turn over 6 turns, -117/turn over 24 turns.
- Limits: cash flow >= -290/turn, prestige >= -1.32/turn (values are after 200 tax a turn).
- Today's settings: value -177/turn, cash -190/turn, prestige +1.11/turn.
- Plan: value +37/turn, cash +39/turn, prestige -1.32/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +1 vs -169, -61 vs -173, +48 vs -189.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +22/turn
  - ship Flax Wyrm -> Blanans: +3/turn
  - mansion 1 1.00 -> 0.42: +154/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.09: +18/turn
  - spinnery 1 1.65 -> 1.24: +13/turn
  - retting pit 1 0.91 -> 0.79: +4/turn
  - flax farm 1 4.64 -> 3.94: +9/turn
- Model check over the last 59 turns: predicted -88/turn for the settings we ran, real +23/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.65, beer 3.42, timber 3.80, prestige 64.44, cash 0.00
- Orders it would set: bread buy 5 (v2 7); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 7 (v2 18); labour buy 64 (v2 20); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Amsdermund (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +85/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 420 (+131 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.22 |
| ret | 3 | 0.91 | 0.84 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 116/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
