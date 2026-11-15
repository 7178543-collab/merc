# v2 shadow report

Turn 14049, 2026-11-15 18:02. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,018, prestige 3,568 (448 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 6 | 0 | 4 | 0 | 0 | min_holding 60, sell 5, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 42 | 0 | 2 | 0 | 0 | min_holding 30, sell 12, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 23, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 6.0 -> v2: add buy 5
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.94 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.94 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~78 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.13, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

352 turns left: prestige gained now converts 83.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| jousting 3 | arena | 230 | 55.5 | 55.9 | needs a arena (build cost 26,549); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.0 | 56.0 |  |
| hold banquet 3 (pies) | mansion | 8 | 56.3 | 56.3 | thin at home: pasties, candles |
| hold banquet 4 (pies) | mansion | 18 | 57.7 | 57.7 | thin at home: stockfish, candles |
| hold banquet 2 (pies) | mansion | 7 | 57.8 | 57.8 | thin at home: pasties, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 60.2 | 60.2 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 60.2 | 60.2 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 |  |
| jousting 2 | arena | 210 | 60.8 | 61.2 | needs a arena (build cost 26,549); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 61.6 | 61.6 | thin at home: stockfish, candles |
| hold banquet 4 (premium) | mansion | 20 | 61.7 | 61.7 | thin at home: stockfish, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 13.7, pasties buy 4 @ 14.7; crew 0.2; est +262 a turn; stock: furniture 21 @ 13.7 (keep 145); stock: pasties 4 @ 14.7 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Amsdermund +641, Chatgnan +623, Gotthafen +461, Bedenis +442, Bordees +374
- Amsdermund would trade: furniture buy 58 @ 13.7; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (85/turn) | timber 47 (7.88->12.63), firewood 33 (3.07->6.03), furniture 16 (12.08->14.25), charcoal 19 (2.71->4.58) | candles 1 (86.1->88.5), cheese 4 (6.51->7.12), garments 2 (23.73->24.6), yarn 3 (4.96->5.42) | +329 |
| Fontaux | 411 | 0.12 | 1.00 (106/turn) | thread 23 (4.98->7.27), timber 11 (7.88->12.16), furniture 8 (12.08->15.77), charcoal 11 (2.71->5.51) | flax fibres 6 (5.35->5.95), candles 0 (85.58->88.5), flax plants 10 (1.12->1.49), flour 0 (17.75->19.38) | +171 |
| Etallaen | 774 | 0.22 | 0.40 (42/turn) | garments 11 (24.4->30.97), furniture 16 (12.08->14.54), spinning wheels 2 (249.9->256.5), cloth 1 (8->10.73) | candles 1 (84->88.5), seeds 6 (1.94->2.58) | +114 |
| Briclives | 1041 | 0.36 | 0.40 (42/turn) | steel ingots 12 (19.43->24.13), furniture 16 (12.08->14.91), garments 11 (24.4->25.84), acid 1 (142.8->150.1) | cheese 4 (4.85->7.12), candles 1 (82.42->88.5) | +103 |
| Coburgbaum | 619 | 0.17 | 0.90 (95/turn) | bread 141 (2.5->3.25), furniture 12 (12.08->14.25), nets 6 (35.2->38.57), ham 2 (92.92->100.7) | flour 5 (15.02->19.38), salt 4 (4.12->4.94), candles 1 (86.1->88.5), cheese 4 (6.77->7.12) | +102 |

**Best:** Grandgues at about +329 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.24, stop 9 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 6 = 1.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 78, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat |  | 2 @ min 24 | goal planner: trial sale of an idle pile, 2 a turn at 24, keeps 0 (13 over) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 14.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21.2 | goal planner: sells 11 at 21.2 (v2 had 11 at 24.2) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34 | goal planner: sells 9 at 34 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.8k (cash + stock at home prices); -2/turn over 6 turns, -30/turn over 24 turns.
- Limits: cash flow >= -251/turn, prestige >= -0.62/turn (values are after 200 tax a turn).
- Today's settings: value +80/turn, cash +51/turn, prestige -2.45/turn - breaks the prestige floor.
- Plan: value +29/turn, cash +56/turn, prestige -0.62/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +100 vs +140, -163 vs +99, +227 vs +102.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Cobholme: +0/turn
  - ship Flax Wyrm -> Toqueque: +0/turn
  - brewery 1 0.14 -> 0.01: +22/turn
  - net maker 0.00 -> 0.27: +9/turn
  - flax farm 1 4.64 -> 4.27: -1/turn
  - retting pit 1 0.91 -> 0.85: -0/turn
  - ropewalk 1 0.25 -> 0.00: -3/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.11: +20/turn
  - weavery 1 0.50 -> 0.57: -10/turn
  - spinnery 1 1.65 -> 1.35: -7/turn
- Model check over the last 59 turns: predicted -123/turn for the settings we ran, real -91/turn.
- Worth of one more unit per turn: labour 1.71, thread 4.30, cloth 6.86, flax fibres 5.09, garments 19.85, nets 31.07, beer 3.10, timber 3.38, prestige 60.31, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat sell 2 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.11, worth +5/turn.
- Ship linen snake: Grandgues -> Cobholme (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Toqueque (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3790 coin: +2/turn, payback 1822 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 8.9/turn (+0.0 exported); plan makes 32.0 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 410 (+121 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.05 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.25 |
| sew | 2 | 0.30 | 0.78 |

Buffers: flax fibres 121/76, thread 1064/225, cloth 72/125

## Self-diagnosis

- R1: beer slot dry: 6.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.1 -> **buy 9 @ 3.16 (ask 3.1, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.94; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
