# v2 shadow report

Turn 14171, 2026-11-20 20:36. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,982, prestige 3,740 (620 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 81 | 0 | 12 | 0 | 0 | sell 17, sell @ 4.44; stop 116, buy 39, buy @ 4.68 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 6 | 6 | 7 | 2 | 0 | stop 23, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 516 | 0 | 48 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: home ask 2.66 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **grain**: brewery 1 ran short of grain (buy is live (6 @ 3.7), 6 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.7 turns of grain left and buying 6 (need 18) -> v2: buy 18
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.00 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 48 labour expired last turn (~98 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 12.00 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 516, not 614
- labour expiry guard: 48 bought labour expired last turn, buy 16 (not 16) this turn

## Prestige spending, cheapest coin per prestige first

230 turns left: prestige gained now converts 68.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.7 | 52.4 | needs a arena (build cost 29,059); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 56.7 | 57.4 | needs a arena (build cost 29,059); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 57.9 | 57.9 | thin at home: hop beer, stockfish, candles |
| hold banquet 4 (premium) | mansion | 20 | 59.5 | 59.5 | thin at home: hop beer, stockfish, candles |
| hold banquet 3 (pies) | mansion | 8 | 59.6 | 59.6 | thin at home: hop beer, candles |
| hold banquet 2 (pies) | mansion | 7 | 60.9 | 60.9 | thin at home: candles |
| maintain 1 | park | 0.5 | 61.2 | 61.2 | running |
| hold banquet 4 | mansion | 17.5 | 61.7 | 61.7 | thin at home: hop beer, ham, stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 55.1 | 62.8 | needs a cathedral (build cost 305,420); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (meat) | mansion | 7.6 | 67.1 | 67.1 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 67.2 | 67.2 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 70.5 | 70.5 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 3 @ 24.8, pasties buy 12 @ 16.0; crew 0.1; est +26 a turn; stock: pasties 12 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- best towns now: Heilegg +249, Blanans +241, Großmühle +240, Clairlond +236, Angefont +232
- Heilegg would trade: cured meat buy 3 @ 24.2, furniture buy 20 @ 14.6, pasties buy 12 @ 15.1; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~131 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.14 | 0.80 (105/turn) | garments 10 (32.2->38), timber 23 (8.93->12.06), flour 4 (21.63->27.93), thread 61 (6.95->7.27) | cured fish 4 (28.56->36.48), fleece 3 (9.87->12.44), cloth 4 (12.5->13.5) | +160 |
| Unterhufe | 595 | 0.21 | 0.30 (39/turn) | thread 49 (6.95->7.89), axes 1 (16.7->18.62) | cured fish 4 (28.14->36.48), yarn 26 (6.46->7.55), flax fibres 18 (5.41->6.8), fleece 4 (8.51->12.44) | +148 |
| Amsdermund | 1111 | 0.50 | 0.40 (53/turn) | casks 11 (7.25->9.88), windows 2 (850.5->855), dyed yarn 1 (4.91->6.7) | cured fish 4 (28.35->36.48), cloth 24 (12.18->13.5), wrought iron 6 (12.5->16.25), cured meat 3 (21->26.4) | +142 |
| Heidlowe | 662 | 0.23 | 0.20 (26/turn) | thread 92 (6.95->7.65), nets 2 (42.4->45.03), wool 3 (11.76->12.35) | cloth 24 (11.45->13.5), cured fish 4 (33.18->36.48), dyed cloth 3 (13.76->17.1), flax fibres 16 (5.83->6.8) | +138 |
| Clairlond | 1288 | 0.62 | 0.20 (26/turn) | garments 10 (32.2->39.71), paper 4 (26.46->28.5), yarn 2 (8.51->11.4), axes 1 (16.7->17.57) | cured fish 4 (27.3->36.48), fleece 4 (6.83->12.44), cloth 4 (11.97->13.5), dyed cloth 3 (16.38->17.1) | +135 |

**Best:** Fontaux at about +160 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 39.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 12 @ 4.64, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 81 = 7.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 17.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 31.4) |
| grain | 7 @ 3.7, stop 26 |  | goal planner: buys 7 a turn for today's rates, keeps up to 26 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 16) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 41.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.0k (cash + stock at home prices); +70/turn over 6 turns, -22/turn over 24 turns.
- Limits: cash flow >= -291/turn, prestige >= -1.34/turn (values are after 200 tax a turn).
- Today's settings: value -158/turn, cash -169/turn, prestige +1.09/turn.
- Plan: value +53/turn, cash +56/turn, prestige -1.34/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +153 vs -164, +137 vs -168, -142 vs -167.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +24/turn
  - ship Flax Wyrm -> Blanans: +3/turn
  - mansion 1 1.00 -> 0.42: +156/turn
  - ropewalk 1 0.25 -> 0.11: +12/turn
  - spinnery 1 1.65 -> 1.27: +15/turn
  - net maker 0.00 -> 0.29: +4/turn
  - retting pit 1 0.91 -> 0.81: +3/turn
  - flax farm 1 4.64 -> 4.05: +7/turn
- Model check over the last 59 turns: predicted -75/turn for the settings we ran, real +32/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.67, beer 3.55, timber 3.83, prestige 65.23, cash 0.00
- Orders it would set: bread buy 5 (v2 8); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 7 (v2 18); labour buy 64 (v2 16); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Amsdermund (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 422 (+133 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.29 |
| ret | 3 | 0.91 | 0.86 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 111/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
