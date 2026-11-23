# v2 shadow report

Turn 14246, 2026-11-23 23:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,907, prestige 3,691 (571 free, +1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 42 | 0 | 19 | 0 | 0 | none |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 11 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 7 | 6 | 6 | 3 | 0 | stop 26, buy 7, buy @ 3.7 |
| labour | 65 | 64 | 564 | 4 | 0 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **grain**: brewery 1 ran short of grain (buy is live (7 @ 3.7), 6 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.8 turns of grain left and buying 7 (need 18) -> v2: buy 18

## Tuning

- **cured meat**: home ask 29.80 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 53.2 coin per prestige at mansion, vs 67.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 55.8 coin per prestige at mansion, vs 67.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 109 over real use lately; planning 568, not 652

## Prestige spending, cheapest coin per prestige first

155 turns left: prestige gained now converts 54.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 47.1 | 48.2 | needs a arena (build cost 26,485); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| jousting 3 (premium) | arena | 420 | 49.1 | 49.7 | needs a arena (build cost 26,485); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| jousting 2 | arena | 210 | 51.6 | 52.8 | needs a arena (build cost 26,485); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 53.2 | 53.2 |  |
| jousting 2 (premium) | arena | 400 | 52.6 | 53.3 | needs a arena (build cost 26,485); thin at home: protection, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 55.8 | 55.8 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.4 | 59.4 |  |
| hold banquet 4 (pies) | mansion | 18 | 62.4 | 62.4 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 63.5 | 63.5 | thin at home: hop beer, stockfish, sculptures |
| jousting 1 | arena | 170 | 63.9 | 65.3 | needs a arena (build cost 26,485); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 65.9 | 65.9 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0 | - | cured meat 5, pasties 1 | -158 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | beer 4 | cured meat 6 | -127 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 3 @ 5.15, cured meat buy 6 @ 24.4; crew 0.1; est +28 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 13.8 (keep 14); best orders clear only 15 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +65, Donaunieder +45, Coburgbaum +39, Dortgart +36, Gotthafen +35
- Hofkirchen would trade: cured meat buy 6 @ 21.0, pasties buy 5 @ 14.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.22 | 0.20 (21/turn) | nets 6 (15.52->37.24), garments 10 (26.8->29.26), dyed cloth 7 (19.01->20.9), wine 23 (6.35->6.6) | sculptures 1 (2373->2603), cured meat 3 (26.67->29.8), thread 10 (5.57->6.05), flax fibres 3 (5.78->6.55) | +400 |
| Bremcop | 1326 | 0.52 | 0.20 (21/turn) | nets 6 (15.52->42.56), garments 10 (26.8->41.23), axes 2 (15.65->16.91), honey 1 (8.87->9.5) | cured meat 6 (26.46->29.8), paper 6 (21.84->24.32), wax 3 (25.83->28.12), wool 11 (10.29->11.3) | +332 |
| Vauxvais | 204 | 0.06 | 0.50 (53/turn) | bread 178 (2.35->3.13), nets 5 (15.52->36.48), grain 95 (2.94->3.74), beer 3 (3.02->3.38) | cured meat 4 (26.67->29.8), bricks 5 (7.14->10.07), tools 18 (5.46->5.89), flax fibres 6 (5.78->6.55) | +317 |
| Bedenis | 566 | 0.16 | 0.40 (42/turn) | nets 6 (15.52->40.09), cloth 14 (9.45->17.1), axes 4 (15.65->17.67), garments 10 (26.8->27.36) | bricks 9 (5.3->10.07), thread 18 (5.57->6.05), wine 21 (5.25->5.7), casks 4 (4.68->5.84) | +301 |
| Angefont | 686 | 0.19 | 0.30 (32/turn) | nets 6 (15.52->38), garments 10 (26.8->33.63), ploughs 2 (77.17->83.6), cloth 14 (9.45->10.07) | thread 55 (5.25->6.05), flax fibres 28 (5.25->6.55), cheese 7 (5.78->6.41), premium cheese 1 (31.5->34.39) | +291 |

**Best:** Etallaen at about +400 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 37 @ 3.18, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 42 = 2.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 10 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 17 = 2.8 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.0) |
| grain | 7 @ 3.7, stop 25 |  | goal planner: buys 7 a turn for today's rates, keeps up to 25 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 68) |
| light armour | 1 @ 92.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 82.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.3k (cash + stock at home prices); -50/turn over 6 turns, -31/turn over 24 turns.
- Limits: cash flow >= -371/turn, prestige >= -1.13/turn (values are after 200 tax a turn).
- Today's settings: value -131/turn, cash -126/turn, prestige +1.35/turn.
- Plan: value +33/turn, cash +37/turn, prestige -1.13/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -77 vs -124, +40 vs -117, -369 vs -132.
- Route sales counted at most (what the ships really sold, a turn): beer 2.0, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: +4/turn
  - ship Flax Wyrm -> Grandgues: +18/turn
  - mansion 1 1.00 -> 0.41: +143/turn
  - spinnery 1 1.65 -> 1.47: +1/turn
  - flax farm 1 4.64 -> 2.47: -4/turn
  - sewing shop 1 0.30 -> 0.36: -6/turn
  - weavery 1 0.50 -> 0.60: +11/turn
- Model check over the last 59 turns: predicted -156/turn for the settings we ran, real +28/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.69, thread 4.25, cloth 6.78, flax fibres 5.03, garments 19.62, nets 16.98, beer 2.99, timber 3.31, prestige 61.31, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 6); garments sell 11 (v2 10); grain buy 7 (v2 18); labour buy 64 (v2 68); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Calange (+19/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+4/turn over staying).
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

Buffers: flax fibres 84/77, thread 1058/228, cloth 72/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1058 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R7 stale ask: light armour ask 93 over the market for 4 turns: the town trades ~3 a turn at 85.75, we sold 0 with 5 over what we keep (held back: acted on light armour at turn 14245 (one action per 2 turns))
