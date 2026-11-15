# v2 shadow report

Turn 14035, 2026-11-15 04:29. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,869, prestige 3,598 (478 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 45 | 0 | 12 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 33, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 501 | 0 | 63 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.04 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.04 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 63 labour expired last turn (~106 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 56.5 coin per prestige at mansion, vs 67.0 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 502, not 602
- labour expiry guard: 63 bought labour expired last turn, buy 2 (not 2) this turn

## Prestige spending, cheapest coin per prestige first

366 turns left: prestige gained now converts 84.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| jousting 3 | arena | 230 | 55.2 | 55.5 | needs a arena (build cost 26,232); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.5 | 56.5 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 56.5 | 56.5 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 56.7 | 56.7 | thin at home: pasties, cheese |
| hold banquet 4 (pies) | mansion | 18 | 58.4 | 58.4 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 59.7 | 59.7 | thin at home: pasties, hop beer |
| hold banquet 3 (fish) | mansion | 7.6 | 60.6 | 60.6 | thin at home: hop beer, cheese |
| hold banquet 4 (premium) | mansion | 20 | 60.8 | 60.8 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 60.4 | 60.8 | needs a arena (build cost 26,232); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 61.7 | 61.7 | thin at home: hop beer, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 59.8 | 62.9 | needs a cathedral (build cost 274,910); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 3 @ 24.6, pasties buy 10 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 10 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.4 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Gotthafen +429, Bedenis +412, Disscester +331, Bordees +322, Nürnnieder +266
- Gotthafen would trade: cured meat buy 2 @ 24.4, furniture buy 39 @ 14.6, pasties buy 6 @ 15.0; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.22 | 0.50 (54/turn) | beer 75 (3.46->4.46), garments 10 (23.6->25.27), grain 2 (2.26->3.23), limestone 1 (18.59->28.5) | tapestries 1 (593.25->788.5), tools 16 (5.25->6.65), cured meat 3 (25.41->27.36), cloth 3 (9.45->10.9) | +289 |
| Grandgues | 152 | 0.04 | 0.90 (97/turn) | timber 25 (7.98->12.44), bread 158 (2.44->2.77), firewood 30 (3.19->5.56), charcoal 19 (2.5->4.1) | tapestries 1 (761.25->788.5), cloth 6 (8.77->10.9), cured meat 3 (25.41->27.36), tools 12 (6.51->6.65) | +241 |
| Coburgbaum | 619 | 0.18 | 0.10 (11/turn) | garments 10 (23.6->26.22), wine 10 (6.09->7.17), grain 2 (2.26->2.83), seeds 9 (2.94->3.32) | tapestries 1 (651->788.5), cloth 21 (9.66->10.9), cured meat 3 (24.57->27.36), tools 16 (6.3->6.65) | +203 |
| Chatgnan | 728 | 0.21 | 0.10 (11/turn) | windows 1 (861->950), pies 1 (20.06->21.47), salt 7 (4.39->4.67) | tapestries 1 (724.5->788.5), cloth 24 (9.87->10.9), garments 2 (23.94->25.4), butter 2 (84->85.5) | +178 |
| Hanstein | 380 | 0.11 | 0.40 (43/turn) | flour 6 (17.12->20.71), charcoal 16 (2.5->4.26), timber 10 (7.98->10.83), salt 7 (4.39->5.22) | cloth 21 (8.93->10.9), tapestries 1 (756->788.5), thread 13 (3.82->5.22), seeds 23 (1.84->2.58) | +169 |

**Best:** Etallaen at about +289 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 13 @ 3.46, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 45 = 3.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 89, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 17.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.0) |
| grain | 9 @ 3.7, stop 33 |  | goal planner: buys 9 a turn for today's rates, keeps up to 33 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 2) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.2k (cash + stock at home prices); +4/turn over 6 turns, -144/turn over 24 turns.
- Limits: cash flow >= -286/turn, prestige >= -0.74/turn (values are after 200 tax a turn).
- Today's settings: value -187/turn, cash -189/turn, prestige +1.61/turn.
- Plan: value -21/turn, cash -15/turn, prestige -0.74/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -28 vs -171, -68 vs -180, -26 vs -184.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +14/turn
  - ship Flax Wyrm -> Kirchwerp: +29/turn
  - mansion 1 1.00 -> 0.44: +146/turn
  - net maker 0.00 -> 0.29: +7/turn
  - flax farm 1 4.64 -> 4.16: -2/turn
  - retting pit 1 0.91 -> 0.83: -2/turn
  - spinnery 1 1.65 -> 1.31: +5/turn
  - ropewalk 1 0.25 -> 0.00: +0/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.23: +7/turn
  - sewing shop 1 0.30 -> 0.24: -11/turn
- Model check over the last 58 turns: predicted -98/turn for the settings we ran, real -85/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.13, beer 3.00, timber 3.42, prestige 61.41, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 2); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.23, worth +8/turn.
- Ship linen snake: Grandgues -> Vauxvais (+17/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Kirchwerp (+13/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 425 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.50 |
| ret | 3 | 0.91 | 0.90 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 96/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.04; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
