# v2 shadow report

Turn 13941, 2026-11-11 06:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,228, prestige 3,495 (375 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 5 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 4.6 -> v2: add buy 9
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.14 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.14 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~81 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +7 crew for Flax Wyrm (crew 0.14, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

460 turns left: prestige gained now converts 90.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.4 | 53.4 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.7 | 55.7 | thin at home: beer |
| jousting 3 | arena | 230 | 56.2 | 56.5 | needs a arena (build cost 29,300); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.6 | 58.6 | thin at home: wine, ham, stockfish, cheese, pies |
| hold banquet 4 (premium) | mansion | 20 | 60.1 | 60.1 | thin at home: wine, ham, stockfish, premium cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 60.8 | 60.8 | thin at home: beer |
| hold banquet 4 | mansion | 17.5 | 61.2 | 61.2 | thin at home: wine, ham, stockfish, cheese |
| jousting 2 | arena | 210 | 61.5 | 61.9 | needs a arena (build cost 29,300); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 56.7 | 64.0 | needs a chapel (build cost 37,712) |
| hold banquet 3 (fish) | mansion | 7.6 | 65.0 | 65.0 | thin at home: cheese |
| hold sermon 2 (candles) | church | 31 | 59.3 | 65.8 | needs a church (build cost 74,821) |
| hold banquet 2 (fish) | mansion | 6.8 | 66.0 | 66.0 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 19 @ 14.6, pasties buy 7 @ 14.9; crew 0.2; est +230 a turn; stock: furniture 19 @ 14.6 (keep 145); stock: pasties 7 @ 14.9 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Marmont +284, Brebronn +274, Boistot +272, Hofkirchen +269, Caillechâtel +230
- Marmont would trade: furniture buy 23 @ 13.1; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.23 | 0.50 (55/turn) | garments 10 (23.2->30.02), charcoal 19 (2.37->5.7), nets 6 (35.2->39.9), thread 27 (4.92->5.7) | cheese 8 (8.82->11.02), tiles 1 (5.25->8.31), tar 1 (10.61->11.4) | +168 |
| Clarfranche | 1484 | 0.64 | 0.40 (44/turn) | garments 10 (23.2->29.07) | cheese 8 (6.3->11.02), wrought iron 4 (11.23->17), cookware 3 (17.22->24.13), acid 1 (116.55->126.35) | +145 |
| Kirchwerp | 1072 | 0.40 | 0.60 (66/turn) | arms 8 (33.81->40.28), thread 92 (4.92->5.7), nets 6 (35.2->38.76), cured meat 3 (25.62->29.83) | cloth 24 (7.35->8.1), garments 2 (22.68->23.4), nails 3 (6.3->7.12) | +125 |
| Darmwald | 1022 | 0.36 | 0.50 (55/turn) | beer 64 (3.7->5.65), nets 1 (35.2->38.57), wax 3 (23.31->24.13), flax fibres 1 (5.95->6.7) | cheese 7 (7.61->11.02), candles 1 (84.53->87.5) | +104 |
| Arnsreuth | 921 | 0.31 | 0.10 (11/turn) | tapestries 1 (687.75->769.5), furniture 5 (12.18->14.15), nets 1 (35.2->37.81), cloth 1 (7.85->8.84) | candles 1 (85.58->87.5), tiles 1 (4.35->8.31) | +90 |

**Best:** Etallaen at about +168 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 9 @ 3.68, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 5 = 1.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 89.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.95 | goal planner: trial sale of an idle pile, 2 a turn at 5.95, keeps 85 (23 over) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| furniture | 2 @ 15.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 10 @ min 19.3 | goal planner: sells 10 at 19.3 (v2 had 10 at 21.6) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.2k (cash + stock at home prices); -90/turn over 6 turns, -5/turn over 24 turns.
- Limits: cash flow >= -135/turn, prestige >= -0.31/turn (values are after 200 tax a turn).
- Today's settings: value +3/turn, cash -6/turn, prestige -2.09/turn - breaks the prestige floor.
- Plan: value -34/turn, cash +31/turn, prestige -0.31/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -82 vs -68, +589 vs -70, +45 vs -70.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +34/turn
  - ship Flax Wyrm -> Calange: +1/turn
  - brewery 1 0.14 -> 0.07: +16/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: +8/turn
  - spinnery 1 1.65 -> 1.40: +8/turn
  - retting pit 1 0.91 -> 0.79: -0/turn
  - flax farm 1 4.64 -> 3.98: -7/turn
  - mansion 1 0.00 -> 0.42: -80/turn
- HAND-OVER: goal planner: model check held 12 runs, it now runs 'buys' live.
- Model check over the last 60 turns: predicted +105/turn for the settings we ran, real +114/turn.
- Worth of one more unit per turn: labour 1.57, thread 3.96, cloth 6.32, flax fibres 4.70, garments 18.29, nets 28.70, beer 3.10, timber 3.33, prestige 59.05, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +4/turn.
- Ship linen snake: Grandgues -> Donaunieder (+34/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Calange (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +64/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.5/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 416 (+127 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.25 |
| ret | 3 | 0.91 | 0.85 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 108/77, thread 1064/225, cloth 73/126

## Self-diagnosis

- R1: beer slot dry: 4.6 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.52 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.58 (ask 3.52, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.14; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
