# v2 shadow report

Turn 13841, 2026-11-07 02:05. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,476, prestige 3,386 (266 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 6 | 0 | 4 | 0 | 0 | min_holding 60, sell 11, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 29, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 507 | 0 | 22 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 6.4 -> v2: add buy 5
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.62 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.62 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~35 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 607

## Prestige spending, cheapest coin per prestige first

560 turns left: prestige gained now converts 94.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 53.2 | 53.2 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 53.5 | 53.5 |  |
| hold banquet 4 (pies) | mansion | 18 | 53.9 | 53.9 | thin at home: ham, stockfish |
| jousting 3 | arena | 230 | 53.9 | 54.1 | needs a arena (build cost 25,828); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 54.2 | 54.2 | thin at home: pasties |
| hold banquet 2 (meat) | mansion | 6.8 | 55.5 | 55.5 |  |
| hold banquet 3 (pies) | mansion | 8 | 56.7 | 56.7 | thin at home: pasties |
| hold banquet 3 (fish) | mansion | 7.6 | 56.8 | 56.8 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 56.9 | 56.9 |  |
| hold banquet 4 | mansion | 17.5 | 56.9 | 56.9 | thin at home: ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 58.4 | 58.4 | thin at home: ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 15.5 (keep 14); best orders clear only 13 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.4 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Bedenis +29, Clairlond +26, Bordees +26, Rouhomme +25, Orlesailles +25
- Bedenis would trade: pasties buy 7 @ 13.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.70 (72/turn) | thread 48 (4.66->7.27), timber 23 (7.25->11.3), wine 13 (6.51->7.74), salt 4 (4.49->7.79) | flax fibres 10 (5.46->6), cloth 3 (10.19->10.8), slaked lime 1 (9.08->10.83) | +222 |
| Neuborn | 780 | 0.22 | 1.00 (104/turn) | timber 25 (7.25->12.54), furniture 10 (15.75->17.86), rope 0 (80->90.25), raw cloth 1 (7.51->9.17) | cloth 10 (8.77->10.8), flax fibres 19 (5.25->6), thread 13 (4.39->5.1), candles 0 (77.7->84) | +129 |
| Heilegg | 826 | 0.23 | 0.20 (21/turn) | nets 4 (32.2->38.76), wool 6 (9.19->12.25), wine 20 (6.51->7.55), raw cloth 4 (7.51->11.59) | garments 2 (22.68->26.6), flax fibres 20 (5.25->6) | +87 |
| Etallaen | 774 | 0.21 | 0.40 (41/turn) | medicine 1 (138.6->149.15), timber 9 (7.25->11.3), cured fish 10 (24.36->25.46), wine 6 (6.51->7.08) | cloth 24 (9.03->10.8), candles 1 (76.65->84), gears 1 (65.62->71.72), garments 2 (24.78->26.6) | +85 |
| Hofkirchen | 991 | 0.33 | 0.80 (83/turn) | beer 95 (3.46->4.64), lead bars 9 (19.64->20.71), glass ingots 1 (64.05->68.4), nets 5 (32.2->33.25) | flax fibres 27 (5.17->6), candles 1 (79.8->84), garments 2 (24.36->26.6), gears 1 (66.67->71.72) | +83 |

**Best:** Fontaux at about +222 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.46, stop 9 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 6 = 1.5 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 3 @ min 1.21 | goal planner: sells 3 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 94, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.7k (cash + stock at home prices); +75/turn over 6 turns, -29/turn over 24 turns.
- Limits: cash flow >= -270/turn, prestige >= +1.40/turn (values are after 200 tax a turn).
- Today's settings: value +60/turn, cash +31/turn, prestige -1.54/turn - breaks the prestige floor.
- Plan: value -67/turn, cash -58/turn, prestige +1.40/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +150 vs +51, +178 vs +48, -3 vs +16.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.28: +8/turn
  - ropewalk 1 0.25 -> 0.00: +3/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.11: +14/turn
  - flax farm 1 4.64 -> 3.87: -2/turn
  - retting pit 1 0.91 -> 0.79: -2/turn
  - spinnery 1 1.65 -> 1.39: +6/turn
  - weavery 1 0.50 -> 0.61: -9/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
- Model check over the last 61 turns: predicted +97/turn for the settings we ran, real +26/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.61, thread 4.09, cloth 6.50, flax fibres 4.92, garments 18.77, nets 29.16, beer 3.04, timber 3.10, prestige 55.98, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 3 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.11, worth +6/turn.
- Ship linen snake: Grandgues -> Brunnham (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 434 (+146 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.86 |
| ret | 3 | 0.91 | 0.97 |
| spin | 4 | 1.65 | 1.72 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 565/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 6.4 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.3 -> **buy 9 @ 3.36 (ask 3.3, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.62; ask over the cap 2.1 (60 coin per prestige)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.0 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
