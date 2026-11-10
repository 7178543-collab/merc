# v2 shadow report

Turn 13930, 2026-11-10 19:13. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,452, prestige 3,444 (324 free, -1.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 26 | 5 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 70, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 24, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.38 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.38 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~74 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.03, no projection from the game)
- labour: projection runs 100 over real use lately; planning 485, not 585

## Prestige spending, cheapest coin per prestige first

471 turns left: prestige gained now converts 90.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.8 | 54.8 | thin at home: ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.0 | 55.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 55.1 | 55.1 | thin at home: cheese |
| jousting 3 | arena | 230 | 55.3 | 55.6 | needs a arena (build cost 26,236); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 56.0 | 56.0 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 56.6 | 56.6 | thin at home: ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.2 | 57.2 | thin at home: ham, stockfish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 59.1 | 59.1 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 59.4 | 59.4 | thin at home: cheese |
| jousting 2 | arena | 210 | 60.6 | 60.9 | needs a arena (build cost 26,236); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 61.4 | 61.4 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 10 @ 15.6; crew 0.1; est +23 a turn; stock: pasties 10 @ 15.6 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.4 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Herschweig +261, Essenbrucke +255, Bedenis +251, Friedwerp +240, Marmont +229
- Herschweig would trade: furniture buy 18 @ 13.3, pasties buy 14 @ 14.9; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (51/turn) | timber 37 (7.77->11.88), bread 149 (2.62->3.61), flour 2 (26.04->29.45), nets 5 (35.8->36.86) | candles 1 (86.62->88.5), cloth 11 (7.77->8), furniture 14 (16.07->16.25), salt 2 (5.51->5.56) | +274 |
| Vauxvais | 204 | 0.06 | 0.30 (31/turn) | bread 149 (2.62->3.78), flour 3 (26.04->32.87), leather 1 (32.13->38.38), cloth 1 (7.8->10.83) | flax fibres 9 (4.83->6.7), tallow 1 (17.96->23.18), thread 12 (4.73->5.2), tools 18 (5.35->5.65) | +212 |
| Kirchwerp | 1072 | 0.37 | 0.50 (51/turn) | tools 18 (6.3->11.21), thread 92 (4.9->5.7), nets 6 (35.8->37.05), steel ingots 3 (17.75->18.14) | flax fibres 23 (5.78->6.7), candles 1 (87.15->88.5), garments 2 (23.52->24.4), salt 3 (4.73->5.56) | +132 |
| Großaue | 1136 | 0.40 | 0.10 (10/turn) | windows 1 (714->831.25), tools 11 (6.3->7.65), lead ore 1 (9.45->13.49) | candles 1 (87.67->88.5), salt 3 (5.02->5.56) | +127 |
| Heidlowe | 662 | 0.18 | 0.30 (31/turn) | beer 64 (3.46->5.03), nets 6 (35.8->37.43), cloth 1 (7.8->8.22), wine 8 (5.99->6.17) | cured meat 5 (22.68->24.51), candles 1 (84.53->88.5), jewellery 2 (98.7->100.7), tapestries 1 (603.75->608) | +104 |

**Best:** Grandgues at about +274 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 5 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 26 = 6.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.0) |
| grain | 6 @ 3.7, stop 23 |  | goal planner: buys 6 a turn for today's rates, keeps up to 23 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 99.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.2k (cash + stock at home prices); +195/turn over 6 turns, +154/turn over 24 turns.
- Limits: cash flow >= -310/turn, prestige >= -0.10/turn (values are after 200 tax a turn).
- Today's settings: value +31/turn, cash -23/turn, prestige -1.83/turn - breaks the prestige floor.
- Plan: value -25/turn, cash -21/turn, prestige -0.10/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +76 vs +9, +24 vs -3, +46 vs -14.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +8/turn
  - ship Flax Wyrm -> Karlmoor: +7/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: +4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.06: +15/turn
  - flax farm 1 4.64 -> 3.80: -3/turn
  - retting pit 1 0.91 -> 0.76: -5/turn
  - spinnery 1 1.65 -> 1.35: +2/turn
  - sewing shop 1 0.30 -> 0.36: +5/turn
  - weavery 1 0.50 -> 0.61: +7/turn
- Model check over the last 60 turns: predicted +107/turn for the settings we ran, real +146/turn.
- Worth of one more unit per turn: labour 1.64, thread 4.16, cloth 6.62, flax fibres 5.00, garments 19.12, nets 29.80, beer 2.90, timber 3.33, prestige 62.01, cash 0.00
- Orders it would set: arms buy 1 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.06, worth +4/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Karlmoor (+7/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 39.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 510 (+221 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.52 |
| ret | 3 | 0.91 | 1.10 |
| spin | 4 | 1.65 | 1.95 |
| weave | 3 | 0.50 | 1.55 |
| sew | 2 | 0.30 | 0.97 |

Buffers: flax fibres 66/87, thread 1064/255, cloth 73/155
- chain plan needed 571 labour, budget left 510: cut to 510 (sewing capped at 0.97)

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.38; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.7 for 6 turns, bought 0.0 of 1, 65.8 held (2.8 turns); raise needs Taylor (ceiling None)
