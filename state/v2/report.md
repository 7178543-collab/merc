# v2 shadow report

Turn 14187, 2026-11-21 12:39. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,040, prestige 3,718 (598 free, -3.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 59 | 0 | 4 | 0 | 0 | min_holding 58, sell 15, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 3 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 9 | 9 | 0 | 0 | stop 36, buy 10, buy @ 3.7 |
| labour | 64 | 64 | 529 | 0 | 35 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), but the home ask 30.00 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 3 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 35 labour expired last turn (~73 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 30.00 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.50 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 114 over real use lately; planning 529, not 624
- labour expiry guard: 35 bought labour expired last turn, buy 29 (not 29) this turn

## Prestige spending, cheapest coin per prestige first

214 turns left: prestige gained now converts 65.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.3 | 53.1 | needs a arena (build cost 29,718); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.3 | 58.2 | needs a arena (build cost 29,718); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.5 | 60.5 | thin at home: wine, stockfish, candles |
| hold banquet 4 (pies) | mansion | 18 | 60.9 | 60.9 | thin at home: wine, stockfish, candles |
| maintain 1 | park | 0.5 | 62.4 | 62.4 | running |
| hold mass 2 (premium) | cathedral | 360 | 53.8 | 63.1 | needs a cathedral (build cost 316,120); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 1 (fish) | mansion | 4.2 | 66.0 | 66.0 |  |
| hold banquet 4 | mansion | 17.5 | 66.0 | 66.0 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 3 (pies) | mansion | 8 | 66.6 | 66.6 | thin at home: cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 69.5 | 69.5 | thin at home: wine, cheese, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 74.3 | 74.3 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 76.1 | 76.1 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 13.8 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Blanans +96, Toqueque +87, Brunnham +76, Donaunieder +75, Boistot +74
- Blanans would trade: furniture buy 7 @ 12.7, grain buy 8 @ 3.02, pasties buy 3 @ 16.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~128 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.70 (90/turn) | firewood 44 (2.84->7.6), charcoal 19 (2.84->7.74), thread 72 (6.8->7.03), beer 15 (3.96->4.39) | cloth 4 (6.88->10.6), cheese 10 (12.5->13.96), fleece 2 (8.82->14.72), tackles 1 (160.65->170.05) | +302 |
| Kirchwerp | 1072 | 0.46 | 0.50 (64/turn) | furniture 8 (17.85->25.84), thread 36 (6.8->8.41), premium ham 1 (249.9->275.5), casks 11 (6.51->9.36) | fleece 2 (10.92->14.72), garments 2 (30.45->32.4), chisels 3 (8.4->9.59) | +189 |
| Brebronn | 862 | 0.32 | 0.20 (26/turn) | garments 10 (32->34.77), nets 3 (45.8->50.35), dyed cloth 6 (20.79->22.8), leather 1 (23.31->25.27) | cheese 12 (6.3->13.96), fleece 7 (9.66->14.72), cloth 24 (9.61->10.6), flax fibres 3 (6.09->8.2) | +188 |
| Hanstein | 380 | 0.13 | 0.20 (26/turn) | charcoal 19 (2.84->4.52), nets 1 (45.8->50.82), cloth 1 (10.1->12.44), leather 1 (23.31->25.65) | thread 37 (5.23->6.85), cheese 12 (9.5->13.96), fleece 7 (10.34->14.72), yarn 28 (5.72->6.17) | +175 |
| Fontaux | 411 | 0.14 | 0.60 (77/turn) | charcoal 19 (2.84->4.99), casks 11 (6.51->7.55), leather 1 (23.31->26.41), varnish 3 (17.12->18.34) | cheese 12 (7.4->13.96), fleece 6 (9.55->14.72), butter 1 (41.79->64.6), cured fish 4 (22.68->24.32) | +163 |

**Best:** Grandgues at about +302 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.86 |  |
| bread | 5 @ 3.22, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 29.0, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| furniture | 2 @ 17.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 31.2) |
| grain | 10 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 35 = 3.9 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 29) |
| light armour | 1 @ 114, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 44.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 81.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.6k (cash + stock at home prices); +212/turn over 6 turns, +92/turn over 24 turns.
- Limits: cash flow >= -335/turn, prestige >= -1.24/turn (values are after 200 tax a turn).
- Today's settings: value -172/turn, cash -189/turn, prestige +0.49/turn.
- Plan: value +12/turn, cash +15/turn, prestige -1.24/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +137 vs -183, +266 vs -192, +220 vs -201.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Blanans: +5/turn
  - ship Flax Wyrm -> Nürnnieder: +1/turn
  - mansion 1 1.00 -> 0.59: +129/turn
  - ropewalk 1 0.25 -> 0.10: +14/turn
  - spinnery 1 1.65 -> 1.18: +19/turn
  - retting pit 1 0.91 -> 0.75: +3/turn
  - flax farm 1 4.64 -> 3.79: +0/turn
  - net maker 0.00 -> 0.29: +6/turn
  - weavery 1 0.50 -> 0.39: -15/turn
  - sewing shop 1 0.30 -> 0.24: -1/turn
- Model check over the last 59 turns: predicted -130/turn for the settings we ran, real -6/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.62, beer 3.59, timber 3.73, prestige 70.74, cash 0.00
- Orders it would set: bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 4 (v2 12); firewood buy 4 (v2 8); fish buy 0 (v2 None); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 29); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.25, worth +14/turn.
- Ship linen snake: Grandgues -> Blanans (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Nürnnieder (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1953 coin: +2/turn, payback 873 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 417 (+128 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.04 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 129/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 0.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 3.22, home ask 3.14; our bid is already at/over the ask (sellers too thin)
- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 29, home ask 30.0 -> **buy 12 @ 30.6 (ask 30.0, cap 42.0)** (ok)
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 2.28 -> **buy 14 @ 2.32 (ask 2.28, cap 2.6)** (ok)
- R1: prestige rate -3.71 a turn vs 12-turn median -0.98; likely: dry slot: bread, cured meat, fish; mansion 1 projected 0 (cured meat)
- R5: firewood buy not filling: bid 2.4 under the home ask 2.7 for 6 turns, bought 3.0 of 4, 5.9 held (1.5 turns); raise needs Taylor (ceiling 2.4)
- R5: tar buy not filling: bid 11 under the home ask 11.5 for 6 turns, bought 0.0 of 1, 0.1 held (0.3 turns); raise needs Taylor (ceiling 11.0)
