# v2 shadow report

Turn 13966, 2026-11-12 07:14. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,354, prestige 3,558 (438 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 3 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 36 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 2.6 -> v2: add buy 9
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~30 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

435 turns left: prestige gained now converts 88.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.0 | 54.0 | thin at home: pasties, wine, ham, stockfish |
| jousting 3 | arena | 230 | 54.8 | 55.1 | needs a arena (build cost 26,904); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.2 | 57.2 |  |
| hold banquet 4 | mansion | 17.5 | 57.2 | 57.2 | thin at home: wine, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 58.3 | 58.3 | thin at home: pasties |
| hold banquet 4 (premium) | mansion | 20 | 59.4 | 59.4 | thin at home: wine, ham, stockfish, premium cheese |
| jousting 2 | arena | 210 | 60.0 | 60.3 | needs a arena (build cost 26,904); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 60.6 | 60.6 | thin at home: pasties, wine |
| hold banquet 3 (fish) | mansion | 7.6 | 62.4 | 62.4 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 63.1 | 63.1 | thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 66.0 | 66.0 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.4 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.1 (keep 14); best orders clear only 8 a turn after crew: ship stays at 0
- best towns now: Orlesailles +31, Clarfranche +19
- Orlesailles would trade: pasties buy 5 @ 10.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Amsdermund | 1111 | 0.41 | 0.30 (32/turn) | cured fish 6 (24.57->32.87), rope 1 (60.35->74.58), nets 5 (36.2->38), wine 5 (7.35->8.79) | cloth 9 (7.56->9.59), bellows 1 (268.8->285), coats 2 (74.55->79.33), tools 16 (5.15->6.03) | +130 |
| Darmwald | 1022 | 0.35 | 0.60 (64/turn) | beer 60 (3.78->5.56), rope 1 (60.35->77.42), ham 1 (67.73->79.33), cheese 11 (9.66->10.92) | cured meat 3 (22.05->23.56), axes 1 (16.91->18.24), cloth 9 (9.13->9.59), resin 1 (3.23->4.14) | +125 |
| Hanstein | 380 | 0.11 | 0.30 (32/turn) | ham 1 (67.73->86.92), rope 1 (60.35->77.42), wax 6 (24.57->25.65), timber 12 (8.45->10.26) | thread 28 (4.68->5.6), bellows 1 (262.5->285), cloth 9 (8.4->9.59), seeds 22 (1.84->2.51) | +122 |
| Pontmont | 341 | 0.10 | 0.30 (32/turn) | limestone 5 (18.79->38), rope 1 (60.35->76), pies 3 (17.54->20.71), clay 2 (5.15->11.97) | garments 2 (23.1->24.2), wine 12 (6.2->6.32) | +115 |
| Angefont | 686 | 0.20 | 0.30 (32/turn) | rope 1 (60.35->83.12), ham 1 (67.73->81.7), pies 4 (17.54->18.81), salt 4 (5.72->5.98) | thread 62 (4.94->5.6), flax fibres 28 (5.46->6.5), cloth 9 (8.09->9.59) | +95 |

**Best:** Amsdermund at about +130 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 37.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 9 @ 3.78, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 3 = 0.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.85 | goal planner: sells 2 a turn at 5.85, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.4) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 35.2) |
| pasties |  | 1 @ min 13.5 | goal planner: trial sale of an idle pile, 1 a turn at 13.5, keeps 0 (9 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 72.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.4 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.3k (cash + stock at home prices); +111/turn over 6 turns, -37/turn over 24 turns.
- Limits: cash flow >= -265/turn, prestige >= -0.57/turn (values are after 200 tax a turn).
- Today's settings: value +35/turn, cash +86/turn, prestige -2.40/turn - breaks the prestige floor.
- Plan: value -23/turn, cash +74/turn, prestige -0.57/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +7 vs +83, +404 vs +105, +141 vs +79.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanbrücken: +3/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: +13/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.06: +10/turn
  - flax farm 1 4.64 -> 4.10: -2/turn
  - retting pit 1 0.91 -> 0.82: -0/turn
  - weavery 1 0.50 -> 0.59: -6/turn
  - sewing shop 1 0.30 -> 0.36: +8/turn
  - spinnery 1 1.65 -> 1.33: +7/turn
- Model check over the last 61 turns: predicted +107/turn for the settings we ran, real +13/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.65, thread 4.14, cloth 6.62, flax fibres 4.91, garments 19.15, nets 29.94, beer 3.01, timber 3.38, prestige 63.94, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.06, worth +2/turn.
- Ship linen snake: Grandgues -> Hanbrücken (+3/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +1/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1825 coin: +1/turn, payback 1494 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 405 (+115 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.55 |
| ret | 3 | 0.91 | 0.71 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 161/77, thread 1050/227, cloth 72/127

## Self-diagnosis

- R1: beer slot dry: 2.6 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.6 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.66 (ask 3.6, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
