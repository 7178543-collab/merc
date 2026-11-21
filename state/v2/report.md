# v2 shadow report

Turn 14188, 2026-11-21 13:45. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,015, prestige 3,714 (594 free, -3.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 59 | 0 | 4 | 0 | 0 | min_holding 58, sell 15, sell @ 3.86 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 5 | 0 | 0 | 0 | 0 | stop 42, buy 14, buy @ 2.32 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 9 | 9 | 0 | 0 | stop 36, buy 10, buy @ 3.7 |
| labour | 64 | 64 | 524 | 0 | 40 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (12 @ 30.6), but the home ask 30.80 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 40 labour expired last turn (~82 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 30.80 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 114 over real use lately; planning 529, not 643
- labour expiry guard: 40 bought labour expired last turn, buy 24 (not 29) this turn

## Prestige spending, cheapest coin per prestige first

213 turns left: prestige gained now converts 65.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.0 | 52.8 | needs a arena (build cost 29,386); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 56.9 | 57.8 | needs a arena (build cost 29,386); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.5 | 60.5 | thin at home: wine, stockfish, candles |
| hold banquet 4 (pies) | mansion | 18 | 60.7 | 60.7 | thin at home: wine, stockfish, cheese, candles |
| maintain 1 | park | 0.5 | 61.2 | 61.2 | running |
| hold mass 2 (premium) | cathedral | 360 | 53.7 | 63.1 | needs a cathedral (build cost 313,690); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 1 (fish) | mansion | 4.2 | 65.5 | 65.5 |  |
| hold banquet 4 | mansion | 17.5 | 65.6 | 65.6 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 3 (pies) | mansion | 8 | 65.8 | 65.8 | thin at home: cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 68.0 | 68.0 | thin at home: wine, cheese, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 74.3 | 74.3 | thin at home: wine, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 74.6 | 74.6 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 12.9 (keep 14); best orders clear only -7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Blanans +85, Toqueque +79, Chatgnan +78, Clairlond +70, Donaunieder +66
- Blanans would trade: furniture buy 6 @ 12.7, grain buy 8 @ 3.0, pasties buy 4 @ 16.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~127 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.46 | 0.70 (89/turn) | thread 102 (6.8->9.5), casks 19 (6.51->9.36), varnish 6 (17.12->20.52), dyed cloth 14 (20.79->22.42) | cheese 5 (9.5->13.3), garments 2 (28.77->33.2), nails 5 (5.35->6.7), cookware 6 (21->21.85) | +371 |
| Grandgues | 152 | 0.05 | 0.60 (76/turn) | firewood 36 (2.84->7.65), charcoal 19 (2.79->7.69), thread 97 (6.8->7.03), acid 1 (113.4->118.75) | cured meat 6 (27.72->29.07), cheese 5 (12.81->13.3), yarn 4 (7.25->7.65), furniture 1 (16.38->17) | +239 |
| Brebronn | 862 | 0.31 | 0.20 (25/turn) | garments 10 (31.8->35.34), dyed cloth 14 (20.79->22.8), jewellery 1 (89.25->98.8), acid 1 (113.4->115.9) | cheese 5 (6.3->13.3), yarn 19 (5.72->7.65), flax fibres 3 (5.93->8.25), grain 8 (3.11->3.8) | +139 |
| Heilegg | 826 | 0.29 | 0.90 (114/turn) | acid 1 (113.4->133.95), charcoal 19 (2.79->6.13), beer 15 (3.9->5.42), arms 16 (31.92->33.25) | cheese 5 (7.93->13.3), wool 15 (11.76->12.35), garments 2 (32.34->33.2) | +134 |
| Hanstein | 380 | 0.13 | 0.20 (25/turn) | charcoal 19 (2.79->4.84), cloth 1 (10.1->11.88), flax fibres 3 (7.45->7.74), resin 3 (2.31->2.64) | yarn 28 (5.72->7.65), thread 19 (5.51->6.95), cheese 5 (9.77->13.3), wool 14 (11.55->12.35) | +123 |

**Best:** Kirchwerp at about +371 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 15 @ min 3.8 |  |
| bread | 5 @ 3.1, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 29.0, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| furniture | 2 @ 17.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 10 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 35 = 4.0 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 24) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 44.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.9k (cash + stock at home prices); +283/turn over 6 turns, +101/turn over 24 turns.
- Limits: cash flow >= -334/turn, prestige >= -1.22/turn (values are after 200 tax a turn).
- Today's settings: value -179/turn, cash -191/turn, prestige +0.51/turn.
- Plan: value +2/turn, cash +6/turn, prestige -1.22/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +266 vs -192, +220 vs -201, -24 vs -189.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Blanans: +5/turn
  - ship Flax Wyrm -> Magdeach: +0/turn
  - mansion 1 1.00 -> 0.59: +130/turn
  - ropewalk 1 0.25 -> 0.12: +13/turn
  - spinnery 1 1.65 -> 1.20: +15/turn
  - retting pit 1 0.91 -> 0.76: +3/turn
  - flax farm 1 4.64 -> 3.83: +4/turn
  - net maker 0.00 -> 0.29: +1/turn
  - weavery 1 0.50 -> 0.38: -13/turn
  - sewing shop 1 0.30 -> 0.24: -1/turn
- Model check over the last 59 turns: predicted -130/turn for the settings we ran, real -2/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.63, beer 3.50, timber 4.28, prestige 71.58, cash 0.00
- Orders it would set: arms buy 1 (v2 None); bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 4 (v2 12); firewood buy 4 (v2 8); fish buy 0 (v2 None); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 24)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.24, worth +15/turn.
- Ship linen snake: Grandgues -> Blanans (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Magdeach (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2064 coin: +3/turn, payback 776 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 418 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.07 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 126/77, thread 1060/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 5.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 3.1, home ask 3.02; our bid is already at/over the ask (sellers too thin)
- R1: cured meat slot dry: 6.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 12 @ 30.6, home ask 30.8 (held back: acted on cured meat at turn 14187 (one action per 2 turns))
- R1: fish slot dry: 5.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy 14 @ 2.32, home ask none (no sellers at home)
- R1: prestige rate -3.69 a turn vs 12-turn median -0.98; likely: dry slot: bread, cured meat, fish
- R2: spinnery 1 blocked by thread space: 1060 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.1 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
