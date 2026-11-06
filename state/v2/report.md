# v2 shadow report

Turn 13828, 2026-11-06 13:43. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,474, prestige 3,280 (160 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 2 | 0 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 8 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +0 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 518, not 601

## Prestige spending, cheapest coin per prestige first

573 turns left: prestige gained now converts 94.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| jousting 3 | arena | 230 | 54.0 | 54.3 | needs a arena (build cost 26,772); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.0 | 55.0 | thin at home: hop beer, wine, ham, stockfish, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 56.3 | 56.3 |  |
| hold banquet 4 | mansion | 17.5 | 58.4 | 58.4 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 59.0 | 59.0 | thin at home: hop beer, wine, ham, stockfish, premium cheese |
| hold banquet 2 (pies) | mansion | 7 | 59.4 | 59.4 | thin at home: wine, pies |
| jousting 2 | arena | 210 | 59.2 | 59.4 | needs a arena (build cost 26,772); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 59.6 | 59.6 |  |
| hold banquet 3 (pies) | mansion | 8 | 59.9 | 59.9 | thin at home: hop beer, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 60.4 | 60.4 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 62.6 | 62.6 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 14.0 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 15.7 (keep 14); best orders clear only 12 a turn after crew: ship stays at 0
- best towns now: Orlesailles +53, Donaunieder +41, Toqueque +38, Bordees +36, Fulkirch +34
- Orlesailles would trade: pasties buy 14 @ 13.6; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.33 | 0.50 (52/turn) | nets 6 (33.8->36.29), yarn 14 (4.83->5.7), glass ingots 1 (64.05->68.4), mouldboards 1 (38.01->38.95) | tapestries 2 (745.5->798), cloth 23 (7.25->8.3), jewellery 5 (72.98->76.47), thread 38 (4.3->5) | +192 |
| Friedwerp | 684 | 0.19 | 0.20 (21/turn) | nets 4 (33.8->35.72), yarn 14 (4.83->5.22), cloth 1 (7.2->7.41) | tapestries 1 (635.25->798), cheese 4 (5.78->8.31), blades 1 (11.34->12.16), candles 1 (81.9->83.5) | +177 |
| Herschweig | 775 | 0.22 | 0.10 (10/turn) | wine 5 (6.46->6.7) | tapestries 1 (640.5->798), cheese 4 (5.78->8.31), jewellery 2 (72.98->76.47), candles 1 (79.8->83.5) | +174 |
| Rouhomme | 368 | 0.10 | 0.10 (10/turn) | hop beer 1 (11.23->15.2), yarn 14 (4.83->5.22), premium ham 1 (252->254.6), grain 2 (2.54->3.19) | tapestries 2 (735->798), flax fibres 10 (4.94->6), cheese 4 (6.46->8.31), cloth 10 (7.61->8.3) | +162 |
| Amsdermund | 1111 | 0.40 | 0.40 (42/turn) | limestone 2 (18.69->41.04), cured fish 5 (22.68->24.89), yarn 14 (4.83->5.7) | tapestries 2 (745.5->798), cheese 4 (6.35->8.31), candles 1 (78.23->83.5), cloth 9 (7.35->8.3) | +156 |

**Best:** Hofkirchen at about +192 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 90.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.0k (cash + stock at home prices); +113/turn over 6 turns, +167/turn over 24 turns.
- Limits: cash flow >= -270/turn, prestige >= +5.83/turn (values are after 200 tax a turn).
- Today's settings: value +64/turn, cash +50/turn, prestige -0.80/turn - breaks the prestige floor.
- Plan: value -155/turn, cash -55/turn, prestige +3.40/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +37 vs +89, +252 vs +67, -246 vs +60.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +5/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: -15/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.19: +23/turn
  - brewery 1 0.14 -> 0.27: -23/turn
  - spinnery 1 1.65 -> 0.89: -28/turn
  - retting pit 1 0.91 -> 0.50: -7/turn
  - flax farm 1 4.64 -> 2.55: -25/turn
  - mansion 1 0.00 -> 1.00: -163/turn
- Model check over the last 62 turns: predicted +99/turn for the settings we ran, real +64/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 30.10, beer 3.06, timber 3.46, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 18); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.19, worth +10/turn.
- Ship linen snake: Grandgues -> Vauxvais (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 452 (+163 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.27 |
| ret | 3 | 0.91 | 1.05 |
| spin | 4 | 1.65 | 1.86 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 480/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 2.3 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 4 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.0 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
