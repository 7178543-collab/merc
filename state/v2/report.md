# v2 shadow report

Turn 13556, 2026-10-26 05:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 502, prestige 3,559 (439 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 7 | 0 | 6 | 0 | 0 | buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 48 | 21 | 29 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 466 | 0 | 34 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 33.6 |
| porterage | 14 | 14 | 13 | 0 | 1 | buy 14, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy

## Tuning

- **cured meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: we make 0/turn more than we use but there is no sell order -> v2: sell 0
- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187

## Notes

- labour: projection runs 112 over real use lately; planning 468, not 580

## Prestige spending, cheapest coin per prestige first

845 turns left: prestige gained now converts 98.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 46.1 | 46.1 | thin at home: hop beer, pies |
| maintain 1 | park | 0.5 | 46.8 | 46.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 48.9 | 48.9 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 49.5 | 49.5 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 49.6 | 49.6 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 52.1 | 52.1 | thin at home: hop beer, cured meat |
| hold banquet 2 (fish) | mansion | 6.8 | 52.6 | 52.6 | thin at home: wine |
| hold banquet 4 | mansion | 17.5 | 52.6 | 52.6 | thin at home: wine, hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 52.7 | 52.8 | needs a arena (build cost 23,007); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 54.4 | 54.4 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 54.6 | 54.6 |  |
| hold prayer 2 | chapel | 13 | 52.0 | 54.8 | needs a chapel (build cost 28,637) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Amsdermund | 1111 | 0.37 | 0.30 (29/turn) | grindstones 1 (241.5->256.5), malt 1 (4.6->6.89), glass ingots 2 (61.43->62.7), potash 1 (19.32->20.9) | premium ham 1 (193.2->245.1), harnesses 2 (51.03->62.22), jewellery 3 (89.25->93.57), candles 1 (67.2->71) | +101 |
| Karlmoor | 787 | 0.20 | 0.20 (19/turn) | flax fibres 7 (5.1->10.45), cloth 18 (7.56->8.88), thread 10 (4.4->5.75), tackles 1 (159.6->166.25) | premium cheese 1 (20.79->27.55), candles 1 (67.73->71) | +84 |
| Neuborn | 780 | 0.20 | 0.50 (48/turn) | charcoal 11 (1.9->4.48), bricks 5 (4.12->9.5), malt 2 (4.6->5.27), cloth 4 (7.56->7.89) | harnesses 2 (47.25->62.22), cured meat 9 (21->22.23), canvas 3 (32.76->34.01), bellows 1 (252->254.6) | +61 |
| Grandgues | 152 | 0.04 | 0.50 (48/turn) | bricks 11 (4.12->5.89), charcoal 11 (1.9->3.23), malt 4 (4.6->6.03), firewood 28 (1.66->2.96) | cured meat 7 (21.21->22.23), candles 1 (68.78->71), pasties 2 (11.55->12.6), casks 4 (4.43->4.75) | +44 |
| Hofkirchen | 991 | 0.30 | 0.10 (10/turn) | tackles 1 (159.6->167.2), iron ore 2 (5.25->7.6), hop beer 3 (6.62->7.6) | harnesses 2 (49.35->62.22), medicine 1 (122.85->128.25), bellows 1 (252->254.6), tools 2 (4.2->5.15) | +41 |

**Best:** Amsdermund at about +101 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 1 = 2.0 turns |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.38) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 0 @ 2.4, stop 13 | 1 @ min 1.73 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 7 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 4.82 | goal planner: sells 2 a turn at 4.82, keeps 82 (no one offered it) |
| grain | 29 @ 3.7, stop 115 |  | goal planner: buys 29 a turn for today's rates, keeps up to 115 (v2 had 58) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 10 @ min 33.6 | goal planner: sells 10 at 33.6 (v2 had 10 at 36.0) |
| pasties | 4 @ 14.5, stop 8 |  | uses 2.0/turn (household upkeep), makes 0.0, holds 1 = 0.5 turns |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 13) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 (v2 had 1) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 2.0 turns |
| thread |  | 21 @ min 4.26 | goal planner: sells 21 a turn at 4.26, keeps 180 (no one offered it) |
| tools | 3 @ 6.2, stop 18 |  | uses 2.2/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 90.0 turns |
| varnish | 1 @ 20.6, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 1.2 turns |
| wax | 1 @ 23.6, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 7.2 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.7k (cash + stock at home prices); -63/turn over 6 turns, -36/turn over 24 turns.
- Limits: cash flow >= +146/turn, prestige >= -0.58/turn (values are after 220 tax a turn).
- Today's settings: value +67/turn, cash -13/turn, prestige -1.89/turn - breaks the prestige floor and cash floor.
- Plan: value +38/turn, cash +47/turn, prestige -0.58/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): -200 vs +41, -193 vs +18, -101 vs +1 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +3/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.57: +5/turn
  - ropewalk 1 0.25 -> 0.00: +17/turn
  - spinnery 1 1.59 -> 1.87: +22/turn
  - net maker 0.23 -> 0.00: +11/turn
  - logging camp w/ tool 5.00 -> 4.87: +0/turn
  - mansion 1 0.15 -> 0.47: -68/turn
  - retting pit 1 1.04 -> 0.00: -106/turn
  - flax farm 1 5.88 -> 0.00: -27/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.31, thread 3.56, cloth 5.52, flax fibres 4.70, garments 15.71, nets 16.65, beer 121.48, timber 3.08, prestige 3821.04, cash 100.00
- Orders it would set: cured meat buy 1 (v2 2); flax fibres sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 29 (v2 58); light armour buy 1 (v2 None); porterage buy 14 (v2 13); rope sell 2 (v2 1); thread sell 21 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 8.20, worth +155/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.57, worth +63/turn.
- Ship linen snake: Grandgues -> Angefont (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +49/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~4133 coin: +11/turn, payback 368 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - +1 plot park 1 for ~1674 coin: +1/turn, payback 1786 turns, doesn't pay yet (materials thin at home: limestone)
- Trim: donate logging camp w/ tool: +16/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 1.2/turn (+0.0 exported); plan makes 6.6 garments a turn.
Labour: own 500, everything else 394, chain may buy 0 -> chain allowance 106, chain plan 105 (-135 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.39 |
| ret | 3 | 1.04 | 0.07 |
| spin | 4 | 1.59 | 0.73 |
| weave | 3 | 0.13 | 0.26 |
| sew | 2 | 0.09 | 0.16 |

Buffers: flax fibres 331/45, thread 1045/133, cloth 0/26
- chain plan needed 393 labour, budget left 106: cut to 106 (sewing capped at 0.16)

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1045 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
