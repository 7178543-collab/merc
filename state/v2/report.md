# v2 shadow report

Turn 13942, 2026-11-11 07:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,168, prestige 3,493 (373 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 0.4 -> v2: add buy 9
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.16 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.16 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~79 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.13, no projection from the game)
- labour: projection runs 100 over real use lately; planning 490, not 590

## Prestige spending, cheapest coin per prestige first

459 turns left: prestige gained now converts 90.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.5 | 52.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.4 | 55.4 |  |
| jousting 3 | arena | 230 | 56.8 | 57.1 | needs a arena (build cost 29,122); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 57.9 | 57.9 | thin at home: wine, ham, stockfish, cheese, pies |
| hold banquet 4 (premium) | mansion | 20 | 59.7 | 59.7 | thin at home: wine, ham, stockfish, premium cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 60.9 | 60.9 |  |
| hold banquet 4 | mansion | 17.5 | 60.9 | 60.9 | thin at home: wine, ham, stockfish, cheese |
| jousting 2 | arena | 210 | 62.2 | 62.5 | needs a arena (build cost 29,122); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 64.6 | 64.6 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 65.7 | 65.7 | thin at home: cheese, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 66.0 | 66.0 | thin at home: wine, cheese |
| hold prayer 2 | chapel | 13 | 59.6 | 67.0 | needs a chapel (build cost 38,273); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 18 @ 13.8, pasties buy 9 @ 15.5; crew 0.2; est +236 a turn; stock: furniture 18 @ 13.8 (keep 145); stock: pasties 9 @ 15.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Marmont +298, Boistot +283, Brebronn +278, Vauxvais +272, Hofkirchen +261
- Marmont would trade: furniture buy 24 @ 13.1; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clairas | 374 | 0.11 | 0.20 (22/turn) | charcoal 19 (2.33->5.61), nets 6 (35.2->38) | looms 1 (535.5->693.5), cheese 4 (8.72->11.11), acid 1 (140.7->148.2), tar 3 (10.5->11.4) | +240 |
| Etallaen | 774 | 0.22 | 0.50 (54/turn) | garments 10 (22.4->30.21), charcoal 19 (2.33->5.79), nets 6 (35.2->39.14), thread 23 (4.92->5.65) | cheese 7 (7.19->11.11), looms 1 (682.5->693.5), cookware 3 (22.05->24.13), fleece 5 (6.25->6.79) | +198 |
| Grandgues | 152 | 0.04 | 0.50 (54/turn) | bread 154 (2.58->3.12), charcoal 19 (2.33->4.26), cured fish 7 (24.57->27.93), timber 27 (7.77->9.03) | cheese 7 (9.03->11.11), acid 1 (141.75->148.2), cloth 11 (7.61->8.15), looms 1 (687.75->693.5) | +180 |
| Darmwald | 1022 | 0.36 | 0.50 (54/turn) | beer 63 (3.53->5.89), garments 10 (22.4->24.89), nets 2 (35.2->37.81), wax 3 (23.31->24.51) | cheese 6 (7.88->11.11), ham 1 (82.95->87.4), candles 1 (84.53->85.5), tar 3 (10.5->11.4) | +155 |
| Kirchwerp | 1072 | 0.39 | 0.50 (54/turn) | arms 7 (32.76->40.28), thread 92 (4.92->5.7), nets 5 (35.2->38.57), flax fibres 5 (6.1->7.41) | cheese 7 (6.88->11.11), acid 1 (127.05->148.2), cloth 24 (7.67->8.15), tallow 1 (22.47->23.37) | +149 |

**Best:** Clairas at about +240 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 9 @ 3.52, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 0 = 0.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 87.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 3 @ min 6.55 | goal planner: trial sale of an idle pile, 3 a turn at 6.55, keeps 85 (24 over) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 10 @ min 19.3 | goal planner: sells 10 at 19.3 (v2 had 10 at 21.8) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 110, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.7k (cash + stock at home prices); -65/turn over 6 turns, +13/turn over 24 turns.
- Limits: cash flow >= -132/turn, prestige >= -0.31/turn (values are after 200 tax a turn).
- Today's settings: value +12/turn, cash +3/turn, prestige -2.08/turn - breaks the prestige floor.
- Plan: value -29/turn, cash +36/turn, prestige -0.31/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +589 vs -70, +45 vs -70, -60 vs -6.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bremcop: +4/turn
  - ship Flax Wyrm -> Disscester: +1/turn
  - brewery 1 0.14 -> 0.07: +14/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: +7/turn
  - spinnery 1 1.65 -> 1.40: +9/turn
  - retting pit 1 0.91 -> 0.79: -1/turn
  - flax farm 1 4.64 -> 3.98: -7/turn
  - mansion 1 0.00 -> 0.42: -81/turn
- Model check over the last 59 turns: predicted +105/turn for the settings we ran, real +115/turn.
- Worth of one more unit per turn: labour 1.58, thread 3.96, cloth 6.32, flax fibres 4.70, garments 18.30, nets 28.73, beer 2.92, timber 3.33, prestige 58.97, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 3 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +4/turn.
- Ship linen snake: Grandgues -> Bremcop (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Disscester (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +65/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.5/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 415 (+126 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.23 |
| ret | 3 | 0.91 | 0.85 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 110/77, thread 1064/225, cloth 73/126

## Self-diagnosis

- R1: beer slot dry: 0.4 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.36 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.42 (ask 3.36, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.16; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
