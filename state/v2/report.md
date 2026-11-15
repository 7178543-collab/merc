# v2 shadow report

Turn 14033, 2026-11-15 02:18. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,963, prestige 3,599 (479 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 68 | 0 | 12 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 29, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 501 | 0 | 63 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.08 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.08 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 63 labour expired last turn (~108 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 502, not 602
- labour expiry guard: 63 bought labour expired last turn, buy 2 (not 2) this turn

## Prestige spending, cheapest coin per prestige first

368 turns left: prestige gained now converts 84.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 56.7 | 56.7 | thin at home: cured fish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 56.9 | 56.9 | thin at home: cheese |
| jousting 3 | arena | 230 | 56.8 | 57.1 | needs a arena (build cost 26,544); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 59.4 | 59.4 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 60.9 | 60.9 | thin at home: hop beer, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 61.8 | 61.8 | thin at home: hop beer, cured fish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 62.5 | 62.5 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 62.2 | 62.6 | needs a arena (build cost 26,544); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 62.7 | 62.7 | thin at home: hop beer, ham, stockfish, cheese |
| hold mass 2 (premium) | cathedral | 360 | 60.6 | 63.7 | needs a cathedral (build cost 277,210); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 3 @ 24.4, pasties buy 8 @ 15.3; crew 0.1; est +30 a turn; stock: pasties 8 @ 15.3 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.4 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Gotthafen +437, Bedenis +399, Bordees +314, Nürnnieder +250, Brebronn +242
- Gotthafen would trade: cured meat buy 3 @ 23.4, furniture buy 39 @ 14.3, pasties buy 1 @ 13.6; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Amsdermund | 1111 | 0.42 | 0.30 (33/turn) | tapestries 1 (603.75->707.75), wine 20 (6.09->9.5), pasties 6 (14.49->17.76), nets 5 (35.8->38) | tools 17 (4.83->6.84), cloth 10 (7.56->10.07), jewellery 7 (94.5->95.95), leather 2 (27.3->30.21) | +246 |
| Heidlowe | 662 | 0.20 | 0.10 (11/turn) | tapestries 1 (603.75->769.5), pies 3 (20.48->28.12), wine 7 (6.09->6.98), nets 6 (35.8->36.48) | cloth 10 (8.03->10.07), cured meat 3 (22.68->27.36), jewellery 3 (93.98->95.95), looms 1 (687.75->693.5) | +236 |
| Hofkirchen | 991 | 0.35 | 0.50 (55/turn) | tapestries 1 (603.75->646), nails 5 (8.24->9.12), nets 6 (35.8->36.86), wine 5 (6.09->6.74) | jewellery 7 (85.05->95.95), cloth 10 (7.35->10.07), spinning wheels 3 (220.5->228), coats 3 (81.9->85.97) | +188 |
| Bremcop | 1326 | 0.55 | 0.70 (77/turn) | beer 48 (3.46->5.61), tapestries 1 (603.75->655.5), garments 10 (23.2->28.31), pies 2 (20.48->32.3) | butter 1 (69.83->77.42) | +170 |
| Fontaux | 411 | 0.12 | 0.80 (88/turn) | tapestries 1 (603.75->646), charcoal 18 (2.48->5.61), wine 20 (6.09->6.89), bread 158 (2.58->3) | jewellery 6 (93.98->95.95), cured meat 3 (24.78->27.36), tools 17 (6.51->6.84), cloth 4 (9.24->10.07) | +140 |

**Best:** Amsdermund at about +246 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 12 @ 3.46, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 68 = 5.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 84, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.6) |
| grain | 8 @ 3.7, stop 32 |  | goal planner: buys 8 a turn for today's rates, keeps up to 32 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 2) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.8) |
| pasties |  | 1 @ min 12.3 | goal planner: sells 1 a turn at 12.3, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.3k (cash + stock at home prices); +10/turn over 6 turns, -152/turn over 24 turns.
- Limits: cash flow >= -290/turn, prestige >= -0.74/turn (values are after 200 tax a turn).
- Today's settings: value -184/turn, cash -180/turn, prestige +1.60/turn.
- Plan: value -20/turn, cash -9/turn, prestige -0.74/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +3 vs -160, -29 vs -158, -28 vs -171.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +6/turn
  - ship Flax Wyrm -> Hofkirchen: +14/turn
  - mansion 1 1.00 -> 0.44: +146/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.32: -1/turn
  - retting pit 1 0.91 -> 0.83: +1/turn
  - flax farm 1 4.64 -> 4.19: +4/turn
  - ropewalk 1 0.25 -> 0.00: -6/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.26: +10/turn
  - sewing shop 1 0.30 -> 0.23: -9/turn
- Model check over the last 59 turns: predicted -85/turn for the settings we ran, real -67/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.25, beer 3.04, timber 3.49, prestige 61.26, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 64 (v2 2); light armour buy 1 (v2 None); pasties sell 1 (v2 none); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.26, worth +9/turn.
- Ship linen snake: Grandgues -> Vauxvais (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Hofkirchen (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 92/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.08; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.4 for 5 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
