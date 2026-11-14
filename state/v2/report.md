# v2 shadow report

Turn 14021, 2026-11-14 14:42. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,657, prestige 3,527 (407 free, +2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 20 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 535 | 0 | 29 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: only 0.7 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~51 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 535, not 634

## Prestige spending, cheapest coin per prestige first

380 turns left: prestige gained now converts 85.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.8 | 52.8 | running |
| jousting 3 | arena | 230 | 55.0 | 55.3 | needs a arena (build cost 27,218); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.5 | 58.5 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 58.9 | 58.9 | thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 60.0 | 60.0 | thin at home: wine, cured fish |
| jousting 2 | arena | 210 | 60.2 | 60.6 | needs a arena (build cost 27,218); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 61.1 | 61.1 | thin at home: hop beer, wine, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 62.3 | 62.3 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 62.6 | 62.6 | thin at home: wine |
| hold mass 2 (premium) | cathedral | 360 | 60.6 | 63.8 | needs a cathedral (build cost 297,835); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 (premium) | mansion | 20 | 63.9 | 63.9 | thin at home: hop beer, wine, stockfish, premium ham |
| hold banquet 3 (pies) | mansion | 8 | 64.2 | 64.2 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.9 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.6 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Herschweig +26, Gotthafen +21, Gottweiler +19, Clairlond +18, Großmühle +18
- Herschweig would trade: cured meat buy 6 @ 22.6, furniture buy 1 @ 14.5, pasties buy 3 @ 14.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Blanans | 297 | 0.09 | 0.70 (77/turn) | timber 42 (8.03->12.44), cheese 11 (7.77->11.21), axes 7 (21.63->22.8), flour 1 (18.17->21.09) | dyed cloth 5 (10.71->12.82), cloth 13 (7.88->8.55), grindstones 1 (256.2->266), garments 2 (22.68->23) | +208 |
| Grandgues | 152 | 0.04 | 0.70 (77/turn) | timber 42 (8.03->11.97), firewood 29 (3.76->6.55), charcoal 20 (2.69->3.42), flour 1 (18.17->18.71) | cloth 7 (8.4->8.55), cured meat 6 (24.15->24.4), salt 4 (5.35->5.56), dyed yarn 1 (4.66->5.08) | +190 |
| Fontaux | 411 | 0.12 | 0.60 (66/turn) | thread 79 (4.7->5.65), charcoal 19 (2.69->5.27), timber 18 (8.03->10.64), garments 10 (21.2->21.66) | cured meat 4 (23.31->24.4), dyed cloth 2 (11.34->12.82), cloth 9 (8.29->8.55), dyed yarn 1 (4.58->5.08) | +131 |
| Clairlond | 1288 | 0.52 | 0.20 (22/turn) | garments 10 (21.2->29.07), nets 2 (36.6->42.75), varnish 2 (17.12->20.9), premium cheese 1 (34.23->36.86) | tools 29 (5.62->6.32), butter 1 (73.5->78.38), wool 1 (7.35->9.4), furniture 1 (12.92->15.3) | +103 |
| Rouhomme | 368 | 0.11 | 0.20 (22/turn) | windows 1 (813.75->855), tin ingots 1 (36.12->37.81), grain 2 (3->3.7), leather 1 (23.31->24.89) | tools 29 (5.02->6.32), grindstones 1 (252->266), thread 62 (4.73->4.94), dyed cloth 5 (11.87->12.82) | +100 |

**Best:** Blanans at about +208 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 108 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 81.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.6) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 35) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 35.6) |
| pasties |  | 1 @ min 12.5 | goal planner: sells 1 a turn at 12.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 83.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.2k (cash + stock at home prices); -262/turn over 6 turns, -154/turn over 24 turns.
- Limits: cash flow >= -319/turn, prestige >= -0.44/turn (values are after 200 tax a turn).
- Today's settings: value -178/turn, cash -155/turn, prestige +1.98/turn.
- Plan: value -14/turn, cash +1/turn, prestige -0.44/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +125 vs -158, -280 vs -164, -30 vs -164.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Heidlowe: +5/turn
  - ship Flax Wyrm -> Brebronn: +0/turn
  - mansion 1 1.00 -> 0.42: +148/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.36: -0/turn
  - retting pit 1 0.91 -> 0.84: +2/turn
  - flax farm 1 4.64 -> 4.20: +4/turn
  - weavery 1 0.50 -> 0.42: -6/turn
  - sewing shop 1 0.30 -> 0.24: +8/turn
- Model check over the last 59 turns: predicted -30/turn for the settings we ran, real -7/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.29, beer 3.31, timber 3.94, prestige 60.54, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 64 (v2 35); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Heidlowe (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brebronn (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 422 (+133 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.34 |
| ret | 3 | 0.91 | 0.87 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 107/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
