# v2 shadow report

Turn 13902, 2026-11-09 15:16. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,403, prestige 3,499 (379 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 10 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 1 | 0 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 530, not 630

## Prestige spending, cheapest coin per prestige first

499 turns left: prestige gained now converts 91.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.9 | 54.9 | thin at home: hop beer, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 55.5 | 55.8 | needs a arena (build cost 25,272); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 57.0 | 57.0 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.1 | 57.1 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 57.3 | 57.3 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.3 | 59.3 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 59.3 | 59.3 | thin at home: hop beer, cheese |
| jousting 2 | arena | 210 | 60.8 | 61.1 | needs a arena (build cost 25,272); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 61.2 | 61.2 | thin at home: hop beer, cheese |
| hold banquet 2 (pies) | mansion | 7 | 63.3 | 63.3 | thin at home: cheese |
| hold banquet 3 (meat) | mansion | 7.6 | 64.4 | 64.4 | thin at home: hop beer, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.056 | - | furniture 2, pasties 2 | -54 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 13.7 (keep 145); stock: pasties 2 @ 13.4 (keep 14); best orders clear only 13 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.1 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Orlesailles +38, Bordetes +28, Brunnham +27, Clarfranche +27, Etallaen +23
- Orlesailles would trade: pasties buy 12 @ 14.0; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | bread 154 (2.29->3.61), firewood 38 (2.52->6.37), cured fish 6 (25.41->29.26), limestone 3 (15.12->18.62) | flour 5 (23.94->24.7), candles 1 (81.9->83), thread 19 (5.15->5.2) | +323 |
| Rouhomme | 368 | 0.10 | 0.60 (63/turn) | bread 154 (2.29->3.97), grain 2 (2.58->4.52), copper ingots 1 (15.86->17.1), pickaxes 1 (9.71->11.11) | thread 49 (4.73->5.2), cookware 7 (23.31->24.13), candles 1 (79.8->83), cheese 4 (6.51->7.12) | +248 |
| Fontaux | 411 | 0.12 | 1.00 (106/turn) | thread 46 (4.68->5.65), timber 12 (8.77->12.35), firewood 12 (2.52->6.74), bread 88 (2.29->2.7) | salt 7 (4.98->5.56), candles 0 (81.9->83), cloth 4 (9.5->9.7) | +85 |
| Hanstein | 380 | 0.11 | 0.50 (53/turn) | timber 13 (8.77->12.44), wool 4 (10.82->16.15), limestone 3 (15.12->25.08), thread 79 (4.68->4.84) | flax fibres 10 (4.58->5.55), garments 2 (24.99->27), salt 9 (5.25->5.56), candles 1 (81.9->83) | +83 |
| Amsdermund | 1111 | 0.40 | 0.30 (32/turn) | cured meat 8 (28.77->30.78), chisels 3 (10.82->13.3), nets 4 (38.4->40.09), lead bars 1 (15.44->16.53) | cloth 24 (7.61->9.7), flour 5 (19.43->24.7), garments 2 (24.57->27), hop beer 3 (6.56->8.69) | +81 |

**Best:** Grandgues at about +323 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 25.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 30) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 1 = 3.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.4k (cash + stock at home prices); +182/turn over 6 turns, +200/turn over 24 turns.
- Limits: cash flow >= -267/turn, prestige >= -0.33/turn (values are after 200 tax a turn).
- Today's settings: value +86/turn, cash +74/turn, prestige -1.90/turn - breaks the prestige floor.
- Plan: value +5/turn, cash +9/turn, prestige -0.33/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -527 vs +58, +143 vs +63, +40 vs +70 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bremcop: +7/turn
  - net maker 0.00 -> 0.29: +8/turn
  - flax farm 1 4.64 -> 4.27: -1/turn
  - retting pit 1 0.91 -> 0.85: +0/turn
  - spinnery 1 1.65 -> 1.50: +3/turn
  - ropewalk 1 0.25 -> 0.00: -4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.22: +10/turn
  - brewery 1 0.14 -> 0.21: -6/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +60/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.66, flax fibres 4.95, garments 19.27, nets 29.92, beer 2.90, timber 3.33, prestige 63.31, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 30); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.22, worth +8/turn.
- Ship linen snake: Grandgues -> Bremcop (+7/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +1/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1630 coin: +1/turn, payback 2151 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 899/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.55 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
