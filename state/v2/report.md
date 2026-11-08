# v2 shadow report

Turn 13870, 2026-11-08 07:35. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,792, prestige 3,488 (368 free, -1.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.28 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 9 | 9 | 9 | 0 | 0 | stop 35, buy 9, buy @ 3.7 |
| labour | 30 | 29 | 518 | 0 | 11 | buy 30, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 102 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

531 turns left: prestige gained now converts 93.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| jousting 3 | arena | 230 | 54.3 | 54.5 | needs a arena (build cost 24,746); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 54.8 | 54.8 | thin at home: pasties, hop beer, wine, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.4 | 55.4 |  |
| hold banquet 4 | mansion | 17.5 | 57.3 | 57.3 | thin at home: wine, hop beer, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.4 | 57.4 | thin at home: hop beer, wine, ham, stockfish, premium cheese |
| jousting 2 | arena | 210 | 59.5 | 59.7 | needs a arena (build cost 24,746); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.2 | 60.2 | thin at home: wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 | thin at home: hop beer, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 61.5 | 61.5 | thin at home: cured meat |
| hold banquet 3 (pies) | mansion | 8 | 61.6 | 61.6 | thin at home: pasties, hop beer, cheese |
| jousting 1 | arena | 170 | 63.2 | 63.5 | needs a arena (build cost 24,746); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Bordetes +24, Amsdermund +20, Rotterburg +20
- Bordetes would trade: pasties buy 14 @ 16.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (107/turn) | firewood 34 (2.18->4.8), charcoal 19 (2.84->4.08), bread 152 (2.71->2.89), bricks 3 (7.14->10.26) | candles 1 (76.65->80.5), cured meat 11 (22.89->23.18), flax plants 3 (1.29->1.53), wool 1 (13.02->13.49) | +101 |
| Pontmont | 341 | 0.10 | 0.90 (96/turn) | bread 152 (2.71->3.15), charcoal 19 (2.84->4.75), garments 10 (24.4->25.65), grain 100 (2.81->3.12) | gold ore 1 (142.8->151.05), candles 1 (77.7->80.5) | +96 |
| Amsdermund | 1111 | 0.41 | 0.30 (32/turn) | gold ore 1 (180.6->203.3), cured fish 8 (24.57->27.93), glass ingots 1 (55.12->62.22), lead bars 3 (19.11->20.52) | rope 7 (79.8->83.6), tools 16 (4.37->5.08), candles 1 (76.65->80.5), cloth 24 (7.88->8.4) | +87 |
| Darmwald | 1022 | 0.35 | 0.30 (32/turn) | beer 15 (3.26->6.37), glass ingots 1 (55.12->63.65), hides 2 (11.87->15.77), tiles 2 (3.38->9.21) | cloth 24 (7.35->8.4), rope 1 (81.38->83.6), wool 2 (12.29->13.49) | +83 |
| Brebronn | 862 | 0.26 | 0.10 (11/turn) | garments 10 (24.4->29.83), glass ingots 1 (55.12->58.42), cloth 1 (8.3->10.07), flour 2 (18.06->20.9) | candles 1 (72.98->80.5), yarn 9 (3.93->4.71), tar 6 (10.5->11.4), wool 2 (12.6->13.49) | +74 |

**Best:** Grandgues at about +101 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.26 | goal planner: sells 15 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.6) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 93, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.6k (cash + stock at home prices); +87/turn over 6 turns, -34/turn over 24 turns.
- Limits: cash flow >= -200/turn, prestige >= -0.28/turn (values are after 200 tax a turn).
- Today's settings: value +83/turn, cash +67/turn, prestige -1.85/turn - breaks the prestige floor.
- Plan: value +11/turn, cash +14/turn, prestige -0.28/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +56 vs +61, +53 vs +64, +52 vs +61.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rouhomme: +5/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - weavery 1 0.50 -> 0.43: -6/turn
  - spinnery 1 1.65 -> 1.35: -6/turn
  - retting pit 1 0.91 -> 0.77: +4/turn
  - flax farm 1 4.64 -> 3.82: -2/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.24: -16/turn
  - ropewalk 1 0.25 -> 0.00: +20/turn
  - mansion 1 0.00 -> 0.37: -78/turn
- Model check over the last 58 turns: predicted +103/turn for the settings we ran, real +1/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 29.97, beer 2.91, timber 3.26, prestige 60.52, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 18); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.24, worth +10/turn.
- Ship linen snake: Grandgues -> Rouhomme (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/77, thread 642/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.75 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
