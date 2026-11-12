# v2 shadow report

Turn 13962, 2026-11-12 03:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,890, prestige 3,567 (447 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 10 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 35 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~75 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +5 crew for Flax Wyrm (crew 0.11, no projection from the game)
- labour: +2 crew for linen snake (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

439 turns left: prestige gained now converts 88.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| jousting 3 | arena | 230 | 55.6 | 55.9 | needs a arena (build cost 26,818); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 56.0 | 56.0 | thin at home: wine, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 56.9 | 56.9 |  |
| hold banquet 4 | mansion | 17.5 | 59.3 | 59.3 | thin at home: wine, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 59.7 | 59.7 | thin at home: wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 60.5 | 60.5 |  |
| jousting 2 | arena | 210 | 60.9 | 61.2 | needs a arena (build cost 26,818); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 61.4 | 61.4 | thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 61.7 | 61.7 | thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 62.5 | 62.5 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 62.7 | 62.7 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 23 @ 14.6, pasties buy 4 @ 16.0; crew 0.1; est +273 a turn; stock: furniture 23 @ 14.6 (keep 145); stock: pasties 4 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 13.8, pasties buy 2 @ 15.6; crew 0.2; est +238 a turn; stock: furniture 20 @ 13.8 (keep 145); stock: pasties 2 @ 15.6 (keep 14)
- best towns now: Angefont +281, Unterhufe +278, Grandgues +273, Amsdermund +272, Calange +261
- Angefont would trade: furniture buy 23 @ 14.4, pasties buy 11 @ 15.6; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Darmwald | 1022 | 0.35 | 0.70 (73/turn) | beer 85 (3.68->5.84), garments 10 (19.05->25.08), nets 3 (35.4->37.62), malt 1 (7.19->11.88) | butter 4 (87.15->91.67), cookware 4 (28.35->30.02), resin 1 (3.09->7.12) | +219 |
| Heidlowe | 662 | 0.18 | 0.20 (21/turn) | lead ore 10 (9.45->15.48), tapestries 1 (609->655.5), garments 10 (19.05->21.85), copper ingots 1 (15.33->18.05) | butter 4 (84->91.67), thread 21 (4.85->5.65), cookware 4 (27.51->30.02), cloth 20 (8.19->8.65) | +192 |
| Kleinburgh | 1440 | 0.58 | 0.10 (10/turn) | garments 10 (19.05->30.02), tapestries 1 (609->636.5) | cookware 4 (27.51->30.02), bellows 1 (279.3->285), cloth 9 (7.77->8.65) | +143 |
| Hanstein | 380 | 0.11 | 0.30 (31/turn) | garments 10 (19.05->21.47), tapestries 1 (609->617.5), timber 11 (8.19->10.36), nets 3 (35.4->37.24) | thread 26 (4.49->5.65), cloth 13 (7.56->8.65), butter 4 (88.73->91.67), flax fibres 12 (5.51->6.65) | +139 |
| Kirchwerp | 1072 | 0.37 | 0.20 (21/turn) | tapestries 1 (609->684), garments 10 (19.05->20.33), nets 5 (35.4->37.62), flax fibres 8 (6.1->7.55) | cloth 24 (7.56->8.65), cookware 4 (26.25->30.02), resin 1 (4.43->7.12), stockfish 1 (115.5->117.8) | +139 |

**Best:** Darmwald at about +219 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 88.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.95 | goal planner: sells 2 a turn at 5.95, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.2) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.7k (cash + stock at home prices); +183/turn over 6 turns, -109/turn over 24 turns.
- Limits: cash flow >= -245/turn, prestige >= -0.61/turn (values are after 200 tax a turn).
- Today's settings: value +27/turn, cash +67/turn, prestige -2.45/turn - breaks the prestige floor.
- Plan: value -26/turn, cash +70/turn, prestige -0.61/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +47 vs +116, +86 vs +114, +7 vs +83.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +6/turn
  - ship Flax Wyrm -> Essenbrucke: +2/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +9/turn
  - spinnery 1 1.65 -> 1.31: -0/turn
  - sewing shop 1 0.30 -> 0.36: +1/turn
  - weavery 1 0.50 -> 0.59: +9/turn
  - retting pit 1 0.91 -> 0.79: +2/turn
  - flax farm 1 4.64 -> 3.99: +5/turn
- Model check over the last 61 turns: predicted +108/turn for the settings we ran, real +28/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.65, thread 4.14, cloth 6.62, flax fibres 4.91, garments 19.15, nets 29.95, beer 3.18, timber 3.73, prestige 61.39, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Essenbrucke (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 408 (+118 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.62 |
| ret | 3 | 0.91 | 0.72 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 157/77, thread 1064/227, cloth 73/127

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
