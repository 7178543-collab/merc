# v2 shadow report

Turn 14050, 2026-11-15 19:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,109, prestige 3,565 (445 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 11 | 0 | 4 | 0 | 0 | min_holding 60, sell 5, sell @ 3.26; stop 26, buy 9, buy @ 3.16 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 41 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.00 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.00 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.90 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~77 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.90 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

351 turns left: prestige gained now converts 82.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| jousting 3 | arena | 230 | 54.8 | 55.1 | needs a arena (build cost 26,570); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.5 | 55.5 |  |
| hold banquet 4 (pies) | mansion | 18 | 55.8 | 55.8 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 57.4 | 57.4 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 58.8 | 58.8 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 59.5 | 59.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.7 | 59.7 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 59.8 | 59.8 | thin at home: hop beer, cured fish |
| jousting 2 | arena | 210 | 60.0 | 60.4 | needs a arena (build cost 26,570); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.6 | 60.6 | thin at home: hop beer, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.8 | 60.8 | thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 14.2, pasties buy 5 @ 14.6; crew 0.2; est +256 a turn; stock: furniture 21 @ 14.2 (keep 145); stock: pasties 5 @ 14.6 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Amsdermund +582, Boistot +330, Bordees +322, Fulkirch +293, Friedwerp +286
- Amsdermund would trade: furniture buy 56 @ 14.3; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | timber 39 (7.88->12.63), firewood 28 (3.15->6.17), charcoal 15 (2.75->5.08), bread 132 (2.54->2.85) | candles 0 (85.58->89), dyed cloth 2 (12.18->12.82), garments 1 (23.94->25.2), cheese 8 (6.56->6.74) | +318 |
| Kirchwerp | 1072 | 0.38 | 0.40 (42/turn) | steel ingots 12 (19.32->27.17), furniture 9 (11.65->15.67), blades 3 (17.43->20.52), honey 7 (8.24->9.5) | ploughs 5 (73.5->79.8), cloth 24 (7.56->8.25), dyed cloth 3 (10.92->12.82), candles 1 (85.05->89) | +166 |
| Fontaux | 411 | 0.12 | 1.00 (106/turn) | thread 26 (4.84->7.27), timber 11 (7.88->12.16), firewood 16 (3.15->7.84), furniture 5 (11.65->13.96) | candles 0 (83.48->89), flax fibres 2 (5.35->5.8), flax plants 1 (1.07->1.47) | +151 |
| Hanbrücken | 531 | 0.15 | 0.80 (85/turn) | timber 23 (7.88->12.16), tapestries 1 (782.25->798), charcoal 16 (2.75->4.64), furniture 5 (11.65->14.15) | candles 1 (74.55->89), tackles 1 (155.4->166.25), cheese 5 (5.88->6.74), leather 1 (23.1->25.65) | +114 |
| Angefont | 686 | 0.19 | 1.00 (106/turn) | furniture 9 (11.65->15.86), beer 159 (3.15->3.72), charcoal 19 (2.75->5.65), ham 1 (92.92->96.9) | cheese 10 (5.57->6.74), tools 16 (5.15->5.61), seeds 7 (1.78->2.58), garments 2 (24.36->25.2) | +111 |

**Best:** Grandgues at about +318 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 11.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21.2 | goal planner: sells 11 at 21.2 (v2 had 10 at 24.4) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34 | goal planner: sells 9 at 34 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.6k (cash + stock at home prices); -45/turn over 6 turns, -30/turn over 24 turns.
- Limits: cash flow >= -255/turn, prestige >= -0.61/turn (values are after 200 tax a turn).
- Today's settings: value +71/turn, cash +44/turn, prestige -2.44/turn - breaks the prestige floor.
- Plan: value +23/turn, cash +46/turn, prestige -0.61/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -163 vs +99, +227 vs +102, +91 vs +52.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +7/turn
  - ship Flax Wyrm -> Pontmont: +0/turn
  - brewery 1 0.14 -> 0.01: +22/turn
  - net maker 0.00 -> 0.29: +10/turn
  - flax farm 1 4.64 -> 4.27: -1/turn
  - retting pit 1 0.91 -> 0.85: -0/turn
  - ropewalk 1 0.25 -> 0.00: -1/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.10: +18/turn
  - weavery 1 0.50 -> 0.58: -10/turn
  - spinnery 1 1.65 -> 1.35: -7/turn
- Model check over the last 59 turns: predicted -122/turn for the settings we ran, real -104/turn.
- Worth of one more unit per turn: labour 1.70, thread 4.27, cloth 6.82, flax fibres 5.06, garments 19.74, nets 30.98, beer 3.00, timber 3.38, prestige 59.59, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.10, worth +5/turn.
- Ship linen snake: Grandgues -> Brunnham (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Pontmont (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3806 coin: +6/turn, payback 637 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 9.1/turn (+0.0 exported); plan makes 32.0 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 410 (+121 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.03 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.78 |

Buffers: flax fibres 123/77, thread 1064/225, cloth 72/126

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.0; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
