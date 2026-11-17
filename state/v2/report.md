# v2 shadow report

Turn 14081, 2026-11-17 02:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,430, prestige 3,602 (482 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 5, buy @ 3.6 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 1 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 508 | 0 | 21 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 17 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.70 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.9 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 21 labour expired last turn (~39 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

320 turns left: prestige gained now converts 79.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.3 | 49.6 | needs a arena (build cost 27,961); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 50.0 | 50.4 | needs a arena (build cost 27,961); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.0 | 53.2 | needs a arena (build cost 27,961); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.7 | 55.2 | needs a arena (build cost 27,961); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 55.2 | 55.2 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 58.8 | 58.8 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 59.2 | 59.2 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 61.7 | 61.7 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 61.8 | 61.8 | thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 62.6 | 62.6 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 62.6 | 62.6 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 63.4 | 63.4 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.9 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 16.0 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +25, Gottweiler +24, Vauxvais +20, Cobholme +19, Bremcop +19
- Hofkirchen would trade: furniture buy 1 @ 14.0, pasties buy 5 @ 14.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (104/turn) | timber 38 (8.24->12.35), firewood 31 (2.84->6.51), bread 161 (2.58->3.08), looms 1 (588->627) | bricks 5 (9.45->12.63), cookware 3 (26.67->28.31), flax fibres 8 (6.93->7.4), beer 4 (3.36->3.62) | +373 |
| Fontaux | 411 | 0.13 | 0.60 (69/turn) | thread 48 (5.05->7.27), garments 10 (26.4->34.96), charcoal 19 (2.77->4.1), timber 19 (8.24->10.36) | tools 17 (5.15->6.03), cookware 3 (26.04->28.31) | +224 |
| Kirchwerp | 1072 | 0.42 | 0.60 (69/turn) | thread 89 (5.05->5.7), lead ore 9 (6.35->10.45), steel ingots 7 (19.53->22.42), looms 1 (588->603.25) | cloth 24 (7.98->10.3), dyed cloth 8 (12.6->16.72), stockfish 1 (115.5->135.85), flax fibres 17 (5.78->7.4) | +200 |
| Birkeningen | 1006 | 0.38 | 0.90 (104/turn) | looms 1 (588->674.5), beer 53 (3.8->5.27), charcoal 17 (2.77->6.22), nets 3 (33.8->36.86) | medicine 1 (142.8->157.7), cookware 3 (24.36->28.31), cloth 19 (9.71->10.3), cheese 7 (6.04->6.6) | +174 |
| Hofkirchen | 991 | 0.36 | 0.40 (46/turn) | looms 1 (588->603.25) | jewellery 5 (84->92.62), flax fibres 27 (5.78->7.4), dyed cloth 8 (13.65->16.72), ham 3 (108.15->113.05) | +151 |

**Best:** Grandgues at about +373 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.8, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.3k (cash + stock at home prices); +203/turn over 6 turns, +45/turn over 24 turns.
- Limits: cash flow >= -268/turn, prestige >= -0.76/turn (values are after 200 tax a turn).
- Today's settings: value +81/turn, cash +69/turn, prestige -2.62/turn - breaks the prestige floor.
- Plan: value +4/turn, cash +17/turn, prestige -0.76/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +257 vs +78, +151 vs +76, +18 vs +82.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +7/turn
  - ship Flax Wyrm -> Vauxvais: +2/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.39: +9/turn
  - net maker 0.00 -> 0.26: +1/turn
  - ropewalk 1 0.25 -> 0.32: -1/turn
  - flax farm 1 4.64 -> 4.37: -1/turn
  - weavery 1 0.50 -> 0.37: -22/turn
  - sewing shop 1 0.30 -> 0.23: -3/turn
  - mansion 1 0.00 -> 0.44: -81/turn
- Model check over the last 60 turns: predicted +32/turn for the settings we ran, real -15/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.78, beer 3.38, timber 3.38, prestige 63.56, cash 0.00
- Orders it would set: bread buy 5 (v2 7); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Amsdermund (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 86/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 1.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.7; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
