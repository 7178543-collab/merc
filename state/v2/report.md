# v2 shadow report

Turn 13917, 2026-11-10 06:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,423, prestige 3,470 (350 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 19 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 500 | 0 | 29 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~42 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.05, no projection from the game)
- labour: projection runs 100 over real use lately; planning 503, not 603

## Prestige spending, cheapest coin per prestige first

484 turns left: prestige gained now converts 91.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.4 | 44.4 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 53.3 | 53.3 |  |
| hold banquet 4 (pies) | mansion | 18 | 53.9 | 53.9 | thin at home: hop beer, ham, stockfish, pies |
| jousting 3 | arena | 230 | 54.7 | 54.9 | needs a arena (build cost 25,152); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 55.6 | 55.6 |  |
| hold banquet 4 (premium) | mansion | 20 | 55.6 | 55.6 | thin at home: hop beer, ham, stockfish, premium cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 56.1 | 56.1 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 56.3 | 56.3 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 58.4 | 58.4 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 59.7 | 59.7 | thin at home: pies |
| jousting 2 | arena | 210 | 59.9 | 60.1 | needs a arena (build cost 25,152); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 62.4 | 62.4 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 12 @ 14.5; crew 0.1; est +43 a turn; stock: pasties 12 @ 14.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 16.0 (keep 14); best orders clear only 8 a turn after crew: ship stays at 0
- best towns now: Bedenis +118, Vauxvais +104, Marmont +92, Clairlond +82, Toqueque +81
- Bedenis would trade: furniture buy 6 @ 14.6, pasties buy 12 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (86/turn) | firewood 26 (3.07->10.45), charcoal 20 (2.77->6.22), timber 29 (8.4->10.07), bread 154 (2.16->2.41) | bricks 1 (9.55->15.67), nails 3 (7.56->8.17), flax fibres 6 (6.88->7.15), tar 1 (10.71->11.4) | +291 |
| Fontaux | 411 | 0.10 | 1.00 (96/turn) | thread 59 (4.72->7.27), bread 109 (2.16->2.79), charcoal 13 (2.77->5.27), salt 6 (5.35->7.79) | bricks 0 (11.45->15.67), nails 0 (7.56->8.17), yarn 4 (4.87->4.99) | +241 |
| Etallaen | 774 | 0.20 | 1.00 (96/turn) | bread 110 (2.16->4.03), charcoal 14 (2.77->5.89), leather 0 (23.31->31.92), tallow 0 (17.75->24.7) | bricks 0 (8.61->15.67), candles 0 (81.9->84.5), nails 2 (7.72->8.17), yarn 0 (4.41->4.99) | +189 |
| Rouhomme | 368 | 0.09 | 0.50 (48/turn) | bread 154 (2.16->3), thread 24 (4.72->6.27), grain 2 (2.44->3.34), cloth 1 (6.2->6.46) | bricks 1 (6.46->15.67), dyed cloth 7 (12.92->13.96), tools 17 (4.89->5.32), candles 1 (81.9->84.5) | +146 |
| Kirchwerp | 1072 | 0.35 | 0.90 (86/turn) | thread 101 (4.72->5.7), beer 57 (3.51->4.58), pickaxes 3 (12.18->15.2), leather 1 (23.31->30.4) | flax fibres 24 (5.78->7.15), dyed cloth 7 (12.08->13.96), bricks 1 (5.83->15.67), blades 4 (14.7->15.58) | +138 |

**Best:** Grandgues at about +291 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 5 @ 3.5, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 19 = 4.5 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.8) |
| grain | 0 @ 3.7, stop 34 |  | goal planner: buys 0 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 3) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 38.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.4k (cash + stock at home prices); +145/turn over 6 turns, +188/turn over 24 turns.
- Limits: cash flow >= -309/turn, prestige >= -0.21/turn (values are after 200 tax a turn).
- Today's settings: value +82/turn, cash +55/turn, prestige -1.96/turn - breaks the prestige floor.
- Plan: value +9/turn, cash +12/turn, prestige -0.21/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +89 vs +75, +74 vs +68, -635 vs +63 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +10/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +9/turn
  - sewing shop 1 0.30 -> 0.36: -0/turn
  - weavery 1 0.50 -> 0.60: +4/turn
  - ropewalk 1 0.25 -> 0.00: +1/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.17: +10/turn
  - retting pit 1 0.91 -> 1.05: -5/turn
  - spinnery 1 1.65 -> 1.85: +6/turn
  - flax farm 1 4.64 -> 5.35: +3/turn
- HAND-OVER: goal planner: model check held 12 runs, it now runs 'rates' live.
- Model check over the last 59 turns: predicted +105/turn for the settings we ran, real +68/turn.
- Worth of one more unit per turn: labour 1.48, thread 3.72, cloth 5.94, flax fibres 4.41, garments 17.18, nets 26.98, beer 2.68, timber 3.60, prestige 60.20, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 3); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.17, worth +12/turn.
- Ship linen snake: Grandgues -> Gosschweig (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +74/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1643 coin: +2/turn, payback 864 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 1032/228, cloth 74/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 7.15 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
