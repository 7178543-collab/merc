# v2 shadow report

Turn 14156, 2026-11-20 05:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,892, prestige 3,624 (504 free, -3.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 14 | 0 | 1 | 15 | 0 | stop 77, buy 39, buy @ 4.78 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 484 | 0 | 80 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 80 labour expired last turn (~162 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +3 crew for Flax Wyrm (crew 0.06, no projection from the game)
- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 510, not 610
- labour expiry guard: 80 bought labour expired last turn, buy 0 (not 10) this turn

## Prestige spending, cheapest coin per prestige first

245 turns left: prestige gained now converts 70.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 48.3 | 48.7 | needs a arena (build cost 29,382); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 52.0 | 52.4 | needs a arena (build cost 29,382); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.1 | 52.7 | needs a arena (build cost 29,382); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.0 | 57.7 | needs a arena (build cost 29,382); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 60.3 | 60.3 | thin at home: wine, stockfish, cheese |
| maintain 1 | park | 0.5 | 60.6 | 60.6 | running |
| hold banquet 3 (pies) | mansion | 8 | 60.7 | 60.7 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 62.4 | 62.4 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 62.9 | 62.9 | thin at home: wine, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 63.5 | 63.5 | thin at home: beer |
| hold banquet 2 (fish) | mansion | 6.8 | 63.9 | 63.9 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 64.0 | 64.0 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 15.3 (keep 14); best orders clear only 12 a turn after crew: ship stays at 0
- best towns now: Angefont +611, Gotthafen +517, Cobholme +359, Fulkirch +318, Chatgnan +275
- Angefont would trade: furniture buy 54 @ 14.4, pasties buy 7 @ 15.0; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~129 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Amsdermund | 1111 | 0.49 | 0.60 (77/turn) | flour 4 (21.21->28.88), nets 6 (36.8->39.14), slaked lime 1 (8.77->11.4) | cloth 24 (9.61->12.4), cheese 7 (6.62->9.5), axes 3 (17.85->22.99), casks 12 (5.35->7.22) | +158 |
| Kirchwerp | 1072 | 0.46 | 0.40 (51/turn) | furniture 10 (17.12->25.08), nets 6 (36.8->40.28), nails 14 (8.09->8.79), slaked lime 1 (8.77->12.35) | cheese 7 (5.83->9.5), axes 3 (17.85->22.99), canvas 8 (37.38->39.9), tools 32 (6.41->6.98) | +151 |
| Bedenis | 566 | 0.19 | 0.10 (13/turn) | yarn 29 (8.24->10.54), garments 10 (32.8->35.53), nets 1 (36.8->41.8), acid 1 (141.75->144.4) | tools 32 (6.09->6.98), cheese 7 (6.93->9.5), candles 1 (75.6->83), wine 8 (6.25->6.74) | +143 |
| Grandgues | 152 | 0.05 | 0.40 (51/turn) | bread 236 (3->3.38), flour 4 (21.21->32.11), tiles 3 (3.97->9.21), beer 1 (4.78->7.98) | cheese 7 (6.83->9.5), candles 1 (77.17->83), cured meat 2 (21->23.18) | +133 |
| Hofkirchen | 991 | 0.41 | 0.20 (26/turn) | nets 6 (36.8->43.89), nails 14 (8.09->10.83) | cheese 7 (6.3->9.5), tools 32 (6.3->6.98), axes 3 (20.06->22.99), garments 2 (31.29->33.8) | +128 |

**Best:** Amsdermund at about +158 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 32 @ ?, stop 63 |  | uses 15.6/turn (household upkeep), makes 0.0, holds 14 = 0.9 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 32.0) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 34 |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.9k (cash + stock at home prices); +110/turn over 6 turns, +115/turn over 24 turns.
- Limits: cash flow >= -329/turn, prestige >= -0.85/turn (values are after 200 tax a turn).
- Today's settings: value -166/turn, cash -176/turn, prestige +0.98/turn.
- Plan: value +3/turn, cash +7/turn, prestige -0.85/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +113 vs -178, -547 vs -110, -479 vs -137 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +8/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.56: +117/turn
  - ropewalk 1 0.25 -> 0.14: +13/turn
  - spinnery 1 1.65 -> 1.27: +11/turn
  - retting pit 1 0.91 -> 0.80: +3/turn
  - flax farm 1 4.64 -> 4.03: +7/turn
  - net maker 0.00 -> 0.29: +1/turn
  - weavery 1 0.50 -> 0.44: -6/turn
  - brewery 1 [brew mead 1] 0.00 -> 0.11: -19/turn
- Model check over the last 59 turns: predicted -14/turn for the settings we ran, real +92/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.77, beer 3.50, timber 4.16, prestige 66.42, cash 0.00
- Orders it would set: cured meat buy 4 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 0); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.11, worth +19/turn.
- Ship linen snake: Grandgues -> Donaunieder (+12/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 425 (+136 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.47 |
| ret | 3 | 0.91 | 0.89 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 98/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 14.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 32 @ 4.78, home ask none (no sellers at home)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.1 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
