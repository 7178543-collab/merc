# v2 shadow report

Turn 14148, 2026-11-19 21:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,532, prestige 3,641 (521 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 5 | 14 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 47, buy 39, buy @ 3.68 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 1 | 1 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 19, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 497 | 0 | 67 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 6 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.74 is above it); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.74 is above our ceiling 2.40 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 5) -> v2: buy 5

## Waste (money lost now)

- **labour**: 67 labour expired last turn (~137 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **bread**: home ask 3.26 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 58.7 coin per prestige at mansion, vs 71.3 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (pies)**: hold banquet 2 (pies) costs 58.9 coin per prestige at mansion, vs 71.3 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 3 (fish)**: hold banquet 3 (fish) costs 60.5 coin per prestige at mansion, vs 71.3 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 3 (pies)**: hold banquet 3 (pies) costs 59.3 coin per prestige at mansion, vs 71.3 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 100 over real use lately; planning 516, not 616
- labour expiry guard: 67 bought labour expired last turn, buy 0 (not 16) this turn

## Prestige spending, cheapest coin per prestige first

253 turns left: prestige gained now converts 71.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.3 | 50.7 | needs a arena (build cost 28,842); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 51.3 | 51.9 | needs a arena (build cost 28,842); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.1 | 54.4 | needs a arena (build cost 28,842); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 56.2 | 56.9 | needs a arena (build cost 28,842); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 58.7 | 58.7 |  |
| hold banquet 2 (pies) | mansion | 7 | 58.9 | 58.9 |  |
| hold banquet 3 (pies) | mansion | 8 | 59.3 | 59.3 |  |
| hold banquet 4 (pies) | mansion | 18 | 59.6 | 59.6 | thin at home: stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 60.5 | 60.5 |  |
| hold banquet 4 (premium) | mansion | 20 | 60.9 | 60.9 | thin at home: stockfish |
| maintain 1 | park | 0.5 | 61.8 | 61.8 | running |
| hold mass 2 (premium) | cathedral | 360 | 56.3 | 62.8 | needs a cathedral (build cost 309,400); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 12 | 151802239 | 0.2 | - | cured meat 4, pasties 2 | -126 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 12 @ 16.4; crew 0.1; est +17 a turn; stock: pasties 12 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 11.8 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Angefont +574, Cobholme +358, Fulkirch +314, Großmühle +255, Disscester +231
- Angefont would trade: furniture buy 49 @ 14.2, pasties buy 12 @ 15.5; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~130 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.13 | 0.80 (104/turn) | bread 220 (3.04->4.33), thread 58 (5.55->6.27), flour 4 (23.31->30.97), nets 6 (36.8->38.57) | tools 16 (6.3->6.84), candles 1 (75.6->80.5), seeds 2 (1.94->2.58) | +292 |
| Angefont | 686 | 0.24 | 0.30 (39/turn) | cloth 21 (12.6->17.1), books 1 (750.75->821.75), thread 70 (5.55->6.65), tackles 1 (150.15->170.05) | flax fibres 18 (6.98->8.35), candles 1 (73.5->80.5), seeds 11 (1.78->2.58), tools 16 (6.41->6.84) | +292 |
| Grandgues | 152 | 0.05 | 0.40 (52/turn) | timber 40 (9.4->12.44), thread 78 (5.55->6.27), flour 4 (23.31->31.73), charcoal 19 (2.6->4.24) | candles 1 (76.12->80.5), garments 2 (35.07->35.2) | +207 |
| Kirchwerp | 1072 | 0.47 | 0.90 (117/turn) | dyed cloth 15 (23.73->27.36), furniture 11 (16.91->21.66), thread 78 (5.55->6.32), wine 9 (6.88->9.36) | garments 2 (27.3->35.2), belts 7 (32.55->33.82), lathes 1 (189->195.7), flax fibres 13 (7.35->8.35) | +189 |
| Heilegg | 826 | 0.29 | 0.20 (26/turn) | wrought iron 7 (19.21->27.55), casks 7 (6.88->11.3), nets 3 (36.8->45.98), tackles 1 (150.15->172.9) | dyed cloth 12 (19.84->21.28), tools 16 (6.41->6.84), garments 2 (34.23->35.2) | +162 |

**Best:** Rouhomme at about +292 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 39 @ ?, stop 77 | off | a building is stalled on beer: no sell until it runs again |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 27.2, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 7 |  | goal planner: buys 2 a turn for today's rates, keeps up to 7 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 32.2) |
| grain | 5 @ 3.7, stop 19 |  | goal planner: buys 5 a turn for today's rates, keeps up to 19 (v2 had 0) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 0) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 71.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.8k (cash + stock at home prices); +74/turn over 6 turns, -2/turn over 24 turns.
- Limits: cash flow >= -439/turn, prestige >= -0.92/turn (values are after 200 tax a turn).
- Today's settings: value -179/turn, cash -182/turn, prestige +1.42/turn.
- Plan: value +24/turn, cash +34/turn, prestige -0.92/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +3 vs -122, +180 vs -140, -168 vs -159.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +4/turn
  - ship Flax Wyrm -> no route: -0/turn
  - mansion 1 1.00 -> 0.44: +148/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - ropewalk 1 0.25 -> 0.16: +13/turn
  - spinnery 1 1.65 -> 1.31: +12/turn
  - net maker 0.00 -> 0.29: +4/turn
  - retting pit 1 0.91 -> 0.79: +3/turn
  - flax farm 1 4.64 -> 3.99: +7/turn
- Model check over the last 59 turns: predicted +21/turn for the settings we ran, real +73/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.70, beer 3.55, timber 3.69, prestige 66.41, cash 0.00
- Orders it would set: arms buy 1 (v2 None); bread buy 5 (v2 9); cloth sell 1 (v2 none); cured meat buy 3 (v2 None); firewood buy 2 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 65 (v2 0); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Angefont (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 424 (+136 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.45 |
| ret | 3 | 0.91 | 0.89 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 99/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 39 @ 3.68, home ask none (no sellers at home)
- R1: bread slot dry: 5.4 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 3.26 -> **buy 9 @ 3.32 (ask 3.26, cap 4.3)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.74; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
