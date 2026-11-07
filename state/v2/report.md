# v2 shadow report

Turn 13849, 2026-11-07 10:09. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,356, prestige 3,373 (253 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 5, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 507 | 0 | 22 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~35 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 607

## Prestige spending, cheapest coin per prestige first

552 turns left: prestige gained now converts 93.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 53.6 | 53.6 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 53.9 | 53.9 |  |
| jousting 3 | arena | 230 | 54.2 | 54.4 | needs a arena (build cost 26,817); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 56.8 | 56.8 |  |
| hold banquet 4 | mansion | 17.5 | 57.0 | 57.0 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 57.4 | 57.4 | thin at home: pasties, cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.6 | 57.6 | thin at home: wine, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 58.6 | 58.6 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 58.8 | 58.8 | thin at home: pasties, wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 59.3 | 59.3 | thin at home: cheese |
| jousting 2 | arena | 210 | 59.3 | 59.6 | needs a arena (build cost 26,817); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 9 @ 15.6; crew 0.1; est +20 a turn; stock: pasties 9 @ 15.6 (keep 14)
- **Flax Wyrm** on Caillechâtel: pasties buy 6 @ 14.6; crew 0.1; est +16 a turn; stock: pasties 6 @ 14.6 (keep 14)
- best towns now: Rouhomme +31, Bedenis +29, Toqueque +26, Chatgnan +24, Clairas +24
- Rouhomme would trade: pasties buy 9 @ 14.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.21 | 0.50 (51/turn) | beer 92 (3.46->5.51), garments 10 (18.76->24.7), cured fish 6 (24.99->28.31), glass ingots 1 (66.67->71.25) | candles 1 (78.23->86), cheese 5 (7.25->8.64), thread 10 (4.73->5.35), flax fibres 4 (5.17->5.9) | +253 |
| Hofkirchen | 991 | 0.32 | 0.90 (92/turn) | beer 98 (3.46->5.7), nets 6 (33.6->39.33), blades 6 (15.33->17.1), hinges 1 (39.27->47.5) | cheese 5 (5.78->8.64), candles 1 (79.8->86), nails 2 (5.78->6.65) | +238 |
| Brebronn | 862 | 0.25 | 0.10 (10/turn) | garments 10 (18.76->31.92), wool 2 (12.08->17.67), rope 1 (80->85.02), flax plants 2 (1.43->2.26) | cheese 5 (6.09->8.64), candles 1 (76.12->86), coats 2 (71.4->72.67), wrought iron 1 (10.29->12.16) | +170 |
| Grandgues | 152 | 0.04 | 0.10 (10/turn) | beer 98 (3.46->4.67), garments 10 (18.76->22.04), hinges 1 (39.27->52.25), logs 1 (3.99->7.6) | candles 1 (81.38->86), thread 10 (5.17->5.35), bricks 7 (7.67->8.5) | +165 |
| Pontmont | 341 | 0.09 | 0.10 (10/turn) | looms 1 (609->698.25), garments 10 (18.76->22.61), thread 36 (4.66->5.08), nets 1 (33.6->36.48) | cheese 5 (6.46->8.64), candles 1 (79.8->86), chisels 1 (7.19->8.69), cloth 11 (8.24->8.4) | +162 |

**Best:** Etallaen at about +253 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 4 @ min 3.06 | goal planner: sells 4 a turn at 3.06, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 12.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 94.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.7k (cash + stock at home prices); +60/turn over 6 turns, -35/turn over 24 turns.
- Limits: cash flow >= -306/turn, prestige >= +1.96/turn (values are after 200 tax a turn).
- Today's settings: value +85/turn, cash +75/turn, prestige -1.97/turn - breaks the prestige floor.
- Plan: value -109/turn, cash -104/turn, prestige +1.96/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +152 vs +70, +139 vs +69, +145 vs +76.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +10/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - spinnery 1 1.65 -> 1.59: +1/turn
  - flax farm 1 4.64 -> 4.56: +0/turn
  - sewing shop 1 0.30 -> 0.36: -7/turn
  - weavery 1 0.50 -> 0.60: +9/turn
  - mansion 1 0.00 -> 0.94: -203/turn
- Model check over the last 61 turns: predicted +103/turn for the settings we ran, real +73/turn.
- Worth of one more unit per turn: labour 1.63, thread 4.14, cloth 6.58, flax fibres 4.97, garments 19.00, nets 29.55, beer 2.89, timber 3.26, prestige 55.33, cash 0.00
- Orders it would set: beer sell 4 (v2 none); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Amsdermund (+14/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 438 (+149 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.94 |
| ret | 3 | 0.91 | 0.99 |
| spin | 4 | 1.65 | 1.75 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 547/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.36 (ask 3.3, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.9 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
