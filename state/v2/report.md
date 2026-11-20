# v2 shadow report

Turn 14164, 2026-11-20 13:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,778, prestige 3,742 (622 free, -0.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 14 | 5 | 0 | stop 60, buy 30, buy @ 4.78 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 3 | 3 | 3 | 1 | 0 | stop 11, buy 3, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 32 | 0 | 2 | 0 | 0 | stop 22, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 510 | 0 | 54 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (3 @ 2.4), 3 bought last turn); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: only 0.8 turns of firewood left and buying 3 (need 8) -> v2: buy 8
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.90 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 54 labour expired last turn (~116 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.78 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **grain**: home ask 3.72 is above our ceiling 3.70 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.90 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +0 crew for Flax Wyrm (crew 0.01, no projection from the game)
- labour: +0 crew for linen snake (crew 0.00, no projection from the game)
- labour: projection runs 119 over real use lately; planning 510, not 596

## Prestige spending, cheapest coin per prestige first

237 turns left: prestige gained now converts 69.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 51.1 | 51.5 | needs a arena (build cost 30,007); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.9 | 53.5 | needs a arena (build cost 30,007); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 55.0 | 55.3 | needs a arena (build cost 30,007); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 57.9 | 57.9 | thin at home: cheese, candles |
| hold banquet 4 (pies) | mansion | 18 | 58.4 | 58.4 | thin at home: stockfish, candles |
| jousting 2 | arena | 210 | 57.9 | 58.6 | needs a arena (build cost 30,007); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 59.5 | 59.5 | thin at home: cheese, candles |
| hold banquet 4 (premium) | mansion | 20 | 61.1 | 61.1 | thin at home: stockfish, candles |
| hold banquet 3 (meat) | mansion | 7.6 | 61.8 | 61.8 | thin at home: cured meat, cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 62.3 | 62.3 | thin at home: cured meat, cheese |
| hold banquet 4 | mansion | 17.5 | 62.3 | 62.3 | thin at home: stockfish, cheese, candles |
| hold mass 2 (premium) | cathedral | 360 | 55.3 | 62.7 | needs a cathedral (build cost 313,240); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: candles buy 2 @ 77.0, furniture buy 20 @ 14.2, pasties buy 1 @ 15.0; crew 0.2; est +246 a turn; stock: candles 2 @ 77.0 (keep 12); stock: furniture 20 @ 14.2 (keep 145); stock: pasties 1 @ 15.0 (keep 14)
- **linen snake** on Grandgues: candles buy 2 @ 74.0, cured meat buy 4 @ 22.2, pasties buy 5 @ 16.0; crew 0.1; est +38 a turn; stock: candles 2 @ 74.0 (keep 12); stock: pasties 5 @ 16.0 (keep 14)
- best towns now: Chatgnan +268, Angefont +254, Caillechâtel +246, Clairlond +213, Gotthafen +209
- Chatgnan would trade: candles buy 2 @ 73.5, furniture buy 18 @ 13.2, pasties buy 5 @ 14.0; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~136 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.06 | 1.00 (136/turn) | beer 109 (5.51->7.98), firewood 44 (2.35->5.7), tackles 1 (182.7->201.4), bread 242 (2.92->3.1) | cured fish 5 (26.25->33.44), garments 2 (29.4->33.6), yarn 11 (8.14->8.79), cured meat 4 (23.1->23.6) | +406 |
| Bordetes | 831 | 0.31 | 0.60 (82/turn) | beer 109 (5.51->7.98), salt 11 (5.62->7.12), hides 2 (14.28->17.95), flax fibres 4 (6.8->7.55) | cured fish 5 (25.83->33.44), wrought iron 4 (15.65->16.81) | +258 |
| Rouhomme | 368 | 0.13 | 0.30 (41/turn) | beer 109 (5.51->7.69), lathes 1 (181.65->197.6), raw cloth 2 (11.34->13.59) | tools 23 (6.3->6.98), yarn 8 (7.56->8.79), garments 2 (31.71->33.6), wrought iron 4 (15.65->16.81) | +258 |
| Heilegg | 826 | 0.31 | 0.60 (82/turn) | beer 109 (5.51->7.36), casks 18 (7.4->8.36), malt 3 (7.61->9.21), wool 2 (12.92->14.91) | cured fish 5 (26.46->33.44), yarn 26 (7.98->8.79), cookware 4 (20.79->23.56), garments 2 (29.4->33.6) | +222 |
| Herschweig | 775 | 0.28 | 0.40 (55/turn) | beer 65 (5.51->6.51), thread 20 (7->7.79), nets 1 (40.8->43.89), cheese 3 (6.04->6.65) | yarn 26 (6.67->8.79), cured fish 5 (24.57->33.44), cloth 24 (11.65->13.2), dyed cloth 5 (17.12->18.71) | +181 |

**Best:** Grandgues at about +406 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 39 @ 5.5, stop 77 |  | uses 19.2/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 7 @ 29.0, stop 17 |  | uses 4.0/turn (observed), makes 0.0, holds 12 = 3.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 32.4) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 2) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 10) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 39.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.4k (cash + stock at home prices); -589/turn over 6 turns, -39/turn over 24 turns.
- Limits: cash flow >= -282/turn, prestige >= -1.34/turn (values are after 200 tax a turn).
- Today's settings: value -135/turn, cash -147/turn, prestige +1.09/turn.
- Plan: value +74/turn, cash +85/turn, prestige -1.34/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -374 vs -155, +353 vs -129, +27 vs -125.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +8/turn
  - ship Flax Wyrm -> Clairas: +2/turn
  - mansion 1 1.00 -> 0.42: +145/turn
  - brewery 1 0.14 -> 0.07: +14/turn
  - ropewalk 1 0.25 -> 0.11: +14/turn
  - spinnery 1 1.65 -> 1.28: +20/turn
  - retting pit 1 0.91 -> 0.81: +3/turn
  - net maker 0.00 -> 0.29: +3/turn
  - flax farm 1 4.64 -> 4.07: +7/turn
- Model check over the last 59 turns: predicted -42/turn for the settings we ran, real +3/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.77, beer 3.53, timber 4.16, prestige 61.31, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 2); labour buy 64 (v2 10); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Hofkirchen (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Clairas (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 425 (+136 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.47 |
| ret | 3 | 0.91 | 0.89 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 98/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 30 @ 4.78, home ask 5.25 -> **buy 39 @ 5.35 (ask 5.25, cap 14.4)** (ok)
- R1: bread slot dry: 4.2 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.78 -> **buy 9 @ 2.84 (ask 2.78, cap 4.3)** (ok)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.9 for 4 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
