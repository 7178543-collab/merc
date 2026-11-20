# v2 shadow report

Turn 14167, 2026-11-20 16:22. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,799, prestige 3,741 (621 free, +1.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 54 | 20 | 19 | 0 | 0 | sell 5, sell @ 4.6 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 17 | 0 | 9 | 0 | 0 | stop 20, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 537 | 0 | 27 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.64 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **grain**: home ask 3.74 is above our ceiling 3.70 and last turn bought 0 of ~9 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 27 labour expired last turn (~58 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 543, not 643

## Prestige spending, cheapest coin per prestige first

234 turns left: prestige gained now converts 69.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 51.3 | 51.7 | needs a arena (build cost 29,232); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 53.3 | 54.0 | needs a arena (build cost 29,232); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 55.2 | 55.6 | needs a arena (build cost 29,232); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 59.0 | 59.0 | thin at home: stockfish, cheese, candles |
| jousting 2 | arena | 210 | 58.4 | 59.1 | needs a arena (build cost 29,232); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 61.5 | 61.5 | thin at home: cheese, candles |
| hold banquet 4 (premium) | mansion | 20 | 61.5 | 61.5 | thin at home: stockfish, candles |
| hold banquet 2 (pies) | mansion | 7 | 62.1 | 62.1 | thin at home: cheese, candles |
| hold mass 2 (premium) | cathedral | 360 | 55.0 | 62.4 | needs a cathedral (build cost 306,960); thin at home: furniture, jewellery, glassware, candles, premium garments |
| maintain 1 | park | 0.5 | 63.0 | 63.0 | running |
| hold banquet 4 | mansion | 17.5 | 63.2 | 63.2 | thin at home: ham, stockfish, cheese, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 68.2 | 68.2 | thin at home: cured meat, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: candles buy 1 @ 72.0, furniture buy 18 @ 14.2, pasties buy 1 @ 14.7; crew 0.1; est +228 a turn; stock: candles 1 @ 72.0 (keep 12); stock: furniture 18 @ 14.2 (keep 145); stock: pasties 1 @ 14.7 (keep 14)
- **linen snake** on Grandgues: beer sell 4 @ 7.75, candles buy 1 @ 73.0, cured meat buy 6 @ 23.8, pasties buy 8 @ 16.0; crew 0.1; est +46 a turn; stock: candles 1 @ 73.0 (keep 12); stock: pasties 8 @ 16.0 (keep 14)
- best towns now: Chatgnan +237, Disscester +237, Großmühle +234, Caillechâtel +228, Nürnnieder +191
- Chatgnan would trade: candles buy 1 @ 78.0, furniture buy 17 @ 13.9, pasties buy 8 @ 14.0; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~134 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (121/turn) | firewood 39 (2.77->6.84), bread 242 (2.9->3.31), lathes 1 (181.65->193.8), beer 4 (4.68->7.6) | dyed cloth 6 (10.08->15.48), garments 2 (28.35->35), cheese 9 (6.93->8.22), cured meat 6 (24.99->25.4) | +249 |
| Amsdermund | 1111 | 0.51 | 0.60 (80/turn) | casks 7 (7.88->9.79), canvas 1 (42.21->45.03) | ham 2 (59.85->102.6), cured fish 6 (25.62->33.06), cured meat 6 (21->25.4), garments 2 (28.35->35) | +196 |
| Heilegg | 826 | 0.30 | 0.40 (54/turn) | leather 1 (23.52->32.3), varnish 10 (17.12->18.05), wine 16 (7.14->7.84), beer 4 (4.68->6.46) | cured fish 6 (26.88->33.06), tools 42 (6.41->7.12), cheese 9 (6.3->8.22), garments 2 (28.35->35) | +133 |
| Blanans | 297 | 0.11 | 0.10 (13/turn) | wine 9 (7.14->8.12), wool 3 (11.13->14.06), beer 4 (4.68->5.61), flax fibres 5 (6.6->7.36) | cured fish 6 (22.68->33.06), dyed cloth 6 (10.08->15.48), garments 2 (31.08->35), grain 8 (3.4->3.74) | +128 |
| Nürnnieder | 520 | 0.19 | 0.20 (27/turn) | nets 4 (42->43.51), wine 2 (7.14->9.03), canvas 1 (42.21->44.46), bricks 1 (6.25->10.83) | cured fish 6 (28.35->33.06), cloth 24 (12.08->13.2), beer 19 (3.59->4.82), yarn 19 (6.46->7.22) | +115 |

**Best:** Grandgues at about +249 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 5 @ min 4.54 | makes 19.3, uses 19.2, holds 54 (keeps 0): sells the surplus + 5/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 8 = 1.3 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 32.8) |
| grain | 5 @ 3.7, stop 20 |  | goal planner: buys 5 a turn for today's rates, keeps up to 20 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 43) |
| light armour | 1 @ 110, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 40.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.6k (cash + stock at home prices); +105/turn over 6 turns, -38/turn over 24 turns.
- Limits: cash flow >= -283/turn, prestige >= -1.34/turn (values are after 200 tax a turn).
- Today's settings: value -149/turn, cash -166/turn, prestige +1.10/turn.
- Plan: value +62/turn, cash +67/turn, prestige -1.34/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -62 vs -147, -45 vs -163, +128 vs -156.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Kirchwerp: +19/turn
  - ship Flax Wyrm -> Nürnnieder: +4/turn
  - mansion 1 1.00 -> 0.42: +150/turn
  - brewery 1 0.14 -> 0.07: +15/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +2/turn
  - spinnery 1 1.65 -> 1.28: +22/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.13: +3/turn
  - retting pit 1 0.91 -> 0.81: +3/turn
  - flax farm 1 4.64 -> 4.08: +7/turn
- Model check over the last 59 turns: predicted -57/turn for the settings we ran, real +7/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.80, beer 3.57, timber 3.96, prestige 64.09, cash 0.00
- Orders it would set: bread buy 5 (v2 8); cloth sell 1 (v2 none); firewood buy 4 (v2 8); garments sell 11 (v2 10); grain buy 5 (v2 18); labour buy 64 (v2 43); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.13, worth +2/turn.
- Ship linen snake: Grandgues -> Kirchwerp (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Nürnnieder (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.39 |
| ret | 3 | 0.91 | 0.88 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 103/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: grain buy not filling: bid 3.7 under the home ask 3.74 for 5 turns, bought 0.0 of 5, 17.3 held (1.9 turns); raise needs Taylor (ceiling 3.7)
