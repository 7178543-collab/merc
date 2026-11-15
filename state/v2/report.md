# v2 shadow report

Turn 14043, 2026-11-15 12:29. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,693, prestige 3,583 (463 free, -3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 41 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 24.6 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 31, buy 8, buy @ 3.7 |
| labour | 29 | 64 | 484 | 0 | 80 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 35.2 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.88 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.88 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 80 labour expired last turn (~136 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 12.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

358 turns left: prestige gained now converts 83.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| jousting 3 | arena | 230 | 54.5 | 54.9 | needs a arena (build cost 25,830); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 55.9 | 55.9 | thin at home: pasties, hop beer, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 56.6 | 56.6 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 57.2 | 57.2 | thin at home: pasties, wine, cheese |
| hold banquet 4 (pies) | mansion | 18 | 57.4 | 57.4 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 58.7 | 58.7 | thin at home: hop beer, cured fish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 59.1 | 59.1 | thin at home: wine, cured fish, cheese |
| jousting 2 | arena | 210 | 59.7 | 60.1 | needs a arena (build cost 25,830); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.2 | 60.2 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 | mansion | 17.5 | 61.0 | 61.0 | thin at home: wine, hop beer, stockfish, cheese |
| hold mass 2 (premium) | cathedral | 360 | 58.3 | 61.4 | needs a cathedral (build cost 270,260); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 14.0, pasties buy 4 @ 14.9; crew 0.2; est +243 a turn; stock: furniture 20 @ 14.0 (keep 145); stock: pasties 4 @ 14.9 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Heidlowe +628, Vauxvais +396, Brebronn +384, Bordees +355, Friedwerp +336
- Heidlowe would trade: furniture buy 53 @ 13.9, pasties buy 2 @ 15.0; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | timber 46 (7.88->12.35), firewood 33 (3.02->5.37), bread 161 (2.33->2.6), charcoal 19 (2.94->4.24) | acid 1 (137.55->148.2), tools 8 (4.66->5.46), candles 1 (86.1->91.5), spinning wheels 1 (260.4->266) | +302 |
| Fontaux | 411 | 0.12 | 1.00 (106/turn) | garments 7 (21.4->29.83), timber 11 (7.88->11.97), charcoal 12 (2.94->5.84), firewood 16 (3.02->7.27) | thread 32 (5.04->5.65), flax fibres 6 (5.35->6.8), spinning wheels 0 (258.3->266), candles 0 (86.62->91.5) | +176 |
| Großaue | 1136 | 0.42 | 0.10 (11/turn) | garments 11 (21.4->28.5), raw cloth 3 (7.88->10.36) | spinning wheels 1 (203.7->266), belts 2 (23.94->31.73), acid 1 (134.4->148.2), candles 1 (86.62->91.5) | +172 |
| Kleinburgh | 1440 | 0.59 | 0.30 (32/turn) | garments 11 (21.4->28.31), dyed cloth 7 (14.18->15.29), malt 2 (6.46->9.07), tools 18 (6.25->7.03) | spinning wheels 1 (237.3->266), acid 1 (137.55->148.2), cloth 16 (7.56->8.5), candles 1 (86.1->91.5) | +129 |
| Vauxvais | 204 | 0.06 | 0.50 (53/turn) | bread 161 (2.33->2.75), charcoal 19 (2.94->4.39), wax 6 (25.41->27.17), beer 65 (3.46->3.67) | thread 9 (4.09->5.65), flax fibres 9 (5.35->6.8), acid 1 (138.6->148.2), garments 2 (23.73->24.6) | +127 |

**Best:** Grandgues at about +302 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 5 @ min 3.26 | goal planner: sells 5 a turn at 3.26, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 20.8 | goal planner: sells 11 (v2 had 10) |
| grain | 8 @ 3.7, stop 30 |  | goal planner: buys 8 a turn for today's rates, keeps up to 30 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 35.2 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.9k (cash + stock at home prices); -6/turn over 6 turns, -118/turn over 24 turns.
- Limits: cash flow >= -237/turn, prestige >= -0.68/turn (values are after 200 tax a turn).
- Today's settings: value +110/turn, cash +99/turn, prestige -3.03/turn - breaks the prestige floor.
- Plan: value +16/turn, cash +46/turn, prestige -0.68/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -175 vs -170, -93 vs -193, -258 vs +127.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Unterhufe: +3/turn
  - net maker 0.00 -> 0.29: +12/turn
  - spinnery 1 1.65 -> 1.40: +4/turn
  - ropewalk 1 0.25 -> 0.00: -0/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.18: +10/turn
  - flax farm 1 4.64 -> 4.40: -1/turn
  - sewing shop 1 0.30 -> 0.36: -2/turn
  - weavery 1 0.50 -> 0.60: +9/turn
  - mansion 1 0.00 -> 0.56: -132/turn
- Model check over the last 58 turns: predicted -125/turn for the settings we ran, real -79/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.69, thread 4.25, cloth 6.78, flax fibres 5.03, garments 19.62, nets 30.60, beer 3.00, timber 3.38, prestige 62.93, cash 0.00
- Orders it would set: beer sell 5 (v2 none); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.18, worth +8/turn.
- Ship linen snake: Grandgues -> Unterhufe (+4/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +0/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +84/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3593 coin: +3/turn, payback 1093 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 416 (+126 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.22 |
| ret | 3 | 0.91 | 0.84 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 110/77, thread 1064/226, cloth 72/126

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.3 -> **buy 9 @ 3.36 (ask 3.3, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.88; ask over the cap 2.1 (60 coin per prestige)
- R1: prestige rate -3.03 a turn vs 12-turn median -0.50; likely: dry slot: beer, firewood
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
