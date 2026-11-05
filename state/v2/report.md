# v2 shadow report

Turn 13803, 2026-11-05 12:24. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,938, prestige 3,301 (181 free, -0.9/turn).

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

598 turns left: prestige gained now converts 95.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.3 | 55.3 | thin at home: pasties, wine, ham, stockfish, cheese, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 56.5 | 56.5 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 56.5 | 56.5 | thin at home: wine, cured fish, cheese |
| hold prayer 2 | chapel | 13 | 52.8 | 57.0 | needs a chapel (build cost 29,432); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 52.9 | 57.1 | needs a church (build cost 65,848); thin at home: candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 57.2 | 57.2 | thin at home: pasties, wine, cheese, pies, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 57.5 | 57.5 | thin at home: wine, cheese |
| jousting 3 | arena | 230 | 57.3 | 57.5 | needs a arena (build cost 25,430); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 58.0 | 58.0 | thin at home: wine, ham, stockfish, cheese, candles |
| hold sermon 2 | church | 24 | 52.9 | 58.3 | needs a church (build cost 65,848); thin at home: furniture |
| hold banquet 4 (premium) | mansion | 20 | 58.4 | 58.4 | thin at home: wine, ham, stockfish, candles, premium cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.9 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.3 (keep 14); best orders clear only 0 a turn after crew: ship stays at 0
- best towns now: Heilegg +61, Vauxvais +54, Disscester +41, Brunnham +34, Chatgnan +33
- Heilegg would trade: pasties buy 14 @ 13.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (50/turn) | charcoal 19 (2.16->6.6), timber 24 (6.98->9.5), limestone 4 (16.28->21.47), medicine 2 (149.1->155.8) | garments 2 (21.21->22.6), cloth 5 (7.61->7.85), cheese 4 (6.2->6.32) | +171 |
| Pontmont | 341 | 0.09 | 0.20 (20/turn) | cured fish 4 (26.88->29.83), charcoal 19 (2.16->3.42), beer 15 (3.24->3.84), glass ingots 1 (54.6->60.8) | slaked lime 4 (6.83->16.25), garments 2 (20.27->22.6), lead bars 3 (11.55->12.92) | +85 |
| Bordetes | 831 | 0.23 | 0.70 (70/turn) | dyed cloth 15 (10.82->12.35), cured fish 4 (26.88->32.11), charcoal 19 (2.16->4.73), cured meat 5 (24.36->25.46) | cloth 23 (7.35->7.85), herbs 1 (32.76->39.33), garments 2 (20.16->22.6) | +78 |
| Bremcop | 1326 | 0.49 | 0.10 (10/turn) | medicine 2 (149.1->186.2) | garments 2 (20.68->22.6), cloth 8 (7.25->7.85) | +73 |
| Heilegg | 826 | 0.23 | 0.40 (40/turn) | lead bars 8 (15.33->15.96), glass ingots 1 (54.6->56.05) | thread 62 (4.3->4.88), cured meat 12 (20.16->21.85), cloth 24 (7.04->7.85), slaked lime 5 (13.97->16.25) | +65 |

**Best:** Grandgues at about +171 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 75.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres | 1 @ 5.05, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had None) |
| flax plants |  | 1 @ min 1.21 | goal planner: sells 1 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 13.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 92, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 35.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.1k (cash + stock at home prices); +123/turn over 6 turns, -0/turn over 24 turns.
- Limits: cash flow >= -247/turn, prestige >= +4.95/turn (values are after 200 tax a turn).
- Today's settings: value +99/turn, cash +101/turn, prestige -0.91/turn - breaks the prestige floor.
- Plan: value -130/turn, cash -123/turn, prestige +3.29/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +71 vs +114, +193 vs +110, +254 vs +110.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - sewing shop 1 0.30 -> 0.36: -4/turn
  - weavery 1 0.50 -> 0.61: +7/turn
  - retting pit 1 0.91 -> 0.72: -14/turn
  - flax farm 1 4.64 -> 3.22: +12/turn
  - brewery 1 0.14 -> 0.27: -19/turn
  - mansion 1 0.00 -> 1.00: -219/turn
- Model check over the last 60 turns: predicted +97/turn for the settings we ran, real +61/turn.
- Worth of one more unit per turn: labour 1.63, thread 4.14, cloth 6.58, flax fibres 4.97, garments 19.00, nets 29.65, beer 2.84, timber 2.99, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax fibres buy 1 (v2 None); flax plants sell 1 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25)
- Ship linen snake: Grandgues -> Amsdermund (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 482 (+193 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.95 |
| ret | 3 | 0.91 | 1.19 |
| spin | 4 | 1.65 | 2.10 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 334/228, cloth 73/128

## Self-diagnosis

Nothing found this run.
