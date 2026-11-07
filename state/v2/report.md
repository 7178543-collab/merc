# v2 shadow report

Turn 13842, 2026-11-07 03:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,598, prestige 3,385 (265 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 11 | 0 | 4 | 0 | 0 | min_holding 60, sell 11, sell @ 3.06; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 507 | 0 | 22 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~35 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 607

## Prestige spending, cheapest coin per prestige first

559 turns left: prestige gained now converts 94.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 53.3 | 53.3 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 |  |
| hold banquet 4 (pies) | mansion | 18 | 53.7 | 53.7 | thin at home: ham, stockfish |
| jousting 3 | arena | 230 | 53.7 | 53.9 | needs a arena (build cost 25,865); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 54.8 | 54.8 | thin at home: pasties |
| hold banquet 2 (meat) | mansion | 6.8 | 55.5 | 55.5 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 56.3 | 56.3 |  |
| hold banquet 3 (pies) | mansion | 8 | 56.6 | 56.6 | thin at home: pasties |
| hold banquet 4 | mansion | 17.5 | 56.7 | 56.7 | thin at home: ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 56.9 | 56.9 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.1 | 58.1 | thin at home: ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 8 @ 15.5; crew 0.1; est +17 a turn; stock: pasties 8 @ 15.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.4 (keep 14); best orders clear only 0 a turn after crew: ship stays at 0
- best towns now: Bedenis +35, Rouhomme +31, Orlesailles +27, Pontmont +25, Clairas +25
- Bedenis would trade: pasties buy 8 @ 13.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.70 (72/turn) | timber 28 (7.19->11.69), tapestries 2 (630->660.25), thread 48 (4.66->5.65), furniture 12 (15.54->18.14) | lead bars 1 (12.71->16.53), salt 5 (4.73->4.94) | +214 |
| Etallaen | 774 | 0.21 | 0.20 (20/turn) | tapestries 2 (630->665), cured meat 5 (23.31->26.41), wine 7 (6.14->8.03), cheese 10 (5.99->6.84) | silver bars 1 (296.1->326.8), garments 19 (24.36->26.03), candles 1 (78.75->83.5), flax fibres 5 (4.94->5.95) | +183 |
| Orlesailles | 1178 | 0.42 | 0.20 (20/turn) | tapestries 2 (630->665), rope 1 (80->85.02), wool 1 (9.29->12.06), nets 6 (32.2->33.25) | garments 19 (20.48->26.03), candles 1 (78.75->83.5), salt 5 (4.28->4.94), pies 1 (14.8->16.43) | +175 |
| Hofkirchen | 991 | 0.32 | 0.90 (92/turn) | beer 101 (3.46->4.89), nets 5 (32.2->35.72), glass ingots 1 (56.18->68.4), blades 6 (14.91->17.1) | garments 19 (24.36->26.03), flax fibres 27 (5.17->5.95), candles 1 (79.8->83.5), salt 5 (4.45->4.94) | +163 |
| Kirchwerp | 1072 | 0.37 | 0.40 (41/turn) | tapestries 2 (630->665), thread 48 (4.66->5.7), fleece 4 (7.46->8.79), rope 1 (80->82.17) | garments 19 (23.1->26.03), flax fibres 27 (5.17->5.95), cookware 9 (23.73->24.13), copper ingots 1 (14.18->14.82) | +153 |

**Best:** Fontaux at about +214 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 3 @ min 1.21 | goal planner: sells 3 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 26.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 94, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 2.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.8k (cash + stock at home prices); +100/turn over 6 turns, -36/turn over 24 turns.
- Limits: cash flow >= -275/turn, prestige >= +1.47/turn (values are after 200 tax a turn).
- Today's settings: value +73/turn, cash +53/turn, prestige -1.53/turn - breaks the prestige floor.
- Plan: value -61/turn, cash -47/turn, prestige +1.47/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +178 vs +48, -3 vs +16, +123 vs +29.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.28: +8/turn
  - flax farm 1 4.64 -> 4.02: -1/turn
  - retting pit 1 0.91 -> 0.82: -1/turn
  - spinnery 1 1.65 -> 1.44: +5/turn
  - ropewalk 1 0.25 -> 0.00: +3/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.17: +9/turn
  - sewing shop 1 0.30 -> 0.36: -8/turn
  - weavery 1 0.50 -> 0.60: +10/turn
- Model check over the last 61 turns: predicted +97/turn for the settings we ran, real +22/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.63, thread 4.14, cloth 6.58, flax fibres 4.97, garments 19.00, nets 29.48, beer 3.02, timber 3.08, prestige 56.06, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 3 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.17, worth +7/turn.
- Ship linen snake: Grandgues -> Brunnham (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 435 (+146 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.87 |
| ret | 3 | 0.91 | 0.97 |
| spin | 4 | 1.65 | 1.72 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 562/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.95 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
