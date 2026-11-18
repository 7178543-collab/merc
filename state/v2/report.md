# v2 shadow report

Turn 14117, 2026-11-18 14:13. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,530, prestige 3,604 (484 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 2 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.10 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.10 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 11 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 18 labour expired last turn (~33 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 81.00 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 521, not 621

## Prestige spending, cheapest coin per prestige first

284 turns left: prestige gained now converts 76.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 46.3 | 46.6 | needs a arena (build cost 26,500); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 49.8 | 50.1 | needs a arena (build cost 26,500); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 53.4 | 53.9 | needs a arena (build cost 26,500); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.6 | 54.6 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 59.0 | 59.0 |  |
| jousting 2 | arena | 210 | 58.5 | 59.0 | needs a arena (build cost 26,500); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.7 | 59.7 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.0 | 61.0 | thin at home: cheese, pies |
| hold mass 2 (premium) | cathedral | 360 | 56.2 | 61.1 | needs a cathedral (build cost 293,380); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 2 (meat) | mansion | 6.8 | 61.5 | 61.5 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 61.7 | 61.7 |  |
| hold banquet 3 (pies) | mansion | 8 | 62.9 | 62.9 | thin at home: pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 11 | 134102075 | 0.012 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.08 | - | candles 1, pasties 5 | -155 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 5 @ 78.0, pasties buy 1 @ 16.0; crew 0.1; est +51 a turn; stock: candles 5 @ 78.0 (keep 12); stock: pasties 1 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- best towns now: Hofkirchen +486, Boistot +411, Bordees +392, Cobholme +333, Fulkirch +323
- Hofkirchen would trade: candles buy 5 @ 78.0, furniture buy 41 @ 14.4, pasties buy 1 @ 14.4; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.80 (93/turn) | timber 30 (7.88->11.11), firewood 33 (3.26->6.74), charcoal 19 (3.02->5.18), limestone 3 (15.86->24.7) | copper ingots 2 (17.64->19.95), bricks 4 (7.98->9.97), cloth 3 (10.24->11) | +228 |
| Amsdermund | 1111 | 0.44 | 0.30 (35/turn) | jewellery 6 (96.6->104.5), nets 6 (35.8->38), yarn 11 (4.56->5.22) | cloth 24 (7.35->11), wax 5 (24.78->28.5), thread 24 (4.56->5.5), copper ingots 1 (16.48->19.95) | +172 |
| Pontmont | 341 | 0.10 | 0.70 (81/turn) | timber 43 (7.88->12.54), premium ham 1 (239.4->254.6), dyed cloth 2 (10.92->12.54), blades 1 (21.21->21.85) | furniture 11 (16.38->17.76), copper ingots 2 (16.48->19.95), cloth 10 (10.71->11), garments 2 (28.56->29.4) | +171 |
| Kirchwerp | 1072 | 0.42 | 0.20 (23/turn) | wrought iron 12 (19.11->27.55), slaked lime 2 (8.35->11.4), lead ore 3 (7.25->10.45), dyed cloth 2 (10.92->12.25) | cloth 19 (9.5->11), spinning wheels 1 (243.6->266), copper ingots 2 (14.38->19.95), wax 5 (27.3->28.5) | +169 |
| Fontaux | 411 | 0.13 | 0.70 (81/turn) | timber 28 (7.88->11.97), beer 70 (3.86->4.62), premium ham 1 (239.4->250.8), wine 23 (7.25->7.65) | cloth 10 (9.4->11), copper ingots 2 (15.75->19.95), resin 3 (3.34->3.7) | +143 |

**Best:** Grandgues at about +228 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.86, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 6 = 4.3 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 10 @ min 21 | goal planner: sells 10 at 21 (v2 had 10 at 28.4) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 21) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.8k (cash + stock at home prices); +108/turn over 6 turns, +70/turn over 24 turns.
- Limits: cash flow >= -397/turn, prestige >= -0.77/turn (values are after 200 tax a turn).
- Today's settings: value +83/turn, cash +47/turn, prestige -2.63/turn - breaks the prestige floor.
- Plan: value +17/turn, cash +25/turn, prestige -0.77/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +353 vs +41, +145 vs +44, +363 vs +47.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bordees: +1/turn
  - ship Flax Wyrm -> Etallaen: +3/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.28: +4/turn
  - ropewalk 1 0.25 -> 0.32: +2/turn
  - sewing shop 1 0.30 -> 0.24: -1/turn
  - weavery 1 0.50 -> 0.39: +8/turn
  - flax farm 1 4.64 -> 4.04: -4/turn
  - retting pit 1 0.91 -> 0.80: -3/turn
  - spinnery 1 1.65 -> 1.41: -13/turn
- Model check over the last 60 turns: predicted +126/turn for the settings we ran, real +42/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.80, beer 3.26, timber 3.38, prestige 60.28, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); grain buy 5 (v2 0); labour buy 29 (v2 21); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Bordees (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Etallaen (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.2/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.68 |
| ret | 3 | 0.91 | 0.94 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 74/77, thread 1050/225, cloth 73/126

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.1; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R7 stale ask: limestone ask 16.4 over the market for 5 turns: the town trades ~7 a turn at 15.1, we sold 0 with 46 over what we keep; floor 21.73 (config sell_floor / unit cost) is at or over the market: Taylor's call
