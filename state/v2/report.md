# v2 shadow report

Turn 13929, 2026-11-10 18:07. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,406, prestige 3,446 (326 free, -1.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 26 | 6 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 26, buy 7, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~73 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 486, not 586

## Prestige spending, cheapest coin per prestige first

472 turns left: prestige gained now converts 90.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.8 | 54.8 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 55.0 | 55.0 | thin at home: wine, cheese |
| hold banquet 4 (pies) | mansion | 18 | 55.4 | 55.4 | thin at home: wine, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 56.1 | 56.4 | needs a arena (build cost 26,018); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 57.1 | 57.1 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.2 | 57.2 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.8 | 57.8 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 2 (pies) | mansion | 7 | 59.4 | 59.4 | thin at home: wine, cheese |
| hold banquet 3 (pies) | mansion | 8 | 60.2 | 60.2 | thin at home: cheese |
| hold feast 2 | townhouse | 2.6 | 55.5 | 61.7 | needs a townhouse (build cost 7,326); thin at home: wine |
| jousting 2 | arena | 210 | 61.4 | 61.7 | needs a arena (build cost 26,018); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 8 @ 15.5; crew 0.1; est +17 a turn; stock: pasties 8 @ 15.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 8 @ 15.8 (keep 14); best orders clear only 15 a turn after crew: ship stays at 0
- best towns now: Herschweig +289, Marmont +219, Friedwerp +216, Unterhufe +210, Toqueque +208
- Herschweig would trade: furniture buy 17 @ 14.1, pasties buy 14 @ 11.0; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.06 | 0.30 (30/turn) | bread 149 (2.75->3.67), wax 3 (22.68->27.17) | flax fibres 9 (4.89->6.55), cloth 8 (7.35->8), candles 1 (82.42->86.5), thread 12 (4.73->5) | +157 |
| Grandgues | 152 | 0.04 | 0.30 (30/turn) | timber 36 (7.72->11.69), flax plants 1 (1.25->1.67), flour 1 (27.93->28.5), grain 2 (2.54->2.83) | flax fibres 5 (5.83->6.55), furniture 1 (16.17->18.5), cloth 12 (7.88->8), salt 5 (5.35->5.56) | +122 |
| Fontaux | 411 | 0.11 | 1.00 (101/turn) | bread 130 (2.75->3.44), thread 81 (4.9->5.37), timber 21 (7.72->10.64), garments 9 (22.8->23.75) | candles 0 (85.58->86.5), chisels 0 (7.77->8.64), furniture 0 (17.12->18.5) | +121 |
| Neuborn | 780 | 0.21 | 1.00 (101/turn) | timber 30 (7.72->13.3), honey 0 (7.93->8.41) | cured meat 8 (21->24.51), cloth 20 (7.35->8), furniture 0 (15.33->18.5), cheese 3 (5.25->5.79) | +110 |
| Blanans | 297 | 0.08 | 0.90 (91/turn) | timber 36 (7.72->9.88), bread 149 (2.75->3.06), limestone 1 (18.17->23.75), grain 2 (2.54->3.23) | jewellery 2 (93.98->101.65), cloth 12 (7.35->8), salt 6 (5.04->5.56), flax fibres 2 (5.93->6.55) | +72 |

**Best:** Vauxvais at about +157 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 26 = 6.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 88.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.2) |
| grain | 6 @ 3.7, stop 24 |  | goal planner: buys 6 a turn for today's rates, keeps up to 24 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 99.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.4k (cash + stock at home prices); +261/turn over 6 turns, +184/turn over 24 turns.
- Limits: cash flow >= -309/turn, prestige >= -0.11/turn (values are after 200 tax a turn).
- Today's settings: value +37/turn, cash -14/turn, prestige -1.84/turn - breaks the prestige floor.
- Plan: value -23/turn, cash -20/turn, prestige -0.11/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +47 vs +25, +76 vs +9, +24 vs -3.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Unterhufe: +5/turn
  - ship Flax Wyrm -> Brunnham: +3/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: +3/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.08: +16/turn
  - sewing shop 1 0.30 -> 0.36: -5/turn
  - weavery 1 0.50 -> 0.60: +7/turn
  - spinnery 1 1.65 -> 1.36: -5/turn
  - retting pit 1 0.91 -> 0.77: +0/turn
  - flax farm 1 4.64 -> 2.92: +8/turn
- Model check over the last 60 turns: predicted +107/turn for the settings we ran, real +150/turn.
- Worth of one more unit per turn: labour 1.61, thread 4.04, cloth 6.46, flax fibres 4.79, garments 18.69, nets 29.11, beer 2.87, timber 3.31, prestige 62.53, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.08, worth +5/turn.
- Ship linen snake: Grandgues -> Unterhufe (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brunnham (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1751 coin: +1/turn, payback 1569 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 62/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.55 for 6 turns, bought 0.0 of 1, 62.0 held (2.6 turns); raise needs Taylor (ceiling None)
