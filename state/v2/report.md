# v2 shadow report

Turn 14100, 2026-11-17 21:10. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,742, prestige 3,599 (479 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.02 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.02 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~33 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 521, not 621

## Prestige spending, cheapest coin per prestige first

301 turns left: prestige gained now converts 78.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.3 | 52.8 | needs a arena (build cost 28,200); thin at home: swords, protection, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 55.2 | 55.2 | running |
| jousting 2 | arena | 210 | 57.2 | 57.8 | needs a arena (build cost 28,200); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 59.2 | 59.2 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 59.8 | 59.8 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 61.1 | 61.1 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 61.3 | 61.3 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 61.3 | 61.3 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 61.8 | 61.8 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 62.3 | 62.3 |  |
| hold banquet 4 (premium) | mansion | 20 | 62.6 | 62.6 | thin at home: hop beer, stockfish, premium cheese, premium ham |
| hold mass 2 (premium) | cathedral | 360 | 58.4 | 63.0 | needs a cathedral (build cost 301,260); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0.34 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.0 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +708, Gotthafen +463, Vauxvais +406, Chatgnan +361, Fulkirch +317
- Amsdermund would trade: furniture buy 65 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~117 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.80 (94/turn) | timber 25 (8.35->12.73), firewood 33 (3.17->6.08), charcoal 19 (3.02->4.35), limestone 5 (20.27->24.7) | bricks 4 (7.61->10.54), candles 1 (84->89), medicine 1 (152.25->157.7), tools 4 (5.08->5.94) | +202 |
| Amsdermund | 1111 | 0.45 | 0.30 (35/turn) | wine 15 (7.09->9.5), chisels 4 (12.92->17.1), paper 2 (28.56->32.3), hides 1 (11.03->15.29) | cloth 24 (7.3->11.2), medicine 1 (149.1->157.7), garments 2 (26.25->29.4), nails 3 (6.3->8.26) | +170 |
| Hofkirchen | 991 | 0.37 | 0.70 (82/turn) | lead ore 4 (6.2->14.25), wine 8 (7.09->8.17), lead bars 5 (13.12->14.54) | flax fibres 28 (5.62->7.3), jewellery 8 (84->86.92), dyed cloth 9 (13.65->15.77), wrought iron 4 (13.55->17.67) | +165 |
| Pontmont | 341 | 0.11 | 1.00 (117/turn) | firewood 25 (3.17->8.55), timber 18 (8.35->12.63), garments 4 (28->35.15), flour 0 (20.37->25.65) | tools 9 (5.46->5.94), medicine 0 (153.3->157.7), candles 0 (87.67->89) | +148 |
| Kirchwerp | 1072 | 0.42 | 0.40 (47/turn) | light armour 4 (98.7->112.1), honey 5 (8.93->13.21), lead ore 8 (6.2->10.45), hides 1 (11.03->12.73) | flax fibres 28 (5.62->7.3), wrought iron 4 (14.7->17.67), tools 19 (5.02->5.94), belts 2 (32.55->35.72) | +147 |

**Best:** Grandgues at about +202 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.94, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.2) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 21) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.9k (cash + stock at home prices); +91/turn over 6 turns, +73/turn over 24 turns.
- Limits: cash flow >= -323/turn, prestige >= -0.75/turn (values are after 200 tax a turn).
- Today's settings: value +91/turn, cash +70/turn, prestige -2.61/turn - breaks the prestige floor.
- Plan: value +16/turn, cash +25/turn, prestige -0.75/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +227 vs +67, +230 vs +82, +104 vs +70.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +7/turn
  - ship Flax Wyrm -> Vauxvais: +2/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - spinnery 1 1.65 -> 1.38: +5/turn
  - net maker 0.00 -> 0.28: +1/turn
  - retting pit 1 0.91 -> 0.82: +1/turn
  - flax farm 1 4.64 -> 4.13: +3/turn
  - weavery 1 0.50 -> 0.41: -28/turn
  - mansion 1 0.00 -> 0.44: -87/turn
- Model check over the last 57 turns: predicted +128/turn for the settings we ran, real +35/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.73, beer 3.21, timber 3.44, prestige 60.38, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 21); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Brunnham (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 82/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.02; ask over the cap 2.1 (60 coin per prestige)
