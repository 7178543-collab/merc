# v2 shadow report

Turn 14040, 2026-11-15 09:12. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,158, prestige 3,592 (472 free, -3.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 15 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 1 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 22.6 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 30, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 484 | 0 | 80 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 35 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (15.0/turn) but there is NO buy order, stock 0.0 -> v2: add buy 30
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 2.30 x1, yet 0 bought last turn); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.9 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 80 labour expired last turn (~134 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 12.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

361 turns left: prestige gained now converts 83.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 3 (pies) | mansion | 8 | 55.1 | 55.1 | thin at home: pasties, hop beer, pies |
| jousting 3 | arena | 230 | 54.7 | 55.1 | needs a arena (build cost 25,877); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 55.6 | 55.6 | thin at home: pasties, wine, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 56.3 | 56.3 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 56.8 | 56.8 | thin at home: hop beer, wine, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 57.4 | 57.4 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 57.7 | 57.7 | thin at home: hop beer, cured fish |
| hold banquet 4 (premium) | mansion | 20 | 59.8 | 59.8 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 | mansion | 17.5 | 60.3 | 60.3 | thin at home: wine, hop beer, stockfish |
| jousting 2 | arena | 210 | 60.0 | 60.4 | needs a arena (build cost 25,877); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 58.4 | 61.5 | needs a cathedral (build cost 270,090); thin at home: jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 13.4, pasties buy 4 @ 14.9; crew 0.2; est +254 a turn; stock: furniture 20 @ 13.4 (keep 145); stock: pasties 4 @ 14.9 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Chatgnan +504, Vauxvais +404, Bordees +342, Essenbrucke +299, Toqueque +293
- Chatgnan would trade: furniture buy 41 @ 13.5, pasties buy 7 @ 16.4; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (97/turn) | timber 33 (7.88->12.35), firewood 32 (2.42->5.7), bread 160 (2.35->2.66), charcoal 19 (2.56->4.16) | cloth 5 (8.82->9.95), coats 1 (72.98->78.38), thread 10 (5.51->5.8), garments 2 (23.94->24.2) | +263 |
| Darmwald | 1022 | 0.36 | 0.80 (86/turn) | charcoal 19 (2.56->9.12), tools 19 (6.3->7.08), dyed cloth 5 (14.18->15.67), lead ore 3 (7.98->11.69) | cloth 24 (7.35->9.95), thread 36 (4.77->5.8), garments 2 (20.79->24.2), tar 6 (10.45->11.4) | +189 |
| Vauxvais | 204 | 0.06 | 1.00 (107/turn) | beer 55 (3.46->4.29), firewood 49 (2.42->4.94), charcoal 17 (2.56->4.75), wax 3 (26.25->27.17) | thread 10 (4.73->5.8), flax fibres 6 (5.35->6.65), garments 1 (23.1->24.2), logs 0 (4.43->7.22) | +137 |
| Fontaux | 411 | 0.12 | 1.00 (107/turn) | charcoal 12 (2.56->5.65), timber 12 (7.88->11.78), firewood 16 (2.42->7.03), bricks 4 (6.72->11.11) | thread 32 (5.04->5.8), flax fibres 6 (5.35->6.65), belts 0 (27.51->31.73) | +122 |
| Birkeningen | 1006 | 0.35 | 0.20 (21/turn) | garments 10 (23.6->34.2), arms 7 (30.66->33.25), tools 14 (6.3->6.79), nets 6 (36->36.86) | chisels 1 (9.29->9.88), seeds 1 (1.88->2.58) | +120 |

**Best:** Grandgues at about +263 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 30 @ 3.46, stop 60 | off | a building is stalled on beer: no sell until it runs again |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 27.2, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 10 @ min 23.0 |  |
| grain | 9 @ 3.7, stop 33 |  | goal planner: buys 9 a turn for today's rates, keeps up to 33 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 35.0 |  |
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
| flax | 11 | 4.64 | 4.37 |
| ret | 3 | 0.91 | 0.87 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 105/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 39 @ 3.36 (ask 3.3, cap 14.4))
- R1: cured meat slot dry: 6.8 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 27.2, home ask 26.6; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 1.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.3; our bid is already at/over the ask (sellers too thin)
- R1: prestige rate -3.08 a turn vs 12-turn median -0.49; likely: dry slot: beer, cured meat, firewood; mansion 1 projected 0 (beer)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
