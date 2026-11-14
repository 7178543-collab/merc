# v2 shadow report

Turn 14016, 2026-11-14 09:12. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,969, prestige 3,521 (401 free, +0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 22 | 14 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 507 | 0 | 57 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 32.8), 4 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.7 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.44 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.44 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 11.00 x17, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 57 labour expired last turn (~103 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 99 over real use lately; planning 520, not 619
- labour expiry guard: 57 bought labour expired last turn, buy 7 (not 20) this turn

## Prestige spending, cheapest coin per prestige first

385 turns left: prestige gained now converts 85.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 54.3 | 54.3 | running |
| jousting 3 | arena | 230 | 55.9 | 56.2 | needs a arena (build cost 27,232); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.7 | 58.7 | thin at home: candles |
| hold banquet 2 (fish) | mansion | 6.8 | 60.7 | 60.7 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 60.9 | 60.9 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 61.5 | 61.5 | thin at home: hop beer, ham, stockfish, candles |
| jousting 2 | arena | 210 | 61.2 | 61.6 | needs a arena (build cost 27,232); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 63.2 | 63.2 |  |
| hold banquet 4 (premium) | mansion | 20 | 63.7 | 63.7 | thin at home: hop beer, ham, stockfish, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 64.7 | 64.7 | running |
| hold mass 2 (premium) | cathedral | 360 | 61.5 | 64.7 | needs a cathedral (build cost 303,135); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 65.0 | 65.0 | thin at home: hop beer, ham, stockfish, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.104 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: cured meat buy 4 @ 24.0, furniture buy 2 @ 14.6, pasties buy 7 @ 15.0; crew 0.1; est +46 a turn; stock: furniture 2 @ 14.6 (keep 145); stock: pasties 7 @ 15.0 (keep 14)
- **linen snake** on Grandgues: cured meat buy 4 @ 23.6, pasties buy 7 @ 15.4; crew 0.1; est +22 a turn; stock: pasties 7 @ 15.4 (keep 14)
- best towns now: Unterhufe +58, Hofkirchen +50, Bedenis +49, Caillechâtel +46, Disscester +44
- Unterhufe would trade: cured meat buy 4 @ 24.0, furniture buy 2 @ 14.3, pasties buy 7 @ 13.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Blanans | 297 | 0.09 | 0.60 (68/turn) | timber 41 (8.09->12.44), cheese 11 (7.67->8.74), limestone 2 (17.43->24.89), tools 15 (5.93->6.37) | cloth 17 (7.56->9.55), dyed cloth 11 (10.71->11.69), tackles 3 (164.85->167.2), garments 2 (22.89->23.6) | +200 |
| Grandgues | 152 | 0.05 | 0.90 (102/turn) | timber 41 (8.09->11.59), firewood 30 (3.61->6.27), thread 11 (5.1->6.03), bread 155 (2.56->2.72) | cloth 8 (8.93->9.55), cured meat 4 (24.36->25.8), garments 2 (22.47->23.6), flax fibres 4 (6.46->6.7) | +178 |
| Disscester | 1474 | 0.65 | 0.60 (68/turn) | - | looms 1 (588->693.5), furniture 17 (12.5->16.81), butter 2 (77.7->86.45), cloth 7 (8.56->9.55) | +135 |
| Hofkirchen | 991 | 0.36 | 0.70 (79/turn) | malt 2 (6.2->7.98) | cloth 24 (7.35->9.55), looms 1 (651->693.5), cheese 14 (5.25->6.41), furniture 17 (14.91->16.81) | +126 |
| Bordetes | 831 | 0.26 | 0.50 (57/turn) | cured fish 6 (28.14->33.63), charcoal 20 (2.62->5.42), honey 7 (8.56->9.12), malt 3 (6.2->7.08) | cloth 23 (7.56->9.55), butter 1 (66.67->86.45), dyed cloth 11 (10.71->11.69), garments 2 (22.89->23.6) | +116 |

**Best:** Blanans at about +200 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 15 @ 3.88, stop 57 |  | uses 14.2/turn (household upkeep), makes 0.0, holds 108 = 7.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 | off | a building is stalled on cured meat: no sell until it runs again |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 7) |
| light armour | 1 @ 94.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.0) |
| pasties |  | 1 @ min 12.5 | goal planner: sells 1 a turn at 12.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.8k (cash + stock at home prices); -28/turn over 6 turns, -70/turn over 24 turns.
- Limits: cash flow >= -332/turn, prestige >= -0.42/turn (values are after 200 tax a turn).
- Today's settings: value -179/turn, cash -159/turn, prestige +2.00/turn.
- Plan: value -13/turn, cash -4/turn, prestige -0.42/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -352 vs -158, +15 vs -142, -176 vs -143.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Heilegg: +5/turn
  - mansion 1 1.00 -> 0.42: +150/turn
  - spinnery 1 1.65 -> 1.37: +4/turn
  - retting pit 1 0.91 -> 0.85: +1/turn
  - flax farm 1 4.64 -> 4.24: +5/turn
  - net maker 0.00 -> 0.29: +1/turn
  - brewery 1 0.14 -> 0.00: -3/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.14: +4/turn
  - weavery 1 0.50 -> 0.41: -9/turn
  - sewing shop 1 0.30 -> 0.24: +12/turn
- Model check over the last 59 turns: predicted -4/turn for the settings we ran, real +38/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.20, cloth 6.68, flax fibres 5.05, garments 19.30, nets 30.39, beer 3.18, timber 3.46, prestige 60.59, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); labour buy 64 (v2 7); light armour buy 1 (v2 None); pasties sell 1 (v2 none); rope sell 2 (v2 none)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.14, worth +5/turn.
- Ship linen snake: Grandgues -> Heilegg (+5/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +4/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 421 (+132 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.25 |
| ret | 3 | 0.91 | 0.85 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 114/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.44; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
