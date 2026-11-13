# v2 shadow report

Turn 13994, 2026-11-13 11:11. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 15,253, prestige 3,490 (370 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 15 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 508 | 0 | 21 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (15.0/turn) but there is NO buy order, stock 0.0 -> v2: add buy 30
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.64 is above it); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.64 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.20 x9, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 21 labour expired last turn (~38 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 99 over real use lately; planning 508, not 607

## Prestige spending, cheapest coin per prestige first

407 turns left: prestige gained now converts 87.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 55.2 | 55.2 | running |
| jousting 3 | arena | 230 | 56.3 | 56.7 | needs a arena (build cost 27,648); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.5 | 58.5 | thin at home: hop beer, stockfish, pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 59.6 | 59.6 | thin at home: hop beer, stockfish, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 59.8 | 59.8 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 60.0 | 60.0 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 60.6 | 60.6 | thin at home: pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 61.2 | 61.2 | thin at home: hop beer, pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 61.6 | 61.6 | thin at home: hop beer, cured fish |
| hold banquet 4 | mansion | 17.5 | 61.6 | 61.6 | thin at home: hop beer, ham, stockfish, candles |
| jousting 2 | arena | 210 | 61.7 | 62.1 | needs a arena (build cost 27,648); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 61.9 | 64.9 | needs a cathedral (build cost 313,200); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.7 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.4 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~112 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (112/turn) | timber 37 (7.82->12.35), firewood 43 (2.77->6.65), bread 137 (2.65->2.94), wine 8 (7.25->7.69) | cured meat 5 (24.57->27.55), tools 8 (4.91->5.42), copper ingots 0 (19.01->19.76), malt 0 (8.4->8.5) | +304 |
| Vauxvais | 204 | 0.06 | 1.00 (112/turn) | beer 59 (3.89->5.46), firewood 51 (2.77->5.7), charcoal 18 (2.35->4.22), premium cheese 1 (28.98->33.82) | furniture 20 (13.97->14.91), cured meat 6 (26.04->27.55), flax fibres 12 (6.14->6.8), tools 23 (5.15->5.42) | +212 |
| Corstoft | 1496 | 0.66 | 0.10 (11/turn) | tapestries 1 (609->764.75), tools 8 (6.14->7.27) | garments 2 (19.95->23.8), axes 1 (21->22.42), copper ingots 1 (17.75->19.76), copper ore 1 (24.57->28.88) | +165 |
| Etallaen | 774 | 0.23 | 0.30 (34/turn) | beer 64 (3.89->5.79), tapestries 1 (609->631.75), hides 1 (13.02->17.67) | thread 27 (4.73->5.3), cured meat 6 (25.83->27.55), axes 1 (20.58->22.42), copper ingots 1 (17.75->19.76) | +144 |
| Calange | 218 | 0.07 | 0.20 (22/turn) | wrought iron 6 (18.17->26.6), ham 1 (87.15->133), premium garments 1 (127.05->136.8), limestone 2 (20.27->27.36) | cured meat 6 (25.83->27.55), cloth 24 (8.03->8.45), axes 1 (21.21->22.42), thread 8 (5.1->5.3) | +141 |

**Best:** Grandgues at about +304 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 30 @ 3.88, stop 60 | off | a building is stalled on beer: no sell until it runs again |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 2 @ 75.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 4 @ 30.6, stop 13 |  | goal planner: buys 4 a turn for today's rates, keeps up to 13 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.0) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 8) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.6) |
| pasties |  | 1 @ min 17.8 | goal planner: trial sale of an idle pile, 1 a turn at 17.8, keeps 0 (12 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.6k (cash + stock at home prices); +223/turn over 6 turns, +110/turn over 24 turns.
- Limits: cash flow >= -469/turn, prestige >= -0.29/turn (values are after 200 tax a turn).
- Today's settings: value -248/turn, cash -126/turn, prestige +1.64/turn.
- Plan: value -44/turn, cash -40/turn, prestige -0.29/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +229 vs +70, +190 vs +52, +127 vs +51.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.54: +176/turn
  - brewery 1 0.14 -> 0.09: +11/turn
  - spinnery 1 1.65 -> 1.35: +5/turn
  - retting pit 1 0.91 -> 0.85: +2/turn
  - flax farm 1 4.64 -> 4.27: +3/turn
  - net maker 0.00 -> 0.29: -0/turn
  - weavery 1 0.50 -> 0.39: -5/turn
  - sewing shop 1 0.30 -> 0.23: +10/turn
- Model check over the last 60 turns: predicted +106/turn for the settings we ran, real -11/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.15, beer 3.12, timber 3.35, prestige 67.87, cash 0.00
- Orders it would set: bread buy 5 (v2 7); candles buy 2 (v2 None); cured meat buy 4 (v2 None); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 64 (v2 8); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Vauxvais (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1934 coin: +3/turn, payback 645 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 416 (+127 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.95 |
| ret | 3 | 0.91 | 0.79 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 135/77, thread 1055/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.7 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 39 @ 3.76 (ask 3.7, cap 14.4))
- R1: cured meat slot dry: 1.2 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 30.6, home ask 30.0; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.64; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1055 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
