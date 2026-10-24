# v2 shadow report

Turn 13526, 2026-10-24 23:29. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 697, prestige 3,573 (453 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 7 | 0 | 0 | min_holding 60, sell 82, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 8 | 0 | 6 | 2 | 0 | stop 7, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 34 | 0 | 2 | 0 | 0 | min_holding 30, sell 7, sell @ 17.8 |
| grain | 44 | 10 | 22 | 0 | 0 | stop 145, buy 10, buy @ 3.7 |
| labour | 24 | 65 | 556 | 0 | 9 | buy 24, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 13 | 13 | 12 | 0 | 1 | buy 13, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.3 turns (holds 6, next step uses 17/turn) -> v2: check the step that makes it
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 1.77 x3, yet 0 bought last turn); labour need rises ~82/turn when they restart -> v2: find out why the buy isn't filling
- **labour**: buying 24, short of ~56 needed -> v2: buy 56

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57

## Notes

- labour: projection runs 139 over real use lately; planning 556, not 694

## Prestige spending, cheapest coin per prestige first

875 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.8 | 46.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.9 | 49.9 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 50.2 | 50.2 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.8 | 51.8 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 52.4 | 52.4 | thin at home: hop beer, cured fish |
| hold prayer 2 | chapel | 13 | 49.8 | 52.7 | needs a chapel (build cost 30,850); thin at home: furniture |
| jousting 3 | arena | 230 | 52.5 | 52.7 | needs a arena (build cost 24,445); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 53.0 | 53.0 | thin at home: wine, cured fish |
| hold banquet 4 | mansion | 17.5 | 53.3 | 53.3 | thin at home: wine, hop beer, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 53.8 | 53.8 | thin at home: cured fish |
| hold sermon 2 (candles) | church | 31 | 51.7 | 54.4 | needs a church (build cost 66,414); thin at home: jewellery, candles, furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 54.5 | 54.5 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 1 @ 66.5, rope sell 4 @ 79.5; crew 0.1; est +38 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Briclives +43, Grandgues +38, Pontmont +21, Marmont +19
- Briclives would trade: candles buy 1 @ 69.0, rope sell 3 @ 85.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.31 | 0.20 (19/turn) | windows 1 (504->641.25), wrought iron 7 (14.18->17.39), glass ingots 2 (59.85->68.4), salt 16 (4.3->4.73) | beer 6 (2.29->3.5), jewellery 2 (98.17->99.75), candles 1 (71.4->74), garments 2 (18.9->19.3) | +185 |
| Heilegg | 826 | 0.22 | 0.20 (19/turn) | grindstones 1 (270.9->347.7), windows 1 (504->570), nets 8 (35.6->37.43) | candles 1 (72.98->74), silver ore 1 (34.65->36.1) | +140 |
| Rotterburg | 1056 | 0.34 | 0.10 (10/turn) | windows 1 (504->622.25), nets 4 (35.6->36.48), garments 6 (17.8->18.14), hides 1 (14.28->15.01) | candles 1 (69.83->74) | +120 |
| Brunnham | 1281 | 0.46 | 0.20 (19/turn) | windows 1 (504->603.25), nets 8 (35.6->38.57), garments 6 (17.8->18.9), steel ingots 1 (13.97->14.44) | candles 1 (67.2->74) | +117 |
| Kirchwerp | 1072 | 0.35 | 0.20 (19/turn) | windows 1 (504->589), glass ingots 2 (59.85->68.88), lead ore 1 (8.82->19.95), salt 21 (4.3->4.75) | nails 13 (5.41->5.98), garments 2 (18.9->19.3), tools 1 (4.28->4.64) | +114 |

**Best:** Hofkirchen at about +185 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 6 |  | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 2) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 7 @ min 17.8 | goal planner: sells 7 at 17.8 (v2 had 6 at 20.0) |
| grain | 31 @ 3.7, stop 98 |  | goal planner: buys 31 a turn for today's rates, keeps up to 98 (v2 had 49) |
| labour | 95 @ 2.2, stop - |  | goal planner: buys 95 for today's rates (v2 had 56) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 12 @ min 34 | goal planner: sells 12 at 34 (v2 had 12 at 34.6) |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 13 @ 1.1, stop - |  | goal planner: buys 13 for today's rates (v2 had 5) |
| rope |  | 5 @ min 67.5 | makes 2.0, uses 0.2, holds 36 (keeps 0): sells the surplus + 3/turn of the excess |
| thread |  | 10 @ min 4.1 | goal planner: sells 10 a turn at 4.1, keeps 221 (no one offered it) |
| tools | 2 @ 6.2, stop 16 |  | uses 2.0/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 101.6 turns |
| varnish | 1 @ 19.1, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 2.2 turns |
| wax | 1 @ 20.6, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 5.0 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.8k (cash + stock at home prices); -22/turn over 6 turns, +53/turn over 24 turns.
- Limits: cash flow >= +138/turn, prestige >= -0.64/turn (values are after 240 tax a turn).
- Today's settings: value -11/turn, cash -37/turn, prestige -0.62/turn - breaks the cash floor.
- Plan: value +35/turn, cash +138/turn, prestige -0.64/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +1 vs +20, -167 vs +11, -144 vs +6 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rouhomme: +0/turn
  - brewery 1 0.63 -> 0.47: +28/turn
  - logging camp w/ tool 5.00 -> 0.00: +2/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 1.67: +2/turn
  - sewing shop 1 0.21 -> 0.15: -1/turn
  - spinnery 1 1.70 -> 1.16: -17/turn
  - retting pit 1 0.83 -> 0.56: +7/turn
  - flax farm 1 4.60 -> 3.24: +12/turn
- Model check over the last 31 turns: predicted +121/turn for the settings we ran, real +51/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.60, thread 4.00, cloth 6.40, flax fibres 4.67, garments 18.56, nets 29.49, beer 2.87, timber 5.62, prestige 56.70, cash 0.04
- Orders it would set: cured meat buy 1 (v2 2); furniture buy 2 (v2 None); garments sell 7 (v2 6); grain buy 31 (v2 49); labour buy 95 (v2 56); light armour buy 1 (v2 None); pasties buy 3 (v2 4); porterage buy 13 (v2 5); thread sell 10 (v2 none)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 1.67, worth +2/turn.
- Ship linen snake: Grandgues -> Rouhomme (+2/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +5/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +20/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +19/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 9.2/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 434, chain may buy 0 -> chain allowance 66, chain plan 94 (-166 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.14 |
| ret | 3 | 0.83 | 0.38 |
| spin | 4 | 1.70 | 0.79 |
| weave | 3 | 0.33 | 0.00 |
| sew | 2 | 0.21 | 0.00 |

Buffers: flax fibres 35/47, thread 817/138, cloth 6/0
- chain plan needed 94 labour, budget left 66: cut to 94

## Self-diagnosis

- R5: varnish buy not filling: bid 17.1 under the home ask 18.2 for 3 turns, bought 0.0 of 1, 0.3 held (2.2 turns); raise needs Taylor (ceiling None)
- R7 stale ask: rope ask 74 over the market for 3 turns: the town trades ~4 a turn at 69.5, we sold 0 with 36 over what we keep -> **sell price 74 -> 69.5 (last trade 69.5, floor 59.07)** (ok)
