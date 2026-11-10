# v2 shadow report

Turn 13924, 2026-11-10 13:39. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,898, prestige 3,455 (335 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 9 | 0 | 0 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 32, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~74 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 56
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +4 crew for Flax Wyrm (crew 0.08, no projection from the game)
- labour: projection runs 100 over real use lately; planning 488, not 588

## Prestige spending, cheapest coin per prestige first

477 turns left: prestige gained now converts 90.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.4 | 54.4 |  |
| hold banquet 4 (pies) | mansion | 18 | 55.1 | 55.1 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 55.2 | 55.2 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 56.7 | 56.7 | thin at home: hop beer, cheese |
| hold banquet 4 (premium) | mansion | 20 | 56.8 | 56.8 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.5 | 57.5 | thin at home: hop beer, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 57.9 | 58.2 | needs a arena (build cost 26,086); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 60.3 | 60.3 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 60.3 | 60.3 | thin at home: hop beer, cheese |
| hold feast 2 | townhouse | 2.6 | 55.9 | 62.4 | needs a townhouse (build cost 7,586) |
| jousting 2 | arena | 210 | 63.4 | 63.7 | needs a arena (build cost 26,086); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 14 @ 13.7, pasties buy 10 @ 15.0; crew 0.2; est +196 a turn; stock: furniture 14 @ 13.7 (keep 145); stock: pasties 10 @ 15.0 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.4 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- best towns now: Bedenis +206, Caillechâtel +196, Marmont +189, Friedwerp +178, Chatgnan +178
- Bedenis would trade: furniture buy 14 @ 14.0, pasties buy 13 @ 14.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.21 | 1.00 (103/turn) | beer 31 (3.49->7.41), bread 87 (2.69->3.97), garments 5 (17.99->21.85), clay 2 (4.91->19) | flax fibres 10 (4.94->6.85), thread 4 (4.73->5.75), candles 0 (81.9->85), pies 0 (15.86->19.76) | +244 |
| Grandgues | 152 | 0.04 | 0.50 (51/turn) | bread 148 (2.69->3.61), timber 37 (7.88->10.16), garments 10 (17.99->21.47), tools 18 (6.46->6.98) | candles 1 (84.53->85) | +226 |
| Neuborn | 780 | 0.21 | 1.00 (103/turn) | bread 64 (2.69->4.31), timber 16 (7.88->13.3), garments 4 (17.99->21.28), premium cheese 2 (34.02->37.24) | cloth 10 (7.61->8.75), cookware 2 (23.31->26.6), thread 6 (4.6->5.75), garments 0 (23.73->24.8) | +153 |
| Heilegg | 826 | 0.23 | 0.50 (51/turn) | beer 54 (3.49->4.52), garments 10 (17.99->21.28), lead ore 5 (7.72->12.16), gold ore 1 (175.35->191.9) | cloth 24 (7.56->8.75), cookware 6 (25.62->26.6) | +131 |
| Amsdermund | 1111 | 0.39 | 0.30 (31/turn) | gold ore 2 (175.35->207.1), garments 10 (17.99->20.71), lead ore 1 (7.72->10.83), cloth 1 (6.12->6.74) | cloth 24 (7.56->8.75), cookware 6 (24.78->26.6), flax fibres 15 (5.78->6.85), garments 2 (23.1->24.8) | +125 |

**Best:** Etallaen at about +244 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.2) |
| grain | 8 @ 3.7, stop 32 |  | goal planner: buys 8 a turn for today's rates, keeps up to 32 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.3k (cash + stock at home prices); +323/turn over 6 turns, +215/turn over 24 turns.
- Limits: cash flow >= -329/turn, prestige >= -0.15/turn (values are after 200 tax a turn).
- Today's settings: value +54/turn, cash +9/turn, prestige -2.39/turn - breaks the prestige floor.
- Plan: value -67/turn, cash -63/turn, prestige -0.15/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -28 vs +34, +146 vs +17, +47 vs +25.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +8/turn
  - ship Flax Wyrm -> Marmont: +1/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: -2/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.09: +20/turn
  - flax farm 1 4.64 -> 3.85: -5/turn
  - retting pit 1 0.91 -> 0.77: -4/turn
  - spinnery 1 1.65 -> 1.35: +5/turn
  - sewing shop 1 0.30 -> 0.36: -1/turn
  - weavery 1 0.50 -> 0.61: +11/turn
- Model check over the last 59 turns: predicted +107/turn for the settings we ran, real +155/turn.
- Worth of one more unit per turn: labour 1.62, thread 4.07, cloth 6.50, flax fibres 4.82, garments 18.81, nets 29.38, beer 2.83, timber 3.38, prestige 73.03, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.09, worth +5/turn.
- Ship linen snake: Grandgues -> Corstoft (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Marmont (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1711 coin: +6/turn, payback 275 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 43/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.85 for 6 turns, bought 0.0 of 1, 42.9 held (1.8 turns); raise needs Taylor (ceiling None)
