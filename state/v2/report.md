# v2 shadow report

Turn 14030, 2026-11-14 23:01. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,016, prestige 3,600 (480 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 92 | 39 | 12 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 501 | 0 | 63 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.42 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.42 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 63 labour expired last turn (~112 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +0 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 502, not 602
- labour expiry guard: 63 bought labour expired last turn, buy 2 (not 2) this turn

## Prestige spending, cheapest coin per prestige first

371 turns left: prestige gained now converts 84.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.4 | 53.4 | running |
| jousting 3 | arena | 230 | 55.5 | 55.9 | needs a arena (build cost 26,672); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 57.0 | 57.0 | thin at home: cheese, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 57.3 | 57.3 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.5 | 58.5 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 59.9 | 59.9 | thin at home: hop beer, cheese, pies |
| hold banquet 4 (pies) | mansion | 18 | 59.9 | 59.9 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 60.8 | 61.2 | needs a arena (build cost 26,672); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 61.9 | 61.9 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 62.0 | 62.0 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 62.3 | 62.3 | thin at home: hop beer, cheese |
| hold mass 2 (premium) | cathedral | 360 | 59.7 | 62.7 | needs a cathedral (build cost 273,980); thin at home: jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 3 @ 23.0, pasties buy 5 @ 15.3; crew 0.1; est +17 a turn; stock: pasties 5 @ 15.3 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 13.9 (keep 14); best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Chatgnan +474, Gotthafen +453, Disscester +336, Chribruck +275, Boistot +269
- Chatgnan would trade: furniture buy 38 @ 13.1, pasties buy 5 @ 16.3; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (100/turn) | timber 41 (7.98->12.06), firewood 29 (2.62->6.17), bread 157 (2.48->2.85), lathes 1 (182.7->205.2) | tools 23 (6.14->7.17), cloth 6 (8.45->10.2), cured meat 3 (23.73->26.4), garments 2 (22.89->23.4) | +343 |
| Kirchwerp | 1072 | 0.40 | 0.70 (77/turn) | thread 92 (4.66->5.56), steel ingots 4 (17.12->25.46), lathes 1 (182.7->207.1), nets 4 (34.6->37.62) | cloth 24 (7.56->10.2), tools 38 (5.83->7.17), dyed cloth 7 (10.92->13.3), garments 2 (22.05->23.4) | +222 |
| Angefont | 686 | 0.20 | 0.40 (44/turn) | lathes 1 (182.7->252.7), charcoal 19 (2.73->4.58), nets 6 (34.6->35.53), resin 5 (2.58->3.5) | tools 38 (5.15->7.17), flax fibres 23 (5.41->6.8), cloth 23 (9.03->10.2), dyed cloth 7 (12.6->13.3) | +196 |
| Amsdermund | 1111 | 0.42 | 0.40 (44/turn) | wine 11 (6.83->9.5), nets 6 (34.6->38.19), pasties 6 (14.6->18.05) | tools 38 (4.83->7.17), cloth 24 (7.35->10.2), garments 2 (22.05->23.4), casks 8 (5.35->6.32) | +189 |
| Vauxvais | 204 | 0.06 | 0.40 (44/turn) | charcoal 19 (2.73->4.71), bread 157 (2.48->2.75), lathes 1 (182.7->195.7), wax 4 (24.36->27.17) | tools 32 (5.41->7.17), candles 4 (73.5->82.17), cloth 9 (9.45->10.2), flax fibres 8 (6.04->6.8) | +172 |

**Best:** Grandgues at about +343 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 12 @ 3.46, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 92 = 7.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 88, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.2) |
| grain | 8 @ 3.7, stop 30 |  | goal planner: buys 8 a turn for today's rates, keeps up to 30 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 2) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| pasties |  | 1 @ min 12.3 | goal planner: sells 1 a turn at 12.3, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.1k (cash + stock at home prices); -25/turn over 6 turns, -194/turn over 24 turns.
- Limits: cash flow >= -292/turn, prestige >= -0.75/turn (values are after 200 tax a turn).
- Today's settings: value -183/turn, cash -160/turn, prestige +1.60/turn.
- Plan: value -26/turn, cash -5/turn, prestige -0.75/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +108 vs -167, -213 vs -177, -50 vs -169.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +14/turn
  - ship Flax Wyrm -> Neuborn: +5/turn
  - mansion 1 1.00 -> 0.44: +142/turn
  - spinnery 1 1.65 -> 1.38: +6/turn
  - flax farm 1 4.64 -> 4.35: +0/turn
  - net maker 0.00 -> 0.29: -0/turn
  - ropewalk 1 0.25 -> 0.00: -14/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.36: +16/turn
  - weavery 1 0.50 -> 0.34: -17/turn
  - sewing shop 1 0.30 -> 0.20: +21/turn
- Model check over the last 59 turns: predicted -71/turn for the settings we ran, real -65/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.60, beer 3.04, timber 3.42, prestige 59.16, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 64 (v2 2); light armour buy 1 (v2 None); pasties sell 1 (v2 none); rope sell 2 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.36, worth +13/turn.
- Ship linen snake: Grandgues -> Vauxvais (+16/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Neuborn (+2/turn over staying).
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

Buffers: flax fibres 87/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.42; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
