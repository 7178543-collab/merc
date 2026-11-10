# v2 shadow report

Turn 13920, 2026-11-10 09:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,730, prestige 3,464 (344 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 6 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 499 | 0 | 30 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 6.2 -> v2: add buy 9
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.04 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.04 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 28, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 30 labour expired last turn (~47 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 12.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 499, not 586

## Prestige spending, cheapest coin per prestige first

481 turns left: prestige gained now converts 91.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.9 | 45.9 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 53.6 | 53.6 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 53.6 | 53.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 53.8 | 53.8 | thin at home: hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 53.8 | 54.1 | needs a arena (build cost 25,470); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 54.6 | 54.6 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 55.9 | 55.9 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 56.2 | 56.2 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 57.4 | 57.4 | thin at home: pasties, hop beer |
| hold banquet 2 (pies) | mansion | 7 | 57.8 | 57.8 | thin at home: pasties |
| jousting 2 | arena | 210 | 58.9 | 59.2 | needs a arena (build cost 25,470); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 58.2 | 60.3 | needs a cathedral (build cost 267,085); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 11 @ 14.5; crew 0.1; est +39 a turn; stock: pasties 11 @ 14.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.4 (keep 14); best orders clear only 8 a turn after crew: ship stays at 0
- best towns now: Chatgnan +135, Essenbrucke +131, Marmont +127, Disscester +126, Boistot +124
- Chatgnan would trade: furniture buy 10 @ 13.4, pasties buy 7 @ 15.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.60 (59/turn) | firewood 26 (3.19->8.93), thread 21 (4.78->7.89), charcoal 19 (3.32->4.94), logs 1 (6.04->7.79) | bricks 1 (10.4->15.67), flax fibres 3 (7.04->7.2) | +211 |
| Fontaux | 411 | 0.11 | 1.00 (98/turn) | thread 50 (4.78->7.27), bread 90 (2.52->3.17), gold ore 0 (150.15->175.75), charcoal 10 (3.32->5.46) | jewellery 0 (96.6->103.55), bricks 0 (11.34->15.67), flax plants 3 (1.49->1.76) | +189 |
| Pontmont | 341 | 0.09 | 0.80 (78/turn) | beer 55 (3.46->4.41), gold ore 1 (150.15->188.1), bread 154 (2.52->2.94), thread 34 (4.78->5.46) | jewellery 1 (81.9->103.55), windows 1 (693->712.5), cloth 13 (7.88->8.55), garments 2 (25.62->26.6) | +188 |
| Etallaen | 774 | 0.20 | 1.00 (98/turn) | beer 28 (3.46->6.22), bread 81 (2.52->3.74), charcoal 10 (3.32->6.32), clay 1 (4.91->19) | flax fibres 5 (4.94->7.2), thread 7 (4.73->5.15), bricks 0 (9.77->15.67), candles 0 (81.9->84.5) | +163 |
| Disscester | 1474 | 0.56 | 0.10 (10/turn) | gold ore 1 (150.15->168.15) | sails 1 (824.25->969), windows 1 (703.5->712.5), hinges 1 (46.41->48.92) | +161 |

**Best:** Grandgues at about +211 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 9 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 6 = 1.5 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 25.8) |
| grain | 0 @ 3.7, stop 34 |  | goal planner: buys 0 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.3k (cash + stock at home prices); +91/turn over 6 turns, +170/turn over 24 turns.
- Limits: cash flow >= -322/turn, prestige >= -0.18/turn (values are after 200 tax a turn).
- Today's settings: value +76/turn, cash +45/turn, prestige -1.93/turn - breaks the prestige floor.
- Plan: value +0/turn, cash +4/turn, prestige -0.18/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +74 vs +68, -635 vs +63, +88 vs +49 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +11/turn
  - ship Flax Wyrm -> Essenbrucke: +2/turn
  - net maker 0.00 -> 0.29: +8/turn
  - flax farm 1 4.64 -> 5.28: -5/turn
  - retting pit 1 0.91 -> 1.03: +3/turn
  - spinnery 1 1.65 -> 1.82: +5/turn
  - sewing shop 1 0.30 -> 0.36: -7/turn
  - weavery 1 0.50 -> 0.60: +10/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.14: -12/turn
  - ropewalk 1 0.25 -> 0.00: +25/turn
- Model check over the last 59 turns: predicted +105/turn for the settings we ran, real +60/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.53, thread 3.84, cloth 6.14, flax fibres 4.55, garments 17.76, nets 27.88, beer 2.73, timber 3.26, prestige 63.06, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.14, worth +10/turn.
- Ship linen snake: Grandgues -> Gosschweig (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Essenbrucke (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +76/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1752 coin: +3/turn, payback 679 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 28/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 6.2 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.36 (ask 3.3, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.04; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: flax fibres buy not filling: bid 5.05 under the home ask 7.2 for 6 turns, bought 0.0 of 1, 27.7 held (1.0 turns); raise needs Taylor (ceiling None)
