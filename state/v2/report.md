# v2 shadow report

Turn 13800, 2026-11-05 09:13. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,421, prestige 3,304 (184 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
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

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

601 turns left: prestige gained now converts 95.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| jousting 3 | arena | 230 | 54.9 | 55.1 | needs a arena (build cost 25,667); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.6 | 55.6 | thin at home: pasties, wine, ham, stockfish, cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 56.0 | 56.0 | thin at home: pasties, wine, cheese, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 56.6 | 56.6 | thin at home: wine, cheese |
| hold sermon 2 (candles) | church | 31 | 52.7 | 56.9 | needs a church (build cost 66,162); thin at home: candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 57.3 | 57.3 | thin at home: wine, cured fish, cheese |
| hold feast 2 | townhouse | 2.6 | 52.9 | 57.6 | needs a townhouse (build cost 7,068); thin at home: wine |
| hold prayer 2 | chapel | 13 | 53.4 | 57.6 | needs a chapel (build cost 29,737); thin at home: furniture |
| hold banquet 4 | mansion | 17.5 | 58.2 | 58.2 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 58.5 | 58.5 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.5 | 58.5 | thin at home: wine, ham, stockfish, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 5 @ 13.9; crew 0.1; est +15 a turn; stock: pasties 5 @ 13.9 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.4 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Vauxvais +63, Disscester +42, Heilegg +40, Brunnham +35, Clairas +27
- Vauxvais would trade: pasties buy 9 @ 10.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.30 (29/turn) | charcoal 19 (2.07->5.84), timber 26 (7.04->9.12), limestone 3 (16.59->21.47), firewood 1 (1.67->6.6) | cloth 6 (7.3->7.95), wool 4 (8.93->9.59), salt 4 (4.2->4.45), flour 1 (19.01->19.38) | +137 |
| Pontmont | 341 | 0.09 | 0.20 (20/turn) | charcoal 19 (2.07->4.69), thread 25 (4.66->5.03), raw cloth 11 (7.09->7.69), hinges 1 (37.59->39.33) | tools 16 (4.73->4.99), cloth 5 (7.72->7.95), garments 2 (20.27->20.8), wool 4 (9.29->9.59) | +58 |
| Hanbrücken | 531 | 0.14 | 0.10 (10/turn) | flax fibres 2 (4.7->6.17) | tapestries 1 (603.75->665), wool 1 (7.61->9.59) | +57 |
| Bordetes | 831 | 0.23 | 0.50 (49/turn) | cured fish 4 (26.88->32.11), charcoal 19 (2.07->4.54), dyed cloth 11 (11.03->11.78), beer 15 (3.28->3.86) | cloth 21 (7.35->7.95), wool 4 (8.93->9.59), garments 2 (20.16->20.8) | +55 |
| Angefont | 686 | 0.18 | 0.40 (39/turn) | charcoal 19 (2.07->4.75), nets 6 (34.8->36.48), steel ingots 3 (17.32->18.71) | thread 62 (4.51->4.88), cloth 19 (7.61->7.95), cured fish 9 (23.52->24.13), garments 2 (20.27->20.8) | +54 |

**Best:** Grandgues at about +137 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 72, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 14.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 91, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 19.8k (cash + stock at home prices); +103/turn over 6 turns, +4/turn over 24 turns.
- Limits: cash flow >= -226/turn, prestige >= +4.83/turn (values are after 200 tax a turn).
- Today's settings: value +107/turn, cash +115/turn, prestige -0.92/turn - breaks the prestige floor.
- Plan: value -123/turn, cash -114/turn, prestige +3.28/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +50 vs +115, +148 vs +115, +123 vs +113.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> no route: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +4/turn
  - flax farm 1 4.64 -> 4.45: +0/turn
  - sewing shop 1 0.30 -> 0.36: -5/turn
  - weavery 1 0.50 -> 0.61: +8/turn
  - brewery 1 0.14 -> 0.27: -19/turn
  - mansion 1 0.00 -> 1.00: -219/turn
- Model check over the last 60 turns: predicted +97/turn for the settings we ran, real +37/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 3.97, cloth 6.34, flax fibres 4.70, garments 18.34, nets 28.63, beer 2.82, timber 3.02, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> no route (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 481 (+192 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.93 |
| ret | 3 | 0.91 | 1.19 |
| spin | 4 | 1.65 | 2.09 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 339/228, cloth 72/128

## Self-diagnosis

Nothing found this run.
