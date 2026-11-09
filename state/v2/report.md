# v2 shadow report

Turn 13889, 2026-11-09 02:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,215, prestige 3,525 (405 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 8 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 28 | 18 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.90 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.90 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

512 turns left: prestige gained now converts 92.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.6 | 55.6 | thin at home: hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 55.5 | 55.7 | needs a arena (build cost 28,096); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 57.7 | 57.7 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 57.7 | 57.7 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 60.1 | 60.1 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 60.1 | 60.1 | thin at home: hop beer, cured fish |
| jousting 2 | arena | 210 | 60.8 | 61.0 | needs a arena (build cost 28,096); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 61.2 | 61.2 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 61.5 | 61.5 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 63.2 | 63.2 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 64.2 | 64.2 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.0 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 0 a turn after crew: ship stays at 0
- best towns now: Gotthafen +349, Donaunieder +322, Brunnham +305, Essenbrucke +298, Clairlond +290
- Gotthafen would trade: furniture buy 31 @ 13.9, pasties buy 2 @ 15.8; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~112 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Großmühle | 751 | 0.23 | 0.10 (11/turn) | wine 17 (6.83->8.17), nets 6 (37->38.19) | looms 1 (535.5->703), cloth 6 (9.13->10.8), cookware 5 (25.41->27.36), garments 2 (25.2->27.6) | +216 |
| Grandgues | 152 | 0.04 | 0.80 (90/turn) | timber 32 (7.56->11.3), firewood 38 (2.58->5.51), bricks 5 (7.4->10.92), beer 15 (3.52->4.14) | cloth 9 (8.87->10.8), cookware 5 (26.25->27.36), salt 5 (5.41->5.56), flax plants 1 (1.49->1.73) | +198 |
| Rouhomme | 368 | 0.11 | 0.50 (56/turn) | bread 154 (2.75->3.55), flour 1 (24.15->31.35), malt 3 (7.56->9.07), yarn 8 (5.3->5.7) | looms 1 (640.5->703), cookware 5 (23.31->27.36), candles 1 (78.23->80.5), cloth 7 (10.45->10.8) | +174 |
| Neuborn | 780 | 0.23 | 1.00 (112/turn) | timber 29 (7.56->13.3), seeds 10 (2.52->3.32), grain 1 (2.76->3.52), malt 0 (7.56->8.98) | looms 0 (645.75->703), cloth 7 (8.93->10.8), garments 1 (24.78->27.6), salt 5 (4.62->5.56) | +147 |
| Blanans | 297 | 0.09 | 0.50 (56/turn) | timber 32 (7.56->10.83), lead ore 4 (12.29->16.43), wine 7 (6.83->8.12), flour 1 (24.15->26.79) | cloth 15 (8.56->10.8), cookware 5 (24.57->27.36), dyed cloth 6 (12.6->13.87), salt 6 (4.96->5.56) | +143 |

**Best:** Großmühle at about +216 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.42) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 82.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 25.6) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 14) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.3k (cash + stock at home prices); +233/turn over 6 turns, +87/turn over 24 turns.
- Limits: cash flow >= -301/turn, prestige >= -0.44/turn (values are after 200 tax a turn).
- Today's settings: value +54/turn, cash +13/turn, prestige -2.03/turn - breaks the prestige floor.
- Plan: value -2/turn, cash +49/turn, prestige -0.44/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +74 vs +22, -115 vs +20, +98 vs +9.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bremcop: +9/turn
  - ship Flax Wyrm -> no route: +0/turn
  - ropewalk 1 0.25 -> 0.00: +13/turn
  - net maker 0.00 -> 0.29: +9/turn
  - weavery 1 0.50 -> 0.61: -4/turn
  - sewing shop 1 0.30 -> 0.36: +10/turn
  - brewery 1 0.14 -> 0.20: -8/turn
  - spinnery 1 1.65 -> 1.08: -9/turn
  - retting pit 1 0.91 -> 0.61: +8/turn
  - flax farm 1 4.64 -> 3.08: -10/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real -20/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.65, thread 4.18, cloth 6.64, flax fibres 5.02, garments 19.19, nets 30.03, beer 2.96, timber 3.62, prestige 62.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +3/turn.
- Ship linen snake: Grandgues -> Bremcop (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/77, thread 855/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.25 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
