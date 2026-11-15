# v2 shadow report

Turn 14038, 2026-11-15 07:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,433, prestige 3,596 (476 free, -0.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 10 | 0 | 12 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 2 | 2 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 31, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 501 | 0 | 63 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (15.0/turn) but there is NO buy order, stock 9.7 -> v2: add buy 30
- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), 2 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: only 0.0 turns of firewood left and buying 2 (need 7) -> v2: buy 7
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 63 labour expired last turn (~104 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 501, not 597

## Prestige spending, cheapest coin per prestige first

363 turns left: prestige gained now converts 83.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| jousting 3 | arena | 230 | 54.5 | 54.8 | needs a arena (build cost 26,608); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.2 | 56.2 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 57.1 | 57.1 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 57.2 | 57.2 | thin at home: pasties, wine, cheese |
| hold banquet 4 (pies) | mansion | 18 | 58.4 | 58.4 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 59.3 | 59.3 | thin at home: pasties, hop beer |
| jousting 2 | arena | 210 | 59.7 | 60.1 | needs a arena (build cost 26,608); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 | thin at home: hop beer, cheese |
| hold banquet 4 (premium) | mansion | 20 | 60.6 | 60.6 | thin at home: hop beer, wine, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 61.4 | 61.4 | thin at home: wine, cured meat, cheese |
| hold mass 2 (premium) | cathedral | 360 | 58.4 | 61.5 | needs a cathedral (build cost 273,650); thin at home: jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: cured meat buy 2 @ 23.4, furniture buy 21 @ 14.6, pasties buy 2 @ 15.4; crew 0.2; est +244 a turn; stock: furniture 21 @ 14.6 (keep 145); stock: pasties 2 @ 15.4 (keep 14)
- **linen snake** on Grandgues: cured meat buy 3 @ 24.4, pasties buy 13 @ 15.4; crew 0.1; est +48 a turn; stock: pasties 13 @ 15.4 (keep 14)
- best towns now: Gotthafen +412, Vauxvais +410, Bordees +340, Disscester +333, Gottweiler +297
- Gotthafen would trade: cured meat buy 2 @ 25.6, furniture buy 39 @ 14.6, pasties buy 2 @ 13.0; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (99/turn) | timber 26 (7.88->12.44), bread 159 (2.37->2.87), firewood 32 (3.07->5.32), charcoal 19 (2.5->4.08) | cloth 6 (8.82->11.49), candles 1 (85.58->89.5), thread 10 (5.51->5.75), tiles 3 (3.89->4.43) | +250 |
| Birkeningen | 1006 | 0.36 | 0.20 (22/turn) | garments 10 (22.8->32.3), nets 6 (37->39.9), arms 4 (31.29->34.2), wine 7 (6.41->7.74) | spinning wheels 1 (203.7->229.9), cloth 6 (8.77->11.49), candles 1 (88.2->89.5), cookware 6 (23.73->24.13) | +157 |
| Hofkirchen | 991 | 0.35 | 0.50 (55/turn) | furniture 33 (17.22->20.33), varnish 4 (17.12->20.33) | cloth 8 (7.35->11.49), ploughs 3 (73.5->83.12), thread 19 (4.85->5.75), flax fibres 23 (5.78->6.75) | +138 |
| Darmwald | 1022 | 0.37 | 0.60 (66/turn) | charcoal 19 (2.5->9.5), lead ore 4 (8.82->11.4), medicine 1 (135.45->137.75), hides 1 (11.97->13.3) | cloth 8 (7.35->11.49), candles 1 (85.58->89.5), garments 2 (21.63->23.2) | +120 |
| Hanstein | 380 | 0.11 | 0.30 (33/turn) | timber 10 (7.88->10.54), charcoal 15 (2.5->4.01), tin ingots 1 (37.17->39.9), wine 11 (6.41->6.7) | windows 1 (635.25->674.5), cloth 8 (8.93->11.49), thread 14 (4.37->5.75), rope 1 (76.12->80.75) | +109 |

**Best:** Grandgues at about +250 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 30 @ 3.46, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 10 = 0.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 3 @ 2.4, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.2) |
| grain | 8 @ 3.7, stop 30 |  | goal planner: buys 8 a turn for today's rates, keeps up to 30 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 1) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.8k (cash + stock at home prices); -31/turn over 6 turns, -150/turn over 24 turns.
- Limits: cash flow >= -268/turn, prestige >= -0.73/turn (values are after 200 tax a turn).
- Today's settings: value -187/turn, cash -193/turn, prestige +1.69/turn.
- Plan: value -18/turn, cash -13/turn, prestige -0.73/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -110 vs -189, -151 vs -174, -175 vs -170.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Nürnnieder: +6/turn
  - ship Flax Wyrm -> Hofkirchen: +5/turn
  - mansion 1 1.00 -> 0.42: +146/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.48: +3/turn
  - ropewalk 1 0.25 -> 0.00: -4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.20: +12/turn
  - weavery 1 0.50 -> 0.60: -5/turn
  - sewing shop 1 0.30 -> 0.36: +6/turn
- Model check over the last 59 turns: predicted -108/turn for the settings we ran, real -69/turn.
- Worth of one more unit per turn: labour 1.65, thread 4.15, cloth 6.62, flax fibres 4.92, garments 19.16, nets 30.07, beer 3.01, timber 3.96, prestige 61.05, cash 0.00
- Orders it would set: arms buy 1 (v2 None); cloth sell 1 (v2 none); firewood buy 3 (v2 7); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 64 (v2 1); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.20, worth +8/turn.
- Ship linen snake: Grandgues -> Nürnnieder (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Hofkirchen (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3941 coin: +4/turn, payback 1006 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 424 (+135 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.42 |
| ret | 3 | 0.91 | 0.88 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 101/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 9.7 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 39 @ 3.36 (ask 3.3, cap 14.4))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 3 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
