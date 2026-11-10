# v2 shadow report

Turn 13921, 2026-11-10 10:11. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,733, prestige 3,462 (342 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 2 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 2.0 -> v2: add buy 9
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.04 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.04 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~70 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 56
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 486, not 586

## Prestige spending, cheapest coin per prestige first

480 turns left: prestige gained now converts 91.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 53.8 | 53.8 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 53.9 | 53.9 |  |
| hold banquet 4 (pies) | mansion | 18 | 53.9 | 53.9 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 54.8 | 54.8 | thin at home: hop beer |
| jousting 3 | arena | 230 | 55.1 | 55.4 | needs a arena (build cost 26,348); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 55.8 | 55.8 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 56.2 | 56.2 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 58.0 | 58.0 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 58.5 | 58.5 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 60.2 | 60.2 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 60.5 | 60.5 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 11 @ 14.5; crew 0.1; est +38 a turn; stock: pasties 11 @ 14.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Essenbrucke +191, Bedenis +174, Großmühle +163, Chatgnan +158, Unterhufe +148
- Essenbrucke would trade: furniture buy 12 @ 12.2, pasties buy 9 @ 14.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (79/turn) | firewood 28 (3.19->9.69), timber 28 (8.35->9.59), thread 13 (4.68->5.94), bread 154 (2.5->2.68) | bellows 1 (264.6->267.9), salt 4 (5.04->5.51), cloth 12 (8.61->8.75) | +197 |
| Etallaen | 774 | 0.21 | 1.00 (99/turn) | beer 33 (3.46->6.55), bread 96 (2.5->3.31), clay 1 (4.91->19), cured fish 4 (24.57->26.41) | flax fibres 14 (4.94->7.05), candles 0 (81.9->83.5), cloth 4 (8.35->8.75) | +162 |
| Pontmont | 341 | 0.09 | 1.00 (99/turn) | beer 41 (3.46->4.66), bread 118 (2.5->3.04), thread 24 (4.68->5.51), cured meat 3 (27.51->31.73) | windows 0 (693->722), cloth 10 (7.88->8.75), bellows 0 (260.4->267.9), paper 3 (20.58->21.09) | +162 |
| Bordetes | 831 | 0.23 | 1.00 (99/turn) | bread 128 (2.5->3.93), furniture 6 (17.22->21.66), cookware 2 (29.19->30.02), spirits 0 (9.71->11.69) | spinning wheels 0 (191.1->216.6), garments 1 (24.15->26.2) | +148 |
| Kirchwerp | 1072 | 0.36 | 1.00 (99/turn) | thread 92 (4.68->5.7), beer 54 (3.46->4.75), lead ore 10 (7.88->10.45), flour 2 (23.52->27.36) | flax fibres 23 (5.78->7.05), cloth 24 (7.88->8.75), dyed cloth 8 (12.08->12.92), garments 2 (24.15->26.2) | +140 |

**Best:** Grandgues at about +197 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 9 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 2 = 0.5 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.2) |
| grain | 0 @ 3.7, stop 34 |  | goal planner: buys 0 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.0k (cash + stock at home prices); +175/turn over 6 turns, +194/turn over 24 turns.
- Limits: cash flow >= -322/turn, prestige >= -0.18/turn (values are after 200 tax a turn).
- Today's settings: value +71/turn, cash +34/turn, prestige -1.92/turn - breaks the prestige floor.
- Plan: value -0/turn, cash +3/turn, prestige -0.18/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -635 vs +63, +88 vs +49, +3 vs +44 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +9/turn
  - ship Flax Wyrm -> Essenbrucke: +4/turn
  - net maker 0.00 -> 0.29: +8/turn
  - flax farm 1 4.64 -> 5.24: -5/turn
  - retting pit 1 0.91 -> 1.02: +3/turn
  - spinnery 1 1.65 -> 1.81: +4/turn
  - sewing shop 1 0.30 -> 0.36: -8/turn
  - weavery 1 0.50 -> 0.60: +11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.13: -11/turn
  - ropewalk 1 0.25 -> 0.00: +24/turn
- Model check over the last 59 turns: predicted +105/turn for the settings we ran, real +140/turn.
- Worth of one more unit per turn: labour 1.55, thread 3.89, cloth 6.22, flax fibres 4.61, garments 17.99, nets 28.28, beer 2.75, timber 3.33, prestige 60.15, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.13, worth +9/turn.
- Ship linen snake: Grandgues -> Gosschweig (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Essenbrucke (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1831 coin: +1/turn, payback 2217 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 32/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 2.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.36 (ask 3.3, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.04; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: flax fibres buy not filling: bid 5.05 under the home ask 7.05 for 6 turns, bought 0.0 of 1, 31.5 held (1.2 turns); raise needs Taylor (ceiling None)
