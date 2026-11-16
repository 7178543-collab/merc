# v2 shadow report

Turn 14062, 2026-11-16 07:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,416, prestige 3,657 (537 free, +118.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 4 | 0 | 0 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 7, buy @ 3.6 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 506 | 0 | 23 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 23 labour expired last turn (~39 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 526, not 626

## Prestige spending, cheapest coin per prestige first

339 turns left: prestige gained now converts 81.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.9 | 50.3 | needs a arena (build cost 28,163); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| jousting 2 | arena | 210 | 54.6 | 55.1 | needs a arena (build cost 28,163); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 59.7 | 59.7 | thin at home: beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.0 | 60.0 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 60.2 | 60.2 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 61.7 | 61.7 | thin at home: hop beer, wine, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 62.2 | 62.2 | thin at home: wine, cured meat |
| hold banquet 3 (pies) | mansion | 8 | 62.3 | 62.3 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 62.5 | 62.5 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 58.6 | 62.5 | needs a cathedral (build cost 311,060); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 1 (meat) | mansion | 4.2 | 63.0 | 63.0 | thin at home: beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 134102075 | 0.364 | - | furniture 16, pasties 1 | -229 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.096 | - | beer 4, pasties 2 | -45 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: candles buy 2 @ 77.5, furniture buy 22 @ 13.7, pasties buy 2 @ 15.4; crew 0.2; est +290 a turn; stock: candles 2 @ 77.5 (keep 12); stock: furniture 22 @ 13.7 (keep 145); stock: pasties 2 @ 15.4 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.4 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Chatgnan +475, Amsdermund +468, Vauxvais +391, Clairas +331, Blanans +301
- Chatgnan would trade: furniture buy 42 @ 14.2, pasties buy 2 @ 16.3; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (96/turn) | timber 47 (7.72->12.54), firewood 35 (3.11->5.75), charcoal 19 (2.79->5.22), furniture 8 (11.87->15.77) | beer 74 (3.38->3.99), dyed cloth 3 (11.55->13.01), cloth 4 (8.72->9.2), resin 4 (3.32->3.42) | +363 |
| Heilegg | 826 | 0.24 | 0.60 (64/turn) | furniture 8 (11.87->16.53), charcoal 19 (2.79->6.03), garments 10 (22.6->24.7), wine 15 (6.35->7.84) | looms 1 (593.25->688.75), cloth 24 (7.35->9.2), lathes 1 (218.4->231.8), cheese 9 (5.78->6.74) | +266 |
| Nürnnieder | 520 | 0.15 | 0.30 (32/turn) | furniture 8 (11.87->13.3), leather 1 (24.99->32.3), nets 1 (34.2->36.29), wine 2 (6.35->7.08) | looms 1 (630->688.75), cloth 24 (7.35->9.2), beer 59 (3.42->3.99), salt 12 (4.75->5.56) | +142 |
| Chatgnan | 728 | 0.21 | 0.40 (43/turn) | furniture 8 (11.87->13.01), leather 1 (24.99->28.31), coats 2 (81.9->82.65) | looms 1 (572.25->688.75), beer 72 (3.34->3.99), chisels 1 (7.61->9.5), salt 6 (5.19->5.56) | +139 |
| Fontaux | 411 | 0.12 | 1.00 (106/turn) | firewood 16 (3.11->8.12), thread 30 (4.78->5.65), charcoal 11 (2.79->5.18), furniture 5 (11.87->15.2) | cloth 5 (8.09->9.2), resin 7 (2.81->3.42) | +130 |

**Best:** Grandgues at about +363 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 22.0) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 26) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 70.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.4/turn (ropewalk 1), makes 0.0, holds 1 = 1.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.0k (cash + stock at home prices); -540/turn over 6 turns, -123/turn over 24 turns.
- Limits: cash flow >= -184/turn, prestige >= -0.99/turn (values are after 200 tax a turn).
- Today's settings: value +67/turn, cash +28/turn, prestige +118.58/turn.
- Plan: value +418/turn, cash +257/turn, prestige +110.58/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -328 vs +31, -328 vs +30, -22 vs +39 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Pontmont: +0/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - park 1 16.00 -> 0.00: +49/turn
  - flax farm 1 4.64 -> 8.07: +24/turn
  - retting pit 1 0.91 -> 1.59: +42/turn
  - net maker [make nets 1] 0.00 -> 0.38: +21/turn
  - sewing shop 1 0.30 -> 0.39: +13/turn
  - weavery 1 0.50 -> 1.44: +15/turn
  - spinnery 1 1.65 -> 2.66: +148/turn
  - brewery 1 0.14 -> 0.00: +14/turn
- Model check over the last 59 turns: predicted -71/turn for the settings we ran, real -142/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.03, thread 2.60, cloth 4.14, flax fibres 3.10, garments 11.97, nets 19.41, beer 2.53, timber 3.69, prestige 0.00, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 26); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.04, worth +7/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.09, worth +11/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +22/turn.
- Ship linen snake: Grandgues -> Pontmont (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +51/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~4835 coin: +11/turn, payback 434 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 11.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 416 (+127 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.00 |
| ret | 3 | 0.91 | 0.80 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 132/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 4.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 4.28 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 4.36 (ask 4.28, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
