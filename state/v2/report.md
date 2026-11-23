# v2 shadow report

Turn 14245, 2026-11-23 22:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,275, prestige 3,690 (570 free, +1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 52 | 0 | 19 | 0 | 0 | none |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 10 | 4 | 3 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 6 | 5 | 5 | 4 | 0 | stop 24, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 542 | 0 | 22 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **grain**: brewery 1 ran short of grain (buy is live (6 @ 3.7), 5 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.7 turns of grain left and buying 6 (need 18) -> v2: buy 18

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~36 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 30.80 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 54.3 coin per prestige at mansion, vs 65.3 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 106 over real use lately; planning 552, not 658

## Prestige spending, cheapest coin per prestige first

156 turns left: prestige gained now converts 54.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 48.0 | 49.1 | needs a arena (build cost 26,313); thin at home: swords, protection, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 3 (premium) | arena | 420 | 49.6 | 50.2 | needs a arena (build cost 26,313); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 52.6 | 53.7 | needs a arena (build cost 26,313); thin at home: swords, protection, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.2 | 53.8 | needs a arena (build cost 26,313); thin at home: protection, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 54.3 | 54.3 |  |
| maintain 2 | park | 2 | 55.7 | 55.7 | thin at home: sculptures |
| hold banquet 2 (fish) | mansion | 6.8 | 57.2 | 57.2 |  |
| hold banquet 5 | mansion | 22 | 59.7 | 59.7 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 2 (pies) | mansion | 7 | 59.8 | 59.8 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 62.1 | 62.1 | thin at home: hop beer, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 65.3 | 65.3 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 4 @ 4.9, cured meat buy 6 @ 24.4; crew 0.1; est +33 a turn
- **Flax Wyrm** on Caillechâtel: cured meat buy 6 @ 28.8, pasties buy 5 @ 13.5; crew 0.1; est +27 a turn; stock: pasties 5 @ 13.5 (keep 14)
- best towns now: Hofkirchen +70, Donaunieder +51, Vauxvais +44, Coburgbaum +41, Birkeningen +38
- Hofkirchen would trade: cured meat buy 6 @ 21.2, pasties buy 5 @ 14.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Angefont | 686 | 0.19 | 0.50 (52/turn) | nets 6 (15.56->38), garments 10 (26.2->33.25), tools 20 (6.62->7.6), charcoal 19 (2.14->4.39) | thread 62 (5.25->6.05), flax fibres 24 (5.25->6.3), cured meat 6 (29.4->30.8), cheese 19 (6.3->6.7) | +313 |
| Pontmont | 341 | 0.10 | 0.70 (73/turn) | timber 39 (8.03->12.82), nets 2 (15.56->39.14), tiles 9 (3.3->7.31), nails 10 (8.09->9.5) | bricks 13 (7.04->10.07), thread 37 (5.57->6.05), flax fibres 2 (5.78->6.3), wool 13 (11.13->11.3) | +277 |
| Bremcop | 1326 | 0.52 | 0.30 (31/turn) | garments 10 (26.2->38.38), nets 4 (15.56->40.85), axes 2 (14.91->16.91), lead bars 4 (10.45->11.4) | cured meat 6 (26.67->30.8), paper 4 (25.2->28.12), wool 12 (10.34->11.3), thread 22 (5.41->6.05) | +258 |
| Heilegg | 826 | 0.24 | 1.00 (104/turn) | dyed cloth 8 (19.01->27.36), nets 2 (15.56->39.33), grain 56 (2.96->4.31), casks 3 (6.83->11.3) | cured meat 2 (28.35->30.8), wool 5 (10.29->11.3), paper 1 (26.67->28.12), tools 6 (5.25->5.7) | +250 |
| Rouhomme | 368 | 0.10 | 0.50 (52/turn) | nets 5 (15.56->36.29), garments 10 (26.2->28.31), wine 21 (6.35->7.03), axes 3 (14.91->17.86) | bricks 20 (5.46->10.07), tools 18 (4.73->5.7), cookware 7 (24.99->26.79), paper 4 (26.88->28.12) | +241 |

**Best:** Angefont at about +313 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 32 @ 3.16, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 52 = 2.7 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 12 = 2.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.6) |
| grain | 7 @ 3.7, stop 26 |  | goal planner: buys 7 a turn for today's rates, keeps up to 26 (v2 had 18) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 52) |
| light armour | 1 @ 93.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 82.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.2k (cash + stock at home prices); -78/turn over 6 turns, -23/turn over 24 turns.
- Limits: cash flow >= -386/turn, prestige >= -1.12/turn (values are after 200 tax a turn).
- Today's settings: value -134/turn, cash -132/turn, prestige +1.36/turn.
- Plan: value +29/turn, cash +32/turn, prestige -1.12/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -68 vs -120, -77 vs -124, +40 vs -117.
- Route sales counted at most (what the ships really sold, a turn): beer 2.0, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: -4/turn
  - ship Flax Wyrm -> Grandgues: +21/turn
  - mansion 1 1.00 -> 0.41: +146/turn
  - spinnery 1 1.65 -> 1.45: +0/turn
  - retting pit 1 0.91 -> 0.85: +1/turn
  - flax farm 1 4.64 -> 4.26: +3/turn
  - sewing shop 1 0.30 -> 0.36: -6/turn
  - weavery 1 0.50 -> 0.60: +11/turn
- Model check over the last 59 turns: predicted -156/turn for the settings we ran, real +38/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.67, thread 4.20, cloth 6.70, flax fibres 4.97, garments 19.39, nets 16.78, beer 2.98, timber 3.42, prestige 61.11, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 6); garments sell 11 (v2 10); grain buy 7 (v2 18); labour buy 65 (v2 52); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Calange (+13/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R7 stale ask: light armour ask 94 over the market for 3 turns: the town trades ~3 a turn at 86.5, we sold 0 with 4 over what we keep -> **sell price 94 -> 93 (last trade 86.5, floor 92.56)** (ok)
