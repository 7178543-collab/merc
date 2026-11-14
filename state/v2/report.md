# v2 shadow report

Turn 14008, 2026-11-14 01:32. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,257, prestige 3,509 (389 free, +2.1/turn).

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
| labour | 64 | 64 | 545 | 0 | 19 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.04 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.04 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 19 labour expired last turn (~37 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 545, not 643

## Prestige spending, cheapest coin per prestige first

393 turns left: prestige gained now converts 86.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 56.7 | 56.7 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 57.2 | 57.2 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.2 | 58.2 | thin at home: wine |
| jousting 3 | arena | 230 | 57.8 | 58.2 | needs a arena (build cost 28,049); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.9 | 58.9 | thin at home: wine |
| hold mass 2 (premium) | cathedral | 360 | 59.1 | 61.9 | needs a cathedral (build cost 274,490); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 (pies) | mansion | 18 | 62.3 | 62.3 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 62.9 | 62.9 | thin at home: hop beer, wine, stockfish |
| jousting 2 | arena | 210 | 63.3 | 63.7 | needs a arena (build cost 28,049); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 63.8 | 63.8 | thin at home: hop beer |
| hold banquet 3 (fish) | mansion | 7.6 | 64.8 | 64.8 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 65.7 | 65.7 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.1 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.4 (keep 14); best orders clear only 15 a turn after crew: ship stays at 0
- best towns now: Heidlowe +34, Hofkirchen +28, Gottweiler +23, Kirchwerp +22, Karlmoor +21
- Heidlowe would trade: cured meat buy 6 @ 21.0, pasties buy 2 @ 13.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clairas | 374 | 0.12 | 0.70 (81/turn) | timber 28 (8.61->10.83), charcoal 20 (2.65->4.07), tools 15 (5.72->6.22), pasties 4 (12.92->13.49) | windows 1 (603.75->788.5), cloth 10 (7.88->8.75), furniture 14 (15.86->16.72), flax fibres 6 (5.99->6.35) | +230 |
| Karlmoor | 787 | 0.24 | 0.10 (12/turn) | dyed cloth 1 (10.71->11.4), flax plants 1 (1.39->2.15) | windows 1 (645.75->788.5), cured meat 6 (23.94->26.6), wrought iron 4 (13.02->14.72), butter 2 (71.92->74.1) | +167 |
| Blanans | 297 | 0.09 | 0.70 (81/turn) | timber 39 (8.61->11.69), limestone 4 (20.89->28.5), tools 16 (5.72->6.46), cheese 11 (7.61->8.17) | tackles 2 (155.4->171), cloth 13 (7.56->8.75), flax fibres 1 (6.14->6.35), garments 2 (23.1->23.4) | +145 |
| Grandgues | 152 | 0.05 | 0.30 (35/turn) | timber 24 (8.61->12.06), charcoal 20 (2.65->3.84), pasties 6 (12.92->14.25), lead ore 3 (8.45->9.31) | cured meat 6 (24.36->26.6), tackles 1 (158.55->171), cloth 10 (7.98->8.75), windows 1 (782.25->788.5) | +127 |
| Hofkirchen | 991 | 0.36 | 0.60 (69/turn) | flax fibres 2 (5.7->6.46) | spinning wheels 4 (220.5->233.7), cloth 24 (7.35->8.75), furniture 23 (14.38->16.72), cured meat 6 (23.31->26.6) | +122 |

**Best:** Clairas at about +230 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 107 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 87.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 6 = 1.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.85 | goal planner: sells 2 a turn at 5.85, keeps 85 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.2) |
| grain | 8 @ 3.7, stop 30 |  | goal planner: buys 8 a turn for today's rates, keeps up to 30 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 45) |
| light armour | 1 @ 97.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.8) |
| pasties |  | 1 @ min 11.9 | goal planner: sells 1 a turn at 11.9, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 1 = 4.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.5k (cash + stock at home prices); -179/turn over 6 turns, +6/turn over 24 turns.
- Limits: cash flow >= -386/turn, prestige >= -0.37/turn (values are after 200 tax a turn).
- Today's settings: value -189/turn, cash -161/turn, prestige +2.07/turn.
- Plan: value -17/turn, cash -4/turn, prestige -0.37/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -19 vs -180, -214 vs -162, -102 vs -167.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +2/turn
  - ship Flax Wyrm -> Chatgnan: +3/turn
  - mansion 1 1.00 -> 0.42: +150/turn
  - spinnery 1 1.65 -> 1.35: +5/turn
  - retting pit 1 0.91 -> 0.84: +2/turn
  - flax farm 1 4.64 -> 4.24: +4/turn
  - net maker 0.00 -> 0.29: +1/turn
  - weavery 1 0.50 -> 0.38: -8/turn
  - sewing shop 1 0.30 -> 0.22: +14/turn
  - ropewalk 1 0.25 -> 0.00: -24/turn
- Model check over the last 60 turns: predicted +34/turn for the settings we ran, real -17/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.25, beer 3.17, timber 3.53, prestige 60.55, cash 0.00
- Orders it would set: bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 64 (v2 45); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +9/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 420 (+131 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.21 |
| ret | 3 | 0.91 | 0.84 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 116/77, thread 1052/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.04; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1052 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
