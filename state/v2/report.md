# v2 shadow report

Turn 14193, 2026-11-21 18:07. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,850, prestige 3,708 (588 free, -2.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 58 | 0 | 9 | 0 | 0 | min_holding 58, sell 15, sell @ 3.74 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 3 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 544 | 0 | 20 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 2 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (12 @ 32.2), but the home ask 32.60 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.90 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 20 labour expired last turn (~40 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0
- **linen snake**: linen snake cost 12 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **cured meat**: home ask 32.60 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.90 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +5 crew for linen snake (crew 0.10, no projection from the game)
- labour: projection runs 103 over real use lately; planning 549, not 652

## Prestige spending, cheapest coin per prestige first

208 turns left: prestige gained now converts 64.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.5 | 51.0 | needs a arena (build cost 28,720); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 51.4 | 52.2 | needs a arena (build cost 28,720); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.3 | 54.7 | needs a arena (build cost 28,720); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 56.3 | 57.2 | needs a arena (build cost 28,720); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 60.6 | 60.6 | running |
| hold banquet 4 (premium) | mansion | 20 | 60.7 | 60.7 | thin at home: stockfish, candles |
| hold banquet 4 (pies) | mansion | 18 | 61.7 | 61.7 | thin at home: stockfish, cheese, candles |
| hold mass 2 (premium) | cathedral | 360 | 53.9 | 63.5 | needs a cathedral (build cost 307,475); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 1 (fish) | mansion | 4.2 | 65.9 | 65.9 |  |
| hold banquet 4 | mansion | 17.5 | 66.7 | 66.7 | thin at home: stockfish, cheese, candles |
| hold banquet 3 (pies) | mansion | 8 | 67.4 | 67.4 | thin at home: cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 69.6 | 69.6 | thin at home: cheese, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 12 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: cured meat buy 2 @ 30.6, furniture buy 3 @ 14.6, pasties buy 3 @ 14.5; crew 0.1; est +39 a turn; stock: furniture 3 @ 14.6 (keep 145); stock: pasties 3 @ 14.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Blanans +74, Orlesailles +72, Friedwerp +51, Bordees +40, Caillechâtel +39
- Blanans would trade: cured meat buy 2 @ 28.8, furniture buy 3 @ 12.0, pasties buy 9 @ 14.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~127 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (127/turn) | bread 259 (2.9->4.1), firewood 45 (2.84->8.41), charcoal 19 (2.79->7.41), beer 10 (3.6->4.27) | cheese 10 (11.13->13.96), lathes 1 (195.3->203.3), cured meat 2 (30.24->32.6), swords 1 (241.5->245.1) | +591 |
| Kirchwerp | 1072 | 0.46 | 0.60 (76/turn) | thread 94 (6.95->9.5), casks 9 (6.83->9.36), varnish 4 (17.12->20.9), honey 5 (8.87->11.02) | cheese 10 (11.97->13.96), tools 22 (5.25->6.22), cloth 16 (10.5->11.6), lathes 1 (189->203.3) | +307 |
| Amsdermund | 1111 | 0.48 | 0.40 (51/turn) | nets 5 (45.8->47.97), canvas 1 (48.93->52.25), varnish 4 (17.12->17.86) | cheese 10 (9.19->13.96), garments 2 (21->33.6), dyed cloth 8 (15.33->17.67), tools 22 (5.25->6.22) | +130 |
| Heilegg | 826 | 0.29 | 0.70 (89/turn) | charcoal 19 (2.79->6.55), varnish 5 (17.12->22.99), beer 10 (3.6->6.13), furniture 9 (15.96->18.62) | swords 1 (241.5->245.1) | +127 |
| Hofkirchen | 991 | 0.40 | 0.20 (25/turn) | wheels 2 (26.25->37.05), varnish 5 (17.12->20.33), wine 5 (6.72->8.31), resin 3 (2.27->3.89) | cheese 10 (10.34->13.96), cloth 24 (10.5->11.6), lathes 1 (189->203.3), cured meat 2 (28.98->32.6) | +108 |

**Best:** Grandgues at about +591 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.5 |  |
| bread | 5 @ 2.82, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 8 = 1.3 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 2 @ 15.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 32.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 49) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 44.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.2k (cash + stock at home prices); +201/turn over 6 turns, +102/turn over 24 turns.
- Limits: cash flow >= -369/turn, prestige >= -1.20/turn (values are after 200 tax a turn).
- Today's settings: value -161/turn, cash -168/turn, prestige +0.55/turn.
- Plan: value +9/turn, cash +14/turn, prestige -1.20/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +72 vs -191, +228 vs -186, +165 vs -160.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanstein: +8/turn
  - ship Flax Wyrm -> Angefont: +5/turn
  - mansion 1 1.00 -> 0.58: +130/turn
  - ropewalk 1 0.25 -> 0.17: +9/turn
  - spinnery 1 1.65 -> 1.25: +10/turn
  - retting pit 1 0.91 -> 0.79: +3/turn
  - flax farm 1 4.64 -> 3.97: +8/turn
  - net maker 0.00 -> 0.29: -4/turn
  - sewing shop 1 0.30 -> 0.24: -9/turn
  - weavery 1 0.50 -> 0.38: +10/turn
- Model check over the last 59 turns: predicted -128/turn for the settings we ran, real +35/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.66, beer 3.38, timber 3.69, prestige 70.97, cash 0.00
- Orders it would set: bread buy 5 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 64 (v2 49); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Hanstein (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+5/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2005 coin: +2/turn, payback 851 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 419 (+130 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.16 |
| ret | 3 | 0.91 | 0.83 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 120/77, thread 1052/228, cloth 72/128

## Self-diagnosis

- R1: bread slot dry: 5.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.82, home ask 2.76; our bid is already at/over the ask (sellers too thin)
- R1: cured meat slot dry: 8.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 12 @ 32.2, home ask 32.6 -> **buy 12 @ 33.2 (ask 32.6, cap 42.0)** (ok)
- R2: spinnery 1 blocked by thread space: 1052 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
