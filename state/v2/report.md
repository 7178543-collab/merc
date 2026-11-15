# v2 shadow report

Turn 14044, 2026-11-15 13:35. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,373, prestige 3,580 (460 free, -3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 9 | 0 | 0 | 0 | 0 | min_holding 60, sell 5, sell @ 3.26; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 51 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 24.6 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 30, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 35.2 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.96 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.96 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.90 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~77 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.90 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 490, not 590

## Prestige spending, cheapest coin per prestige first

357 turns left: prestige gained now converts 83.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| jousting 3 | arena | 230 | 54.4 | 54.8 | needs a arena (build cost 26,040); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 56.6 | 56.6 | thin at home: pasties, hop beer, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 57.3 | 57.3 | thin at home: pasties, candles |
| hold banquet 4 (pies) | mansion | 18 | 57.8 | 57.8 | thin at home: pasties, hop beer, stockfish, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 59.3 | 59.3 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 59.5 | 59.5 | thin at home: hop beer, cured fish |
| jousting 2 | arena | 210 | 59.6 | 60.0 | needs a arena (build cost 26,040); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.6 | 60.6 | thin at home: hop beer, stockfish, candles |
| hold banquet 4 | mansion | 17.5 | 61.4 | 61.4 | thin at home: hop beer, stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 58.4 | 61.6 | needs a cathedral (build cost 270,510); thin at home: jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 14.1, garments sell 11 @ 23.6, pasties buy 4 @ 14.9; crew 0.2; est +271 a turn; stock: furniture 21 @ 14.1 (keep 145); stock: pasties 4 @ 14.9 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Amsdermund +591, Bedenis +428, Vauxvais +399, Bordees +358, Disscester +339
- Amsdermund would trade: furniture buy 54 @ 13.7; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | timber 41 (7.88->12.54), bread 146 (2.33->2.79), firewood 30 (3.11->5.37), charcoal 17 (2.67->4.27) | acid 0 (137.55->148.2), tools 7 (4.66->5.42), yarn 3 (5.08->6.7), garments 1 (24.36->24.6) | +321 |
| Kirchwerp | 1072 | 0.38 | 0.40 (42/turn) | glassware 5 (106.05->142.5), nets 6 (36.2->37.62), arms 6 (32.34->33.25), honey 6 (8.35->8.84) | ploughs 5 (73.5->83.12), acid 1 (131.25->148.2), yarn 10 (4.91->6.7), cloth 24 (7.56->8.35) | +265 |
| Fontaux | 411 | 0.12 | 1.00 (106/turn) | garments 7 (21.8->30.4), charcoal 12 (2.67->6.13), timber 11 (7.88->12.06), firewood 16 (3.11->7.46) | flax fibres 6 (5.35->6.65), yarn 2 (5.19->6.7), thread 21 (5.04->5.25) | +168 |
| Dortdorf | 871 | 0.27 | 0.20 (21/turn) | cloth 1 (6.6->7.89), dyed yarn 1 (5.99->6.32) | looms 1 (577.5->688.75), yarn 16 (4.96->6.7), garments 2 (22.89->24.6), flax fibres 8 (5.88->6.65) | +133 |
| Marmont | 638 | 0.18 | 0.20 (21/turn) | garments 11 (21.8->26.41), limestone 2 (17.32->25.46), cloth 1 (6.6->8.07) | looms 1 (640.5->688.75), acid 1 (137.55->148.2), ploughs 5 (79.28->83.12), yarn 7 (5.04->6.7) | +130 |

**Best:** Grandgues at about +321 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 12 @ min 21.2 | goal planner: sells 12 (v2 had 10) |
| grain | 0 @ 3.7, stop 29 |  | goal planner: buys 0 a turn for today's rates, keeps up to 29 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 35.2 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.6k (cash + stock at home prices); -64/turn over 6 turns, -134/turn over 24 turns.
- Limits: cash flow >= -224/turn, prestige >= -0.67/turn (values are after 200 tax a turn).
- Today's settings: value +122/turn, cash +140/turn, prestige -3.01/turn - breaks the prestige floor.
- Plan: value +30/turn, cash +61/turn, prestige -0.67/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -93 vs -193, -258 vs +127, -320 vs +99 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brebronn: +1/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - net maker 0.00 -> 0.29: +12/turn
  - spinnery 1 1.65 -> 1.42: +2/turn
  - ropewalk 1 0.25 -> 0.00: +2/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.16: +10/turn
  - flax farm 1 4.64 -> 4.47: -0/turn
  - weavery 1 0.50 -> 0.58: -11/turn
  - mansion 1 0.00 -> 0.56: -129/turn
- Model check over the last 59 turns: predicted -120/turn for the settings we ran, real -82/turn.
- Worth of one more unit per turn: labour 1.69, thread 4.25, cloth 6.78, flax fibres 5.04, garments 19.62, nets 30.66, beer 3.00, timber 3.38, prestige 61.80, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 12 (v2 10); grain buy 8 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.16, worth +7/turn.
- Ship linen snake: Grandgues -> Brebronn (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +84/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3701 coin: +3/turn, payback 1220 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 9.3/turn (+0.0 exported); plan makes 31.6 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 407 (+118 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.12 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.63 |
| weave | 3 | 0.50 | 1.24 |
| sew | 2 | 0.30 | 0.77 |

Buffers: flax fibres 112/76, thread 1064/223, cloth 72/124

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.96; ask over the cap 2.1 (60 coin per prestige)
- R1: prestige rate -3.01 a turn vs 12-turn median -0.50; likely: dry slot: firewood
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
