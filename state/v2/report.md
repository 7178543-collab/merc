# v2 shadow report

Turn 13883, 2026-11-08 20:05. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,995, prestige 3,537 (417 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
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

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **firewood**: home ask 2.46 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

518 turns left: prestige gained now converts 92.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.8 | 52.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.8 | 55.8 | thin at home: hop beer, wine, ham, stockfish |
| jousting 3 | arena | 230 | 56.1 | 56.4 | needs a arena (build cost 25,886); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 58.0 | 58.0 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 58.2 | 58.2 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.5 | 58.5 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 60.5 | 60.5 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 61.5 | 61.5 | thin at home: pasties, hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 61.6 | 61.6 | thin at home: wine, cured fish |
| jousting 2 | arena | 210 | 61.5 | 61.8 | needs a arena (build cost 25,886); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 58.7 | 63.7 | needs a church (build cost 66,245); thin at home: candles, furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 64.3 | 64.3 | thin at home: hop beer, cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.4 (keep 14); best orders clear only -3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Gotthafen +363, Brunnham +311, Essenbrucke +298, Brebronn +296, Donaunieder +270
- Gotthafen would trade: furniture buy 31 @ 13.4, pasties buy 1 @ 15.3; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.60 (66/turn) | bread 156 (2.42->3.32), timber 32 (7.56->11.4), cured fish 6 (25.41->33.63), charcoal 19 (2.18->4.99) | tools 9 (4.58->5.22), candles 1 (77.7->79.5), flax fibres 2 (5.67->6.35), flax plants 3 (1.47->1.68) | +344 |
| Rouhomme | 368 | 0.11 | 1.00 (110/turn) | bread 156 (2.42->3.57), charcoal 19 (2.18->5.13), garments 10 (22.4->23.75), grain 120 (2.96->3.27) | tools 17 (4.51->5.22), flax fibres 3 (4.94->6.35), salt 7 (5.35->5.56), candles 1 (79.28->79.5) | +231 |
| Hofkirchen | 991 | 0.34 | 0.90 (99/turn) | grain 120 (2.96->4.8), thread 21 (4.46->5.7), nets 5 (34.2->36.29), wheels 2 (22.47->23.18) | salt 9 (4.56->5.56), cloth 24 (8.29->8.85), flax fibres 26 (5.46->6.35), candles 1 (75.6->79.5) | +186 |
| Pontmont | 341 | 0.10 | 0.70 (77/turn) | garments 10 (22.4->31.54), charcoal 19 (2.18->4.75), bread 156 (2.42->2.89), nets 5 (34.2->36.1) | salt 9 (5.25->5.56), flax fibres 1 (5.62->6.35) | +169 |
| Kirchwerp | 1072 | 0.39 | 0.50 (55/turn) | thread 81 (4.46->5.7), wine 5 (7.67->9.5), nets 6 (34.2->35.91), casks 10 (6.98->8.31) | cloth 24 (7.56->8.85), dyed cloth 5 (12.6->13.59), flax fibres 27 (5.46->6.35), candles 1 (77.17->79.5) | +118 |

**Best:** Grandgues at about +344 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.52) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 12.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.9k (cash + stock at home prices); +225/turn over 6 turns, -116/turn over 24 turns.
- Limits: cash flow >= -291/turn, prestige >= -0.49/turn (values are after 200 tax a turn).
- Today's settings: value +48/turn, cash +16/turn, prestige -2.10/turn - breaks the prestige floor.
- Plan: value -6/turn, cash +48/turn, prestige -0.49/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +2 vs +57, +59 vs +57, +312 vs +39.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +16/turn
  - ship Flax Wyrm -> no route: +0/turn
  - ropewalk 1 0.25 -> 0.00: +11/turn
  - net maker 0.00 -> 0.29: +10/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.06: +9/turn
  - brewery 1 0.14 -> 0.21: -8/turn
  - sewing shop 1 0.30 -> 0.36: -10/turn
  - weavery 1 0.50 -> 0.60: +11/turn
  - spinnery 1 1.65 -> 1.08: -11/turn
  - retting pit 1 0.91 -> 0.61: +10/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real -28/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 4.01, cloth 6.38, flax fibres 4.83, garments 18.44, nets 28.82, beer 2.92, timber 3.24, prestige 60.45, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.06, worth +3/turn.
- Ship linen snake: Grandgues -> Corstoft (+16/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1778 coin: +1/turn, payback 3473 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 788/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.35 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
