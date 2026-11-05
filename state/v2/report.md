# v2 shadow report

Turn 13804, 2026-11-05 13:30. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,952, prestige 3,300 (180 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 34 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

597 turns left: prestige gained now converts 95.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 54.1 | 54.1 | thin at home: wine, cured fish, cheese |
| hold banquet 4 (pies) | mansion | 18 | 55.7 | 55.7 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 57.2 | 57.2 | thin at home: wine, cheese, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 57.5 | 57.5 | thin at home: wine, cheese |
| jousting 3 | arena | 230 | 57.3 | 57.5 | needs a arena (build cost 26,048); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 58.4 | 58.4 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 58.6 | 58.6 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.8 | 58.8 | thin at home: wine, ham, stockfish, candles, premium cheese |
| hold sermon 2 (candles) | church | 31 | 54.5 | 58.8 | needs a church (build cost 66,944); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 55.6 | 59.9 | needs a chapel (build cost 30,080); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.0 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.4 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Heilegg +63, Fulkirch +44, Disscester +39, Neuborn +29, Brunnham +27
- Heilegg would trade: pasties buy 14 @ 13.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (50/turn) | charcoal 19 (2.16->6.93), bread 147 (2.31->2.85), timber 24 (6.83->9.59), logs 1 (3.84->10.73) | slaked lime 1 (14.38->16.72), garments 2 (22.05->22.6) | +220 |
| Pontmont | 341 | 0.09 | 0.30 (30/turn) | cured fish 4 (22.68->27.93), charcoal 19 (2.16->3.42), beer 15 (3.24->3.72), raw cloth 10 (7.14->7.69) | slaked lime 4 (6.83->16.72), lead bars 16 (11.55->13.21), tackles 2 (179.55->182.4), garments 2 (20.27->22.6) | +135 |
| Bedenis | 566 | 0.15 | 0.10 (10/turn) | premium ham 1 (252->266), nets 4 (36.4->38.38), rope 1 (83->85.97), steel ingots 1 (18.79->19.38) | ploughs 2 (52.29->76), spinning wheels 1 (197.4->220.4), garments 2 (20.27->22.6), herbs 1 (36.96->39.33) | +92 |
| Rouhomme | 368 | 0.10 | 0.70 (70/turn) | bread 147 (2.31->2.79), charcoal 19 (2.16->4.43), beer 15 (3.24->3.84), rope 1 (83->85.5) | spinning wheels 3 (218.4->220.4), garments 2 (21->22.6), slaked lime 2 (16.07->16.72), tools 16 (4.73->4.89) | +80 |
| Heilegg | 826 | 0.23 | 0.40 (40/turn) | lead bars 8 (15.44->16.15), leather 1 (21.84->26.03), lead ore 6 (9.66->11.11), flax fibres 2 (4.66->5.22) | thread 62 (4.28->4.88), cured meat 14 (20.06->22.04), cloth 24 (7.04->7.6), slaked lime 5 (14.6->16.72) | +74 |

**Best:** Grandgues at about +220 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 75.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 2 @ min 7.05 | goal planner: sells 2 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres | 1 @ 5.05, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had None) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 13.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 21.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 10) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 92, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 35.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.3k (cash + stock at home prices); +111/turn over 6 turns, -2/turn over 24 turns.
- Limits: cash flow >= -248/turn, prestige >= +4.98/turn (values are after 200 tax a turn).
- Today's settings: value +105/turn, cash +108/turn, prestige -0.91/turn - breaks the prestige floor.
- Plan: value -125/turn, cash -117/turn, prestige +3.29/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +193 vs +110, +254 vs +110, +13 vs +101.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> no route: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - ropewalk 1 0.25 -> 0.31: +2/turn
  - sewing shop 1 0.30 -> 0.36: -4/turn
  - weavery 1 0.50 -> 0.61: +6/turn
  - retting pit 1 0.91 -> 0.72: -13/turn
  - flax farm 1 4.64 -> 3.41: +12/turn
  - brewery 1 0.14 -> 0.27: -19/turn
  - mansion 1 0.00 -> 1.00: -220/turn
- Model check over the last 60 turns: predicted +98/turn for the settings we ran, real +63/turn.
- Worth of one more unit per turn: labour 1.63, thread 4.14, cloth 6.58, flax fibres 4.97, garments 19.00, nets 29.68, beer 2.83, timber 2.92, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 2 (v2 none); firewood buy 4 (v2 5); flax fibres buy 1 (v2 None); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 10); labour buy 29 (v2 25)
- Ship linen snake: Grandgues -> no route (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 482 (+193 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.96 |
| ret | 3 | 0.91 | 1.19 |
| spin | 4 | 1.65 | 2.10 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 332/228, cloth 73/128

## Self-diagnosis

Nothing found this run.
