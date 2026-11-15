# v2 shadow report

Turn 14034, 2026-11-15 03:23. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,895, prestige 3,598 (478 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 56 | 0 | 12 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 32, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 501 | 0 | 63 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), but the home ask 30.20 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.42 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.42 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 63 labour expired last turn (~108 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 30.20 is above our ceiling 29.00 and last turn bought 3 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 502, not 602
- labour expiry guard: 63 bought labour expired last turn, buy 2 (not 2) this turn

## Prestige spending, cheapest coin per prestige first

367 turns left: prestige gained now converts 84.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 56.6 | 56.6 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 56.6 | 56.6 | thin at home: pasties, cheese |
| jousting 3 | arena | 230 | 56.2 | 56.6 | needs a arena (build cost 26,422); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.7 | 56.7 |  |
| hold banquet 4 (pies) | mansion | 18 | 58.9 | 58.9 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 60.0 | 60.0 | thin at home: pasties, hop beer, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 61.1 | 61.1 | thin at home: hop beer, cheese |
| hold banquet 4 (premium) | mansion | 20 | 61.1 | 61.1 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 61.6 | 62.0 | needs a arena (build cost 26,422); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 62.2 | 62.2 | thin at home: hop beer, stockfish, cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 63.0 | 63.0 | thin at home: cured meat, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 3 @ 24.4, pasties buy 9 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 9 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.4 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Chatgnan +462, Gotthafen +437, Disscester +337, Dortgart +308, Fulkirch +269
- Chatgnan would trade: cured meat buy 3 @ 27.2, furniture buy 36 @ 12.9; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (89/turn) | timber 25 (8.03->12.35), firewood 29 (2.54->5.7), charcoal 19 (2.48->4.1), bread 158 (2.46->2.68) | cloth 6 (8.35->11), cured meat 3 (25.2->30.2), leather 1 (29.4->30.21), tiles 3 (3.89->4.5) | +244 |
| Amsdermund | 1111 | 0.42 | 0.30 (33/turn) | wine 20 (6.09->9.5), nets 6 (37->38.38), acid 1 (115.5->117.8), grain 2 (2.82->4.84) | cloth 24 (7.56->11), spinning wheels 2 (220.5->228), cured meat 3 (26.25->30.2), leather 1 (26.46->30.21) | +167 |
| Darmwald | 1022 | 0.37 | 0.60 (66/turn) | charcoal 19 (2.48->9.4), hides 1 (12.29->13.21), nets 4 (37->37.81), pies 2 (20.06->21.28) | cloth 24 (7.72->11), cured meat 3 (24.57->30.2), flax fibres 7 (5.51->6.8), tar 2 (10.45->11.4) | +165 |
| Hanstein | 380 | 0.11 | 0.40 (44/turn) | timber 10 (8.03->11.11), charcoal 19 (2.48->3.93), wine 20 (6.09->6.46), yarn 6 (4.75->5.08) | thread 29 (3.57->5.55), cloth 22 (8.82->11), cured meat 3 (24.57->30.2), seeds 17 (1.86->2.58) | +158 |
| Bremcop | 1326 | 0.55 | 0.60 (66/turn) | garments 10 (23.4->29.26), beer 48 (3.46->5.65), pies 2 (20.06->32.3), wine 6 (6.09->6.7) | cured meat 3 (26.04->30.2), rope 1 (74.03->80.75), cloth 5 (9.5->11), candles 1 (82.42->84.5) | +149 |

**Best:** Grandgues at about +244 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 12 @ 3.46, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 56 = 4.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 9 @ 3.7, stop 33 |  | goal planner: buys 9 a turn for today's rates, keeps up to 33 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 2) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.2k (cash + stock at home prices); -57/turn over 6 turns, -161/turn over 24 turns.
- Limits: cash flow >= -287/turn, prestige >= -0.74/turn (values are after 200 tax a turn).
- Today's settings: value -185/turn, cash -184/turn, prestige +1.61/turn.
- Plan: value -19/turn, cash -10/turn, prestige -0.74/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -29 vs -158, -28 vs -171, -68 vs -180.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +9/turn
  - ship Flax Wyrm -> Hofkirchen: +14/turn
  - mansion 1 1.00 -> 0.44: +146/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.28: -3/turn
  - retting pit 1 0.91 -> 0.81: +2/turn
  - flax farm 1 4.64 -> 4.07: +5/turn
  - ropewalk 1 0.25 -> 0.00: -4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.24: +9/turn
  - sewing shop 1 0.30 -> 0.25: -6/turn
- Model check over the last 59 turns: predicted -90/turn for the settings we ran, real -78/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.08, beer 3.00, timber 3.44, prestige 61.13, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 2); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.24, worth +10/turn.
- Ship linen snake: Grandgues -> Vauxvais (+12/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Hofkirchen (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 425 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.52 |
| ret | 3 | 0.91 | 0.90 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 94/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.42; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
