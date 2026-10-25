# v2 shadow report

Turn 13541, 2026-10-25 14:28. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,563, prestige 3,563 (443 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 0 | 6 | 0 | 0 | buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 62 | 28 | 29 | 0 | 0 | stop 111, buy 28, buy @ 3.7 |
| labour | 55 | 85 | 528 | 0 | 57 | buy 55, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 33.6 |
| porterage | 14 | 14 | 14 | 0 | 0 | buy 14, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy

## Waste (money lost now)

- **labour**: 57 labour expired last turn (~91 coin): holding 55 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: we make 0/turn more than we use but there is no sell order -> v2: sell 0
- **flax plants**: flax plants buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 100 over real use lately; planning 552, not 652
- labour expiry guard: 57 bought labour expired last turn, buy 28 (not 52) this turn

## Prestige spending, cheapest coin per prestige first

860 turns left: prestige gained now converts 98.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 3 (pies) | mansion | 8 | 48.0 | 48.0 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.6 | 48.6 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.8 | 50.8 | thin at home: wine, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 50.9 | 50.9 | thin at home: hop beer |
| hold banquet 3 (fish) | mansion | 7.6 | 51.1 | 51.1 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 51.9 | 51.9 | thin at home: wine, hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 51.9 | 51.9 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 52.9 | 52.9 | thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 53.1 | 53.1 | thin at home: wine |
| jousting 3 | arena | 230 | 53.0 | 53.1 | needs a arena (build cost 24,365); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 51.1 | 54.0 | needs a chapel (build cost 30,370) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Orlesailles | 1178 | 0.41 | 0.40 (39/turn) | thread 36 (4.62->6.27), grindstones 1 (208.95->229.9), hides 1 (14.38->18.14), cured fish 5 (25.41->26.41) | gears 2 (56.7->59.38), pasties 2 (12.6->14.7), flax fibres 3 (4.94->5.8) | +65 |
| Clairlond | 1288 | 0.47 | 0.10 (10/turn) | nets 1 (34->35.15) | lathes 1 (127.05->191.9), pasties 2 (13.02->14.7) | +60 |
| Hofkirchen | 991 | 0.31 | 0.40 (39/turn) | grindstones 1 (208.95->267.9), flax fibres 16 (5.25->6.17), seeds 11 (2.62->3.57), nails 5 (5.51->6.13) | - | +55 |
| Dortgart | 1045 | 0.34 | 0.20 (20/turn) | grindstones 1 (208.95->269.8), nets 3 (34->36.67), hides 1 (14.38->15.2) | - | +50 |
| Helmgreen | 1354 | 0.50 | 0.10 (10/turn) | spinning wheels 1 (270.9->319.2), tools 10 (4.34->4.94) | - | +45 |

**Best:** Orlesailles at about +65 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.38) |
| candles | 1 @ 70.5, stop 61 |  | goal planner: buys 1 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 0 @ 2.4, stop 13 | 1 @ min 1.76 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 7 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 13.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 28 @ 3.7, stop 111 |  | goal planner: buys 28 a turn for today's rates, keeps up to 111 (v2 had 56) |
| labour | 5 @ 2.2, stop - |  | goal planner: buys 5 for today's rates (v2 had 28) |
| light armour | 1 @ 91.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 13 @ min 33.6 | goal planner: sells 13 at 33.6 (v2 had 13 at 34.0) |
| pasties | 2 @ 14.5, stop 7 |  | goal planner: buys 2 a turn for today's rates, keeps up to 7 (v2 had 5) |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 14) |
| rope |  | 1 @ min 72.0 |  |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| thread |  | 15 @ min 4.5 | goal planner: sells 15 a turn at 4.5, keeps 205 (no one offered it) |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 74.8 turns |
| varnish | 1 @ 20.4, stop 1 |  | uses 0.2/turn (net maker152202386007001), makes 0.0, holds 0 = 2.6 turns |
| wax | 1 @ 21.2, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.5k (cash + stock at home prices); -57/turn over 6 turns, +17/turn over 24 turns.
- Limits: cash flow >= +18/turn, prestige >= -0.60/turn (values are after 240 tax a turn).
- Today's settings: value +86/turn, cash +43/turn, prestige -0.57/turn.
- Plan: value +187/turn, cash +200/turn, prestige -0.60/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +552 vs +130, +472 vs +136, -243 vs -48.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +10/turn
  - ship Flax Wyrm -> Calange: +6/turn
  - ropewalk 1 0.25 -> 1.00: +22/turn
  - spinnery 1 1.59 -> 2.37: +33/turn
  - net maker 0.73 -> 0.00: +17/turn
  - net maker [make nets 2] 0.00 -> 0.32: +19/turn
  - logging camp w/ tool 5.00 -> 4.76: +0/turn
  - flax farm 1 6.29 -> 6.53: -2/turn
- Model check over the last 46 turns: predicted +96/turn for the settings we ran, real +49/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.59, thread 3.92, cloth 6.30, flax fibres 4.50, garments 18.31, nets 29.10, beer 2.83, timber 2.92, prestige 53.91, cash 0.00
- Orders it would set: candles buy 1 (v2 None); cured meat buy 1 (v2 2); furniture buy 2 (v2 None); grain buy 28 (v2 56); labour buy 5 (v2 28); light armour buy 1 (v2 None); pasties buy 2 (v2 5); thread sell 15 (v2 none)
- Recipe: net maker make nets 3 -> make nets 2 at 0.32, worth +6/turn.
- Ship linen snake: Grandgues -> Vauxvais (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Calange (+6/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot ropewalk 1 for ~2734 coin: +3/turn, payback 1018 turns, doesn't pay yet
- Trim: donate quarry 1: +20/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +17/turn (tax 20 saved).
- Trim: donate weavery 1: +13/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 3.2/turn (+0.0 exported); plan makes 32.0 garments a turn.
Labour: own 500, everything else 408, chain may buy 350 -> chain allowance 442, chain plan 441 (+194 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.29 | 5.16 |
| ret | 3 | 1.12 | 0.92 |
| spin | 4 | 1.59 | 1.89 |
| weave | 3 | 0.13 | 1.25 |
| sew | 2 | 0.09 | 0.78 |

Buffers: flax fibres 77/85, thread 793/249, cloth 0/125

## Self-diagnosis

Nothing found this run.
