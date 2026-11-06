# v2 shadow report

Turn 13825, 2026-11-06 10:26. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,431, prestige 3,282 (162 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 6 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 12.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 519, not 619

## Prestige spending, cheapest coin per prestige first

576 turns left: prestige gained now converts 94.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.3 | 54.3 | thin at home: stockfish, candles |
| jousting 3 | arena | 230 | 54.3 | 54.5 | needs a arena (build cost 25,813); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 57.5 | 57.5 | thin at home: ham, stockfish, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 57.8 | 57.8 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.7 | 58.7 | thin at home: stockfish, candles |
| hold banquet 3 (pies) | mansion | 8 | 59.3 | 59.3 | thin at home: pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 59.5 | 59.5 |  |
| jousting 2 | arena | 210 | 59.4 | 59.7 | needs a arena (build cost 25,813); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 60.1 | 60.1 | thin at home: pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 60.7 | 60.7 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 13 @ 15.4; crew 0.1; est +35 a turn; stock: pasties 13 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.0 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Orlesailles +51, Angefont +44, Donaunieder +40, Grandgues +35, Herschweig +30
- Orlesailles would trade: pasties buy 14 @ 13.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bordetes | 831 | 0.24 | 0.20 (21/turn) | cured fish 5 (22.68->32.68), tapestries 1 (645.75->665), ham 1 (85.58->103.55), furniture 13 (14.18->15.96) | jewellery 4 (73.5->77.42), cheese 4 (6.2->8.31), cloth 13 (7.93->8.55), casks 1 (5.99->6.65) | +122 |
| Neuborn | 780 | 0.21 | 0.40 (41/turn) | charcoal 20 (2.58->7.22), honey 3 (7.88->10.92), mouldboards 1 (38.01->41.61), wool 2 (9.19->10.54) | cloth 15 (6.41->8.55), jewellery 4 (74.03->77.42), flax fibres 21 (5.3->5.9), flax plants 4 (1.34->2.04) | +119 |
| Blanans | 297 | 0.08 | 0.40 (41/turn) | charcoal 20 (2.58->4.75), ham 1 (85.58->114), limestone 4 (17.64->23.75), medicine 1 (162.75->168.15) | cloth 15 (7.35->8.55), jewellery 4 (73.5->77.42), cheese 4 (6.56->8.31), flax plants 10 (1.4->2.04) | +118 |
| Grandgues | 152 | 0.04 | 0.10 (10/turn) | looms 1 (614.25->684), bellows 1 (245.7->266), firewood 1 (2.34->6.93), lead bars 6 (17.54->18.05) | casks 1 (5.93->6.65), cheese 4 (8.14->8.31), varnish 1 (14.8->15.58), cloth 3 (8.51->8.55) | +96 |
| Hofkirchen | 991 | 0.33 | 0.70 (72/turn) | tapestries 1 (645.75->669.75), yarn 7 (4.26->5.7), nets 5 (34.6->36.29), glass ingots 1 (66.67->68.4) | cloth 17 (7.25->8.55), thread 46 (4.35->5.05), jewellery 7 (75.6->77.42), cheese 4 (5.78->8.31) | +94 |

**Best:** Bordetes at about +122 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.6) |
| grain | 11 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 33 = 3.6 turns |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 19) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.5k (cash + stock at home prices); +141/turn over 6 turns, +160/turn over 24 turns.
- Limits: cash flow >= -268/turn, prestige >= +5.73/turn (values are after 200 tax a turn).
- Today's settings: value +97/turn, cash +89/turn, prestige -0.82/turn - breaks the prestige floor.
- Plan: value -122/turn, cash -33/turn, prestige +3.38/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -325 vs +96, +132 vs +85, -239 vs +87 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Fontaux: +4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - brewery 1 0.14 -> 0.00: -6/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.13: +11/turn
  - sewing shop 1 0.30 -> 0.36: -8/turn
  - weavery 1 0.50 -> 0.61: +10/turn
  - ropewalk 1 0.25 -> 0.00: -11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.24: +14/turn
  - spinnery 1 1.65 -> 1.10: -17/turn
- Model check over the last 62 turns: predicted +99/turn for the settings we ran, real +66/turn.
- Worth of one more unit per turn: labour 1.64, thread 4.12, cloth 6.58, flax fibres 4.88, garments 19.04, nets 29.56, beer 3.34, timber 3.26, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 19); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.13, worth +15/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.24, worth +13/turn.
- Ship linen snake: Grandgues -> Fontaux (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 459 (+170 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.42 |
| ret | 3 | 0.91 | 1.08 |
| spin | 4 | 1.65 | 1.91 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 446/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.9 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
