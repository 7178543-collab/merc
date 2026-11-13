# v2 shadow report

Turn 14006, 2026-11-13 23:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,573, prestige 3,505 (385 free, +2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 27 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 546 | 0 | 18 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.16 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.16 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~35 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 89 over real use lately; planning 557, not 646

## Prestige spending, cheapest coin per prestige first

395 turns left: prestige gained now converts 86.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 56.3 | 56.7 | needs a arena (build cost 27,975); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.6 | 57.6 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 57.9 | 57.9 |  |
| maintain 1 | park | 0.5 | 57.9 | 57.9 | running |
| hold banquet 2 (pies) | mansion | 7 | 59.9 | 59.9 |  |
| jousting 2 | arena | 210 | 61.7 | 62.1 | needs a arena (build cost 27,975); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 59.9 | 62.7 | needs a cathedral (build cost 274,860); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 (pies) | mansion | 18 | 62.8 | 62.8 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 63.2 | 63.2 | thin at home: hop beer, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 65.0 | 65.0 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 65.2 | 65.2 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 65.6 | 65.6 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.1 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 8 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +25, Gottweiler +25, Orlesailles +22, Großmühle +22, Gotthafen +20
- Hofkirchen would trade: cured meat buy 6 @ 23.0, pasties buy 3 @ 14.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~117 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.30 (35/turn) | timber 27 (8.61->12.06), charcoal 20 (2.65->3.8), nets 4 (32.4->35.15), thread 12 (4.84->5.65) | cured meat 6 (24.36->26.8), dyed cloth 7 (10.92->12.25), garments 2 (22.68->25.6), spinning wheels 1 (210->214.7) | +151 |
| Bordetes | 831 | 0.27 | 0.50 (58/turn) | cured fish 9 (22.68->27.74), charcoal 20 (2.65->6.08), nets 2 (32.4->36.1), rope 1 (76->80.27) | cloth 24 (7.35->8.4), spinning wheels 1 (200.55->214.7), tools 24 (5.15->5.89), dyed cloth 7 (10.71->12.25) | +140 |
| Blanans | 297 | 0.09 | 0.60 (70/turn) | timber 39 (8.61->11.59), nets 6 (32.4->35.91), limestone 2 (17.96->28.5), cheese 11 (7.46->8.03) | cloth 18 (7.56->8.4), dyed cloth 5 (11.13->12.25), garments 2 (23.1->25.6), salt 3 (5.12->5.56) | +139 |
| Essenbrucke | 584 | 0.18 | 0.30 (35/turn) | nets 2 (32.4->40.66), cured fish 5 (22.68->25.08), rope 1 (76->77.9), wine 2 (6.51->7.36) | furniture 21 (13.23->16.43), windows 1 (756->788.5), cured meat 6 (24.36->26.8), belts 1 (24.15->32.49) | +138 |
| Kirchwerp | 1072 | 0.42 | 0.60 (70/turn) | thread 91 (4.84->5.7), cheese 20 (7.46->9.17), nets 4 (32.4->37.62), lead bars 8 (13.33->15.77) | cloth 24 (7.56->8.4), dyed cloth 7 (10.71->12.25), garments 2 (22.26->25.6) | +127 |

**Best:** Grandgues at about +151 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 108 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 12 = 2.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.8) |
| grain | 7 @ 3.7, stop 27 |  | goal planner: buys 7 a turn for today's rates, keeps up to 27 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 57) |
| light armour | 1 @ 97.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| pasties |  | 1 @ min 13.3 | goal planner: sells 1 a turn at 13.3, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 74.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.1k (cash + stock at home prices); -80/turn over 6 turns, +33/turn over 24 turns.
- Limits: cash flow >= -399/turn, prestige >= -0.35/turn (values are after 200 tax a turn).
- Today's settings: value -196/turn, cash -162/turn, prestige +2.09/turn.
- Plan: value -22/turn, cash -4/turn, prestige -0.35/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -214 vs -161, -163 vs -184, -19 vs -180.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +4/turn
  - ship Flax Wyrm -> Etallaen: +1/turn
  - mansion 1 1.00 -> 0.42: +148/turn
  - spinnery 1 1.65 -> 1.35: +6/turn
  - retting pit 1 0.91 -> 0.85: +2/turn
  - flax farm 1 4.64 -> 4.26: +4/turn
  - net maker 0.00 -> 0.28: -0/turn
  - weavery 1 0.50 -> 0.39: -4/turn
  - sewing shop 1 0.30 -> 0.23: +11/turn
- Model check over the last 60 turns: predicted +44/turn for the settings we ran, real -10/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.34, beer 3.18, timber 3.38, prestige 60.57, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 7 (v2 0); labour buy 64 (v2 57); light armour buy 1 (v2 None); pasties sell 1 (v2 none); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Essenbrucke (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Etallaen (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 419 (+130 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.14 |
| ret | 3 | 0.91 | 0.83 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 122/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 7.4 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.54; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.16; ask over the cap 2.1 (60 coin per prestige)
