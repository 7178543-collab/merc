# v2 shadow report

Turn 14108, 2026-11-18 05:14. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,473, prestige 3,579 (459 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 5 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 3 | 2 | 2 | 1 | 0 | stop 11, buy 3, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 71 | 0 | 2 | 0 | 0 | min_holding 75, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (3 @ 2.4), but the home ask 2.70 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 2 of ~3 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 1.0 turns of firewood left and buying 3 (need 7) -> v2: buy 7

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 83.50 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 607

## Prestige spending, cheapest coin per prestige first

293 turns left: prestige gained now converts 77.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.0 | 52.4 | needs a arena (build cost 26,808); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.7 | 53.7 | running |
| jousting 2 | arena | 210 | 56.9 | 57.4 | needs a arena (build cost 26,808); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.5 | 58.5 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 60.5 | 60.5 | thin at home: hop beer, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 61.4 | 61.4 | thin at home: cheese |
| hold mass 2 (premium) | cathedral | 360 | 56.9 | 61.6 | needs a cathedral (build cost 293,340); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 1 (meat) | mansion | 4.2 | 61.8 | 61.8 |  |
| hold banquet 3 (pies) | mansion | 8 | 62.2 | 62.2 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 62.4 | 62.4 | thin at home: hop beer, cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 63.6 | 63.6 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 64.2 | 64.2 | thin at home: hop beer, stockfish, premium ham |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: candles buy 5 @ 77.0, furniture buy 20 @ 14.6, pasties buy 3 @ 15.3; crew 0.2; est +288 a turn; stock: candles 5 @ 77.0 (keep 12); stock: furniture 20 @ 14.6 (keep 145); stock: pasties 3 @ 15.3 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Hofkirchen +477, Gotthafen +468, Vauxvais +404, Clairlond +322, Fulkirch +310
- Hofkirchen would trade: candles buy 5 @ 76.5, furniture buy 37 @ 14.0, pasties buy 7 @ 16.0; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.80 (92/turn) | timber 29 (7.88->12.54), firewood 34 (2.84->5.7), limestone 5 (16.8->24.7), charcoal 19 (2.98->4.45) | dyed cloth 3 (10.08->14.91), garments 2 (28.14->34.6), bricks 4 (8.4->9.97), candles 1 (82.42->83.5) | +252 |
| Fontaux | 411 | 0.12 | 0.60 (69/turn) | thread 41 (5.35->7.27), timber 29 (7.88->11.88), dyed yarn 1 (6.14->6.41) | garments 2 (31.08->34.6), cloth 6 (10.5->10.9), candles 1 (82.42->83.5), resin 3 (3.3->3.7) | +137 |
| Amsdermund | 1111 | 0.43 | 0.30 (34/turn) | wine 11 (7.98->9.12), jewellery 5 (102.9->104.5), flour 2 (23.1->29.07), grain 2 (2.88->3.93) | cloth 24 (7.35->10.9), garments 2 (27.3->34.6), paper 6 (23.73->25.27), cookware 7 (21.63->22.8) | +133 |
| Birkeningen | 1006 | 0.37 | 0.90 (103/turn) | beer 62 (4.03->5.7), nets 6 (35->40.09), malt 3 (6.83->11.4), charcoal 15 (2.98->6.27) | garments 2 (30.03->34.6), cookware 7 (21.84->22.8) | +109 |
| Clairas | 374 | 0.11 | 0.20 (23/turn) | tackles 2 (158.55->183.35), charcoal 19 (2.98->4.35) | cloth 24 (9.82->10.9), dyed cloth 3 (11.03->14.91), garments 2 (28.77->34.6), thread 12 (5.51->5.75) | +104 |

**Best:** Grandgues at about +252 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 4.02, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 7 = 4.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 3 @ 2.4, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.0) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 2) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.4k (cash + stock at home prices); +136/turn over 6 turns, +156/turn over 24 turns.
- Limits: cash flow >= -395/turn, prestige >= -0.66/turn (values are after 200 tax a turn).
- Today's settings: value +102/turn, cash +82/turn, prestige -2.43/turn - breaks the prestige floor.
- Plan: value +31/turn, cash +39/turn, prestige -0.66/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +273 vs +74, +66 vs +80, -5 vs +82.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.07: +13/turn
  - net maker 0.00 -> 0.28: +4/turn
  - spinnery 1 1.65 -> 1.58: +4/turn
  - ropewalk 1 0.25 -> 0.33: +3/turn
  - mansion 1 0.00 -> 0.42: -97/turn
- Model check over the last 60 turns: predicted +125/turn for the settings we ran, real +59/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.79, thread 4.50, cloth 7.18, flax fibres 5.33, garments 20.78, nets 32.44, beer 3.18, timber 3.38, prestige 60.13, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 3 (v2 7); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 2); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Hofkirchen (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +89/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 8.5/turn (+0.0 exported); plan makes 35.7 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 464 (+175 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.08 |
| ret | 3 | 0.91 | 1.02 |
| spin | 4 | 1.65 | 1.79 |
| weave | 3 | 0.50 | 1.40 |
| sew | 2 | 0.30 | 0.87 |

Buffers: flax fibres 75/81, thread 1048/239, cloth 72/140

## Self-diagnosis

- R1: firewood slot dry: 3.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 3 @ 2.4, home ask 2.7; ask over the cap 2.1 (60 coin per prestige)
