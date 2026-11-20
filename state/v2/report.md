# v2 shadow report

Turn 14162, 2026-11-20 11:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,551, prestige 3,741 (621 free, -3.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 30 | 0 | 0 | 15 | 0 | stop 60, buy 30, buy @ 4.78 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 2 | 2 | 2 | 1 | 0 | stop 11, buy 3, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 22, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 485 | 0 | 79 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (3 @ 2.4), 2 bought last turn); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: only 0.6 turns of firewood left and buying 3 (need 7) -> v2: buy 7
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 79 labour expired last turn (~173 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **candles**: home ask 82.00 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +0 crew for Flax Wyrm (crew 0.01, no projection from the game)
- labour: +0 crew for linen snake (crew 0.00, no projection from the game)
- labour: projection runs 100 over real use lately; planning 519, not 619
- labour expiry guard: 79 bought labour expired last turn, buy 0 (not 19) this turn

## Prestige spending, cheapest coin per prestige first

239 turns left: prestige gained now converts 69.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 48.1 | 48.5 | needs a arena (build cost 29,893); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 51.8 | 52.2 | needs a arena (build cost 29,893); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 53.0 | 53.6 | needs a arena (build cost 29,893); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.6 | 58.6 | thin at home: wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 58.7 | 58.7 |  |
| jousting 2 | arena | 210 | 58.0 | 58.7 | needs a arena (build cost 29,893); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.5 | 60.5 | thin at home: wine, stockfish |
| hold banquet 3 (meat) | mansion | 7.6 | 61.0 | 61.0 |  |
| hold banquet 2 (pies) | mansion | 7 | 61.4 | 61.4 | thin at home: wine |
| hold banquet 4 | mansion | 17.5 | 62.3 | 62.3 | thin at home: wine, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 62.5 | 62.5 | thin at home: wine |
| hold mass 2 (premium) | cathedral | 360 | 56.2 | 63.6 | needs a cathedral (build cost 318,850); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: candles buy 3 @ 73.0, pasties buy 1 @ 14.8; crew 0.1; est +41 a turn; stock: candles 3 @ 73.0 (keep 12); stock: pasties 1 @ 14.8 (keep 14)
- **linen snake** on Grandgues: candles buy 2 @ 74.0, pasties buy 3 @ 16.0; crew 0.1; est +27 a turn; stock: candles 2 @ 74.0 (keep 12); stock: pasties 3 @ 16.0 (keep 14)
- best towns now: Angefont +290, Dortgart +254, Cobholme +230, Disscester +220, Clairlond +190
- Angefont would trade: candles buy 3 @ 75.5, furniture buy 21 @ 14.0, pasties buy 3 @ 14.3; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~135 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Nürnnieder | 520 | 0.19 | 0.30 (40/turn) | spinning wheels 1 (367.5->427.5), belts 4 (36.75->44.08), nets 6 (40.8->42.56), bricks 1 (6.25->15.67) | cured fish 5 (24.15->37.24), beer 64 (3.68->4.75), yarn 28 (6.14->7.46), fleece 3 (12.5->17.67) | +298 |
| Hofkirchen | 991 | 0.43 | 0.30 (40/turn) | spinning wheels 2 (367.5->427.5), candles 2 (63->75.05), nets 6 (40.8->42.94), malt 3 (7.35->8.64) | cured fish 5 (25.2->37.24), dyed cloth 8 (15.75->19.76), fleece 3 (11.87->17.67), garments 2 (27.3->34.6) | +276 |
| Kirchwerp | 1072 | 0.48 | 0.30 (40/turn) | furniture 9 (16.59->27.55), spinning wheels 1 (367.5->427.5), candles 2 (63->69.35), nets 6 (40.8->42.94) | cloth 16 (10.5->13.4), dyed cloth 8 (15.75->19.76), garments 2 (24.15->34.6), fleece 1 (8.77->17.67) | +264 |
| Amsdermund | 1111 | 0.51 | 0.30 (40/turn) | spinning wheels 2 (367.5->427.5), furniture 9 (16.59->20.9), candles 2 (63->66.5), grain 2 (3.4->4.94) | cured fish 5 (26.67->37.24), dyed cloth 8 (16.48->19.76), fleece 3 (11.03->17.67), garments 2 (27.3->34.6) | +258 |
| Hanstein | 380 | 0.14 | 0.70 (94/turn) | spinning wheels 2 (367.5->399), firewood 18 (2.39->7.08), candles 2 (63->65.55), charcoal 16 (2.62->3.93) | cured fish 5 (24.15->37.24), cloth 21 (11.55->13.4), beer 101 (4.2->4.75), fleece 3 (10.82->17.67) | +242 |

**Best:** Nürnnieder at about +298 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 30 @ ?, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 30 = 2.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 23.2, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 3 @ 2.4, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 6 @ 3.7, stop 22 |  | goal planner: buys 6 a turn for today's rates, keeps up to 22 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 0) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 39.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.2k (cash + stock at home prices); -628/turn over 6 turns, -43/turn over 24 turns.
- Limits: cash flow >= -273/turn, prestige >= -1.34/turn (values are after 200 tax a turn).
- Today's settings: value -167/turn, cash -176/turn, prestige +0.45/turn.
- Plan: value -1/turn, cash +11/turn, prestige -1.34/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -374 vs -155, +353 vs -129, +27 vs -125.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.57: +103/turn
  - spinnery 1 1.65 -> 1.27: +9/turn
  - ropewalk 1 0.25 -> 0.00: +25/turn
  - retting pit 1 0.91 -> 0.80: +2/turn
  - flax farm 1 4.64 -> 4.04: +8/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.15: +0/turn
  - net maker 0.00 -> 0.29: -2/turn
  - weavery 1 0.50 -> 0.44: -6/turn
- Model check over the last 59 turns: predicted -37/turn for the settings we ran, real +8/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.78, beer 3.56, timber 4.39, prestige 60.05, cash 0.00
- Orders it would set: arms buy 1 (v2 None); bread buy 5 (v2 7); cloth sell 1 (v2 none); cured meat buy 4 (v2 None); firewood buy 3 (v2 7); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 64 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.15, worth +1/turn.
- Ship linen snake: Grandgues -> Vauxvais (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 425 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.52 |
| ret | 3 | 0.91 | 0.90 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 94/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 30.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 30 @ 4.78, home ask none (no sellers at home)
- R1: firewood slot dry: 2.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 3 @ 2.4, home ask 2.28; our bid is already at/over the ask (sellers too thin)
- R1: prestige rate -3.75 a turn vs 12-turn median -1.67; likely: dry slot: beer, firewood
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 12.2 for 3 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
