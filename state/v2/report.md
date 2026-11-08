# v2 shadow report

Turn 13869, 2026-11-08 06:24. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,739, prestige 3,490 (370 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.28 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 9 | 7 | 7 | 2 | 0 | stop 33, buy 9, buy @ 3.7 |
| labour | 29 | 30 | 514 | 0 | 16 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.66 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **grain**: brewery 1 ran short of grain (buy is live (9 @ 3.7), 7 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 16 labour expired last turn (~26 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

532 turns left: prestige gained now converts 93.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.5 | 54.5 | thin at home: wine, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 54.6 | 54.8 | needs a arena (build cost 24,748); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.3 | 55.3 |  |
| hold banquet 4 (premium) | mansion | 20 | 57.0 | 57.0 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.1 | 57.1 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 59.8 | 59.8 | thin at home: wine, cheese |
| jousting 2 | arena | 210 | 59.8 | 60.1 | needs a arena (build cost 24,748); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 60.5 | 60.5 | thin at home: cured meat |
| hold banquet 3 (pies) | mansion | 8 | 61.2 | 61.2 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 63.1 | 63.1 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Bordetes +26, Amsdermund +24
- Bordetes would trade: pasties buy 14 @ 16.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (96/turn) | timber 22 (8.66->11.02), bread 152 (2.62->2.93), firewood 33 (2.79->4.84), grain 69 (3->3.34) | candles 1 (76.65->81), cured meat 12 (22.68->22.8), flax plants 3 (1.12->1.28) | +149 |
| Kirchwerp | 1072 | 0.38 | 0.50 (53/turn) | thread 68 (4.78->5.7), flour 2 (17.22->26.98), garments 10 (24.2->25.84), glass ingots 1 (52.29->58.9) | cloth 24 (7.35->8.5), rope 10 (79.8->81.22), candles 1 (76.12->81), dyed cloth 7 (12.6->13.21) | +111 |
| Brebronn | 862 | 0.26 | 0.10 (11/turn) | garments 10 (24.2->28.31), glass ingots 1 (52.29->58.42), nets 2 (33.6->34.39) | tapestries 1 (609->641.25), candles 1 (74.03->81), hinges 1 (36.12->37.24), wool 2 (12.81->13.11) | +80 |
| Darmwald | 1022 | 0.35 | 0.20 (21/turn) | beer 10 (3.26->6.22), glass ingots 1 (52.29->63.65), nets 2 (33.6->39.52), malt 1 (6.77->14.82) | cloth 24 (7.35->8.5), wool 2 (12.18->13.11) | +80 |
| Rouhomme | 368 | 0.10 | 0.50 (53/turn) | grain 100 (3->3.46), thread 17 (4.78->5.42), blades 5 (20.06->20.9), flour 2 (17.22->19.38) | cloth 17 (7.25->8.5), ploughs 1 (67.73->76), tools 16 (4.51->5.08), candles 1 (79.8->81) | +79 |

**Best:** Grandgues at about +149 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.6) |
| grain | 9 @ 3.7, stop 35 |  | goal planner: buys 9 a turn for today's rates, keeps up to 35 (v2 had 18) |
| labour | 30 @ 2.2, stop - |  | goal planner: buys 30 for today's rates (v2 had 18) |
| light armour | 1 @ 95.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.4k (cash + stock at home prices); +78/turn over 6 turns, -35/turn over 24 turns.
- Limits: cash flow >= -197/turn, prestige >= -0.29/turn (values are after 200 tax a turn).
- Today's settings: value +78/turn, cash +61/turn, prestige -1.86/turn - breaks the prestige floor.
- Plan: value +8/turn, cash +10/turn, prestige -0.29/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +90 vs +61, +56 vs +61, +53 vs +64.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - weavery 1 0.50 -> 0.43: -6/turn
  - spinnery 1 1.65 -> 1.36: -6/turn
  - retting pit 1 0.91 -> 0.77: +3/turn
  - flax farm 1 4.64 -> 3.85: -0/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.26: -20/turn
  - ropewalk 1 0.25 -> 0.00: +23/turn
  - mansion 1 0.00 -> 0.37: -78/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real -3/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 29.92, beer 3.02, timber 3.27, prestige 59.80, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 30 (v2 18); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.26, worth +11/turn.
- Ship linen snake: Grandgues -> Etallaen (+4/turn over staying).
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

Buffers: flax fibres 27/77, thread 631/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.8 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
