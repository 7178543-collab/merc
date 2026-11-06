# v2 shadow report

Turn 13833, 2026-11-06 18:20. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,909, prestige 3,399 (279 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 40 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 500 | 0 | 29 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~48 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 501, not 601

## Prestige spending, cheapest coin per prestige first

568 turns left: prestige gained now converts 94.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 54.1 | 54.1 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.6 | 54.6 | thin at home: hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 55.1 | 55.3 | needs a arena (build cost 26,155); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 56.4 | 56.4 |  |
| hold banquet 4 | mansion | 17.5 | 57.3 | 57.3 | thin at home: hop beer, ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 57.4 | 57.4 | thin at home: pies |
| hold banquet 1 (meat) | mansion | 4.2 | 57.5 | 57.5 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 57.6 | 57.6 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 58.8 | 58.8 | thin at home: hop beer, ham, stockfish, premium cheese |
| hold banquet 3 (pies) | mansion | 8 | 59.3 | 59.3 | thin at home: hop beer, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 13 @ 15.8; crew 0.1; est +29 a turn; stock: pasties 13 @ 15.8 (keep 14)
- **Flax Wyrm** on Caillechâtel: pasties buy 8 @ 15.6; crew 0.1; est +16 a turn; stock: pasties 8 @ 15.6 (keep 14)
- best towns now: Rouhomme +65, Orlesailles +50, Toqueque +38, Bedenis +36, Bordees +36
- Rouhomme would trade: pasties buy 14 @ 13.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.25 | 0.20 (22/turn) | nets 6 (15.24->35.53), wine 16 (6.14->7.27), yarn 11 (4.98->6.08), lead bars 8 (18.69->19.95) | dyed cloth 24 (10.5->18.14), cloth 24 (7.19->13.3), garments 2 (25.2->31.4), gears 1 (65.1->70.77) | +496 |
| Rotterburg | 1056 | 0.38 | 0.20 (22/turn) | nets 2 (15.24->32.87), hides 1 (11.03->13.39) | cloth 24 (7.19->13.3), dyed cloth 24 (13.55->18.14), garments 2 (23.94->31.4), candles 1 (76.12->83.5) | +303 |
| Amsdermund | 1111 | 0.41 | 0.70 (76/turn) | nets 3 (15.24->32.68), wine 16 (6.14->6.74), charcoal 19 (3.21->6.65) | dyed cloth 21 (10.61->18.14), cloth 11 (7.35->13.3), garments 2 (26.67->31.4), cookware 5 (23.31->25.27) | +289 |
| Fulkirch | 1576 | 0.68 | 0.30 (33/turn) | nets 6 (15.24->36.67), yarn 11 (4.98->6.08), wine 16 (6.14->6.93), lead bars 2 (18.69->19.95) | cloth 24 (8.19->13.3), dyed cloth 6 (15.54->18.14), gears 1 (66.67->70.77) | +249 |
| Fontaux | 411 | 0.12 | 0.70 (76/turn) | nets 3 (15.24->33.25), timber 27 (7.88->11.59), charcoal 17 (3.21->5.65), garments 10 (28.2->30.4) | cloth 8 (9.5->13.3), dyed cloth 6 (13.97->18.14), flax fibres 10 (4.94->6.15), mouldboards 1 (41.16->44.46) | +245 |

**Best:** Heilegg at about +496 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 a turn at 3.06, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 27.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 1) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.2k (cash + stock at home prices); -375/turn over 6 turns, +15/turn over 24 turns.
- Limits: cash flow >= -246/turn, prestige >= +0.88/turn (values are after 200 tax a turn).
- Today's settings: value +86/turn, cash +80/turn, prestige -1.60/turn - breaks the prestige floor.
- Plan: value -26/turn, cash +89/turn, prestige +0.88/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -292 vs +77, +116 vs +72, +127 vs +81.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +3/turn
  - ship Flax Wyrm -> Karlmoor: +6/turn
  - ropewalk 1 0.25 -> 0.00: -3/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.09: +13/turn
  - weavery 1 0.50 -> 0.60: +1/turn
  - sewing shop 1 0.30 -> 0.36: +8/turn
  - brewery 1 0.14 -> 0.21: -12/turn
  - spinnery 1 1.65 -> 1.05: -12/turn
  - retting pit 1 0.91 -> 0.59: +2/turn
  - flax farm 1 4.64 -> 3.13: -15/turn
- Model check over the last 62 turns: predicted +98/turn for the settings we ran, real +38/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 3.96, cloth 6.33, flax fibres 4.69, garments 18.30, nets 15.84, beer 2.84, timber 3.26, prestige 55.55, cash 0.00
- Orders it would set: beer sell 16 (v2 none); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 1); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.09, worth +4/turn.
- Ship linen snake: Grandgues -> Vauxvais (+13/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Karlmoor (+6/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 440 (+151 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.00 |
| ret | 3 | 0.91 | 1.00 |
| spin | 4 | 1.65 | 1.76 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 536/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.15 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
