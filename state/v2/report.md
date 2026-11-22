# v2 shadow report

Turn 14200, 2026-11-22 01:41. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,013, prestige 3,707 (587 free, -3.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 100 | 0 | 4 | 0 | 0 | min_holding 58, sell 18, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 509 | 0 | 55 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (12 @ 34), home ask 33.60 x13, yet 0 bought last turn); labour need rises ~35/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 55 labour expired last turn (~112 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.76 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **cured meat**: home ask 33.60 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 88 over real use lately; planning 575, not 664
- labour expiry guard: 55 bought labour expired last turn, buy 9 (not 75) this turn

## Prestige spending, cheapest coin per prestige first

201 turns left: prestige gained now converts 63.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 53.0 | 53.8 | needs a arena (build cost 28,510); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 58.1 | 59.0 | needs a arena (build cost 28,510); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 60.6 | 60.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 62.4 | 62.4 | thin at home: pasties, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 53.1 | 63.5 | needs a cathedral (build cost 305,975); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 (premium) | mansion | 20 | 63.8 | 63.8 | thin at home: wine, stockfish, premium ham |
| hold banquet 1 (fish) | mansion | 4.2 | 65.5 | 65.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 67.0 | 67.0 | thin at home: pasties, wine |
| hold banquet 3 (pies) | mansion | 8 | 67.1 | 67.1 | thin at home: pasties |
| hold banquet 4 | mansion | 17.5 | 67.6 | 67.6 | thin at home: wine, ham, stockfish |
| jousting 1 | arena | 170 | 70.1 | 71.2 | needs a arena (build cost 28,510); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 72.4 | 72.4 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.6 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 16.4 (keep 14); best orders clear only 13 a turn after crew: ship stays at 0
- best towns now: Heilegg +38, Orlesailles +27, Boistot +24, Blanans +24, Clairlond +22
- Heilegg would trade: beer sell 18 @ 6.3, pasties buy 6 @ 16.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~129 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (129/turn) | bread 220 (2.9->5.75), firewood 36 (2.31->11.78), charcoal 14 (2.77->5.75), beer 13 (3.81->4.75) | garments 1 (28.35->33.2), cloth 4 (11.65->13), yarn 2 (6.83->7.69) | +993 |
| Kirchwerp | 1072 | 0.46 | 0.80 (103/turn) | thread 78 (6.7->9.5), casks 23 (6.51->9.36), nets 6 (40.2->44.27), butter 1 (76.12->92.15) | cloth 24 (10.5->13), cookware 7 (21->24.51), garments 2 (24.15->33.2), jewellery 2 (73.5->82.17) | +423 |
| Rouhomme | 368 | 0.13 | 1.00 (129/turn) | bread 287 (2.9->3.88), flour 3 (24.15->30.59), butter 1 (76.12->88.83), hop beer 5 (12.39->14.82) | yarn 21 (6.77->7.69), tools 16 (4.73->5.7), cloth 16 (12.71->13), cookware 7 (24.15->24.51) | +250 |
| Hofkirchen | 991 | 0.41 | 0.50 (64/turn) | windows 2 (840->855), flax fibres 6 (7.2->10.16), nets 6 (40.2->42.94), thread 75 (6.7->7.27) | cloth 24 (9.66->13), coats 4 (81.9->86.45), cured meat 8 (29.82->31.73), garments 2 (28.35->33.2) | +190 |
| Heilegg | 826 | 0.29 | 0.40 (52/turn) | beer 18 (3.81->6.51), malt 3 (8.29->12.63), wine 5 (6.93->9.31), flour 3 (24.15->29.07) | cloth 24 (10.45->13), garments 2 (25.2->33.2), tools 16 (4.62->5.7), dyed cloth 2 (14.7->16.25) | +181 |

**Best:** Grandgues at about +993 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 17 @ min 3.86 | makes 19.3, uses 4.2, holds 100 (keeps 58): sells the surplus + 2/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 76.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 9) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 39.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.7k (cash + stock at home prices); +15/turn over 6 turns, +137/turn over 24 turns.
- Limits: cash flow >= -376/turn, prestige >= -1.19/turn (values are after 200 tax a turn).
- Today's settings: value -190/turn, cash -177/turn, prestige +0.95/turn.
- Plan: value +11/turn, cash +15/turn, prestige -1.19/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -115 vs -150, +93 vs -184, -138 vs -162.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +6/turn
  - ship Flax Wyrm -> Donaunieder: +5/turn
  - mansion 1 1.00 -> 0.49: +169/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.29: -4/turn
  - retting pit 1 0.91 -> 0.82: +3/turn
  - flax farm 1 4.64 -> 4.10: +5/turn
  - sewing shop 1 0.30 -> 0.23: -6/turn
  - weavery 1 0.50 -> 0.38: +14/turn
- Model check over the last 59 turns: predicted -129/turn for the settings we ran, real +40/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.66, beer 3.31, timber 3.77, prestige 74.90, cash 0.00
- Orders it would set: arms buy 1 (v2 None); bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 64 (v2 9); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Vauxvais (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+5/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2011 coin: +4/turn, payback 466 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 114/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: prestige rate -3.25 a turn vs 12-turn median +0.44; likely: no slot, building or contract cause found: check the impacts
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
