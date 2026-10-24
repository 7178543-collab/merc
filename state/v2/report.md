# v2 shadow report

Turn 13507, 2026-10-24 04:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,115, prestige 3,586 (466 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 63 | 0 | 4 | 0 | 0 | min_holding 60, sell 73, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 0 | 7 | 0 | 0 | stop 15, buy 1, buy @ 2.4; sell 3, sell @ 1.61 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 97 | 0 | 2 | 0 | 0 | min_holding 30, sell 7, sell @ 19 |
| grain | 95 | 32 | 34 | 0 | 0 | stop 125, buy 32, buy @ 3.7 |
| labour | 26 | 35 | 535 | 60 | 0 | buy 26, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 13 | 13 | 6 | 0 | 7 | buy 13, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 26, short of ~95 needed -> v2: buy 95

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 70
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 182

## Notes

- labour: projection runs 100 over real use lately; planning 595, not 695

## Prestige spending, cheapest coin per prestige first

894 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 43.5 | 43.5 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.8 | 49.8 | thin at home: hop beer, wine, candles |
| hold banquet 3 (pies) | mansion | 8 | 50.0 | 50.0 | thin at home: hop beer, pies, candles |
| hold prayer 2 | chapel | 13 | 47.2 | 50.0 | needs a chapel (build cost 30,899); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 51.4 | 51.4 | thin at home: wine, pies, candles |
| jousting 3 | arena | 230 | 51.5 | 51.6 | needs a arena (build cost 23,984); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 52.0 | 52.0 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 52.8 | 52.8 | thin at home: wine, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 52.9 | 52.9 |  |
| hold banquet 4 | mansion | 17.5 | 53.1 | 53.1 | thin at home: wine, hop beer, ham, candles |
| hold sermon 2 | church | 24 | 50.4 | 53.7 | needs a church (build cost 63,414); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 51.1 | 53.7 | needs a church (build cost 63,414); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~91 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 0.60 (54/turn) | beer 69 (2.98->6.08), tallow 2 (19.84->24.13), lead ore 2 (7.88->10.64), blades 1 (13.12->14.25) | candles 7 (67.2->71.25), steel ingots 3 (13.97->15.96), garments 2 (18.38->19.3), flax plants 1 (1.41->2.22) | +218 |
| Rouhomme | 368 | 0.09 | 0.80 (73/turn) | bread 142 (2.05->2.72), beer 69 (2.98->3.42), charcoal 12 (1.58->3.29), iron ore 2 (4.85->8.46) | grindstones 1 (252->267.9), flax plants 1 (1.46->2.22) | +119 |
| Donaunieder | 985 | 0.28 | 0.10 (9/turn) | premium ham 1 (361.2->484.5) | flax plants 1 (1.24->2.22), steel ingots 3 (15.65->15.96) | +116 |
| Chribruck | 1202 | 0.39 | 0.70 (64/turn) | beer 69 (2.98->4.84), thread 5 (3.39->4.99), malt 2 (7.04->10.16), nets 1 (35->39.33) | candles 3 (70.35->71.25), yarn 2 (3.38->4.12), flax plants 1 (1.42->2.22) | +98 |
| Caillechâtel | 488 | 0.12 | 0.20 (18/turn) | beer 26 (2.98->5.79), thread 25 (3.39->3.99), windows 1 (640.5->650.75) | candles 2 (69.83->71.25), flax plants 1 (1.28->2.22), steel ingots 1 (15.23->15.96) | +86 |

**Best:** Hofkirchen at about +218 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 73 @ min 3.38 |  |
| cloth |  | 1 @ min 7 | goal planner: sells 1 a turn at 7, keeps 0 (no one offered it) |
| cured meat | 1 @ 29.0, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 1) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 | 2 @ min 1.68 | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 1) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 13.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 2 @ min 17.9 | goal planner: sells 2 a turn at 17.9, keeps 30 (no one offered it) |
| grain | 37 @ 3.7, stop 148 |  | goal planner: buys 37 a turn for today's rates, keeps up to 148 (v2 had 64) |
| labour | 98 @ 2.2, stop - |  | goal planner: buys 98 for today's rates (v2 had 95) |
| light armour | 1 @ 85.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| limestone |  | 1 @ min 16.8 |  |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 16 @ 1.1, stop - |  | goal planner: buys 16 for today's rates (v2 had 6) |
| rope |  | 5 @ min 72.0 | makes 3.9, uses 0.0, holds 19 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 1 @ 11.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| thread |  | 3 @ min 4.44 | goal planner: sells 3 a turn at 4.44, keeps 249 (no one offered it) |
| tools | 3 @ 6.2, stop 17 |  | uses 2.0/turn (retting pit 1), makes 0.0, holds 200 = 98.3 turns |
| wax | 1 @ 21.8, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.3k (cash + stock at home prices); +124/turn over 6 turns, +58/turn over 24 turns.
- Limits: cash flow >= +120/turn, prestige >= -0.69/turn (values are after 240 tax a turn).
- Today's settings: value +29/turn, cash +35/turn, prestige -0.69/turn - breaks the cash floor.
- Plan: value +117/turn, cash +207/turn, prestige -0.69/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -5 vs +272, +136 vs +22, +108 vs +5.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bedenis: +5/turn
  - ship Flax Wyrm -> Rouhomme: +0/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 6.56: +10/turn
  - brewery 1 0.57 -> 0.63: +7/turn
  - spinnery 1 2.08 -> 1.47: +7/turn
  - ropewalk 1 0.87 -> 0.64: +26/turn
  - retting pit 1 1.01 -> 0.71: +16/turn
  - quarry 1 0.08 -> 0.01: +6/turn
  - flax farm 1 5.83 -> 4.03: +1/turn
  - logging camp w/ tool 5.00 -> 0.00: -3/turn
- Model check over the last 13 turns: predicted +163/turn for the settings we ran, real +82/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.45, thread 3.58, cloth 5.75, flax fibres 4.12, garments 16.38, nets 26.62, beer 2.54, timber 5.08, prestige 54.02, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); furniture buy 2 (v2 None); garments sell 2 (v2 none); grain buy 37 (v2 64); labour buy 98 (v2 95); light armour buy 1 (v2 None); pasties buy 3 (v2 4); porterage buy 16 (v2 6); thread sell 3 (v2 none)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 6.56, worth +10/turn.
- Recipe: net maker make nets 2 -> make nets 3 at 0.68, worth +25/turn.
- Ship linen snake: Grandgues -> Bedenis (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Rouhomme (+0/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +72/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +19/turn (tax 20 saved).
- Trim: donate weavery 1: +17/turn (tax 18 saved).
- Trim: donate sewing shop 1: +12/turn (tax 12 saved).
- Trim: donate logging camp w/ tool: +10/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 1.2/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 443, chain may buy 0 -> chain allowance 57, chain plan 156 (-96 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.83 | 3.54 |
| ret | 3 | 1.01 | 0.63 |
| spin | 4 | 2.08 | 1.30 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 47/64, thread 562/190, cloth 33/0
- chain plan needed 155 labour, budget left 57: cut to 155

## Self-diagnosis

- R7 stale ask: rope ask 75 over the market for 3 turns: the town trades ~4 a turn at 74, we sold 0 with 19 over what we keep -> **sell price 75 -> 74 (last trade 74, floor 62.9)** (ok)
