# v2 shadow report

Turn 14276, 2026-11-25 05:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,643, prestige 3,721 (601 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 117 | 34 | 12 | 0 | 0 | sell 3, sell @ 3.88; stop 116, buy 39, buy @ 4.14 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 35, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 546 | 0 | 18 | buy 64, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~35 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 97 over real use lately; planning 549, not 646

## Prestige spending, cheapest coin per prestige first

125 turns left: prestige gained now converts 46.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 47.4 | 48.3 | needs a arena (build cost 31,360); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 50.9 | 51.9 | needs a arena (build cost 31,360); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 58.2 | 58.2 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 60.3 | 60.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 60.6 | 60.6 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 60.8 | 60.8 |  |
| jousting 3 | arena | 230 | 59.4 | 61.1 | needs a arena (build cost 31,360); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 66.6 | 66.6 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 65.1 | 67.0 | needs a arena (build cost 31,360); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 5 | mansion | 22 | 67.6 | 67.6 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 2 (meat) | mansion | 6.8 | 67.7 | 67.7 |  |
| hold banquet 4 (premium) | mansion | 20 | 69.0 | 69.0 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 14.6 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Heilegg +64, Bordetes +60, Orlesailles +58, Clairas +36, Hofkirchen +34
- Heilegg would trade: beer sell 17 @ 6.2, cured meat buy 3 @ 23.6, pasties buy 6 @ 13.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~127 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.50 (63/turn) | bread 179 (2.69->3.8), charcoal 19 (2.33->4.99), wine 13 (6.67->9.07), beer 17 (4->5.84) | cloth 3 (11.97->14.91), honey 4 (11.23->13.11), garments 2 (29.61->30.6), thread 6 (5.57->5.9) | +325 |
| Cobholme | 1564 | 0.79 | 0.40 (51/turn) | premium cheese 3 (36.12->38) | sculptures 1 (2478->2736), cloth 6 (10.82->14.91), honey 4 (9.55->13.11), cured meat 3 (23.94->27.4) | +271 |
| Kirchwerp | 1072 | 0.46 | 0.40 (51/turn) | tools 24 (6.56->11.21), garments 10 (30.2->38), wine 13 (6.67->10.54), dyed cloth 10 (18.9->19.57) | honey 4 (11.34->13.11), cured meat 3 (24.99->27.4), wrought iron 3 (15.44->15.96) | +231 |
| Heilegg | 826 | 0.29 | 0.40 (51/turn) | wine 20 (6.67->9.5), dyed cloth 10 (18.9->22.8), beer 17 (4->6.6), silver bars 1 (289.8->307.8) | cloth 6 (13.23->14.91), cured meat 3 (24.36->27.4), honey 3 (11.13->13.11), yarn 18 (5.88->6.46) | +224 |
| Dortgart | 1045 | 0.44 | 0.20 (25/turn) | silver bars 1 (289.8->326.8), dyed cloth 10 (18.9->22.8), tools 20 (6.56->7.74), garments 10 (30.2->31.35) | cloth 6 (10.03->14.91), yarn 17 (5.19->6.46), honey 4 (9.71->13.11), cured meat 3 (24.99->27.4) | +161 |

**Best:** Grandgues at about +325 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 24 @ min 3.58 | makes 19.3, uses 4.2, holds 117 (keeps 0): sells the surplus + 9/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.95 | goal planner: sells 2 a turn at 0.95, keeps 219 (no one offered it) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 49) |
| light armour | 1 @ 100, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 77.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.6k (cash + stock at home prices); +82/turn over 6 turns, -35/turn over 24 turns.
- Limits: cash flow >= -277/turn, prestige >= -1.26/turn (values are after 200 tax a turn).
- Today's settings: value -175/turn, cash -156/turn, prestige +1.19/turn.
- Plan: value +19/turn, cash +28/turn, prestige -1.26/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -103 vs -181, +22 vs -196, -138 vs -187.
- Route sales counted at most (what the ships really sold, a turn): beer 2.3, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +53/turn
  - ship Flax Wyrm -> Heilegg: +3/turn
  - mansion 1 1.00 -> 0.42: +170/turn
  - net maker 0.00 -> 0.28: +7/turn
  - spinnery 1 1.65 -> 1.35: -1/turn
  - retting pit 1 0.91 -> 0.81: +1/turn
  - flax farm 1 4.64 -> 3.81: +11/turn
  - weavery 1 0.50 -> 0.41: -28/turn
- Model check over the last 59 turns: predicted -146/turn for the settings we ran, real -36/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 33.09, beer 3.25, timber 3.69, prestige 66.97, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 49); light armour buy 1 (v2 None); meat buy 0 (v2 None)
- Ship linen snake: Grandgues -> Donaunieder (+39/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Heilegg (+5/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 83/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R1: prestige rate -0.91 a turn vs 12-turn median +1.19; likely: dry slot: meat
