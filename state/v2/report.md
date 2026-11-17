# v2 shadow report

Turn 14095, 2026-11-17 16:41. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,548, prestige 3,612 (492 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 7 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
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

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 608

## Prestige spending, cheapest coin per prestige first

306 turns left: prestige gained now converts 78.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.1 | 52.7 | needs a arena (build cost 29,987); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.0 | 54.0 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 56.5 | 56.5 |  |
| jousting 2 | arena | 210 | 57.1 | 57.7 | needs a arena (build cost 29,987); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 58.8 | 58.8 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 59.0 | 59.0 |  |
| hold banquet 3 (pies) | mansion | 8 | 59.1 | 59.1 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 60.4 | 60.4 | thin at home: pies |
| hold banquet 1 (meat) | mansion | 4.2 | 62.2 | 62.2 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 62.6 | 62.6 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 62.8 | 62.8 | thin at home: hop beer, stockfish, premium cheese, premium ham |
| hold banquet 2 (meat) | mansion | 6.8 | 63.1 | 63.1 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +659, Chatgnan +508, Hofkirchen +431, Gotthafen +430, Clairlond +288
- Amsdermund would trade: furniture buy 61 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (104/turn) | timber 38 (7.98->12.73), bread 161 (2.52->3.15), firewood 30 (2.96->6.65), charcoal 19 (2.86->4.71) | bricks 3 (8.09->13.68), furniture 10 (18.69->20.14), tools 11 (5.67->6.22), coats 1 (76.12->79.33) | +379 |
| Amsdermund | 1111 | 0.44 | 0.50 (58/turn) | chisels 4 (12.29->17.1), cured fish 7 (22.68->24.32), wine 12 (7.88->8.55), nets 3 (34.2->35.91) | cloth 24 (5.57->11.5), furniture 10 (14.18->20.14), dyed cloth 8 (12.6->15.77), tools 17 (5->6.22) | +252 |
| Dortgart | 1045 | 0.40 | 0.30 (35/turn) | nets 6 (34.2->37.81) | tapestries 1 (630->798), furniture 10 (14.7->20.14), cloth 24 (10.61->11.5), candles 1 (82.42->84) | +235 |
| Boistot | 1230 | 0.52 | 0.40 (46/turn) | yarn 8 (5.99->8.07) | tapestries 1 (651->798), dyed cloth 8 (12.6->15.77), furniture 10 (16.07->20.14), cloth 24 (10.82->11.5) | +201 |
| Fontaux | 411 | 0.13 | 0.80 (93/turn) | timber 30 (7.98->11.59), garments 10 (27.6->32.11), salt 11 (5.41->7.79), thread 49 (5.15->5.65) | bricks 3 (9.35->13.68), tools 17 (5.93->6.22), cloth 10 (11.13->11.5), dyed cloth 8 (15.44->15.77) | +191 |

**Best:** Grandgues at about +379 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 5 @ 3.9, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 0 @ 3.7, stop 18 |  | goal planner: buys 0 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 76.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.6 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.6k (cash + stock at home prices); +174/turn over 6 turns, +128/turn over 24 turns.
- Limits: cash flow >= -273/turn, prestige >= -0.80/turn (values are after 200 tax a turn).
- Today's settings: value +88/turn, cash +67/turn, prestige -2.67/turn - breaks the prestige floor.
- Plan: value +10/turn, cash +16/turn, prestige -0.80/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -228 vs +87, +290 vs +82, -274 vs +84 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +7/turn
  - ship Flax Wyrm -> Großmühle: +3/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.28: +4/turn
  - spinnery 1 1.65 -> 1.57: +4/turn
  - flax farm 1 4.64 -> 4.75: -1/turn
  - weavery 1 0.50 -> 0.59: -6/turn
  - sewing shop 1 0.30 -> 0.36: +9/turn
  - mansion 1 0.00 -> 0.45: -103/turn
- Model check over the last 60 turns: predicted +107/turn for the settings we ran, real +25/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.80, thread 4.52, cloth 7.22, flax fibres 5.36, garments 20.89, nets 32.57, beer 3.19, timber 3.80, prestige 60.54, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Brunnham (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Großmühle (+3/turn over staying).
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

Buffers: flax fibres 84/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
