# v2 shadow report

Turn 14166, 2026-11-20 15:17. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,671, prestige 3,740 (620 free, +1.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 59 | 39 | 19 | 0 | 0 | stop 60, buy 39, buy @ 5.35 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 21 | 0 | 9 | 0 | 0 | stop 22, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 537 | 0 | 27 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 5 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.58 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 27 labour expired last turn (~58 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: we make 0/turn more than we use but there is no sell order -> v2: sell 0
- **cured meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **grain**: home ask 3.72 is above our ceiling 3.70 and last turn bought 0 of ~9 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +5 crew for Flax Wyrm (crew 0.11, no projection from the game)
- labour: +0 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 119 over real use lately; planning 537, not 642

## Prestige spending, cheapest coin per prestige first

235 turns left: prestige gained now converts 69.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 48.7 | 49.1 | needs a arena (build cost 30,213); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 52.4 | 52.8 | needs a arena (build cost 30,213); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.8 | 53.5 | needs a arena (build cost 30,213); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.8 | 58.6 | needs a arena (build cost 30,213); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 59.0 | 59.0 | thin at home: stockfish, cheese, candles |
| hold banquet 3 (pies) | mansion | 8 | 61.0 | 61.0 | thin at home: cheese, candles |
| hold banquet 4 (premium) | mansion | 20 | 61.3 | 61.3 | thin at home: stockfish, candles |
| hold banquet 2 (pies) | mansion | 7 | 61.4 | 61.4 | thin at home: cheese, candles |
| hold mass 2 (premium) | cathedral | 360 | 55.2 | 62.7 | needs a cathedral (build cost 313,360); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 63.0 | 63.0 | thin at home: ham, stockfish, cheese, candles |
| maintain 1 | park | 0.5 | 63.6 | 63.6 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 65.7 | 65.7 | thin at home: cured meat, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: candles buy 1 @ 72.5, cured meat buy 6 @ 24.6, furniture buy 18 @ 13.6, pasties buy 1 @ 13.7; crew 0.2; est +238 a turn; stock: candles 1 @ 72.5 (keep 12); stock: furniture 18 @ 13.6 (keep 145); stock: pasties 1 @ 13.7 (keep 14)
- **linen snake** on Grandgues: beer sell 5 @ 7.8, candles buy 1 @ 73.5, cured meat buy 6 @ 24.0, pasties buy 7 @ 16.0; crew 0.1; est +52 a turn; stock: candles 1 @ 73.5 (keep 12); stock: pasties 7 @ 16.0 (keep 14)
- best towns now: Caillechâtel +238, Disscester +236, Gotthafen +230, Clairlond +219, Brunnham +200
- Caillechâtel would trade: candles buy 1 @ 72.5, cured meat buy 6 @ 24.6, furniture buy 18 @ 13.6, pasties buy 1 @ 13.7; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~136 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.06 | 0.60 (81/turn) | firewood 39 (2.71->6.65), charcoal 20 (2.46->3.89), beer 5 (4.74->7.69), tackles 1 (163.8->170.05) | garments 2 (29.4->34), cheese 8 (6.77->7.08) | +150 |
| Helmgreen | 1354 | 0.69 | 0.20 (27/turn) | tackles 1 (163.8->180.5), wool 4 (11.13->13.77) | cloth 23 (9.24->13.6), garments 2 (30.66->34) | +107 |
| Kirchwerp | 1072 | 0.49 | 0.50 (68/turn) | cured fish 6 (32.55->35.91), casks 11 (7.72->9.36), salt 5 (5.25->6.93), lead ore 3 (7.25->10.45) | dyed cloth 9 (15.75->18.52), garments 2 (24.15->34), cheese 8 (5.1->7.08), tools 48 (6.41->7.12) | +106 |
| Heidlowe | 662 | 0.24 | 0.20 (27/turn) | nets 3 (42->44.84), wool 6 (11.13->12.06) | cloth 24 (10.29->13.6), garments 2 (29.4->34), tools 21 (6.67->7.12), cheese 8 (6.3->7.08) | +105 |
| Rouhomme | 368 | 0.13 | 0.10 (14/turn) | cured fish 6 (32.55->36.48), beer 5 (4.74->7.69), flax fibres 5 (6.5->7.17), raw cloth 1 (11.87->13.77) | tools 48 (6.3->7.12), dyed cloth 9 (16.38->18.52), garments 2 (29.4->34) | +102 |

**Best:** Grandgues at about +150 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 5 @ min 4.6 | makes 19.3, uses 19.2, holds 59 (keeps 0): sells the surplus + 5/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 32.8) |
| grain | 5 @ 3.7, stop 20 |  | goal planner: buys 5 a turn for today's rates, keeps up to 20 (v2 had 17) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 37) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 40.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.6k (cash + stock at home prices); +187/turn over 6 turns, -31/turn over 24 turns.
- Limits: cash flow >= -278/turn, prestige >= -1.33/turn (values are after 200 tax a turn).
- Today's settings: value -141/turn, cash -156/turn, prestige +1.11/turn.
- Plan: value +68/turn, cash +74/turn, prestige -1.33/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +27 vs -125, -62 vs -147, -45 vs -163.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Kirchwerp: +12/turn
  - ship Flax Wyrm -> Nürnnieder: +1/turn
  - mansion 1 1.00 -> 0.42: +146/turn
  - brewery 1 0.14 -> 0.07: +15/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +2/turn
  - spinnery 1 1.65 -> 1.28: +22/turn
  - retting pit 1 0.91 -> 0.81: +3/turn
  - flax farm 1 4.64 -> 4.08: +4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.13: +6/turn
- Model check over the last 58 turns: predicted -53/turn for the settings we ran, real +4/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.81, beer 3.55, timber 4.03, prestige 62.33, cash 0.00
- Orders it would set: bread buy 5 (v2 6); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); garments sell 11 (v2 10); grain buy 5 (v2 17); labour buy 64 (v2 37); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.13, worth +2/turn.
- Ship linen snake: Grandgues -> Kirchwerp (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Nürnnieder (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 424 (+135 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.42 |
| ret | 3 | 0.91 | 0.88 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 102/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 10.8 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: grain buy not filling: bid 3.7 under the home ask 3.72 for 4 turns, bought 0.0 of 5, 21.3 held (2.4 turns); raise needs Taylor (ceiling 3.7)
- R5: tar buy not filling: bid 11 under the home ask 12.4 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
