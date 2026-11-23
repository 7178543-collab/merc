# v2 shadow report

Turn 14232, 2026-11-23 09:21. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,914, prestige 3,689 (569 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 73 | 0 | 12 | 0 | 0 | min_holding 58, sell 1, sell @ 3.16 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 6 | 6 | 8 | 1 | 0 | stop 23, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 531 | 0 | 33 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), but the home ask 29.80 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **grain**: brewery 1 ran short of grain (buy is live (6 @ 3.7), 6 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.7 turns of grain left and buying 6 (need 18) -> v2: buy 18

## Waste (money lost now)

- **labour**: 33 labour expired last turn (~55 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 29.80 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 106 over real use lately; planning 531, not 623
- labour expiry guard: 33 bought labour expired last turn, buy 31 (not 31) this turn

## Prestige spending, cheapest coin per prestige first

169 turns left: prestige gained now converts 57.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| jousting 3 (premium) | arena | 420 | 49.2 | 49.7 | needs a arena (build cost 25,959); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 52.9 | 53.4 | needs a arena (build cost 25,959); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.2 | 55.2 | needs a arena (build cost 25,959); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 2 | park | 2 | 55.4 | 55.4 | thin at home: sculptures |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 | thin at home: beer |
| jousting 2 | arena | 210 | 59.4 | 60.4 | needs a arena (build cost 25,959); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 63.2 | 63.2 | thin at home: wine |
| hold banquet 5 | mansion | 22 | 63.2 | 63.2 | thin at home: hop beer, wine, stockfish, sculptures |
| hold banquet 2 (pies) | mansion | 7 | 66.1 | 66.1 | thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 66.2 | 66.2 | running; thin at home: beer |
| hold banquet 4 (pies) | mansion | 18 | 66.4 | 66.4 | thin at home: hop beer, wine, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 6 @ 5.4, pasties buy 2 @ 14.5, rope sell 1 @ 85.5; crew 0.1; est +19 a turn; stock: pasties 2 @ 14.5 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.6 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- best towns now: Bordetes +45, Fontaux +34, Heidlowe +25, Kleinburgh +20, Grandgues +19
- Bordetes would trade: beer sell 6 @ 8.2, pasties buy 2 @ 15.1, rope sell 1 @ 96.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.70 (74/turn) | firewood 37 (1.91->6.65), cured fish 9 (26.46->31.73), timber 29 (7.82->9.26), rope 1 (62.79->82.65) | thread 38 (5.08->6.1), bricks 10 (6.51->10.07), axes 3 (20.37->23.75), tools 17 (5.83->6.46) | +331 |
| Heilegg | 826 | 0.24 | 0.40 (42/turn) | dyed cloth 9 (18.9->27.36), casks 15 (6.51->11.3), arms 14 (29.19->31.92), rope 1 (62.79->80.27) | tools 17 (5.04->6.46), cloth 16 (9.35->10.6), axes 3 (20.89->23.75), garments 2 (30.45->32) | +281 |
| Vauxvais | 204 | 0.06 | 0.30 (32/turn) | grain 115 (2.77->3.99), rope 1 (62.79->80.27), tackles 1 (198.45->214.7), flour 3 (17.01->19.38) | bricks 18 (6.77->10.07), tools 17 (5.78->6.46), flax fibres 7 (6.3->7.4), axes 3 (21.84->23.75) | +247 |
| Rouhomme | 368 | 0.10 | 1.00 (106/turn) | grain 98 (2.77->3.7), firewood 24 (1.91->7.03), rope 0 (62.79->85.5), lead bars 1 (9.66->11.49) | bricks 10 (4.96->10.07), tools 10 (4.73->6.46), flax fibres 7 (6.3->7.4), thread 24 (5.78->6.1) | +209 |
| Hanstein | 380 | 0.11 | 1.00 (106/turn) | timber 20 (7.82->12.16), firewood 14 (1.91->6.98), rope 0 (62.79->79.8), charcoal 16 (2.62->4.14) | thread 20 (5.21->6.1), flax fibres 9 (5.83->7.4), cloth 14 (9.66->10.6), garments 1 (27.09->32) | +194 |

**Best:** Grandgues at about +331 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 12 @ 3.3, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 73 = 6.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.6) |
| grain | 8 @ 3.7, stop 32 |  | goal planner: buys 8 a turn for today's rates, keeps up to 32 (v2 had 18) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 31) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 40.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 10 @ min 64.5 | sell; ships offer 1 a turn abroad, so home sells 10 (was 1) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.8k (cash + stock at home prices); -70/turn over 6 turns, -7/turn over 24 turns.
- Limits: cash flow >= -413/turn, prestige >= -1.12/turn (values are after 200 tax a turn).
- Today's settings: value -158/turn, cash -161/turn, prestige +1.35/turn.
- Plan: value +38/turn, cash +53/turn, prestige -1.12/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +174 vs -144, +150 vs -139, +156 vs -159.
- Route sales counted at most (what the ships really sold, a turn): beer 1.5.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Fontaux: +36/turn
  - ship Flax Wyrm -> Donaunieder: +18/turn
  - mansion 1 1.00 -> 0.41: +166/turn
  - net maker 0.00 -> 0.29: +11/turn
  - ropewalk 1 0.25 -> 0.18: +7/turn
  - spinnery 1 1.65 -> 1.40: +3/turn
  - retting pit 1 0.91 -> 0.85: +0/turn
  - flax farm 1 4.64 -> 4.26: +3/turn
  - weavery 1 0.50 -> 0.60: -8/turn
  - sewing shop 1 0.30 -> 0.36: +14/turn
- Model check over the last 59 turns: predicted -156/turn for the settings we ran, real +49/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.12, cloth 6.58, flax fibres 4.88, garments 19.04, nets 30.31, beer 2.85, timber 3.35, prestige 66.43, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 18); labour buy 65 (v2 31); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Fontaux (+15/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+18/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1858 coin: +3/turn, payback 711 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 85/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 29.8 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 30.4 (ask 29.8, cap 42.0))
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
