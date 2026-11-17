# v2 shadow report

Turn 14088, 2026-11-17 09:11. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,721, prestige 3,632 (512 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 9 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 5, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.70 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.90 x9, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~80 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 496, not 596

## Prestige spending, cheapest coin per prestige first

313 turns left: prestige gained now converts 79.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.4 | 50.9 | needs a arena (build cost 29,237); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| jousting 2 | arena | 210 | 55.2 | 55.8 | needs a arena (build cost 29,237); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.5 | 58.5 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 61.9 | 61.9 | thin at home: wine, cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 62.3 | 62.3 |  |
| hold banquet 3 (pies) | mansion | 8 | 62.3 | 62.3 | thin at home: hop beer |
| hold banquet 3 (fish) | mansion | 7.6 | 62.5 | 62.5 | thin at home: hop beer, cured fish |
| hold mass 2 (premium) | cathedral | 360 | 58.8 | 63.1 | needs a cathedral (build cost 302,120); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 (premium) | mansion | 20 | 63.2 | 63.2 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 (pies) | mansion | 18 | 63.3 | 63.3 | thin at home: hop beer, wine, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 63.5 | 63.5 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.132 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 11 @ 16.2; crew 0.1; est +18 a turn; stock: pasties 11 @ 16.2 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.9 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Amsdermund +672, Hofkirchen +549, Fulkirch +296, Clairlond +267, Essenbrucke +253
- Amsdermund would trade: furniture buy 62 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (104/turn) | timber 24 (8.4->12.44), firewood 30 (2.84->6.65), bread 161 (2.52->3.06), charcoal 19 (3->4.66) | beer 4 (3.36->3.66), medicine 1 (156.45->157.7), resin 4 (3.3->3.42) | +239 |
| Amsdermund | 1111 | 0.44 | 0.30 (35/turn) | paper 4 (26.04->31.16), leather 1 (23.1->30.59), acid 1 (115.5->116.85) | cloth 24 (5.72->12.2), garments 19 (27.3->29.26), windows 1 (845.25->864.5), wrought iron 5 (13.97->16.05) | +226 |
| Pontmont | 341 | 0.10 | 1.00 (115/turn) | firewood 21 (2.84->9.5), tiles 3 (3.82->11.78), bread 67 (2.52->3.1), timber 12 (8.4->11.21) | garments 7 (25.2->29.26), cloth 8 (11.13->12.2), tools 6 (5.35->5.98), cookware 1 (21->22.42) | +199 |
| Kleinburgh | 1440 | 0.64 | 0.20 (23/turn) | leather 1 (23.1->28.5), nets 3 (35.2->37.62) | windows 1 (714->864.5), cloth 24 (10.13->12.2), cheese 3 (6.41->7.36) | +189 |
| Heilegg | 826 | 0.26 | 0.70 (81/turn) | wrought iron 14 (18.38->23.75), charcoal 19 (3->6.03), leather 1 (23.1->32.3), acid 1 (115.5->121.6) | cloth 24 (9.24->12.2), cheese 3 (6.04->7.36) | +184 |

**Best:** Grandgues at about +239 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ ?, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 9 @ 3.84, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 9 = 2.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.0) |
| grain | 0 @ 3.7, stop 18 |  | goal planner: buys 0 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 1 = 3.3 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.2k (cash + stock at home prices); -195/turn over 6 turns, +131/turn over 24 turns.
- Limits: cash flow >= -280/turn, prestige >= -0.89/turn (values are after 200 tax a turn).
- Today's settings: value +104/turn, cash +89/turn, prestige -2.78/turn - breaks the prestige floor.
- Plan: value +23/turn, cash +34/turn, prestige -0.89/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +160 vs +66, -153 vs +72, -103 vs +79 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +19/turn
  - ship Flax Wyrm -> Karlmoor: +8/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.28: +4/turn
  - spinnery 1 1.65 -> 1.60: +2/turn
  - ropewalk 1 0.25 -> 0.31: +2/turn
  - flax farm 1 4.64 -> 4.81: -2/turn
  - weavery 1 0.50 -> 0.59: -5/turn
  - sewing shop 1 0.30 -> 0.36: +8/turn
  - mansion 1 0.00 -> 0.45: -105/turn
- Model check over the last 60 turns: predicted +63/turn for the settings we ran, real -2/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.77, thread 4.49, cloth 7.14, flax fibres 5.38, garments 20.62, nets 32.49, beer 3.18, timber 3.43, prestige 61.39, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Ship linen snake: Grandgues -> Donaunieder (+19/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Karlmoor (+8/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~4371 coin: +9/turn, payback 509 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 89/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.7; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
