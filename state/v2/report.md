# v2 shadow report

Turn 14007, 2026-11-14 00:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,359, prestige 3,507 (387 free, +2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 107 | 27 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 27, buy 7, buy @ 3.7 |
| labour | 64 | 64 | 546 | 0 | 18 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~34 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 546, not 645

## Prestige spending, cheapest coin per prestige first

394 turns left: prestige gained now converts 86.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 56.5 | 56.9 | needs a arena (build cost 28,153); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 57.3 | 57.3 | running |
| hold banquet 2 (pies) | mansion | 7 | 58.3 | 58.3 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 59.8 | 59.8 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.9 | 59.9 | thin at home: cured fish |
| jousting 2 | arena | 210 | 61.9 | 62.3 | needs a arena (build cost 28,153); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 59.9 | 62.6 | needs a cathedral (build cost 274,970); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 (pies) | mansion | 18 | 62.7 | 62.7 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 63.4 | 63.4 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 64.2 | 64.2 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 65.9 | 65.9 |  |
| hold banquet 4 | mansion | 17.5 | 67.1 | 67.1 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 23.6, pasties buy 3 @ 16.4; crew 0.1; est +17 a turn; stock: pasties 3 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.1 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +42, Gottweiler +26, Orlesailles +23, Darmwald +22, Magdeach +20
- Hofkirchen would trade: cured meat buy 6 @ 20.4, pasties buy 3 @ 14.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~117 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.30 (35/turn) | timber 23 (8.61->12.06), charcoal 20 (2.27->3.53), pasties 7 (12.5->14.63), nets 4 (32.6->35.53) | cured meat 6 (24.36->27), cloth 10 (7.98->8.65), windows 1 (782.25->788.5), tools 11 (5.46->5.98) | +137 |
| Blanans | 297 | 0.09 | 0.60 (70/turn) | timber 38 (8.61->11.88), limestone 3 (18.27->28.5), nets 5 (32.6->35.91), cheese 11 (7.56->8.12) | cloth 15 (7.56->8.65), cured meat 6 (26.46->27), garments 2 (23.1->23.8), salt 3 (5.1->5.56) | +136 |
| Bordetes | 831 | 0.27 | 0.50 (58/turn) | charcoal 20 (2.27->6.13), cured fish 7 (24.57->27.55), jewellery 3 (110.25->113.05), nets 1 (32.6->41.23) | cloth 24 (7.35->8.65), tools 16 (5.15->5.98), canvas 1 (33.18->34.58), flax fibres 2 (5.25->6.35) | +114 |
| Hofkirchen | 991 | 0.37 | 0.40 (47/turn) | nets 6 (32.6->37.43), flax fibres 2 (5.75->7.65) | cured meat 6 (21->27), cloth 24 (7.35->8.65), cheese 8 (5.25->6.55), cookware 4 (23.73->25.84) | +113 |
| Kleinburgh | 1440 | 0.65 | 0.20 (23/turn) | nets 5 (32.6->38), garments 10 (22.8->24.7), acid 1 (115.5->116.85), hides 2 (13.33->15.11) | windows 1 (735->788.5), cloth 18 (7.56->8.65), salt 3 (4.37->5.56) | +97 |

**Best:** Grandgues at about +137 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 107 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 9 = 1.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 3 @ min 5.75 | goal planner: sells 3 a turn at 5.75, keeps 85 (no one offered it) |
| furniture | 2 @ 16.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.2) |
| grain | 8 @ 3.7, stop 29 |  | goal planner: buys 8 a turn for today's rates, keeps up to 29 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 46) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| pasties |  | 1 @ min 11.7 | goal planner: sells 1 a turn at 11.7, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.8 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.5k (cash + stock at home prices); -146/turn over 6 turns, +24/turn over 24 turns.
- Limits: cash flow >= -390/turn, prestige >= -0.36/turn (values are after 200 tax a turn).
- Today's settings: value -197/turn, cash -167/turn, prestige +2.08/turn.
- Plan: value -24/turn, cash -11/turn, prestige -0.36/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -163 vs -184, -19 vs -180, -214 vs -162.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +16/turn
  - ship Flax Wyrm -> Rouhomme: +1/turn
  - mansion 1 1.00 -> 0.42: +149/turn
  - spinnery 1 1.65 -> 1.35: +6/turn
  - retting pit 1 0.91 -> 0.85: +2/turn
  - flax farm 1 4.64 -> 4.25: +4/turn
  - net maker 0.00 -> 0.29: +1/turn
  - weavery 1 0.50 -> 0.38: -7/turn
  - sewing shop 1 0.30 -> 0.22: +13/turn
  - ropewalk 1 0.25 -> 0.00: -23/turn
- Model check over the last 60 turns: predicted +39/turn for the settings we ran, real -8/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.27, beer 3.18, timber 3.53, prestige 60.58, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 3 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 64 (v2 46); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +9/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Rouhomme (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 419 (+130 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.17 |
| ret | 3 | 0.91 | 0.83 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 119/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 9.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 32.8, home ask 27.0; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
