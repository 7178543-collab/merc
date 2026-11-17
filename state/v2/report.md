# v2 shadow report

Turn 14094, 2026-11-17 15:35. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,822, prestige 3,615 (495 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 9 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.82 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.82 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

307 turns left: prestige gained now converts 78.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.3 | 51.8 | needs a arena (build cost 28,965); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.4 | 53.4 | running |
| jousting 2 | arena | 210 | 56.2 | 56.7 | needs a arena (build cost 28,965); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.7 | 58.7 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 | thin at home: cured fish |
| hold banquet 3 (pies) | mansion | 8 | 60.7 | 60.7 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 60.8 | 60.8 | thin at home: hop beer, stockfish, premium cheese, premium ham |
| hold banquet 3 (fish) | mansion | 7.6 | 61.2 | 61.2 | thin at home: hop beer, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 61.5 | 61.5 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 61.8 | 61.8 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 62.6 | 62.6 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 63.0 | 63.0 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +686, Hofkirchen +492, Gotthafen +443, Vauxvais +387, Essenbrucke +368
- Amsdermund would trade: furniture buy 63 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (114/turn) | timber 37 (8.4->12.73), firewood 36 (2.96->7.17), bread 160 (2.52->3.13), charcoal 19 (2.79->4.71) | bricks 4 (7.93->13.96), furniture 11 (18.69->19.38), coats 1 (72.98->77.42), beer 4 (3.38->3.76) | +383 |
| Amsdermund | 1111 | 0.43 | 0.50 (57/turn) | premium cheese 3 (29.4->31.92), slaked lime 2 (8.98->11.4), grain 2 (2.88->3.78), hides 1 (11.65->12.92) | cloth 24 (5.57->11), furniture 11 (14.18->19.38), dyed cloth 8 (12.6->15.86), tools 16 (4.83->5.79) | +220 |
| Fontaux | 411 | 0.12 | 0.60 (68/turn) | thread 46 (5.15->7.27), timber 29 (8.4->11.49), garments 10 (28.6->31.92), salt 12 (5.51->7.79) | bricks 6 (9.29->13.96), ploughs 1 (70.35->77.42), dyed cloth 8 (15.44->15.86), raw cloth 1 (9.13->9.5) | +211 |
| Kirchwerp | 1072 | 0.41 | 0.70 (80/turn) | jewellery 14 (101.85->104.5), premium cheese 3 (29.4->34.58), thread 91 (5.15->5.7), lead ore 7 (7.61->10.45) | cloth 24 (9.03->11), dyed cloth 8 (13.33->15.86), raw cloth 8 (7.98->9.5), garments 2 (26.25->30.8) | +165 |
| Pontmont | 341 | 0.10 | 1.00 (114/turn) | firewood 20 (2.96->8.88), bread 61 (2.52->3.42), timber 13 (8.4->12.06), wrought iron 2 (18.48->23.75) | furniture 4 (17.75->19.38), cookware 1 (19.95->22.04), tools 6 (5.35->5.79), garments 0 (28.77->30.8) | +163 |

**Best:** Grandgues at about +383 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 5 @ 3.94, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.8) |
| grain | 0 @ 3.7, stop 18 |  | goal planner: buys 0 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 76.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.6 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.3k (cash + stock at home prices); +124/turn over 6 turns, +90/turn over 24 turns.
- Limits: cash flow >= -284/turn, prestige >= -0.81/turn (values are after 200 tax a turn).
- Today's settings: value +104/turn, cash +84/turn, prestige -2.69/turn - breaks the prestige floor.
- Plan: value +25/turn, cash +33/turn, prestige -0.81/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -156 vs +84, -228 vs +87, +290 vs +82 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +4/turn
  - ship Flax Wyrm -> Großmühle: +0/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.30: +4/turn
  - spinnery 1 1.65 -> 1.58: +3/turn
  - flax farm 1 4.64 -> 4.72: -1/turn
  - weavery 1 0.50 -> 0.58: -7/turn
  - sewing shop 1 0.30 -> 0.36: +10/turn
  - mansion 1 0.00 -> 0.45: -103/turn
- Model check over the last 60 turns: predicted +102/turn for the settings we ran, real +17/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.78, thread 4.51, cloth 7.18, flax fibres 5.42, garments 20.74, nets 32.35, beer 3.17, timber 3.43, prestige 60.58, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Essenbrucke (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Großmühle (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +89/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 85/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.82; ask over the cap 2.1 (60 coin per prestige)
