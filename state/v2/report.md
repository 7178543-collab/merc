# v2 shadow report

Turn 14041, 2026-11-15 10:18. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,041, prestige 3,589 (469 free, -3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 15 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 1 | 1 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 23 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 33, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 484 | 0 | 80 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 35 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (15.0/turn) but there is NO buy order, stock 0.0 -> v2: add buy 30
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.76 is above it); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.76 is above our ceiling 2.40 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 2 (need 5) -> v2: buy 5
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.00 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 80 labour expired last turn (~133 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 12.00 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 490, not 590

## Prestige spending, cheapest coin per prestige first

360 turns left: prestige gained now converts 83.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| jousting 3 | arena | 230 | 54.2 | 54.5 | needs a arena (build cost 25,861); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.3 | 56.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 57.2 | 57.2 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 58.5 | 58.5 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 58.8 | 58.8 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 59.4 | 59.4 | thin at home: wine, cured fish, cheese |
| jousting 2 | arena | 210 | 59.3 | 59.7 | needs a arena (build cost 25,861); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 61.3 | 61.3 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 58.4 | 61.5 | needs a cathedral (build cost 270,160); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 62.1 | 62.1 | thin at home: hop beer, cured fish, cheese |
| hold banquet 4 | mansion | 17.5 | 62.2 | 62.2 | thin at home: wine, hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 14.2, pasties buy 4 @ 14.9; crew 0.2; est +251 a turn; stock: furniture 21 @ 14.2 (keep 145); stock: pasties 4 @ 14.9 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Friedwerp +619, Vauxvais +408, Brebronn +397, Toqueque +296, Essenbrucke +296
- Friedwerp would trade: furniture buy 51 @ 13.8, pasties buy 6 @ 14.0; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | timber 42 (7.88->12.35), bread 160 (2.35->2.81), firewood 31 (2.9->5.79), medicine 1 (135.45->160.55) | candles 1 (86.1->92), spinning wheels 1 (260.4->266), cloth 5 (8.98->9.5), cured meat 3 (25.2->25.84) | +346 |
| Darmwald | 1022 | 0.35 | 0.80 (85/turn) | charcoal 19 (2.6->9.5), premium ham 1 (249.9->269.8), tools 18 (6.51->7.31), dyed cloth 4 (14.38->16.15) | garments 21 (21->23.94), cloth 24 (7.35->9.5), spinning wheels 1 (243.6->266), thread 26 (4.16->5.05) | +260 |
| Marmont | 638 | 0.18 | 0.10 (11/turn) | medicine 1 (135.45->140.6), limestone 1 (16.8->26.6), premium ham 1 (249.9->252.7), raw cloth 2 (6.41->7.41) | sails 1 (834.75->988), acid 1 (118.65->130.15), candles 1 (86.1->92), chisels 1 (7.25->9.88) | +184 |
| Hanbrücken | 531 | 0.15 | 0.70 (74/turn) | timber 19 (7.88->11.49), premium ham 1 (249.9->264.1), charcoal 16 (2.6->4.1), bricks 3 (5.25->9.59) | spinning wheels 1 (206.85->266), tapestries 1 (593.25->650.75), candles 1 (87.67->92), cloth 10 (8.98->9.5) | +177 |
| Gotthafen | 964 | 0.32 | 0.30 (32/turn) | looms 1 (588->660.25), arms 4 (32.13->40.28), premium ham 1 (249.9->273.6), cloth 1 (6.64->7.41) | ploughs 4 (73.5->83.12), butter 1 (68.78->81.7), candles 1 (82.95->92), cloth 13 (8.93->9.5) | +176 |

**Best:** Grandgues at about +346 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 30 @ 3.46, stop 60 | off | a building is stalled on beer: no sell until it runs again |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 27.8, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 3 @ 2.4, stop 9 |  | goal planner: buys 3 a turn for today's rates, keeps up to 9 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 10 @ min 24.6 |  |
| grain | 8 @ 3.7, stop 31 |  | goal planner: buys 8 a turn for today's rates, keeps up to 31 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 35.2 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (shadow)
- no plan: goal plan failed: AttributeError: 'str' object has no attribute 'get'

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.35 |
| ret | 3 | 0.91 | 0.87 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 107/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 39 @ 3.36 (ask 3.3, cap 14.4))
- R1: cured meat slot dry: 8.8 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 27.8, home ask none (no sellers at home)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 3 @ 2.4, home ask 2.76; ask over the cap 2.1 (60 coin per prestige)
- R1: prestige rate -3.02 a turn vs 12-turn median -0.50; likely: dry slot: beer, cured meat, firewood; mansion 1 projected 0 (beer)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
