# v2 shadow report

Turn 14165, 2026-11-20 14:11. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,716, prestige 3,739 (619 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 39 | 0 | 4 | 12 | 0 | stop 60, buy 39, buy @ 5.35 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 3 | 3 | 1 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 30 | 0 | 2 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 495 | 0 | 69 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (4 @ 2.4), but the home ask 2.62 is above it); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.62 is above our ceiling 2.40 and last turn bought 3 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.80 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 69 labour expired last turn (~152 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.78 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **grain**: home ask 3.72 is above our ceiling 3.70 and last turn bought 0 of ~9 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.80 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.11, no projection from the game)
- labour: +0 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 119 over real use lately; planning 524, not 643
- labour expiry guard: 69 bought labour expired last turn, buy 0 (not 24) this turn

## Prestige spending, cheapest coin per prestige first

236 turns left: prestige gained now converts 69.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 51.1 | 51.4 | needs a arena (build cost 30,279); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.7 | 53.3 | needs a arena (build cost 30,279); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.8 | 55.2 | needs a arena (build cost 30,279); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.7 | 58.4 | needs a arena (build cost 30,279); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 59.4 | 59.4 | thin at home: stockfish, candles |
| hold banquet 3 (pies) | mansion | 8 | 60.3 | 60.3 | thin at home: candles |
| hold banquet 2 (pies) | mansion | 7 | 60.9 | 60.9 | thin at home: candles |
| hold banquet 4 (premium) | mansion | 20 | 61.6 | 61.6 | thin at home: stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 55.4 | 62.9 | needs a cathedral (build cost 315,330); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 63.3 | 63.3 | thin at home: ham, stockfish, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 63.7 | 63.7 | thin at home: cured meat |
| hold banquet 3 (meat) | mansion | 7.6 | 64.5 | 64.5 | thin at home: cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: candles buy 2 @ 73.0, furniture buy 19 @ 14.1, pasties buy 2 @ 14.5; crew 0.2; est +249 a turn; stock: candles 2 @ 73.0 (keep 12); stock: furniture 19 @ 14.1 (keep 145); stock: pasties 2 @ 14.5 (keep 14)
- **linen snake** on Grandgues: beer sell 3 @ 7.8, candles buy 2 @ 74.0, pasties buy 6 @ 16.0; crew 0.1; est +43 a turn; stock: candles 2 @ 74.0 (keep 12); stock: pasties 6 @ 16.0 (keep 14)
- best towns now: Großmühle +250, Caillechâtel +249, Clairlond +242, Chatgnan +225, Gotthafen +220
- Großmühle would trade: candles buy 2 @ 78.0, furniture buy 19 @ 13.9, pasties buy 6 @ 16.2; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~137 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Unterhufe | 595 | 0.22 | 0.30 (41/turn) | thread 48 (6.9->8.36), butter 1 (79.28->88.35), lathes 1 (190.05->199.5), leather 1 (29.19->33.44) | cloth 24 (11.13->13.3), cookware 4 (21.21->23.56), beer 3 (3.63->5.3), tools 20 (6.72->7.08) | +151 |
| Grandgues | 152 | 0.06 | 0.70 (96/turn) | firewood 45 (2.75->6.03), charcoal 19 (2.73->3.86), beer 3 (5->7.6), thread 92 (6.9->7.03) | garments 2 (29.4->33.4), cured fish 4 (27.3->28.12) | +117 |
| Kirchwerp | 1072 | 0.49 | 0.40 (55/turn) | casks 15 (7.67->9.36), light armour 3 (107.1->112.1), salt 11 (5.78->6.93), cured fish 5 (33.18->35.15) | dyed cloth 8 (15.75->18.71), garments 2 (24.15->33.4), cookware 4 (19.43->23.56), flax fibres 15 (5.62->7.05) | +113 |
| Fontaux | 411 | 0.15 | 1.00 (137/turn) | cured fish 4 (33.18->38), bread 149 (2.92->3.5), thread 75 (6.9->7.27), cured meat 0 (23.2->30.21) | dyed cloth 6 (16.91->18.71), tools 21 (6.62->7.08), cloth 5 (12.6->13.3), pasties 1 (12.6->14.54) | +98 |
| Heidlowe | 662 | 0.24 | 0.20 (27/turn) | nets 4 (42->43.7), cheese 5 (7.77->8.5) | cloth 24 (10.24->13.3), cookware 4 (20.79->23.56), garments 2 (30.03->33.4), copper ingots 4 (13.76->14.54) | +95 |

**Best:** Unterhufe at about +151 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 26 @ 5.55, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 39 = 2.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 29.0, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 31.8) |
| grain | 6 @ 3.7, stop 22 |  | goal planner: buys 6 a turn for today's rates, keeps up to 22 (v2 had 12) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 0) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 40.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.5k (cash + stock at home prices); +281/turn over 6 turns, -61/turn over 24 turns.
- Limits: cash flow >= -280/turn, prestige >= -1.33/turn (values are after 200 tax a turn).
- Today's settings: value -148/turn, cash -163/turn, prestige +0.59/turn.
- Plan: value +35/turn, cash +45/turn, prestige -1.33/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +353 vs -129, +27 vs -125, -62 vs -147.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Kirchwerp: +11/turn
  - ship Flax Wyrm -> Clairas: +2/turn
  - mansion 1 1.00 -> 0.54: +117/turn
  - ropewalk 1 0.25 -> 0.10: +13/turn
  - spinnery 1 1.65 -> 1.25: +23/turn
  - retting pit 1 0.91 -> 0.80: +4/turn
  - flax farm 1 4.64 -> 4.00: +9/turn
  - net maker 0.00 -> 0.29: +1/turn
- Model check over the last 59 turns: predicted -46/turn for the settings we ran, real +12/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.79, beer 3.56, timber 4.05, prestige 62.43, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); cured meat buy 4 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 12); labour buy 64 (v2 0); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Kirchwerp (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Clairas (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 424 (+136 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.44 |
| ret | 3 | 0.91 | 0.89 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 100/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: prestige rate -2.63 a turn vs 12-turn median -0.04; likely: no slot, building or contract cause found: check the impacts
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.8 for 5 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
