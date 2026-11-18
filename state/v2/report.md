# v2 shadow report

Turn 14110, 2026-11-18 07:25. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,827, prestige 3,623 (503 free, +46.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 12 | 0 | 0 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 509 | 0 | 20 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (4 @ 2.4), but the home ask 2.70 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 20 labour expired last turn (~35 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 84.00 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 526, not 626

## Prestige spending, cheapest coin per prestige first

291 turns left: prestige gained now converts 76.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.1 | 52.6 | needs a arena (build cost 27,084); thin at home: swords, protection, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.4 | 53.4 | running |
| jousting 2 | arena | 210 | 57.1 | 57.6 | needs a arena (build cost 27,084); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.7 | 58.7 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 60.9 | 60.9 |  |
| hold mass 2 (premium) | cathedral | 360 | 56.4 | 61.2 | needs a cathedral (build cost 294,940); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 62.5 | 62.5 | thin at home: wine, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 63.7 | 63.7 | thin at home: wine |
| hold banquet 4 (premium) | mansion | 20 | 65.1 | 65.1 | thin at home: hop beer, wine, ham, stockfish, premium ham |
| hold banquet 2 (pies) | mansion | 7 | 65.2 | 65.2 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 65.8 | 65.8 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 66.4 | 66.4 | thin at home: hop beer, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 21 | 134102075 | 0.344 | - | furniture 20, pasties 2 | -322 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.024 | - | candles 3 | -234 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: candles buy 3 @ 78.0, furniture buy 20 @ 14.6, pasties buy 1 @ 16.3; crew 0.2; est +251 a turn; stock: candles 3 @ 78.0 (keep 12); stock: furniture 20 @ 14.6 (keep 145); stock: pasties 1 @ 16.3 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Clairlond +311, Dortgart +292, Fulkirch +263, Cobholme +261, Disscester +253
- Clairlond would trade: candles buy 4 @ 78.0, furniture buy 24 @ 13.4, pasties buy 8 @ 16.4; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.41 | 0.40 (46/turn) | swords 3 (291.9->374.3), looms 1 (593.25->655.5), honey 9 (9.35->13.21), lead ore 6 (5.35->10.45) | spinning wheels 1 (243.6->266), wax 9 (25.41->27.74), flax fibres 14 (5.62->7.25), ham 2 (130.2->134.9) | +448 |
| Grandgues | 152 | 0.05 | 1.00 (114/turn) | timber 37 (7.88->12.44), firewood 30 (2.84->5.89), charcoal 17 (2.94->4.99), bread 146 (2.5->2.83) | bricks 7 (7.3->11.78), dyed cloth 1 (10.08->14.91), hop beer 2 (9.82->11.3), cloth 3 (10.19->10.9) | +323 |
| Chatgnan | 728 | 0.22 | 0.30 (34/turn) | looms 1 (593.25->817), tools 17 (6.25->8.88), medicine 1 (144.9->150.1) | tin ingots 1 (18.27->28.5), bricks 4 (5.93->11.78), cloth 10 (10.61->10.9), thread 9 (5.46->5.75) | +282 |
| Fontaux | 411 | 0.12 | 0.90 (102/turn) | beer 66 (4.03->5.75), timber 36 (7.88->11.69), salt 4 (5.25->7.79), furniture 7 (15.96->17) | ham 2 (127.05->134.9), spinning wheels 1 (252->266), bricks 7 (8.77->11.78), flax fibres 1 (5.08->7.25) | +219 |
| Heilegg | 826 | 0.26 | 0.50 (57/turn) | looms 1 (593.25->693.5), wrought iron 7 (18.59->23.75), lead ore 5 (5.35->8.6), malt 2 (6.83->9.69) | ham 2 (128.1->134.9), spinning wheels 1 (252->266), wax 7 (26.04->27.74), cookware 4 (21.63->23.37) | +202 |

**Best:** Kirchwerp at about +448 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 5 @ 4.02, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.3 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 12 @ min 21 | goal planner: sells 12 at 21 (v2 had 12 at 28.0) |
| grain | 0 @ 3.7, stop 6 |  | goal planner: buys 0 a turn for today's rates, keeps up to 6 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 26) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 74.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.4/turn (ropewalk 1), makes 0.0, holds 1 = 1.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.8k (cash + stock at home prices); -227/turn over 6 turns, +63/turn over 24 turns.
- Limits: cash flow >= -368/turn, prestige >= -0.84/turn (values are after 200 tax a turn).
- Today's settings: value +127/turn, cash +86/turn, prestige +45.97/turn.
- Plan: value +481/turn, cash +247/turn, prestige +37.97/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -5 vs +82, +70 vs +82, -716 vs +79 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Dortgart: +4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - park 1 16.00 -> 0.00: +51/turn
  - flax farm 1 4.64 -> 8.28: +29/turn
  - retting pit 1 0.91 -> 1.63: +45/turn
  - net maker [make nets 1] 0.00 -> 0.38: +21/turn
  - weavery 1 0.50 -> 1.40: +6/turn
  - spinnery 1 1.65 -> 2.84: +171/turn
  - brewery 1 0.14 -> 0.03: +25/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.31: -28/turn
- Model check over the last 60 turns: predicted +125/turn for the settings we ran, real +36/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.22, thread 3.08, cloth 4.91, flax fibres 3.66, garments 14.18, nets 23.00, beer 2.81, timber 3.38, prestige 0.00, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); grain buy 2 (v2 0); labour buy 29 (v2 26); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.31, worth +29/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +16/turn.
- Ship linen snake: Grandgues -> Dortgart (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +61/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~5433 coin: +6/turn, payback 861 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 6.5/turn (+0.0 exported); plan makes 33.2 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 435 (+146 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.81 |
| ret | 3 | 0.91 | 0.96 |
| spin | 4 | 1.65 | 1.70 |
| weave | 3 | 0.50 | 1.30 |
| sew | 2 | 0.30 | 0.81 |

Buffers: flax fibres 78/78, thread 1050/230, cloth 73/130

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.7; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
