# v2 shadow report

Turn 13904, 2026-11-09 17:27. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,839, prestige 3,495 (375 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 10 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 1 | 0 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 530, not 630

## Prestige spending, cheapest coin per prestige first

497 turns left: prestige gained now converts 91.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 57.3 | 57.3 |  |
| hold banquet 4 (pies) | mansion | 18 | 57.9 | 57.9 | thin at home: hop beer, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 57.8 | 58.1 | needs a arena (build cost 27,022); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.2 | 59.2 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 59.9 | 59.9 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 60.1 | 60.1 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 2 (pies) | mansion | 7 | 63.0 | 63.0 | thin at home: cheese |
| jousting 2 | arena | 210 | 63.3 | 63.6 | needs a arena (build cost 27,022); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 65.2 | 65.2 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 65.3 | 65.3 |  |
| hold feast 2 | townhouse | 2.6 | 59.1 | 65.4 | needs a townhouse (build cost 7,816) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.092 | - | furniture 2, pasties 5 | -94 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 2 @ 13.7, pasties buy 2 @ 13.4; crew 0.1; est +26 a turn; stock: furniture 2 @ 13.7 (keep 145); stock: pasties 2 @ 13.4 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.4 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Clairlond +47, Chatgnan +35, Bedenis +32, Essenbrucke +27, Caillechâtel +26
- Clairlond would trade: furniture buy 2 @ 12.6, pasties buy 8 @ 13.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (105/turn) | bread 154 (2.27->3.61), firewood 38 (2.31->6.46), timber 34 (8.51->10.73), charcoal 18 (1.97->5.22) | coats 1 (92.92->95.95), hop beer 1 (9.08->12.06), tools 9 (5->5.42), candles 1 (81.9->83) | +426 |
| Amsdermund | 1111 | 0.40 | 0.20 (21/turn) | gold ore 1 (151.2->180.5), looms 1 (645.75->665), bellows 2 (268.8->277.4), hinges 1 (40.53->51.3) | cloth 18 (7.61->10.2), coats 1 (84.53->95.95), garments 2 (24.36->27.6), hop beer 1 (6.67->12.06) | +144 |
| Rouhomme | 368 | 0.10 | 1.00 (105/turn) | bread 81 (2.27->3.38), charcoal 9 (1.97->5.27), firewood 20 (2.31->5.89), lead bars 3 (12.92->13.77) | thread 25 (4.73->5.2), cookware 3 (23.31->25.84), tools 8 (4.81->5.42), seeds 2 (1.94->2.94) | +134 |
| Kirchwerp | 1072 | 0.38 | 0.40 (42/turn) | thread 79 (4.66->5.7), lead bars 3 (12.92->17.39), chisels 3 (10.82->11.78) | cloth 24 (8.24->10.2), cheese 5 (5.1->7.08), coats 1 (88.2->95.95), garments 2 (24.36->27.6) | +128 |
| Fontaux | 411 | 0.12 | 1.00 (105/turn) | thread 41 (4.66->5.65), charcoal 8 (1.97->5.61), timber 11 (8.51->12.06), firewood 11 (2.31->6.79) | salt 8 (5.12->5.56), cloth 3 (9.61->10.2), hop beer 0 (9.92->12.06), candles 0 (81.9->83) | +126 |

**Best:** Grandgues at about +426 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 26.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 30) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 1.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.9k (cash + stock at home prices); +220/turn over 6 turns, +205/turn over 24 turns.
- Limits: cash flow >= -285/turn, prestige >= -0.31/turn (values are after 200 tax a turn).
- Today's settings: value +100/turn, cash +92/turn, prestige -1.89/turn - breaks the prestige floor.
- Plan: value +18/turn, cash +21/turn, prestige -0.31/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +40 vs +70, +292 vs +74, +144 vs +88.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +3/turn
  - net maker 0.00 -> 0.29: +8/turn
  - flax farm 1 4.64 -> 4.34: -2/turn
  - spinnery 1 1.65 -> 1.52: -2/turn
  - brewery 1 0.14 -> 0.21: -6/turn
  - ropewalk 1 0.25 -> 0.00: -7/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.24: +11/turn
  - weavery 1 0.50 -> 0.60: -9/turn
  - sewing shop 1 0.30 -> 0.36: +10/turn
  - mansion 1 0.00 -> 0.37: -92/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +66/turn.
- Worth of one more unit per turn: labour 1.63, thread 4.09, cloth 6.54, flax fibres 4.85, garments 18.92, nets 29.51, beer 2.86, timber 3.38, prestige 63.21, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 7); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 30); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.24, worth +10/turn.
- Ship linen snake: Grandgues -> Corstoft (+7/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +1/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1984 coin: +1/turn, payback 1717 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 897/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.4 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
