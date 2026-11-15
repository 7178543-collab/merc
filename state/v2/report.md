# v2 shadow report

Turn 14037, 2026-11-15 06:41. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,608, prestige 3,597 (477 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 21 | 0 | 12 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 2 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 32, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 501 | 0 | 63 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (11.7/turn) but there is NO buy order, stock 21.4 -> v2: add buy 24
- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.92 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.92 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.90 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 63 labour expired last turn (~104 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.90 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 502, not 602
- labour expiry guard: 63 bought labour expired last turn, buy 2 (not 2) this turn

## Prestige spending, cheapest coin per prestige first

364 turns left: prestige gained now converts 83.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| jousting 3 | arena | 230 | 54.4 | 54.7 | needs a arena (build cost 25,912); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 56.2 | 56.2 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 56.2 | 56.2 | thin at home: pasties, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 56.3 | 56.3 |  |
| hold banquet 4 (pies) | mansion | 18 | 57.4 | 57.4 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 59.1 | 59.1 | thin at home: pasties, hop beer, cheese |
| hold banquet 4 (premium) | mansion | 20 | 59.8 | 59.8 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 59.6 | 60.0 | needs a arena (build cost 25,912); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 60.3 | 60.3 | thin at home: cured meat, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 | thin at home: hop beer, cheese |
| hold banquet 4 | mansion | 17.5 | 60.6 | 60.6 | thin at home: hop beer, stockfish, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 3 @ 23.6, pasties buy 12 @ 15.4; crew 0.1; est +37 a turn; stock: pasties 12 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.4 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- best towns now: Chatgnan +473, Gotthafen +417, Bordees +343, Disscester +331, Gottweiler +295
- Chatgnan would trade: furniture buy 39 @ 13.6, pasties buy 7 @ 16.4; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (98/turn) | timber 26 (7.88->12.35), bread 159 (2.42->2.87), firewood 31 (3.07->5.32), charcoal 19 (2.5->4.08) | cloth 6 (8.87->12.8), cured meat 3 (24.36->25.4), thread 9 (5.35->5.7), salt 2 (5.41->5.56) | +246 |
| Hofkirchen | 991 | 0.34 | 0.40 (44/turn) | furniture 10 (17.32->21.66), varnish 5 (17.12->20.33), flour 5 (16.17->19.57) | cloth 24 (7.35->12.8), flax fibres 23 (5.78->6.75), thread 19 (5->5.7), cured meat 3 (23.73->25.4) | +189 |
| Magdeach | 667 | 0.19 | 0.20 (22/turn) | premium ham 1 (287.7->336.3), flour 5 (16.17->22.99), grindstones 1 (226.8->243.2), arms 2 (30.03->31.73) | cloth 15 (7.93->12.8), tackles 1 (169.05->178.6), salt 5 (4.22->5.56), thread 11 (5.19->5.7) | +183 |
| Amsdermund | 1111 | 0.41 | 0.30 (33/turn) | flour 5 (16.17->24.13), candles 3 (78.75->79.8), honey 6 (8.35->8.88), nets 6 (37->38) | cloth 24 (7.56->12.8), dyed cloth 2 (10.71->12.25), flax fibres 16 (5.78->6.75), chisels 2 (8.4->9.45) | +149 |
| Hanstein | 380 | 0.11 | 0.40 (44/turn) | timber 10 (7.88->11.4), charcoal 15 (2.5->4.1), flour 4 (16.17->19), wine 15 (6.25->6.79) | cloth 23 (8.82->12.8), rope 1 (72.98->78.38), seeds 15 (2.1->2.58) | +145 |

**Best:** Grandgues at about +246 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 24 @ 3.46, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 21 = 1.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.2) |
| grain | 8 @ 3.7, stop 31 |  | goal planner: buys 8 a turn for today's rates, keeps up to 31 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 2) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.9k (cash + stock at home prices); +35/turn over 6 turns, -145/turn over 24 turns.
- Limits: cash flow >= -275/turn, prestige >= -0.74/turn (values are after 200 tax a turn).
- Today's settings: value -164/turn, cash -170/turn, prestige +1.61/turn.
- Plan: value -1/turn, cash +4/turn, prestige -0.74/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -26 vs -184, -110 vs -189, -151 vs -174.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Kirchwerp: +13/turn
  - ship Flax Wyrm -> Chatgnan: +1/turn
  - mansion 1 1.00 -> 0.44: +140/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.48: +4/turn
  - ropewalk 1 0.25 -> 0.00: -4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.20: +11/turn
  - weavery 1 0.50 -> 0.60: -6/turn
  - sewing shop 1 0.30 -> 0.36: +8/turn
- Model check over the last 59 turns: predicted -103/turn for the settings we ran, real -76/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.66, flax fibres 4.95, garments 19.28, nets 30.09, beer 3.06, timber 3.38, prestige 60.10, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 64 (v2 2); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.20, worth +8/turn.
- Ship linen snake: Grandgues -> Kirchwerp (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 424 (+136 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.44 |
| ret | 3 | 0.91 | 0.89 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 100/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 21.4 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 39 @ 3.36 (ask 3.3, cap 14.4))
- R1: firewood slot dry: 2.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.92; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
