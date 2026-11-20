# v2 shadow report

Turn 14172, 2026-11-20 21:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,983, prestige 3,739 (619 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 116 | 39 | 12 | 0 | 0 | sell 17, sell @ 4.44; stop 116, buy 39, buy @ 4.68 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 7 | 6 | 6 | 3 | 0 | stop 26, buy 7, buy @ 3.7 |
| labour | 64 | 64 | 513 | 0 | 51 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**7 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: home ask 2.68 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **grain**: brewery 1 ran short of grain (buy is live (7 @ 3.7), but the home ask 3.76 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **grain**: home ask 3.76 is above our ceiling 3.70 and last turn bought 6 of ~9 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **grain**: only 0.8 turns of grain left and buying 7 (need 18) -> v2: buy 18
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 51 labour expired last turn (~106 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 12.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 97 over real use lately; planning 519, not 616
- labour expiry guard: 51 bought labour expired last turn, buy 14 (not 19) this turn

## Prestige spending, cheapest coin per prestige first

229 turns left: prestige gained now converts 68.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.9 | 51.6 | needs a arena (build cost 29,104); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 55.7 | 56.5 | needs a arena (build cost 29,104); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.1 | 58.1 | thin at home: stockfish |
| hold banquet 4 (premium) | mansion | 20 | 60.7 | 60.7 | thin at home: stockfish |
| hold banquet 2 (pies) | mansion | 7 | 61.3 | 61.3 |  |
| hold banquet 3 (pies) | mansion | 8 | 61.5 | 61.5 |  |
| hold banquet 4 | mansion | 17.5 | 61.6 | 61.6 | thin at home: ham, stockfish |
| maintain 1 | park | 0.5 | 62.4 | 62.4 | running |
| hold mass 2 (premium) | cathedral | 360 | 55.0 | 62.8 | needs a cathedral (build cost 306,100); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 2 (meat) | mansion | 6.8 | 67.2 | 67.2 | thin at home: cured meat |
| hold banquet 1 (meat) | mansion | 4.2 | 68.6 | 68.6 | running |
| hold banquet 3 (meat) | mansion | 7.6 | 68.6 | 68.6 | thin at home: cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 10 @ 5.0, cured meat buy 3 @ 24.6, pasties buy 13 @ 16.0; crew 0.1; est +36 a turn; stock: pasties 13 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- best towns now: Angefont +235, Clairlond +226, Blanans +223, Dortgart +200, Brunnham +189
- Angefont would trade: furniture buy 19 @ 14.2, pasties buy 11 @ 16.2; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~133 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.48 | 0.30 (40/turn) | swords 1 (237.3->326.8), casks 13 (7.4->9.36), steel ingots 4 (19.43->20.33), cloth 1 (12.2->13.96) | garments 2 (24.15->33.6), cookware 4 (18.9->21.66), cured meat 3 (22.26->26.2), flax fibres 18 (5.62->7) | +173 |
| Grandgues | 152 | 0.05 | 0.50 (67/turn) | firewood 29 (2.81->5.7), charcoal 19 (2.35->4.54), dyed cloth 8 (19.53->22.23), thread 92 (6.85->7.03) | cloth 6 (11.55->13.3), candles 1 (74.03->82), fleece 3 (10.92->13.11), garments 2 (31.5->33.6) | +166 |
| Heidlowe | 662 | 0.24 | 0.20 (27/turn) | thread 35 (6.85->9.26), nets 2 (42.4->43.13), wax 1 (27.72->28.88) | cloth 24 (11.45->13.3), flax fibres 23 (5.72->7), dyed cloth 3 (13.55->16.91), garments 2 (30.87->33.6) | +166 |
| Caillechâtel | 488 | 0.17 | 0.10 (13/turn) | - | cloth 20 (8.35->13.3), thread 19 (5.88->7), fleece 4 (10.5->13.11), candles 1 (73.5->82) | +132 |
| Großaue | 1136 | 0.53 | 0.20 (27/turn) | yarn 9 (8.29->9.79) | cloth 24 (8.66->13.3), garments 2 (28.35->33.6), fleece 2 (10.82->13.11), cheese 6 (6.09->6.7) | +117 |

**Best:** Kirchwerp at about +173 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 38.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 17.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 32.4) |
| grain | 18 @ 3.7, stop 36 |  | uses 9.0/turn (observed), makes 0.0, holds 7 = 0.8 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 14) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 41.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.9k (cash + stock at home prices); +46/turn over 6 turns, -38/turn over 24 turns.
- Limits: cash flow >= -291/turn, prestige >= -1.33/turn (values are after 200 tax a turn).
- Today's settings: value -166/turn, cash -173/turn, prestige +1.10/turn.
- Plan: value +46/turn, cash +67/turn, prestige -1.33/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +137 vs -168, -142 vs -167, +1 vs -169.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Kirchwerp: +16/turn
  - mansion 1 1.00 -> 0.42: +154/turn
  - brewery 1 0.14 -> 0.06: +13/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +1/turn
  - spinnery 1 1.65 -> 1.29: +22/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.13: +4/turn
  - retting pit 1 0.91 -> 0.81: +3/turn
  - flax farm 1 4.64 -> 4.09: +7/turn
- Model check over the last 59 turns: predicted -79/turn for the settings we ran, real +26/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.72, beer 3.57, timber 3.80, prestige 65.24, cash 0.00
- Orders it would set: bread buy 5 (v2 7); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 14); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.13, worth +2/turn.
- Ship linen snake: Grandgues -> Kirchwerp (+1/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +7/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 421 (+132 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.26 |
| ret | 3 | 0.91 | 0.85 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 112/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
