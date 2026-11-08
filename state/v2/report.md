# v2 shadow report

Turn 13885, 2026-11-08 22:17. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,042, prestige 3,533 (413 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 8 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 9 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

516 turns left: prestige gained now converts 92.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 52.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.5 | 55.5 | thin at home: hop beer, wine, ham, stockfish |
| jousting 3 | arena | 230 | 55.7 | 56.0 | needs a arena (build cost 27,240); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 57.8 | 57.8 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 57.9 | 57.9 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.1 | 59.1 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 59.9 | 59.9 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 | thin at home: wine, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 61.1 | 61.1 | thin at home: pasties, hop beer |
| jousting 2 | arena | 210 | 61.0 | 61.3 | needs a arena (build cost 27,240); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 63.4 | 63.4 | thin at home: pasties, wine |
| hold banquet 3 (meat) | mansion | 7.6 | 64.0 | 64.0 | thin at home: hop beer, cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Gotthafen +346, Brunnham +303, Brebronn +296, Essenbrucke +294, Fulkirch +289
- Gotthafen would trade: furniture buy 31 @ 14.0, pasties buy 1 @ 12.5; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (113/turn) | cured fish 5 (26.88->36.1), timber 29 (8.19->10.54), charcoal 17 (2.6->5.51), bread 141 (2.39->2.74) | cloth 8 (8.93->14), tackles 0 (161.7->169.1), flax plants 0 (1.48->1.71) | +286 |
| Rouhomme | 368 | 0.11 | 1.00 (113/turn) | bread 156 (2.39->3.5), charcoal 19 (2.6->5.37), garments 10 (22.2->23.75), flour 2 (22.47->28.31) | cloth 8 (9.19->14), flax fibres 4 (5.62->6.25), salt 9 (5.19->5.56), tar 3 (10.61->11.4) | +243 |
| Kirchwerp | 1072 | 0.41 | 0.50 (57/turn) | thread 82 (4.66->5.7), casks 11 (6.09->8.31), wine 6 (7.35->9.5), chisels 3 (8.24->11.69) | cloth 24 (7.88->14), salt 9 (4.87->5.56), cured meat 14 (24.36->25.27), garments 2 (24.57->25.2) | +237 |
| Blanans | 297 | 0.09 | 0.50 (57/turn) | lead ore 10 (9.97->17.57), timber 32 (8.19->10.92), garments 10 (22.2->22.42), flax plants 1 (0.94->1.12) | cloth 15 (8.29->14), jewellery 1 (71.4->81.7), salt 9 (4.83->5.56), flax plants 10 (1.34->1.71) | +218 |
| Darmwald | 1022 | 0.38 | 0.30 (34/turn) | arms 2 (32.13->37.24), beer 15 (3.62->4.75), tiles 2 (3.19->9.88), lead ore 1 (9.97->16.43) | cloth 23 (7.56->14), belts 1 (26.46->29.45) | +173 |

**Best:** Grandgues at about +286 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.52) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 81.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 16, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.6) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 35.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.5k (cash + stock at home prices); +308/turn over 6 turns, -92/turn over 24 turns.
- Limits: cash flow >= -293/turn, prestige >= -0.47/turn (values are after 200 tax a turn).
- Today's settings: value +50/turn, cash +13/turn, prestige -2.07/turn - breaks the prestige floor.
- Plan: value -8/turn, cash -7/turn, prestige -0.47/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +312 vs +39, -28 vs +16, +74 vs +22.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +7/turn
  - ship Flax Wyrm -> Vauxvais: +1/turn
  - ropewalk 1 0.25 -> 0.00: +12/turn
  - net maker 0.00 -> 0.29: +10/turn
  - spinnery 1 1.65 -> 1.23: -4/turn
  - brewery 1 0.14 -> 0.21: -2/turn
  - retting pit 1 0.91 -> 0.69: +3/turn
  - flax farm 1 4.64 -> 3.47: -13/turn
  - mansion 1 0.00 -> 0.38: -70/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real -22/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 30.06, beer 2.97, timber 3.35, prestige 62.47, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.05, worth +2/turn.
- Ship linen snake: Grandgues -> Gosschweig (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+1/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/77, thread 810/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.25 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
