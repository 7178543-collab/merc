# v2 shadow report

Turn 13887, 2026-11-09 00:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,232, prestige 3,529 (409 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 8 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 10 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

514 turns left: prestige gained now converts 92.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.5 | 52.5 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.5 | 55.5 | thin at home: pasties, ham, stockfish |
| jousting 3 | arena | 230 | 55.8 | 56.0 | needs a arena (build cost 27,004); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 57.6 | 57.6 | thin at home: ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.7 | 57.7 | thin at home: ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.8 | 58.8 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 59.9 | 59.9 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.2 | 60.2 | thin at home: cured fish |
| jousting 2 | arena | 210 | 61.1 | 61.3 | needs a arena (build cost 27,004); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 61.6 | 61.6 | thin at home: pasties |
| hold banquet 2 (pies) | mansion | 7 | 63.7 | 63.7 | thin at home: pasties |
| hold banquet 3 (meat) | mansion | 7.6 | 63.8 | 63.8 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.4 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Gotthafen +349, Essenbrucke +314, Donaunieder +304, Großmühle +299, Fulkirch +293
- Gotthafen would trade: furniture buy 31 @ 13.9, pasties buy 2 @ 15.5; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (113/turn) | bread 140 (2.37->3.1), timber 29 (7.61->11.02), charcoal 17 (2.46->5.08), firewood 34 (2.5->4.64) | cloth 8 (10.45->11.1), tools 8 (4.79->5.13), flax plants 2 (1.55->1.7), flour 1 (21->21.47) | +281 |
| Rotterburg | 1056 | 0.40 | 0.20 (23/turn) | wine 31 (6.77->9.03), looms 1 (598.5->608), nets 4 (37->39.14), malt 2 (5.41->7.27) | cloth 24 (7.09->11.1), garments 20 (21.63->26.03), candles 1 (79.8->80.5) | +238 |
| Rouhomme | 368 | 0.11 | 1.00 (113/turn) | bread 155 (2.37->3.42), charcoal 19 (2.46->5.37), malt 5 (5.41->11.4), grain 122 (2.92->3.25) | tools 17 (4.51->5.13), ploughs 1 (67.73->76), cloth 7 (10.45->11.1), flax fibres 3 (5.62->6.35) | +230 |
| Kirchwerp | 1072 | 0.41 | 0.50 (56/turn) | wine 24 (6.77->9.5), thread 84 (4.64->5.7), casks 4 (6.56->8.31), chisels 3 (10.13->11.69) | cloth 24 (7.88->11.1), garments 20 (24.15->26.03), dyed cloth 7 (13.12->13.77) | +218 |
| Heilegg | 826 | 0.26 | 0.20 (23/turn) | nets 6 (37->41.04), casks 4 (6.56->9.17), malt 4 (5.41->6.93) | garments 20 (22.68->26.03), cloth 24 (8.77->11.1), cured meat 8 (24.36->24.89) | +145 |

**Best:** Grandgues at about +281 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.42) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 82.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 26.6) |
| grain | 18 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 10 = 1.1 turns |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 110, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.7k (cash + stock at home prices); +263/turn over 6 turns, +71/turn over 24 turns.
- Limits: cash flow >= -301/turn, prestige >= -0.45/turn (values are after 200 tax a turn).
- Today's settings: value +61/turn, cash +20/turn, prestige -2.05/turn - breaks the prestige floor.
- Plan: value +6/turn, cash +8/turn, prestige -0.45/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +312 vs +39, -28 vs +16, +74 vs +22.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +10/turn
  - ship Flax Wyrm -> no route: +0/turn
  - ropewalk 1 0.25 -> 0.00: +12/turn
  - net maker 0.00 -> 0.29: +9/turn
  - spinnery 1 1.65 -> 1.26: +1/turn
  - retting pit 1 0.91 -> 0.71: -6/turn
  - flax farm 1 4.64 -> 3.58: -12/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.19: -5/turn
  - brewery 1 0.14 -> 0.00: -3/turn
  - mansion 1 0.00 -> 0.38: -69/turn
- Model check over the last 59 turns: predicted +102/turn for the settings we ran, real -16/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 30.02, beer 2.87, timber 3.26, prestige 61.82, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.19, worth +15/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +3/turn.
- Ship linen snake: Grandgues -> Donaunieder (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3676 coin: +10/turn, payback 360 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 27/77, thread 833/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.35 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
