# v2 shadow report

Turn 14266, 2026-11-24 19:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,601, prestige 3,717 (597 free, +1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 67 | 19 | 19 | 0 | 0 | sell 3, sell @ 3.32; stop 116, buy 39, buy @ 3.42 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 29, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 564 | 5 | 0 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**0 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Tuning

- **cured meat**: home ask 30.40 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.0 coin per prestige at mansion, vs 70.0 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 57.3 coin per prestige at mansion, vs 70.0 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (pies)**: hold banquet 2 (pies) costs 59.0 coin per prestige at mansion, vs 70.0 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 114 over real use lately; planning 569, not 640

## Prestige spending, cheapest coin per prestige first

135 turns left: prestige gained now converts 49.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 47.3 | 48.1 | needs a arena (build cost 28,529); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 50.8 | 51.6 | needs a arena (build cost 28,529); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.6 | 54.6 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 57.0 | 57.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 57.3 | 57.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.0 | 59.0 |  |
| jousting 3 | arena | 230 | 58.8 | 60.2 | needs a arena (build cost 28,529); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 63.9 | 63.9 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 65.4 | 65.4 | thin at home: hop beer, stockfish, sculptures |
| jousting 2 | arena | 210 | 64.4 | 65.9 | needs a arena (build cost 28,529); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 67.4 | 67.4 |  |
| hold banquet 4 (premium) | mansion | 20 | 67.4 | 67.4 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0 | - | pasties 1 | -15 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 25.4, pasties buy 1 @ 15.5; crew 0.1; est +23 a turn; stock: pasties 1 @ 15.5 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 11.5 (keep 14); best orders clear only 15 a turn after crew: ship stays at 0
- best towns now: Donaunieder +44, Hanbrücken +43, Darmwald +41, Fontaux +40, Bremcop +39
- Donaunieder would trade: cured meat buy 6 @ 22.0, pasties buy 1 @ 14.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.06 | 0.10 (11/turn) | windows 1 (1023.75->1453.5), limestone 4 (21->34.39), varnish 1 (17.12->22.04), beer 5 (3.42->4.16) | cured meat 4 (27.3->30.4), thread 23 (5.62->6.05), dyed cloth 3 (13.02->15.29), tools 17 (5.78->6.22) | +534 |
| Calange | 218 | 0.07 | 0.10 (11/turn) | windows 1 (1023.75->1235), varnish 1 (17.12->25.84), yarn 23 (6.2->6.6), beer 5 (3.42->3.8) | candles 1 (56.7->87.5), thread 30 (5.25->6.05), flax fibres 28 (5.78->6.6), butter 1 (68.78->79.33) | +327 |
| Rouhomme | 368 | 0.11 | 0.20 (23/turn) | windows 1 (1023.75->1235), wine 35 (6.56->7.03), limestone 3 (21->28.12), beer 5 (3.42->4.71) | thread 53 (5.25->6.05), butter 1 (69.3->79.33), tools 17 (5.51->6.22), flax fibres 14 (5.78->6.6) | +321 |
| Heilegg | 826 | 0.26 | 0.40 (46/turn) | dyed cloth 13 (17.32->27.36), nets 6 (35.6->41.8), tackles 1 (154.35->186.2), wine 19 (6.56->7.98) | cured meat 6 (28.56->30.4), fleece 5 (8.87->9.69), slaked lime 1 (9.71->12.92) | +278 |
| Rotterburg | 1056 | 0.40 | 0.20 (23/turn) | tackles 1 (154.35->178.6), yarn 7 (6.2->9.88), wool 4 (11.03->14.15), garments 10 (28.8->30.02) | cloth 24 (6.93->10.4), cured meat 5 (23.31->30.4), thread 12 (4.73->6.05), fleece 2 (7.3->9.69) | +191 |

**Best:** Vauxvais at about +534 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 6 @ min 3.38 | makes 19.3, uses 19.2, holds 67 (keeps 0): sells the surplus + 6/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 89.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 4 = 0.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.96 | goal planner: sells 2 a turn at 0.96, keeps 219 (no one offered it) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 28.0) |
| grain | 8 @ 3.7, stop 31 |  | goal planner: buys 8 a turn for today's rates, keeps up to 31 (v2 had 13) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 69) |
| light armour | 1 @ 99.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.4k (cash + stock at home prices); -8/turn over 6 turns, -47/turn over 24 turns.
- Limits: cash flow >= -317/turn, prestige >= -1.24/turn (values are after 200 tax a turn).
- Today's settings: value -160/turn, cash -156/turn, prestige +1.22/turn.
- Plan: value +18/turn, cash +30/turn, prestige -1.24/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -22 vs -146, -64 vs -148, +124 vs -151.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Fontaux: +17/turn
  - ship Flax Wyrm -> Briclives: +1/turn
  - mansion 1 1.00 -> 0.41: +160/turn
  - net maker 0.00 -> 0.28: +8/turn
  - flax farm 1 4.64 -> 4.01: -1/turn
  - retting pit 1 0.91 -> 0.81: -2/turn
  - spinnery 1 1.65 -> 1.35: +8/turn
  - weavery 1 0.50 -> 0.41: -8/turn
- Model check over the last 59 turns: predicted -148/turn for the settings we ran, real -10/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.89, beer 3.14, timber 3.42, prestige 64.34, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 8 (v2 13); labour buy 64 (v2 69); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Fontaux (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Briclives (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 84/77, thread 1060/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 4.3 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 12 @ 29.8, home ask 30.4 (held back: acted on cured meat at turn 14265 (one action per 2 turns))
- R2: spinnery 1 blocked by thread space: 1060 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
