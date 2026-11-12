# v2 shadow report

Turn 13977, 2026-11-12 18:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,979, prestige 3,529 (409 free, -2.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 19 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.86 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 34 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 4.18 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 4.18 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.50 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~78 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.50 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 486, not 586

## Prestige spending, cheapest coin per prestige first

424 turns left: prestige gained now converts 88.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.5 | 54.5 | thin at home: hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 55.6 | 55.9 | needs a arena (build cost 27,529); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 56.7 | 56.7 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 58.5 | 58.5 | thin at home: hop beer, cured fish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 58.7 | 58.7 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 59.1 | 59.1 | thin at home: cured fish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 59.3 | 59.3 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 59.5 | 59.5 | thin at home: hop beer, cheese, pies |
| hold banquet 2 (pies) | mansion | 7 | 61.0 | 61.0 | thin at home: cheese, pies |
| jousting 2 | arena | 210 | 60.9 | 61.2 | needs a arena (build cost 27,529); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 68.1 | 68.1 | thin at home: hop beer, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 10 @ 14.1, pasties buy 4 @ 14.2; crew 0.1; est +131 a turn; stock: furniture 10 @ 14.1 (keep 145); stock: pasties 4 @ 14.2 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.7 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Caillechâtel +131, Disscester +127, Marmont +124, Vauxvais +124, Nürnnieder +121
- Caillechâtel would trade: furniture buy 10 @ 14.1, pasties buy 4 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (107/turn) | timber 41 (7.61->9.97), firewood 37 (4.39->6.65), charcoal 19 (3.74->4.5), bread 157 (2.48->2.64) | cloth 11 (6.88->9.3), cured meat 3 (23.94->26.41), raw cloth 5 (6.56->7.12), tools 15 (5.93->6.17) | +164 |
| Helmgreen | 1354 | 0.55 | 0.30 (32/turn) | dyed yarn 2 (5.15->5.84) | looms 1 (546->693.5), flax fibres 10 (5.35->7.25), jewellery 1 (111.3->115.9), cloth 13 (8.61->9.3) | +149 |
| Vauxvais | 204 | 0.06 | 0.30 (32/turn) | windows 1 (735->779), bread 157 (2.48->2.75), copper ingots 1 (16.48->16.72), grain 2 (2.88->3.21) | cloth 18 (7.56->9.3), thread 17 (4.73->5.65), flax fibres 12 (6.67->7.25), tools 15 (5.88->6.17) | +123 |
| Hanstein | 380 | 0.11 | 0.20 (21/turn) | pies 2 (23.52->34.01), hides 1 (11.97->12.73), timber 11 (7.61->9.36) | thread 32 (4.41->5.65), cloth 14 (7.82->9.3), flax fibres 12 (5.57->7.25), seeds 18 (1.8->2.51) | +112 |
| Heilegg | 826 | 0.24 | 0.30 (32/turn) | casks 13 (6.46->9.17), lead ore 6 (9.66->11.59), wine 11 (6.98->7.46), nets 6 (38->38.76) | cloth 24 (7.35->9.3), tools 15 (5.25->6.17), cured meat 3 (23.52->26.41), thread 25 (5.15->5.65) | +110 |

**Best:** Grandgues at about +164 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.6) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.3k (cash + stock at home prices); +50/turn over 6 turns, +143/turn over 24 turns.
- Limits: cash flow >= -374/turn, prestige >= -0.45/turn (values are after 200 tax a turn).
- Today's settings: value +44/turn, cash +19/turn, prestige -2.25/turn - breaks the prestige floor.
- Plan: value -42/turn, cash -36/turn, prestige -0.45/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +150 vs +2, +88 vs +15, +125 vs +22.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +8/turn
  - ship Flax Wyrm -> Vauxvais: +0/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.29: +6/turn
  - flax farm 1 4.64 -> 4.22: -0/turn
  - spinnery 1 1.65 -> 1.35: -0/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - weavery 1 0.50 -> 0.43: -14/turn
  - ropewalk 1 0.25 -> 0.00: -20/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.24: +25/turn
- Model check over the last 61 turns: predicted +104/turn for the settings we ran, real +4/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.33, beer 3.14, timber 3.26, prestige 69.63, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.24, worth +9/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1889 coin: +4/turn, payback 487 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 410 (+119 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.67 |
| ret | 3 | 0.91 | 0.73 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 154/77, thread 1064/227, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 4.18; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.5 for 4 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
