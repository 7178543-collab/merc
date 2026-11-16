# v2 shadow report

Turn 14055, 2026-11-16 00:26. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,269, prestige 3,553 (433 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 9 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 26, buy 9, buy @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 1 | 0 | 0 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 37 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 2.38 x10, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.9 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.70 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~76 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.70 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

346 turns left: prestige gained now converts 82.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| jousting 3 | arena | 230 | 54.7 | 55.1 | needs a arena (build cost 26,163); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.4 | 55.4 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 59.0 | 59.0 |  |
| jousting 2 | arena | 210 | 59.9 | 60.3 | needs a arena (build cost 26,163); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 60.5 | 60.5 | thin at home: pasties, hop beer, ham, stockfish, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 60.7 | 60.7 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 62.3 | 62.3 | thin at home: pasties, candles |
| hold banquet 4 (premium) | mansion | 20 | 62.4 | 62.4 | thin at home: hop beer, ham, stockfish, candles |
| hold banquet 3 (pies) | mansion | 8 | 62.8 | 62.8 | thin at home: pasties, hop beer, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 63.0 | 63.0 | thin at home: hop beer, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 63.1 | 63.1 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 22 @ 14.0, pasties buy 3 @ 13.9; crew 0.2; est +267 a turn; stock: furniture 22 @ 14.0 (keep 145); stock: pasties 3 @ 13.9 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Amsdermund +571, Chatgnan +540, Vauxvais +380, Boistot +295, Fulkirch +291
- Amsdermund would trade: furniture buy 56 @ 14.5; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | timber 46 (7.82->12.73), firewood 35 (2.5->6.32), charcoal 19 (3.04->5.18), bread 160 (2.37->2.6) | acid 1 (132.3->149.15), cheese 5 (6.67->7.17), cloth 4 (8.66->9.1), tiles 3 (3.89->4.89) | +362 |
| Calange | 218 | 0.06 | 0.50 (53/turn) | tapestries 1 (740.25->817), dyed cloth 11 (13.65->18.43), beer 99 (3.15->3.44), bread 160 (2.37->2.64) | cloth 9 (7.51->9.1), acid 1 (144.9->149.15), yarn 2 (3.19->4.31), tiles 2 (3.97->4.89) | +181 |
| Vauxvais | 204 | 0.06 | 1.00 (106/turn) | firewood 38 (2.5->5.22), bread 114 (2.37->2.75), beer 50 (3.15->3.69), charcoal 13 (3.04->4.99) | candles 6 (73.5->75.52), tools 10 (6.14->6.7), logs 0 (3.78->7.22), seeds 4 (2.16->2.58) | +139 |
| Fontaux | 411 | 0.12 | 1.00 (106/turn) | beer 56 (3.15->4.39), firewood 10 (2.5->8.36), timber 8 (7.82->11.3), charcoal 8 (3.04->5.18) | cloth 2 (8.82->9.1) | +119 |
| Hanbrücken | 531 | 0.15 | 0.70 (74/turn) | timber 25 (7.82->12.06), nets 4 (34.4->36.48), bricks 5 (5.83->9.03), steel ingots 1 (19.74->21.09) | cloth 24 (8.19->9.1), acid 1 (136.5->149.15), cheese 5 (6.67->7.17), rope 1 (71.92->74.58) | +96 |

**Best:** Grandgues at about +362 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 81.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21.2 | goal planner: sells 11 at 21.2 (v2 had 10 at 23.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.2k (cash + stock at home prices); +98/turn over 6 turns, +21/turn over 24 turns.
- Limits: cash flow >= -261/turn, prestige >= -0.56/turn (values are after 200 tax a turn).
- Today's settings: value +60/turn, cash +31/turn, prestige -2.38/turn - breaks the prestige floor.
- Plan: value +19/turn, cash +29/turn, prestige -0.56/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -262 vs +34, +136 vs +26, +187 vs +44.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Coburgbaum: +16/turn
  - ship Flax Wyrm -> Marmont: +1/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.29: +10/turn
  - ropewalk 1 0.25 -> 0.00: +10/turn
  - spinnery 1 1.65 -> 1.31: +3/turn
  - sewing shop 1 0.30 -> 0.35: +3/turn
  - weavery 1 0.50 -> 0.59: +9/turn
  - retting pit 1 0.91 -> 0.83: +2/turn
  - flax farm 1 4.64 -> 4.15: +5/turn
- Model check over the last 59 turns: predicted -110/turn for the settings we ran, real -108/turn.
- Worth of one more unit per turn: labour 1.68, thread 4.22, cloth 6.74, flax fibres 5.00, garments 19.50, nets 30.68, beer 2.98, timber 3.35, prestige 59.34, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.05, worth +3/turn.
- Ship linen snake: Grandgues -> Coburgbaum (+16/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Marmont (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3666 coin: +1/turn, payback 3653 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 9.6/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 412 (+122 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.94 |
| ret | 3 | 0.91 | 0.79 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 132/77, thread 1064/226, cloth 72/127

## Self-diagnosis

- R1: firewood slot dry: 1.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.38; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
