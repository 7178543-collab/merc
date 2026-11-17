# v2 shadow report

Turn 14096, 2026-11-17 17:47. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,775, prestige 3,610 (490 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 508 | 0 | 21 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 11.00 x9, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 21 labour expired last turn (~38 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 508, not 604

## Prestige spending, cheapest coin per prestige first

305 turns left: prestige gained now converts 78.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.6 | 52.1 | needs a arena (build cost 29,269); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.3 | 54.3 | running |
| hold banquet 3 (pies) | mansion | 8 | 56.8 | 56.8 | thin at home: hop beer, pies |
| jousting 2 | arena | 210 | 56.6 | 57.1 | needs a arena (build cost 29,269); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.2 | 58.2 | thin at home: pies |
| hold banquet 1 (fish) | mansion | 4.2 | 58.9 | 58.9 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.9 | 59.9 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 60.1 | 60.1 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 60.1 | 60.1 | thin at home: hop beer, stockfish, pies |
| hold banquet 4 (premium) | mansion | 20 | 60.1 | 60.1 | thin at home: hop beer, stockfish, premium cheese, premium ham |
| hold banquet 2 (meat) | mansion | 6.8 | 61.9 | 61.9 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 61.9 | 61.9 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.6 (keep 14); best orders clear only -3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +671, Gotthafen +430, Gottweiler +421, Hofkirchen +420, Clairlond +284
- Amsdermund would trade: furniture buy 62 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (116/turn) | timber 38 (8.4->12.82), bread 162 (2.52->3.15), firewood 31 (3.07->6.65), charcoal 19 (2.86->4.84) | furniture 9 (17.22->19.95), tools 17 (5.67->5.84), bricks 2 (7.82->9.45), resin 3 (3.26->3.7) | +371 |
| Hofkirchen | 991 | 0.37 | 0.70 (81/turn) | candles 5 (59.85->74.58), lathes 1 (183.75->212.8), leather 1 (23.1->26.79), lead bars 6 (14.28->14.91) | jewellery 11 (84->89.3), furniture 9 (15.23->19.95), flax fibres 28 (5.62->7.3), cloth 20 (10.13->11.7) | +295 |
| Amsdermund | 1111 | 0.44 | 0.40 (46/turn) | candles 5 (59.85->71.25), chisels 4 (12.39->17.1), wine 12 (7.67->8.93), leather 1 (23.1->28.12) | cloth 24 (6.67->11.7), furniture 9 (14.18->19.95), dyed cloth 8 (13.65->15.77), garments 2 (26.25->29.2) | +266 |
| Brunnham | 1281 | 0.55 | 0.50 (58/turn) | garments 10 (26.8->31.92), candles 5 (59.85->69.35), nets 6 (34.2->36.29), steel ingots 3 (16.07->18.43) | cloth 24 (8.93->11.7), tapestries 1 (771.75->798), furniture 9 (15.96->19.95), raw cloth 5 (7.25->9.97) | +224 |
| Rotterburg | 1056 | 0.41 | 0.30 (35/turn) | candles 4 (59.85->73.62), nets 6 (34.2->36.67), butter 1 (88.73->93.1), hides 1 (11.03->13.96) | cloth 24 (6.93->11.7), garments 2 (19.64->29.2), furniture 9 (17.32->19.95), tapestries 1 (787.5->798) | +218 |

**Best:** Grandgues at about +371 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.9, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 74.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.0) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 8) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.3k (cash + stock at home prices); +77/turn over 6 turns, +89/turn over 24 turns.
- Limits: cash flow >= -282/turn, prestige >= -0.79/turn (values are after 200 tax a turn).
- Today's settings: value +102/turn, cash +82/turn, prestige -2.66/turn - breaks the prestige floor.
- Plan: value +27/turn, cash +35/turn, prestige -0.79/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +290 vs +82, -274 vs +84, +227 vs +67.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Großmühle: +2/turn
  - ship Flax Wyrm -> Pontmont: +0/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - spinnery 1 1.65 -> 1.38: +5/turn
  - net maker 0.00 -> 0.28: +1/turn
  - retting pit 1 0.91 -> 0.83: +1/turn
  - flax farm 1 4.64 -> 4.19: +4/turn
  - sewing shop 1 0.30 -> 0.24: -25/turn
  - weavery 1 0.50 -> 0.40: -4/turn
  - mansion 1 0.00 -> 0.45: -74/turn
- Model check over the last 60 turns: predicted +113/turn for the settings we ran, real +21/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.71, beer 3.37, timber 3.87, prestige 60.97, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 8); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Großmühle (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Pontmont (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 83/77, thread 1055/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1055 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
