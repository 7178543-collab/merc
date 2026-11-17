# v2 shadow report

Turn 14091, 2026-11-17 12:14. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,916, prestige 3,624 (504 free, -3.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 5, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.74 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.74 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 610

## Prestige spending, cheapest coin per prestige first

310 turns left: prestige gained now converts 78.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.0 | 51.4 | needs a arena (build cost 28,343); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| jousting 2 | arena | 210 | 55.8 | 56.3 | needs a arena (build cost 28,343); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.3 | 57.3 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 58.9 | 58.9 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 60.1 | 60.1 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 61.5 | 61.5 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 62.0 | 62.0 | thin at home: hop beer |
| hold banquet 1 (meat) | mansion | 4.2 | 62.2 | 62.2 |  |
| hold banquet 4 (pies) | mansion | 18 | 62.6 | 62.6 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 63.1 | 63.1 | thin at home: hop beer, stockfish, premium ham |
| hold banquet 2 (pies) | mansion | 7 | 64.1 | 64.1 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 17 @ 14.6, pasties buy 3 @ 15.9; crew 0.2; est +187 a turn; stock: furniture 17 @ 14.6 (keep 145); stock: pasties 3 @ 15.9 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +688, Hofkirchen +513, Gotthafen +456, Fulkirch +394, Chatgnan +370
- Amsdermund would trade: furniture buy 63 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (101/turn) | firewood 37 (2.88->7.08), timber 27 (8.45->12.54), bread 160 (2.52->3.13), charcoal 19 (3.02->5.03) | bricks 3 (10.71->13.01), tools 24 (6.3->6.51), candles 1 (87.67->89.5), cloth 2 (10.08->11.1) | +325 |
| Brebronn | 862 | 0.28 | 0.20 (23/turn) | cloth 1 (9.9->10.26), malt 1 (6.98->7.65) | tapestries 2 (672->798), flax fibres 5 (5.57->7.65), yarn 12 (4.62->5.42), candles 1 (85.58->89.5) | +261 |
| Amsdermund | 1111 | 0.43 | 0.60 (68/turn) | beer 65 (3.93->5.32), chisels 5 (11.55->14.25), leather 1 (29.61->30.59) | cloth 24 (5.72->11.1), tools 24 (4.83->6.51), dyed cloth 7 (12.6->15.67), garments 2 (26.25->33.6) | +254 |
| Calange | 218 | 0.07 | 0.30 (34/turn) | bread 160 (2.52->2.81), tiles 1 (3.86->9.88), rope 1 (80->84.55), raw cloth 3 (10.19->11.21) | tapestries 1 (635.25->798), spinning wheels 1 (214.2->222.3), bricks 2 (8.4->13.01), candles 1 (85.58->89.5) | +212 |
| Toqueque | 642 | 0.19 | 0.30 (34/turn) | tackles 2 (174.3->175.75), cloth 1 (9.9->10.54) | tapestries 1 (609->798), garments 2 (28.35->33.6), bricks 4 (7.46->13.01), wine 12 (6.46->7.22) | +211 |

**Best:** Grandgues at about +325 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 1 @ 3.92, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 10 = 7.1 turns |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 31.0) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.8k (cash + stock at home prices); +144/turn over 6 turns, +115/turn over 24 turns.
- Limits: cash flow >= -288/turn, prestige >= -0.85/turn (values are after 200 tax a turn).
- Today's settings: value +105/turn, cash +84/turn, prestige -3.23/turn - breaks the prestige floor.
- Plan: value -4/turn, cash +2/turn, prestige -0.85/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +14 vs +89, +2 vs +74, +179 vs +95.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +9/turn
  - ship Flax Wyrm -> Hofkirchen: +1/turn
  - spinnery 1 1.65 -> 1.57: +5/turn
  - net maker 0.00 -> 0.28: +4/turn
  - flax farm 1 4.64 -> 4.78: -1/turn
  - weavery 1 0.50 -> 0.59: -8/turn
  - sewing shop 1 0.30 -> 0.36: +11/turn
  - mansion 1 0.00 -> 0.57: -133/turn
- Model check over the last 60 turns: predicted +80/turn for the settings we ran, real +16/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.77, thread 4.45, cloth 7.10, flax fibres 5.27, garments 20.55, nets 32.09, beer 3.17, timber 3.46, prestige 61.34, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Amsdermund (+15/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Hofkirchen (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 86/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy 5 @ 3.56, home ask 3.74 -> **buy 9 @ 3.8 (ask 3.74, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.74; ask over the cap 2.1 (60 coin per prestige)
