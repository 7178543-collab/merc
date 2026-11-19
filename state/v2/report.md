# v2 shadow report

Turn 14133, 2026-11-19 06:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,877, prestige 3,654 (534 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 12 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 39, buy @ 3.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 6, buy 2, buy @ 3.7 |
| labour | 64 | 64 | 538 | 0 | 26 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 2 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.80 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.80 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 23 coin last turn (crew 0.20) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 26 labour expired last turn (~50 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 86.00 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 116 over real use lately; planning 538, not 638

## Prestige spending, cheapest coin per prestige first

268 turns left: prestige gained now converts 74.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.3 | 50.6 | needs a arena (build cost 28,658); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.0 | 54.3 | needs a arena (build cost 28,658); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.3 | 54.9 | needs a arena (build cost 28,658); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 57.6 | 57.6 | thin at home: cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 |  |
| maintain 1 | park | 0.5 | 58.8 | 58.8 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 59.2 | 59.2 | thin at home: cheese |
| jousting 2 | arena | 210 | 59.5 | 60.1 | needs a arena (build cost 28,658); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 60.9 | 60.9 |  |
| hold banquet 3 (pies) | mansion | 8 | 61.2 | 61.2 |  |
| hold banquet 4 (pies) | mansion | 18 | 62.3 | 62.3 | thin at home: stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 63.0 | 63.0 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 24 | 134102075 | 0.32 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 16.0 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Amsdermund +676, Gotthafen +474, Chatgnan +402, Clairas +323, Fulkirch +312
- Amsdermund would trade: candles buy 4 @ 76.5, cured meat buy 3 @ 22.4, furniture buy 61 @ 14.3; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~124 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (112/turn) | firewood 27 (2.9->8.88), timber 39 (9.35->12.35), bread 163 (2.75->3.23), premium garments 1 (119.7->154.85) | jewellery 6 (94.5->101.65), yarn 6 (6.83->10.07), wax 10 (27.72->28.5), garments 2 (34.86->36.2) | +402 |
| Marmont | 638 | 0.21 | 0.20 (25/turn) | raw cloth 13 (8.93->16.25), premium ham 1 (243.6->252.7), cheese 3 (6.67->7.93), premium garments 1 (119.7->122.55) | furniture 15 (14.91->19.38), yarn 7 (5.72->10.07), candles 1 (79.28->85.5), axes 1 (17.96->19.38) | +201 |
| Rouhomme | 368 | 0.12 | 0.60 (74/turn) | thread 28 (5.15->7.93), bread 163 (2.75->3.55), premium garments 1 (119.7->136.8), raw cloth 3 (8.93->10.54) | yarn 4 (7.51->10.07), garments 2 (31.92->36.2), tools 20 (4.73->5.22), copper ingots 2 (14.91->17.1) | +194 |
| Clairas | 374 | 0.12 | 0.20 (25/turn) | charcoal 19 (2.77->4.84), premium garments 1 (119.7->136.8), thread 21 (5.15->5.84), dyed cloth 5 (18.59->19.76) | furniture 15 (15.02->19.38), yarn 11 (5.78->10.07), garments 2 (30.03->36.2), candles 1 (77.17->85.5) | +191 |
| Pontmont | 341 | 0.11 | 0.80 (99/turn) | premium garments 1 (119.7->154.85), bricks 6 (7.19->11.88), cloth 8 (12.39->14.25), charcoal 19 (2.77->4.24) | furniture 15 (16.38->19.38), jewellery 6 (96.6->101.65), candles 1 (77.17->85.5), yarn 1 (6.3->10.07) | +178 |

**Best:** Grandgues at about +402 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 24 @ 3.78, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 16 = 1.4 turns |
| bread | 5 @ 2.66, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 29.0, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 23.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 38) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.2k (cash + stock at home prices); -212/turn over 6 turns, +41/turn over 24 turns.
- Limits: cash flow >= -453/turn, prestige >= -0.97/turn (values are after 200 tax a turn).
- Today's settings: value -166/turn, cash -159/turn, prestige +0.93/turn.
- Plan: value -25/turn, cash -17/turn, prestige -0.97/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +39 vs -122, -118 vs -150, +142 vs -144.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +20/turn
  - ship Flax Wyrm -> Amsdermund: +8/turn
  - mansion 1 1.00 -> 0.55: +110/turn
  - spinnery 1 1.65 -> 1.38: +4/turn
  - retting pit 1 0.91 -> 0.78: +3/turn
  - flax farm 1 4.64 -> 3.93: +8/turn
  - net maker 0.00 -> 0.28: -0/turn
  - sewing shop 1 0.30 -> 0.24: -7/turn
  - weavery 1 0.50 -> 0.39: +10/turn
- HAND-OVER: goal planner: model check held 12 runs, it now runs 'rates' live.
- Model check over the last 59 turns: predicted +91/turn for the settings we ran, real +77/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.69, beer 3.28, timber 3.58, prestige 62.78, cash 0.00
- Orders it would set: bread buy 5 (v2 None); cloth sell 1 (v2 none); cured meat buy 4 (v2 12); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 64 (v2 38); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Hofkirchen (+20/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Amsdermund (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 75/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 16.3 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 24 @ 3.78, home ask 3.6; our bid is already at/over the ask (sellers too thin)
- R1: bread slot dry: 5.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.66, home ask 2.6; our bid is already at/over the ask (sellers too thin)
- R1: cured meat slot dry: 3.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 29, home ask 25.2; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.8; ask over the cap 2.1 (60 coin per prestige)
