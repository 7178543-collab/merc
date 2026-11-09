# v2 shadow report

Turn 13903, 2026-11-09 16:21. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,695, prestige 3,497 (377 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 10 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

498 turns left: prestige gained now converts 91.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.1 | 55.1 | thin at home: ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 56.2 | 56.2 |  |
| jousting 3 | arena | 230 | 56.5 | 56.7 | needs a arena (build cost 26,982); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 57.4 | 57.4 | thin at home: ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.5 | 57.5 | thin at home: ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 58.1 | 58.1 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 59.5 | 59.5 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 61.0 | 61.0 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.6 | 61.6 | thin at home: cheese |
| jousting 2 | arena | 210 | 61.9 | 62.1 | needs a arena (build cost 26,982); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 64.7 | 64.7 | thin at home: cured meat, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 2 @ 13.8, pasties buy 5 @ 13.3; crew 0.1; est +43 a turn; stock: furniture 2 @ 13.8 (keep 145); stock: pasties 5 @ 13.3 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Caillechâtel +43, Orlesailles +42, Brunnham +35, Clarfranche +34, Bordetes +31
- Caillechâtel would trade: furniture buy 2 @ 13.8, pasties buy 5 @ 13.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (104/turn) | bread 154 (2.29->3.61), firewood 38 (2.33->6.46), timber 33 (8.45->10.36), nets 4 (38.4->39.14) | candles 1 (81.9->83), flax plants 5 (1.45->1.66) | +339 |
| Rouhomme | 368 | 0.10 | 1.00 (104/turn) | bread 90 (2.29->3.93), firewood 22 (2.33->5.89), hinges 0 (37.17->40.28), grain 1 (2.66->3.29) | cookware 4 (23.31->24.13), tools 10 (4.79->5.22), seeds 2 (1.94->2.94), candles 0 (79.8->83) | +153 |
| Amsdermund | 1111 | 0.40 | 0.10 (10/turn) | looms 1 (598.5->665), hinges 1 (37.17->51.3), chisels 3 (10.82->13.3), steel ingots 1 (16.48->16.91) | cloth 12 (7.88->9.85), dyed cloth 4 (10.24->11.88), garments 2 (24.57->27.4), hop beer 3 (6.62->8.64) | +115 |
| Heidlowe | 662 | 0.18 | 0.10 (10/turn) | looms 1 (598.5->669.75), nets 6 (38.4->39.71), lead ore 6 (9.87->11.11) | cloth 15 (8.35->9.85), tapestries 2 (619.5->622.25), salt 3 (4.6->5.56), furniture 1 (13.55->15.7) | +105 |
| Bremcop | 1326 | 0.52 | 0.20 (21/turn) | looms 1 (598.5->674.5), hinges 1 (37.17->40.28), pickaxes 1 (10.13->11.3) | cloth 12 (8.66->9.85), garments 2 (22.68->27.4), salt 8 (4.03->5.56), candles 1 (79.28->83) | +102 |

**Best:** Grandgues at about +339 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 26.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.9k (cash + stock at home prices); +220/turn over 6 turns, +205/turn over 24 turns.
- Limits: cash flow >= -279/turn, prestige >= -0.32/turn (values are after 200 tax a turn).
- Today's settings: value +97/turn, cash +88/turn, prestige -1.90/turn - breaks the prestige floor.
- Plan: value +14/turn, cash +17/turn, prestige -0.32/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +143 vs +63, +40 vs +70, +292 vs +74.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +4/turn
  - ship Flax Wyrm -> Heidlowe: +1/turn
  - net maker 0.00 -> 0.29: +8/turn
  - flax farm 1 4.64 -> 4.32: -2/turn
  - spinnery 1 1.65 -> 1.52: -2/turn
  - brewery 1 0.14 -> 0.21: -7/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +11/turn
  - mansion 1 0.00 -> 0.38: -92/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +66/turn.
- Worth of one more unit per turn: labour 1.63, thread 4.10, cloth 6.54, flax fibres 4.86, garments 18.93, nets 29.36, beer 2.95, timber 3.38, prestige 63.26, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Corstoft (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Heidlowe (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1946 coin: +1/turn, payback 1648 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 897/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.45 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
