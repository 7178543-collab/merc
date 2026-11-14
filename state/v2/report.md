# v2 shadow report

Turn 14018, 2026-11-14 11:25. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,842, prestige 3,523 (403 free, +2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 107 | 22 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 546 | 0 | 18 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: only 0.8 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.56 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.56 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 546, not 640

## Prestige spending, cheapest coin per prestige first

383 turns left: prestige gained now converts 85.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.4 | 53.4 | running |
| jousting 3 | arena | 230 | 55.2 | 55.6 | needs a arena (build cost 26,915); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.3 | 56.3 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 57.3 | 57.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.3 | 59.3 | thin at home: pasties |
| jousting 2 | arena | 210 | 60.5 | 60.9 | needs a arena (build cost 26,915); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 61.4 | 61.4 | thin at home: hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 61.5 | 61.5 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 62.0 | 62.0 | running |
| hold banquet 4 (premium) | mansion | 20 | 62.5 | 62.5 | thin at home: hop beer, stockfish, premium ham |
| hold mass 2 (premium) | cathedral | 360 | 61.2 | 64.4 | needs a cathedral (build cost 297,950); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 64.9 | 64.9 | thin at home: hop beer, ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.1 (keep 14); best orders clear only 12 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.3 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Karlmoor +29, Hofkirchen +28, Großmühle +26, Herschweig +23, Heilegg +22
- Karlmoor would trade: pasties buy 6 @ 12.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.12 | 0.60 (66/turn) | thread 79 (4.78->7.27), charcoal 20 (2.67->4.73), wine 8 (6.56->7.74), garments 10 (21.2->21.85) | flax fibres 5 (5.35->6.2), cloth 7 (8.45->8.9), candles 1 (84->85.5), cured meat 5 (23.31->23.8) | +231 |
| Grandgues | 152 | 0.04 | 0.70 (77/turn) | timber 42 (8.14->11.59), firewood 29 (3.74->6.46), thread 13 (4.78->5.65), charcoal 20 (2.67->3.44) | rope 3 (77.17->80.27), cloth 7 (8.51->8.9), garments 2 (22.47->23.4), cured meat 6 (23.52->23.8) | +200 |
| Blanans | 297 | 0.09 | 0.70 (77/turn) | timber 42 (8.14->12.44), cheese 14 (7.77->10.26), flour 2 (19.01->21.09), bricks 8 (6.67->8.5) | cloth 12 (7.56->8.9), dyed cloth 6 (10.71->11.78), garments 2 (22.68->23.4), flax fibres 2 (5.93->6.2) | +185 |
| Clairlond | 1288 | 0.52 | 0.30 (33/turn) | garments 10 (21.2->25.27), premium ham 1 (258.3->286.9), varnish 2 (19.95->20.9), cured fish 3 (22.68->23.75) | spinning wheels 1 (186.9->224.2), butter 1 (73.5->76.47), flax fibres 6 (5.06->6.2), tools 17 (5.3->5.89) | +102 |
| Darmwald | 1022 | 0.37 | 0.80 (88/turn) | garments 10 (21.2->25.08), charcoal 20 (2.67->6.74), beer 3 (3.66->5.61), tiles 2 (5.41->10.92) | cloth 24 (7.35->8.9), cheese 11 (6.3->6.84), candles 1 (85.05->85.5) | +100 |

**Best:** Fontaux at about +231 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 107 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 46) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.6) |
| pasties |  | 1 @ min 12.5 | goal planner: sells 1 a turn at 12.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 82.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.6 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.4k (cash + stock at home prices); -63/turn over 6 turns, -132/turn over 24 turns.
- Limits: cash flow >= -327/turn, prestige >= -0.43/turn (values are after 200 tax a turn).
- Today's settings: value -180/turn, cash -158/turn, prestige +1.99/turn.
- Plan: value -17/turn, cash -5/turn, prestige -0.43/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -176 vs -143, -155 vs -159, +27 vs -150.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +1/turn
  - ship Flax Wyrm -> Disscester: +1/turn
  - mansion 1 1.00 -> 0.42: +147/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.33: -2/turn
  - retting pit 1 0.91 -> 0.83: +2/turn
  - flax farm 1 4.64 -> 4.13: +5/turn
  - weavery 1 0.50 -> 0.39: -8/turn
  - sewing shop 1 0.30 -> 0.23: +10/turn
  - ropewalk 1 0.25 -> 0.00: -24/turn
- Model check over the last 59 turns: predicted -15/turn for the settings we ran, real +18/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.36, beer 3.21, timber 3.49, prestige 59.30, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 2 (v2 3); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 46); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.27, worth +9/turn.
- Ship linen snake: Grandgues -> Etallaen (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Disscester (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 421 (+132 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.26 |
| ret | 3 | 0.91 | 0.85 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 113/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.56; ask over the cap 2.1 (60 coin per prestige)
