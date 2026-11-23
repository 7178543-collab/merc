# v2 shadow report

Turn 14237, 2026-11-23 14:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,983, prestige 3,679 (559 free, +1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 83 | 0 | 19 | 0 | 0 | min_holding 58, sell 1, sell @ 3.16 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 8 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 5 | 8 | 8 | 1 | 0 | stop 19, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 562 | 0 | 2 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **grain**: brewery 1 ran short of grain (buy is live (5 @ 3.7), 8 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.6 turns of grain left and buying 5 (need 18) -> v2: buy 18

## Tuning

- **cured meat**: home ask 32.80 is above our ceiling 29.00 and last turn bought 7 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 58.5 coin per prestige at mansion, vs 72.6 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 106 over real use lately; planning 562, not 655

## Prestige spending, cheapest coin per prestige first

164 turns left: prestige gained now converts 56.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| jousting 3 (premium) | arena | 420 | 52.0 | 52.5 | needs a arena (build cost 25,702); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.5 | 55.4 | needs a arena (build cost 25,702); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 55.8 | 56.4 | needs a arena (build cost 25,702); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.2 | 57.2 | thin at home: beer |
| hold banquet 2 (fish) | mansion | 6.8 | 58.5 | 58.5 |  |
| jousting 2 | arena | 210 | 59.7 | 60.7 | needs a arena (build cost 25,702); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 63.9 | 63.9 | thin at home: hop beer, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 64.6 | 64.6 |  |
| hold banquet 5 | mansion | 22 | 64.9 | 64.9 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 65.2 | 65.2 | thin at home: hop beer, stockfish |
| hold banquet 4 | mansion | 17.5 | 66.8 | 66.8 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 21.0, pasties buy 3 @ 16.4; crew 0.1; est +68 a turn; stock: pasties 3 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: cured meat buy 6 @ 26.8, pasties buy 3 @ 12.0; crew 0.1; est +47 a turn; stock: pasties 3 @ 12.0 (keep 14)
- best towns now: Gottweiler +69, Grandgues +68, Caillechâtel +47, Friedwerp +40, Clairas +38
- Gottweiler would trade: cured meat buy 6 @ 21.0, pasties buy 2 @ 14.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (52/turn) | bread 191 (2.5->2.98), timber 28 (7.67->9.97), charcoal 19 (2.14->4.18), logs 2 (5.25->7.98) | cured meat 6 (21.63->32.8), dyed cloth 6 (15.96->18.62), bricks 10 (7.51->9.4), cloth 9 (10.71->11.3) | +259 |
| Vauxvais | 204 | 0.06 | 0.50 (52/turn) | grain 98 (3.02->4.39), charcoal 19 (2.14->3.13), bread 165 (2.5->2.7), wax 5 (28.98->30.02) | cloth 24 (10.34->11.3), cured meat 5 (28.77->32.8), bricks 5 (6.62->9.4), flax fibres 6 (6.09->7.5) | +217 |
| Pontmont | 341 | 0.10 | 0.50 (52/turn) | timber 31 (7.67->11.21), cookware 9 (29.4->34.2), tar 8 (10.13->10.92), clay 1 (4.14->11.97) | cloth 9 (8.51->11.3), cured meat 6 (29.82->32.8), flax fibres 9 (5.78->7.5), dyed cloth 3 (16.48->18.62) | +184 |
| Neuborn | 780 | 0.22 | 1.00 (104/turn) | grain 20 (3.02->5.7), bread 31 (2.5->4.46), firewood 6 (2.18->12.54), timber 6 (7.67->14.34) | cloth 1 (8.03->11.3), cured meat 0 (30.66->32.8), cheese 1 (5.78->6.93), garments 0 (24.36->28) | +164 |
| Clairas | 374 | 0.10 | 1.00 (104/turn) | firewood 27 (2.18->6.41), thread 16 (4.88->5.98), charcoal 19 (2.14->3.59), wine 4 (6.62->6.79) | cured meat 6 (27.72->32.8), cloth 15 (9.35->11.3), flax fibres 15 (6.25->7.5), dyed cloth 6 (16.07->18.62) | +160 |

**Best:** Grandgues at about +259 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ ?, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 83 = 4.3 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 10 = 1.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.8) |
| grain | 7 @ 3.7, stop 27 |  | goal planner: buys 7 a turn for today's rates, keeps up to 27 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 62) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 42.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 80.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.1k (cash + stock at home prices); +52/turn over 6 turns, -85/turn over 24 turns.
- Limits: cash flow >= -416/turn, prestige >= -1.08/turn (values are after 200 tax a turn).
- Today's settings: value -112/turn, cash -114/turn, prestige +1.41/turn.
- Plan: value +52/turn, cash +53/turn, prestige -1.08/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +188 vs -170, -126 vs -165, -238 vs -174.
- Route sales counted at most (what the ships really sold, a turn): beer 2.0, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship Flax Wyrm -> Angefont: +0/turn
  - mansion 1 1.00 -> 0.41: +135/turn
  - net maker 0.00 -> 0.29: +10/turn
  - spinnery 1 1.65 -> 1.45: +3/turn
  - retting pit 1 0.91 -> 0.86: +2/turn
  - flax farm 1 4.64 -> 4.32: +1/turn
  - weavery 1 0.50 -> 0.60: -8/turn
  - sewing shop 1 0.30 -> 0.36: +14/turn
- Model check over the last 59 turns: predicted -158/turn for the settings we ran, real +53/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.61, thread 4.05, cloth 6.46, flax fibres 4.80, garments 18.70, nets 29.67, beer 2.95, timber 3.29, prestige 55.41, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 7 (v2 18); labour buy 64 (v2 62); light armour buy 1 (v2 None)
- Ship linen snake: stays on Grandgues (worth +29/turn).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 84/77, thread 1050/228, cloth 73/128

## Self-diagnosis

Nothing found this run.
