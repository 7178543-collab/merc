# v2 shadow report

Turn 14197, 2026-11-21 23:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,978, prestige 3,711 (591 free, +0.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 72 | 39 | 19 | 0 | 0 | min_holding 58, sell 15, sell @ 3.5; stop 116, buy 39, buy @ 4.24 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 2 | 2 | 1 | 0 | stop 13, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 65 | 65 | 551 | 0 | 14 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.66 is above our ceiling 2.40 and last turn bought 2 of ~3 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 14 labour expired last turn (~28 coin): holding 65 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 34.20 is above our ceiling 29.00 and last turn bought 6 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +5 crew for Flax Wyrm (crew 0.10, no projection from the game)
- labour: projection runs 100 over real use lately; planning 551, not 629

## Prestige spending, cheapest coin per prestige first

204 turns left: prestige gained now converts 64.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.1 | 50.5 | needs a arena (build cost 28,414); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.4 | 53.2 | needs a arena (build cost 28,414); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.9 | 54.3 | needs a arena (build cost 28,414); thin at home: protection, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.4 | 58.3 | needs a arena (build cost 28,414); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 59.1 | 59.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 61.7 | 61.7 | thin at home: stockfish |
| hold banquet 4 (premium) | mansion | 20 | 61.7 | 61.7 | thin at home: stockfish |
| hold mass 2 (premium) | cathedral | 360 | 53.8 | 63.9 | needs a cathedral (build cost 305,285); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 66.4 | 66.4 | thin at home: stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 66.8 | 66.8 |  |
| hold banquet 3 (pies) | mansion | 8 | 68.4 | 68.4 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 68.7 | 68.7 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 12 | 134102075 | 0 | - | pasties 2 | -26 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.8 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Orlesailles +48, Rotterburg +40, Hofkirchen +38, Darmwald +33, Dedlowe +30
- Orlesailles would trade: cured meat buy 6 @ 29.2, pasties buy 5 @ 9.3; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~126 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (126/turn) | bread 244 (2.88->4.56), firewood 42 (2.75->10.07), charcoal 17 (2.35->8.07), flour 3 (22.47->28.69) | garments 1 (31.71->33.6), cured meat 5 (32.97->33.4), candles 0 (82.42->83) | +761 |
| Kirchwerp | 1072 | 0.46 | 0.50 (63/turn) | thread 83 (6.7->9.5), glassware 6 (79.28->89.3), varnish 3 (18.48->23.75), rope 1 (87.5->98.8) | cloth 24 (10.5->12.7), cheese 7 (10.03->13.3), garments 2 (24.15->33.6), jewellery 2 (73.5->80.27) | +392 |
| Rouhomme | 368 | 0.12 | 0.90 (114/turn) | bread 269 (2.88->4.08), flour 4 (22.47->40.47), raw cloth 2 (9.45->14.34), wine 13 (6.46->7.03) | tools 16 (5.04->5.79), candles 1 (77.17->83), garments 2 (32.55->33.6) | +344 |
| Amsdermund | 1111 | 0.48 | 0.30 (38/turn) | windows 1 (840->869.25), nets 4 (44.6->46.17), varnish 1 (18.48->20.33) | cloth 24 (7.35->12.7), cheese 7 (8.61->13.3), garments 2 (25.2->33.6), nails 6 (5.3->6.84) | +204 |
| Gottweiler | 1135 | 0.50 | 0.20 (25/turn) | wine 13 (6.46->8.69), casks 8 (6.51->8.07), nets 1 (44.6->50.82), varnish 3 (18.48->20.52) | ham 2 (59.85->103.55), cheese 7 (8.77->13.3), cloth 11 (10.61->12.7), garments 2 (29.82->33.6) | +183 |

**Best:** Grandgues at about +761 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 2 @ min 3.88 | goal planner: sells 2 (v2 had 1) |
| bread | 5 @ 2.8, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 9 = 1.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 13 |  | goal planner: buys 4 a turn for today's rates, keeps up to 13 (v2 had 7) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 32.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 10) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 51) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 39.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.7k (cash + stock at home prices); +70/turn over 6 turns, +109/turn over 24 turns.
- Limits: cash flow >= -374/turn, prestige >= -1.21/turn (values are after 200 tax a turn).
- Today's settings: value -168/turn, cash -153/turn, prestige +0.42/turn.
- Plan: value -18/turn, cash -12/turn, prestige -1.21/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +35 vs -151, -115 vs -150, +93 vs -184.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bordees: +11/turn
  - ship Flax Wyrm -> Briclives: +3/turn
  - mansion 1 1.00 -> 0.61: +126/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.30: -5/turn
  - retting pit 1 0.91 -> 0.82: +2/turn
  - flax farm 1 4.64 -> 4.11: +6/turn
  - sewing shop 1 0.30 -> 0.20: -9/turn
  - weavery 1 0.50 -> 0.33: +14/turn
- Model check over the last 59 turns: predicted -128/turn for the settings we ran, real +42/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.65, beer 3.35, timber 3.69, prestige 74.70, cash 0.00
- Orders it would set: beer sell 2 (v2 1); bread buy 5 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 7); garments sell 11 (v2 10); grain buy 9 (v2 10); labour buy 64 (v2 51); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Bordees (+17/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Briclives (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1976 coin: +4/turn, payback 475 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 421 (+132 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.24 |
| ret | 3 | 0.91 | 0.85 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 114/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 0.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.8, home ask 2.74; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 4.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 4 @ 2.4, home ask 2.66; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
