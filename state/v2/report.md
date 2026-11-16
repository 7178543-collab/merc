# v2 shadow report

Turn 14065, 2026-11-16 10:27. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,707, prestige 3,647 (527 free, -3.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 514 | 0 | 15 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.92 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.92 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 15 labour expired last turn (~27 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 521, not 621

## Prestige spending, cheapest coin per prestige first

336 turns left: prestige gained now converts 81.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.1 | 50.5 | needs a arena (build cost 27,656); thin at home: swords, protection, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| jousting 2 | arena | 210 | 54.8 | 55.3 | needs a arena (build cost 27,656); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.7 | 57.7 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 61.3 | 61.3 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 62.0 | 62.0 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 63.3 | 63.3 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 63.3 | 63.3 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 63.9 | 63.9 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 64.1 | 64.1 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 60.3 | 64.3 | needs a cathedral (build cost 312,585); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 64.4 | 64.4 | thin at home: hop beer, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 21 | 134102075 | 0.36 | - | candles 2, furniture 21, pasties 1 | -472 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.7 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.1 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- best towns now: Brunnham +60, Bremcop +46, Clairlond +42, Boistot +41, Bedenis +40
- Brunnham would trade: candles buy 4 @ 73.0, pasties buy 1 @ 15.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (86/turn) | timber 35 (8.09->12.44), firewood 35 (3.07->6.41), charcoal 19 (3.07->5.42), flour 2 (17.01->19.57) | garments 2 (24.57->27.4), tools 8 (5.41->6.03), cloth 4 (8.29->9.25), leather 1 (28.56->29.64) | +262 |
| Hofkirchen | 991 | 0.34 | 0.90 (97/turn) | nails 6 (8.56->10.83), lead ore 1 (7.56->13.59), flour 2 (17.01->21.09), rope 1 (72.5->74.58) | jewellery 12 (84->86.92), cloth 24 (7.82->9.25), thread 62 (4.87->5.5), ploughs 6 (77.7->83.12) | +158 |
| Boistot | 1230 | 0.48 | 0.30 (32/turn) | swords 2 (256.2->309.7), flour 1 (17.01->25.46), rope 1 (72.5->76.95), steel ingots 7 (19.74->20.71) | cloth 24 (7.98->9.25), bellows 1 (241.5->252.7), thread 27 (4.77->5.5), salt 5 (4.62->5.56) | +154 |
| Birkeningen | 1006 | 0.35 | 0.60 (65/turn) | beer 52 (3.65->5.65), tapestries 1 (771.75->798), garments 10 (26.6->28.12), fleece 2 (8.03->13.3) | thread 4 (4.77->5.5), cookware 5 (23.73->24.13) | +121 |
| Fontaux | 411 | 0.12 | 1.00 (108/turn) | firewood 15 (3.07->8.31), beer 39 (3.65->4.52), charcoal 11 (3.07->5.79), flour 1 (17.01->30.59) | cloth 5 (7.93->9.25), resin 5 (3.07->3.42) | +114 |

**Best:** Grandgues at about +262 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.4) |
| grain | 0 @ 3.7, stop 22 |  | goal planner: buys 0 a turn for today's rates, keeps up to 22 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 21) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 70.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 1 = 1.9 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.4k (cash + stock at home prices); -498/turn over 6 turns, -94/turn over 24 turns.
- Limits: cash flow >= -154/turn, prestige >= -0.95/turn (values are after 200 tax a turn).
- Today's settings: value +76/turn, cash +48/turn, prestige -3.35/turn - breaks the prestige floor.
- Plan: value -14/turn, cash -4/turn, prestige -0.95/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -268 vs +28, -160 vs +33, -282 vs +45 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +9/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - ropewalk 1 0.25 -> 0.15: +13/turn
  - net maker 0.00 -> 0.28: +10/turn
  - spinnery 1 1.65 -> 1.46: +5/turn
  - flax farm 1 4.64 -> 4.57: +0/turn
  - sewing shop 1 0.30 -> 0.39: -11/turn
  - weavery 1 0.50 -> 0.62: +16/turn
  - mansion 1 0.00 -> 0.57: -134/turn
- HAND-OVER: goal planner: model check failed 3 runs in a row, rates handed back to the old rules.
- Model check over the last 59 turns: predicted -53/turn for the settings we ran, real -125/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.74, thread 4.37, cloth 6.98, flax fibres 5.18, garments 20.20, nets 31.51, beer 3.24, timber 3.31, prestige 61.64, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 21); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Brunnham (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 11.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 419 (+130 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.10 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.29 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 125/78, thread 1050/228, cloth 73/129

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.48 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.54 (ask 3.48, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.92; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
