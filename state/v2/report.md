# v2 shadow report

Turn 13960, 2026-11-12 01:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,797, prestige 3,572 (452 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 10 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 34 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~76 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.13, no projection from the game)
- labour: +2 crew for linen snake (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 492, not 592

## Prestige spending, cheapest coin per prestige first

441 turns left: prestige gained now converts 89.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| jousting 3 | arena | 230 | 55.0 | 55.3 | needs a arena (build cost 28,115); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.7 | 55.7 | thin at home: wine, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 56.9 | 56.9 |  |
| hold banquet 4 | mansion | 17.5 | 58.9 | 58.9 | thin at home: wine, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 59.0 | 59.0 | thin at home: wine, ham, stockfish |
| jousting 2 | arena | 210 | 60.2 | 60.6 | needs a arena (build cost 28,115); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 61.1 | 61.1 |  |
| hold banquet 3 (pies) | mansion | 8 | 61.5 | 61.5 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 61.6 | 61.6 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 62.2 | 62.2 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 63.1 | 63.1 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 24 @ 14.6, pasties buy 3 @ 15.7; crew 0.1; est +282 a turn; stock: furniture 24 @ 14.6 (keep 145); stock: pasties 3 @ 15.7 (keep 14)
- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 14.0, pasties buy 3 @ 12.5; crew 0.2; est +246 a turn; stock: furniture 20 @ 14.0 (keep 145); stock: pasties 3 @ 12.5 (keep 14)
- best towns now: Heidlowe +285, Grandgues +282, Brebronn +277, Amsdermund +275, Marmont +260
- Heidlowe would trade: furniture buy 24 @ 14.5, pasties buy 7 @ 14.4; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.34 | 0.20 (22/turn) | candles 2 (90.3->216.6), lead bars 8 (15.23->20.71), flax fibres 9 (5.16->8.26), garments 10 (19.07->20.14) | cloth 11 (8.29->10.26), belts 6 (32.13->35.53), flour 3 (17.12->23.94), cookware 4 (26.04->28.12) | +390 |
| Darmwald | 1022 | 0.36 | 0.80 (86/turn) | beer 90 (3.68->5.84), garments 10 (19.07->23.56), lead ore 3 (9.13->13.59), wine 3 (6.25->8.46) | cloth 11 (8.93->10.26), cookware 4 (27.09->28.12), resin 1 (3.4->6.41) | +200 |
| Essenbrucke | 584 | 0.17 | 0.40 (43/turn) | beer 29 (3.68->5.65), garments 10 (19.07->22.04), dyed cloth 8 (11.55->14.82), lead ore 6 (9.13->12.54) | thread 12 (3.42->5.55), cloth 4 (8.14->10.26), cookware 4 (26.88->28.12), cheese 4 (8.61->9.17) | +162 |
| Neuborn | 780 | 0.23 | 1.00 (108/turn) | timber 28 (7.35->13.3), garments 8 (19.07->20.71), gold ore 0 (151.2->159.6), wine 4 (6.25->7.17) | cloth 9 (7.56->10.26), butter 3 (84->89.3), cookware 3 (25.62->28.12), thread 8 (4.89->5.55) | +148 |
| Kleinburgh | 1440 | 0.60 | 0.20 (22/turn) | garments 10 (19.07->27.55), gold ore 1 (151.2->156.75) | cloth 11 (7.56->10.26), bellows 1 (262.5->285), butter 1 (77.17->89.3), cookware 4 (27.3->28.12) | +137 |

**Best:** Hofkirchen at about +390 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.66, stop 9 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 10 = 2.3 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 88, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.95 | goal planner: sells 2 a turn at 5.95, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.2) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.6k (cash + stock at home prices); +211/turn over 6 turns, -88/turn over 24 turns.
- Limits: cash flow >= -242/turn, prestige >= -0.63/turn (values are after 200 tax a turn).
- Today's settings: value +40/turn, cash +114/turn, prestige -2.47/turn - breaks the prestige floor.
- Plan: value -10/turn, cash +117/turn, prestige -0.63/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -50 vs +110, +51 vs +116, +47 vs +116.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +2/turn
  - ship Flax Wyrm -> Hanbrücken: +1/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +9/turn
  - flax farm 1 4.64 -> 3.86: -0/turn
  - retting pit 1 0.91 -> 0.77: -2/turn
  - spinnery 1 1.65 -> 1.25: -18/turn
  - mansion 1 0.00 -> 0.44: -74/turn
- Model check over the last 60 turns: predicted +108/turn for the settings we ran, real +24/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 30.12, beer 3.01, timber 3.69, prestige 59.17, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> Essenbrucke (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Hanbrücken (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 409 (+119 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.67 |
| ret | 3 | 0.91 | 0.73 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 153/77, thread 1064/227, cloth 73/127

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
