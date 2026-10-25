# v2 shadow report

Turn 13540, 2026-10-25 13:13. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,806, prestige 3,564 (444 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 0 | 5 | 1 | 0 | buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 63 | 28 | 19 | 0 | 0 | stop 110, buy 28, buy @ 3.7 |
| labour | 85 | 85 | 531 | 0 | 54 | buy 85, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 33.6 |
| porterage | 14 | 14 | 14 | 0 | 0 | buy 14, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.81 x3, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **wax**: net maker152202386007001 ran short of wax (buy is live (1 @ 23.6), home ask 20.40 x5, yet 0 bought last turn); labour need rises ~17/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 54 labour expired last turn (~85 coin): holding 85 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax plants**: flax plants buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201
- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 98 over real use lately; planning 554, not 652
- labour expiry guard: 54 bought labour expired last turn, buy 32 (not 54) this turn

## Prestige spending, cheapest coin per prestige first

861 turns left: prestige gained now converts 98.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 47.4 | 47.4 | thin at home: hop beer, pies |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 48.3 | 48.3 | thin at home: hop beer, wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 49.8 | 49.8 | thin at home: hop beer, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 49.9 | 49.9 | thin at home: wine, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 50.8 | 50.8 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 51.5 | 51.5 | thin at home: wine, cured fish |
| hold banquet 4 | mansion | 17.5 | 51.8 | 51.8 | thin at home: wine, hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 51.8 | 51.8 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 52.6 | 52.6 | thin at home: wine |
| jousting 3 | arena | 230 | 53.1 | 53.3 | needs a arena (build cost 23,220); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 50.7 | 53.4 | needs a chapel (build cost 29,005) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -9 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Orlesailles | 1178 | 0.41 | 0.50 (49/turn) | thread 35 (4.66->6.27), cured fish 5 (22.68->24.32), nails 5 (5.57->6.79), hides 1 (14.6->18.62) | acid 1 (123.9->139.65), gears 2 (56.18->58.42), fleece 1 (5.72->6.41) | +66 |
| Marmont | 638 | 0.17 | 0.20 (20/turn) | beer 34 (3.12->4.89), malt 1 (4.98->6.41), garments 1 (17.9->18.43), medicine 1 (144.9->145.35) | looms 1 (525->536.75), grain 18 (2.29->2.74) | +62 |
| Fontaux | 411 | 0.11 | 0.30 (30/turn) | cheese 10 (5.99->9.79), glass ingots 2 (59.85->67.45), furniture 11 (11.65->12.92), charcoal 11 (1.97->3.1) | flax fibres 11 (5.35->5.65) | +61 |
| Calange | 218 | 0.06 | 0.10 (10/turn) | coats 2 (78.23->80.75), tools 9 (4.38->4.71), furniture 12 (11.65->11.97), malt 1 (4.98->5.65) | spinning wheels 1 (193.2->214.7), acid 1 (120.75->139.65), flax fibres 6 (4.94->5.65), thread 7 (4.62->4.88) | +50 |
| Neuborn | 780 | 0.20 | 0.40 (39/turn) | charcoal 11 (1.97->4.75), furniture 12 (11.65->13.49), tools 16 (4.38->4.73), bricks 1 (4.09->8.55) | soap 1 (61.43->72.2), jewellery 2 (85.58->89.77), flax fibres 12 (4.94->5.65) | +49 |

**Best:** Orlesailles at about +66 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| candles | 2 @ 67, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 0 @ 2.4, stop 13 |  | uses 6.3/turn (household upkeep), makes 6.5, holds 6 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 11.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 28 @ 3.7, stop 111 |  | goal planner: buys 28 a turn for today's rates, keeps up to 111 (v2 had 55) |
| labour | 55 @ 2.2, stop - |  | goal planner: buys 55 for today's rates (v2 had 32) |
| light armour | 1 @ 87, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 10 @ min 33.6 | goal planner: sells 10 at 33.6 (v2 had 9 at 34.0) |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 14) |
| rope |  | 1 @ min 70.5 |  |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| thread |  | 14 @ min 4.5 | goal planner: sells 14 a turn at 4.5, keeps 169 (no one offered it) |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (retting pit 1), makes 0.0, holds 200 = 74.7 turns |
| varnish | 1 @ 21.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 1 = 3.6 turns |
| wax | 1 @ 21.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.7k (cash + stock at home prices); -18/turn over 6 turns, +35/turn over 24 turns.
- Limits: cash flow >= +8/turn, prestige >= -0.60/turn (values are after 240 tax a turn).
- Today's settings: value -15/turn, cash -49/turn, prestige -0.57/turn - breaks the cash floor.
- Plan: value +73/turn, cash +89/turn, prestige -0.60/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +351 vs +99, +552 vs +130, +472 vs +136.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +4/turn
  - ship Flax Wyrm -> Dedlowe: +1/turn
  - ropewalk 1 0.25 -> 1.00: +41/turn
  - spinnery 1 1.59 -> 2.38: +17/turn
  - logging camp w/ tool 5.00 -> 4.77: +0/turn
  - flax farm 1 6.29 -> 6.56: -2/turn
  - net maker 0.73 -> 0.00: -35/turn
  - net maker [make nets 2] 0.00 -> 0.90: +54/turn
- Model check over the last 45 turns: predicted +97/turn for the settings we ran, real +55/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 3.89, cloth 6.26, flax fibres 4.48, garments 18.20, nets 28.94, beer 2.82, timber 2.95, prestige 53.51, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cured meat buy 1 (v2 2); furniture buy 2 (v2 None); grain buy 28 (v2 55); labour buy 55 (v2 32); light armour buy 1 (v2 None); nets sell 10 (v2 9); pasties buy 3 (v2 4); thread sell 14 (v2 none)
- Recipe: net maker make nets 3 -> make nets 2 at 0.90, worth +19/turn.
- Ship linen snake: Grandgues -> Vauxvais (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Dedlowe (+1/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot ropewalk 1 for ~2738 coin: +7/turn, payback 407 turns, doesn't pay yet
- Trim: donate quarry 1: +20/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +17/turn (tax 20 saved).
- Trim: donate weavery 1: +12/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 3.8/turn (+0.0 exported); plan makes 32.0 garments a turn.
Labour: own 500, everything else 408, chain may buy 350 -> chain allowance 442, chain plan 441 (+194 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.29 | 5.16 |
| ret | 3 | 1.12 | 0.92 |
| spin | 4 | 1.59 | 1.89 |
| weave | 3 | 0.13 | 1.25 |
| sew | 2 | 0.09 | 0.78 |

Buffers: flax fibres 65/85, thread 760/249, cloth 0/125
- chain plan needed 443 labour, budget left 442: cut to 442 (sewing capped at 0.78)

## Self-diagnosis

Nothing found this run.
