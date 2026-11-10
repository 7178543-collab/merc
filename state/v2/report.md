# v2 shadow report

Turn 13911, 2026-11-10 00:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,694, prestige 3,482 (362 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 44 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
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
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~45 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for Flax Wyrm (crew 0.03, no projection from the game)
- labour: projection runs 100 over real use lately; planning 502, not 602

## Prestige spending, cheapest coin per prestige first

490 turns left: prestige gained now converts 91.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.8 | 46.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.9 | 54.9 | thin at home: ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 55.0 | 55.0 | thin at home: beer |
| hold banquet 4 (premium) | mansion | 20 | 56.0 | 56.0 | thin at home: ham, stockfish, premium cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 56.1 | 56.1 | thin at home: cheese |
| hold banquet 4 | mansion | 17.5 | 56.6 | 56.6 | thin at home: ham, stockfish, cheese |
| jousting 3 | arena | 230 | 56.6 | 56.8 | needs a arena (build cost 24,800); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 57.4 | 57.4 | thin at home: cheese |
| jousting 2 | arena | 210 | 62.0 | 62.2 | needs a arena (build cost 24,800); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 62.5 | 62.5 | thin at home: cheese, pies |
| hold banquet 2 (pies) | mansion | 7 | 63.4 | 63.4 | thin at home: cheese, pies |
| hold feast 2 | townhouse | 2.6 | 57.4 | 64.2 | needs a townhouse (build cost 8,298) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 11 @ 14.2; crew 0.1; est +42 a turn; stock: pasties 11 @ 14.2 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Chatgnan +60, Cobholme +58, Friedwerp +51, Herschweig +45, Caillechâtel +42
- Chatgnan would trade: furniture buy 4 @ 13.2, pasties buy 7 @ 16.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 1.00 (101/turn) | thread 63 (4.66->7.27), bread 110 (2.23->3.04), timber 16 (8.56->12.73), charcoal 13 (2.42->5.56) | mouldboards 0 (42.21->45.03), seeds 3 (2.54->2.94), flax plants 3 (1.47->1.72) | +324 |
| Hofkirchen | 991 | 0.32 | 1.00 (101/turn) | candles 1 (89.25->216.6), bread 96 (2.23->4.1), lead ore 2 (6.88->11.97), grain 1 (2.46->3.78) | cloth 10 (7.56->9.3), garments 1 (23.31->25.2), flax fibres 16 (5.78->6.5), tar 7 (10.61->11.4) | +280 |
| Grandgues | 152 | 0.04 | 0.30 (30/turn) | beer 60 (3.63->4.99), charcoal 19 (2.42->5.61), timber 25 (8.56->9.88), limestone 1 (14.91->18.52) | tools 9 (4.89->5.61), candles 1 (80.85->85), flour 2 (20.48->21.28), bricks 2 (9.29->10.36) | +168 |
| Kirchwerp | 1072 | 0.36 | 0.70 (70/turn) | thread 95 (4.66->5.7), furniture 9 (16.59->21.09), lead ore 9 (6.88->10.45), nails 3 (8.29->12.35) | cloth 24 (8.45->9.3), candles 1 (77.7->85), garments 2 (24.36->25.2), chisels 1 (8.4->9.12) | +160 |
| Calange | 218 | 0.06 | 0.20 (20/turn) | dyed cloth 19 (14.18->18.81), charcoal 19 (2.42->3.63), medicine 1 (138.6->152.95), lead ore 2 (6.88->8.64) | bricks 2 (5.88->10.36), cloth 10 (8.72->9.3), flax fibres 2 (4.94->6.5), mouldboards 1 (42->45.03) | +143 |

**Best:** Fontaux at about +324 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 a turn at 3.26, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 16.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 2) |
| light armour | 1 @ 110, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 38.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.5k (cash + stock at home prices); +161/turn over 6 turns, +189/turn over 24 turns.
- Limits: cash flow >= -321/turn, prestige >= -0.26/turn (values are after 200 tax a turn).
- Today's settings: value +90/turn, cash +72/turn, prestige -2.02/turn - breaks the prestige floor.
- Plan: value -0/turn, cash +3/turn, prestige -0.26/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +140 vs +76, +93 vs +76, +142 vs +76.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Unterhufe: +5/turn
  - ship Flax Wyrm -> Chatgnan: +1/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: -5/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.18: +15/turn
  - flax farm 1 4.64 -> 5.38: -6/turn
  - retting pit 1 0.91 -> 1.05: +1/turn
  - spinnery 1 1.65 -> 1.86: -2/turn
  - weavery 1 0.50 -> 0.60: -2/turn
  - sewing shop 1 0.30 -> 0.36: +13/turn
- Model check over the last 59 turns: predicted +104/turn for the settings we ran, real +71/turn.
- Worth of one more unit per turn: labour 1.56, thread 3.92, cloth 6.26, flax fibres 4.64, garments 18.11, nets 28.51, beer 2.79, timber 3.35, prestige 64.97, cash 0.00
- Orders it would set: beer sell 16 (v2 none); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 2); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.18, worth +10/turn.
- Ship linen snake: Grandgues -> Unterhufe (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1584 coin: +3/turn, payback 514 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 964/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.5 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
- R7 stale ask: limestone ask 16.4 over the market for 4 turns: the town trades ~5 a turn at 14.2, we sold 0 with 40 over what we keep; floor 19.37 (config sell_floor / unit cost) is at or over the market: Taylor's call
