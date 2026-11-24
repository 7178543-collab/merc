# v2 shadow report

Turn 14270, 2026-11-24 23:34. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,883, prestige 3,720 (600 free, +1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 40 | 0 | 19 | 0 | 0 | sell 3, sell @ 3.96 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 544 | 0 | 20 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**0 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 20 labour expired last turn (~38 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.82 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **cured meat**: home ask 29.60 is above our ceiling 29.00 and last turn bought 1 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **grain**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 58.8 coin per prestige at mansion, vs 70.4 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 114 over real use lately; planning 550, not 664

## Prestige spending, cheapest coin per prestige first

131 turns left: prestige gained now converts 48.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.1 | 51.0 | needs a arena (build cost 29,488); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.8 | 54.7 | needs a arena (build cost 29,488); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 56.7 | 56.7 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 57.2 | 57.2 | thin at home: cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 58.8 | 58.8 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.1 | 59.1 | thin at home: cheese |
| jousting 3 | arena | 230 | 59.3 | 60.8 | needs a arena (build cost 29,488); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 64.7 | 64.7 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 66.0 | 66.0 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 2 (meat) | mansion | 6.8 | 66.2 | 66.2 | thin at home: cheese |
| jousting 2 | arena | 210 | 64.9 | 66.6 | needs a arena (build cost 29,488); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 68.2 | 68.2 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 13.6 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.4 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Donaunieder +42, Darmwald +40, Birkeningen +38, Orlesailles +36, Boistot +34
- Donaunieder would trade: cured meat buy 6 @ 22.0, pasties buy 2 @ 14.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~117 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.11 | 0.50 (58/turn) | limestone 3 (22.26->28.5), beer 3 (3.25->4.35), cheese 4 (5.93->6.51), dyed cloth 12 (18.06->18.24) | sculptures 1 (2373->2736), thread 62 (5.25->5.95), tools 16 (5.51->6.46), axes 9 (17.01->18.14) | +437 |
| Heilegg | 826 | 0.27 | 0.40 (47/turn) | wrought iron 18 (17.43->27.55), garments 10 (28.6->32.11), nets 6 (34.6->38.95), wine 17 (6.51->7.98) | cured meat 6 (25.2->29.4), yarn 21 (5.35->6.17), copper ingots 6 (18.59->19.19) | +345 |
| Kirchwerp | 1072 | 0.42 | 0.60 (70/turn) | glass ingots 3 (70.88->114), garments 10 (28.6->37.05), casks 15 (6.51->9.36), leather 6 (27.09->32.3) | cured meat 6 (27.72->29.4), tin ingots 3 (33.81->35.91), cookware 5 (23.52->24.13), lathes 2 (210->214.7) | +320 |
| Gotthafen | 964 | 0.35 | 0.40 (47/turn) | furniture 16 (16.38->22.61), garments 10 (28.6->34.2), arms 8 (33.18->40.28), nets 4 (34.6->37.24) | cloth 12 (7.51->9.55), yarn 26 (5.15->6.17), cured meat 6 (27.09->29.4), copper ingots 6 (17.64->19.19) | +248 |
| Pontmont | 341 | 0.11 | 0.60 (70/turn) | timber 36 (8.03->13.11), nets 6 (34.6->38), clay 1 (4.14->11.97), beer 3 (3.25->3.84) | tools 16 (5.25->6.46), thread 23 (5.25->5.95), bricks 6 (5.25->8.26), cured meat 4 (28.56->29.4) | +191 |

**Best:** Rouhomme at about +437 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 3 @ min 3.44 | makes 19.3, uses 19.2, holds 40 (keeps 0): sells the surplus + 3/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 2 @ 90.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 11 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 15 = 2.6 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.96 | goal planner: sells 2 a turn at 0.96, keeps 219 (no one offered it) |
| furniture | 2 @ 16, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 50) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.9k (cash + stock at home prices); -88/turn over 6 turns, -58/turn over 24 turns.
- Limits: cash flow >= -287/turn, prestige >= -1.25/turn (values are after 200 tax a turn).
- Today's settings: value -187/turn, cash -191/turn, prestige +1.21/turn.
- Plan: value +4/turn, cash +11/turn, prestige -1.25/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -155 vs -174, -283 vs -186, +56 vs -175.
- Route sales counted at most (what the ships really sold, a turn): beer 2.3, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +26/turn
  - ship Flax Wyrm -> Blanans: +1/turn
  - mansion 1 1.00 -> 0.41: +169/turn
  - net maker 0.00 -> 0.28: +7/turn
  - spinnery 1 1.65 -> 1.33: -5/turn
  - retting pit 1 0.91 -> 0.79: +3/turn
  - flax farm 1 4.64 -> 3.93: +8/turn
  - weavery 1 0.50 -> 0.41: -4/turn
- Model check over the last 59 turns: predicted -147/turn for the settings we ran, real -43/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 33.23, beer 3.30, timber 3.44, prestige 67.34, cash 0.00
- Orders it would set: bread buy 5 (v2 7); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 50); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Donaunieder (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+1/turn over staying).
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

Buffers: flax fibres 88/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
