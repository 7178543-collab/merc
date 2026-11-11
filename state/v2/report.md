# v2 shadow report

Turn 13949, 2026-11-11 14:34. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,798, prestige 3,600 (480 free, +121.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 9 | 0 | 0 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.44 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 2, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~78 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 484, not 584

## Prestige spending, cheapest coin per prestige first

452 turns left: prestige gained now converts 89.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| jousting 3 | arena | 230 | 55.5 | 55.8 | needs a arena (build cost 28,475); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 56.6 | 56.6 | thin at home: wine, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 | thin at home: beer |
| hold banquet 4 (premium) | mansion | 20 | 58.9 | 58.9 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 59.6 | 59.6 | thin at home: wine, ham, stockfish |
| jousting 2 | arena | 210 | 60.8 | 61.1 | needs a arena (build cost 28,475); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 62.1 | 62.1 | thin at home: beer, cured meat |
| hold banquet 3 (pies) | mansion | 8 | 63.9 | 63.9 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 65.4 | 65.4 |  |
| jousting 1 | arena | 170 | 66.1 | 66.5 | needs a arena (build cost 28,475); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 60.0 | 66.8 | needs a church (build cost 76,919); thin at home: candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 8 @ 15.5; crew 0.1; est +16 a turn; stock: pasties 8 @ 15.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Marmont +328, Vauxvais +318, Brebronn +287, Hofkirchen +283, Amsdermund +275
- Marmont would trade: furniture buy 25 @ 12.9, pasties buy 5 @ 16.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.40 | 0.70 (77/turn) | thread 92 (4.66->5.7), furniture 15 (11.87->15.2), honey 6 (7.77->9.5), flax fibres 6 (6.9->8.07) | cloth 24 (7.56->10.6), cheese 5 (7.25->11.02), coats 3 (81.9->86.92), garments 2 (23.1->24.4) | +192 |
| Bordetes | 831 | 0.25 | 0.60 (66/turn) | furniture 15 (11.87->15.58), cured fish 6 (24.57->29.83), charcoal 19 (2.77->5.46), windows 1 (693->703) | cloth 24 (7.56->10.6), slaked lime 2 (6.83->10.26), pickaxes 1 (9.03->10.16) | +182 |
| Grandgues | 152 | 0.04 | 0.60 (66/turn) | charcoal 19 (2.77->5.37), bread 159 (2.44->2.79), furniture 15 (11.87->14.06), timber 37 (8.77->9.69) | cloth 11 (7.61->10.6), tiles 3 (3.89->5.51), cheese 5 (10.4->11.02), slaked lime 2 (9.13->10.26) | +165 |
| Fontaux | 411 | 0.12 | 0.60 (66/turn) | windows 1 (693->736.25), furniture 12 (11.87->14.91), charcoal 19 (2.77->5.03), garments 10 (22.6->25.27) | cheese 5 (8.77->11.02), cloth 6 (9.29->10.6), coats 3 (86.1->86.92), spirits 1 (12.6->12.82) | +157 |
| Heilegg | 826 | 0.25 | 0.70 (77/turn) | furniture 15 (11.87->13.68), thread 35 (4.66->5.22), charcoal 19 (2.77->5.13), lead ore 8 (9.4->11.4) | cloth 24 (7.72->10.6), cheese 5 (7.04->11.02), cookware 5 (20.48->24.13), tools 16 (5.02->5.65) | +146 |

**Best:** Kirchwerp at about +192 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 78.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 6.4 | goal planner: sells 2 a turn at 6.4, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| furniture | 2 @ 11.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.0) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 112, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 39.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.4k (cash + stock at home prices); -723/turn over 6 turns, -252/turn over 24 turns.
- Limits: cash flow >= -158/turn, prestige >= -0.75/turn (values are after 200 tax a turn).
- Today's settings: value +46/turn, cash +57/turn, prestige +121.88/turn.
- Plan: value +407/turn, cash +231/turn, prestige +113.88/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -6 vs +12, +177 vs +26, +10 vs +28.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> no route: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - park 1 16.00 -> 0.00: +50/turn
  - weavery 1 0.50 -> 1.56: +33/turn
  - spinnery 1 1.65 -> 2.69: +72/turn
  - flax farm 1 4.64 -> 7.98: +22/turn
  - retting pit 1 0.91 -> 1.57: +127/turn
  - brewery 1 0.14 -> 0.00: +2/turn
  - net maker [make nets 1] 0.00 -> 0.38: +17/turn
  - ropewalk 1 0.25 -> 0.00: +14/turn
- Model check over the last 60 turns: predicted +106/turn for the settings we ran, real +19/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.19, thread 2.99, cloth 4.77, flax fibres 3.56, garments 13.79, nets 22.37, beer 2.70, timber 3.33, prestige 0.00, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.04, worth +4/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +14/turn.
- Ship linen snake: Grandgues -> no route (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +59/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 9.4/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 418 (+127 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.11 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 122/77, thread 1064/227, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
