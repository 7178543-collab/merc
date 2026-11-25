# v2 shadow report

Turn 14277, 2026-11-25 06:09. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,624, prestige 3,720 (600 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 109 | 0 | 12 | 0 | 0 | sell 16, sell @ 3.58 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 3 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 546 | 0 | 18 | buy 64, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~35 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: home ask 2.46 is above our ceiling 2.40 and last turn bought 3 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 59.1 coin per prestige at mansion, vs 70.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (pies)**: hold banquet 2 (pies) costs 59.9 coin per prestige at mansion, vs 70.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 97 over real use lately; planning 549, not 646

## Prestige spending, cheapest coin per prestige first

124 turns left: prestige gained now converts 46.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.3 | 51.3 | needs a arena (build cost 31,856); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.0 | 55.0 | needs a arena (build cost 31,856); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 58.2 | 58.2 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 59.1 | 59.1 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.9 | 59.9 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 60.8 | 60.8 |  |
| jousting 3 | arena | 230 | 59.8 | 61.6 | needs a arena (build cost 31,856); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 65.7 | 65.7 | thin at home: hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 66.4 | 66.4 |  |
| hold banquet 5 | mansion | 22 | 66.8 | 66.8 | thin at home: hop beer, stockfish, sculptures |
| jousting 2 | arena | 210 | 65.5 | 67.4 | needs a arena (build cost 31,856); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 68.6 | 68.6 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.9 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 14 a turn after crew: ship stays at 0
- best towns now: Bordetes +74, Orlesailles +71, Heilegg +69, Neuborn +52, Friedwerp +44
- Bordetes would trade: beer sell 16 @ 6.55, cured meat buy 3 @ 26.0, pasties buy 8 @ 13.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~125 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Gotthafen | 964 | 0.38 | 0.30 (38/turn) | arms 7 (32.13->40.28), dyed cloth 8 (19.11->21.85), glass ingots 2 (71.92->73.15), wine 3 (6.83->7.5) | sculptures 1 (2184->2736), cloth 11 (10.61->13.2), cookware 5 (21->25.65), honey 4 (9.61->13.39) | +699 |
| Grandgues | 152 | 0.05 | 0.50 (63/turn) | bread 182 (2.67->4.31), charcoal 20 (2.33->5.46), beer 16 (3.9->6.79), dyed cloth 10 (19.11->23.37) | honey 3 (12.29->13.39), candles 1 (91.35->93.5), cured meat 3 (27.93->28.2) | +506 |
| Hanbrücken | 531 | 0.18 | 0.20 (25/turn) | tools 10 (6.93->7.55) | sculptures 1 (2436->2736), cloth 24 (10.5->13.2), cured meat 3 (23.73->28.2), honey 3 (10.5->13.39) | +377 |
| Brunnham | 1281 | 0.59 | 0.30 (38/turn) | garments 10 (29->32.87), ploughs 3 (81.38->92.62), nets 6 (35.8->39.33), dyed cloth 10 (19.11->20.9) | sculptures 1 (2478->2736), honey 4 (10.82->13.39), candles 1 (86.62->93.5), cured meat 3 (25.83->28.2) | +336 |
| Briclives | 1041 | 0.43 | 0.20 (25/turn) | garments 10 (29->35.15) | sculptures 1 (2478->2736), candles 1 (88.2->93.5), cured meat 2 (24.78->28.2), honey 1 (11.45->13.39) | +311 |

**Best:** Gotthafen at about +699 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 23 @ min 3.58 | goal planner: sells 23 at 3.58 (v2 had 23 at 3.8) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.95 | goal planner: sells 2 a turn at 0.95, keeps 219 (no one offered it) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 28.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 49) |
| light armour | 1 @ 100, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 80.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.6k (cash + stock at home prices); +105/turn over 6 turns, -38/turn over 24 turns.
- Limits: cash flow >= -276/turn, prestige >= -1.25/turn (values are after 200 tax a turn).
- Today's settings: value -171/turn, cash -155/turn, prestige +1.19/turn.
- Plan: value +20/turn, cash +27/turn, prestige -1.25/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +22 vs -196, -138 vs -187, -19 vs -156.
- Route sales counted at most (what the ships really sold, a turn): beer 2.3, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bremcop: +7/turn
  - ship Flax Wyrm -> Kirchwerp: +21/turn
  - mansion 1 1.00 -> 0.42: +166/turn
  - net maker 0.00 -> 0.28: +7/turn
  - spinnery 1 1.65 -> 1.35: -1/turn
  - retting pit 1 0.91 -> 0.81: +1/turn
  - flax farm 1 4.64 -> 3.80: +10/turn
  - weavery 1 0.50 -> 0.41: -17/turn
- Model check over the last 59 turns: predicted -146/turn for the settings we ran, real -26/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 33.20, beer 3.24, timber 3.69, prestige 64.15, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 49); light armour buy 1 (v2 None); meat buy 0 (v2 None)
- Ship linen snake: Grandgues -> Bremcop (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Kirchwerp (+8/turn over staying).
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

Buffers: flax fibres 83/77, thread 1049/228, cloth 72/128

## Self-diagnosis

- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R1: prestige rate -0.91 a turn vs 12-turn median +1.19; likely: dry slot: meat
