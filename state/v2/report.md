# v2 shadow report

Turn 14113, 2026-11-18 10:42. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,632, prestige 3,615 (495 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 521 | 0 | 8 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.96 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.96 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Tuning

- **candles**: home ask 83.50 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 521, not 621

## Prestige spending, cheapest coin per prestige first

288 turns left: prestige gained now converts 76.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 53.2 | 53.7 | needs a arena (build cost 26,326); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.7 | 53.7 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 58.8 | 58.8 | thin at home: cured fish |
| jousting 2 | arena | 210 | 58.3 | 58.8 | needs a arena (build cost 26,326); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 60.4 | 60.4 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 62.2 | 62.2 | thin at home: cured fish, cheese |
| hold mass 2 (premium) | cathedral | 360 | 57.3 | 62.2 | needs a cathedral (build cost 292,330); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 2 (meat) | mansion | 6.8 | 62.9 | 62.9 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 63.8 | 63.8 | thin at home: cheese |
| hold banquet 4 (pies) | mansion | 18 | 69.2 | 69.2 | thin at home: ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 69.2 | 69.2 | thin at home: ham, stockfish |
| jousting 1 | arena | 170 | 68.8 | 69.5 | needs a arena (build cost 26,326); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 11 | 134102075 | 0.032 | - | candles 2, pasties 2 | -189 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.116 | - | candles 1, pasties 2 | -108 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 2 @ 78.0, pasties buy 10 @ 16.2; crew 0.1; est +39 a turn; stock: candles 2 @ 78.0 (keep 12); stock: pasties 10 @ 16.2 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- best towns now: Gotthafen +443, Vauxvais +398, Cobholme +358, Fulkirch +300, Clairlond +267
- Gotthafen would trade: furniture buy 42 @ 14.6, pasties buy 4 @ 14.9; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.80 (91/turn) | timber 31 (7.88->12.44), firewood 33 (3.11->6.32), limestone 5 (16.07->24.7), charcoal 19 (3.02->5.08) | bricks 4 (7.98->10.16), hop beer 1 (10.71->14.44), cloth 4 (10.03->10.7), candles 1 (81.38->83.5) | +313 |
| Hofkirchen | 991 | 0.36 | 0.50 (57/turn) | lathes 2 (182.7->197.6), canvas 2 (41.58->44.65) | glassware 2 (58.28->84.55), thread 53 (4.75->5.75), flax fibres 28 (5.62->7.5), cloth 24 (9.19->10.7) | +202 |
| Kirchwerp | 1072 | 0.41 | 0.30 (34/turn) | wrought iron 11 (18.69->27.55), honey 7 (9.45->13.21), nails 11 (8.09->9.5), lead ore 5 (6.62->10.45) | wax 7 (26.25->28.5), garments 2 (26.25->29.4), hop beer 1 (10.71->14.44), cheese 3 (6.2->7.12) | +171 |
| Rotterburg | 1056 | 0.40 | 0.20 (23/turn) | lathes 2 (182.7->247), nets 6 (35->36.67), dyed cloth 2 (13.55->15.39), dyed yarn 1 (6.35->6.89) | cloth 24 (10.03->10.7), ham 1 (129.15->134.9), hop beer 1 (9.66->14.44), candles 1 (79.8->83.5) | +149 |
| Heilegg | 826 | 0.26 | 0.20 (23/turn) | wrought iron 11 (18.69->27.55), nets 6 (35->36.29), hides 4 (12.92->14.25), lead ore 4 (6.62->8.41) | wax 4 (25.62->28.5), ham 1 (127.05->134.9), garments 2 (26.88->29.4), hop beer 1 (9.13->14.44) | +142 |

**Best:** Grandgues at about +313 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 5 @ 4.04, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 10 = 6.3 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 10 @ min 21 | goal planner: sells 10 at 21 (v2 had 10 at 25.8) |
| grain | 0 @ 3.7, stop 19 |  | goal planner: buys 0 a turn for today's rates, keeps up to 19 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 21) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 70.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.4k (cash + stock at home prices); -165/turn over 6 turns, +78/turn over 24 turns.
- Limits: cash flow >= -360/turn, prestige >= -0.81/turn (values are after 200 tax a turn).
- Today's settings: value +75/turn, cash +40/turn, prestige -2.69/turn - breaks the prestige floor.
- Plan: value +11/turn, cash +20/turn, prestige -0.81/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -451 vs +86, +224 vs +66, +32 vs +51 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.28: +4/turn
  - spinnery 1 1.65 -> 1.47: +3/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - flax farm 1 4.64 -> 4.23: +3/turn
  - ropewalk 1 0.25 -> 0.33: -0/turn
  - weavery 1 0.50 -> 0.44: -7/turn
  - mansion 1 0.00 -> 0.45: -100/turn
- Model check over the last 60 turns: predicted +126/turn for the settings we ran, real +38/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.79, thread 4.50, cloth 7.18, flax fibres 5.32, garments 20.78, nets 32.54, beer 3.35, timber 3.38, prestige 59.31, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); grain buy 5 (v2 0); labour buy 29 (v2 21); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Gosschweig (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.1/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.68 |
| ret | 3 | 0.91 | 0.94 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 75/77, thread 1050/225, cloth 72/126

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.96; ask over the cap 2.1 (60 coin per prestige)
