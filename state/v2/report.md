# v2 shadow report

Turn 14258, 2026-11-24 11:12. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,626, prestige 3,707 (587 free, +1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 58 | 0 | 19 | 0 | 0 | sell 5, sell @ 3.34 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 13 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 31 | 18 | 9 | 0 | 0 | stop 36, buy 14, buy @ 3.7 |
| labour | 64 | 64 | 554 | 0 | 10 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**0 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Tuning

- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 55.8 coin per prestige at mansion, vs 66.3 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 55.6 coin per prestige at mansion, vs 66.3 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 116 over real use lately; planning 554, not 664

## Prestige spending, cheapest coin per prestige first

143 turns left: prestige gained now converts 51.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.7 | 53.7 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 55.6 | 55.6 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 55.8 | 55.8 |  |
| jousting 3 | arena | 230 | 56.9 | 58.1 | needs a arena (build cost 27,501); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 59.5 | 59.5 |  |
| hold banquet 4 (pies) | mansion | 18 | 63.0 | 63.0 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 62.3 | 63.7 | needs a arena (build cost 27,501); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 63.8 | 63.8 |  |
| hold banquet 5 | mansion | 22 | 64.5 | 64.5 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 1 (meat) | mansion | 4.2 | 66.3 | 66.3 | running |
| hold banquet 4 | mansion | 17.5 | 66.3 | 66.3 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 66.9 | 66.9 | thin at home: hop beer, stockfish, premium cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: bread buy 4 @ 1.44, cured meat buy 6 @ 24.8, grain buy 8 @ 2.2, pasties buy 2 @ 15.0; crew 0.1; est +26 a turn; stock: pasties 2 @ 15.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 12.0 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Helmgreen +38, Birkeningen +31, Cobholme +31, Donaunieder +30, Vauxvais +29
- Helmgreen would trade: cured meat buy 6 @ 22.8, pasties buy 2 @ 12.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.26 | 0.90 (104/turn) | coats 6 (93.98->114), casks 17 (6.51->11.3), garments 10 (26.6->34.01), nets 6 (35.4->39.52) | tools 55 (6.46->7.12), wool 9 (10.13->11.69), cured meat 6 (26.67->28.6) | +425 |
| Hofkirchen | 991 | 0.36 | 0.70 (81/turn) | garments 10 (26.6->30.59), furniture 16 (14.28->17.1), nets 6 (35.4->39.33), glass ingots 1 (69.3->77.42) | cloth 24 (7.35->11.3), tools 55 (5.25->7.12), dyed cloth 6 (10.45->14.82), cured meat 6 (25.2->28.6) | +349 |
| Gottweiler | 1135 | 0.45 | 0.50 (58/turn) | ploughs 1 (83.48->128.25), nets 5 (35.4->41.99), gears 2 (88.2->95), wine 5 (6.46->9.4) | tools 55 (5.35->7.12), ham 2 (59.85->91.67), cookware 5 (22.47->26.98), dyed cloth 5 (10.61->14.82) | +301 |
| Kirchwerp | 1072 | 0.41 | 0.80 (92/turn) | garments 10 (26.6->37.43), glass ingots 1 (69.3->114), steel ingots 2 (15.86->19.76), salt 8 (5.78->6.93) | cloth 24 (7.61->11.3), cookware 5 (21->26.98), tin ingots 2 (33.18->35.72), nails 5 (5.72->6.7) | +290 |
| Pontmont | 341 | 0.10 | 0.60 (69/turn) | timber 25 (8.4->12.92), furniture 16 (14.28->16.43), cured fish 8 (24.36->26.41), garments 10 (26.6->27.93) | tools 55 (5.72->7.12), tin ingots 2 (27.51->35.72), thread 23 (5.46->6.05), bricks 10 (5.25->8.36) | +278 |

**Best:** Heilegg at about +425 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 5 @ min 3.38 | makes 19.3, uses 19.2, holds 58 (keeps 0): sells the surplus + 5/turn of the excess |
| candles | 2 @ 82, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 11 = 1.9 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 13.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.0) |
| grain | 12 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 31 = 3.5 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 54) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 84.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.6k (cash + stock at home prices); -149/turn over 6 turns, -30/turn over 24 turns.
- Limits: cash flow >= -318/turn, prestige >= -1.19/turn (values are after 200 tax a turn).
- Today's settings: value -141/turn, cash -143/turn, prestige +1.27/turn.
- Plan: value +34/turn, cash +40/turn, prestige -1.19/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -259 vs -146, -75 vs -133, +82 vs -156.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +8/turn
  - ship Flax Wyrm -> Grandgues: +9/turn
  - mansion 1 1.00 -> 0.41: +150/turn
  - net maker [make nets 2] 0.00 -> 0.32: +4/turn
  - spinnery 1 1.65 -> 1.53: +3/turn
  - flax farm 1 4.64 -> 3.59: +3/turn
  - weavery 1 0.50 -> 0.58: -10/turn
  - sewing shop 1 0.30 -> 0.36: +9/turn
- Model check over the last 58 turns: predicted -154/turn for the settings we ran, real +1/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.79, thread 4.49, cloth 7.18, flax fibres 5.32, garments 20.77, nets 33.52, beer 3.01, timber 3.58, prestige 62.84, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 6); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 54); light armour buy 1 (v2 None)
- Recipe: net maker make nets 3 -> make nets 2 at 0.32, worth +0/turn.
- Ship linen snake: Grandgues -> Vauxvais (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 89/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 11.3 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 28.6; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
