# v2 shadow report

Turn 14254, 2026-11-24 07:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,816, prestige 3,702 (582 free, +1.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 82 | 27 | 18 | 0 | 0 | sell 7, sell @ 3.72 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 13 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 18 | 9 | 0 | 0 | stop 36, buy 14, buy @ 3.7 |
| labour | 64 | 65 | 565 | 9 | 0 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 64, short of ~74 needed -> v2: buy 74

## Tuning

- **cured meat**: home ask 30.20 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 55.5 coin per prestige at mansion, vs 68.8 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 116 over real use lately; planning 574, not 654

## Prestige spending, cheapest coin per prestige first

147 turns left: prestige gained now converts 52.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.3 | 49.9 | needs a arena (build cost 26,969); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| jousting 2 (premium) | arena | 400 | 52.9 | 53.6 | needs a arena (build cost 26,969); thin at home: protection, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 55.4 | 55.4 | thin at home: cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.5 | 55.5 |  |
| jousting 3 | arena | 230 | 56.1 | 57.3 | needs a arena (build cost 26,969); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 59.7 | 59.7 | thin at home: cheese |
| jousting 2 | arena | 210 | 61.4 | 62.7 | needs a arena (build cost 26,969); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 63.9 | 63.9 | thin at home: hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 65.9 | 65.9 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 67.0 | 67.0 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 67.3 | 67.3 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0 | - | cured meat 3, pasties 2 | -95 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | - | cured meat 6, grain 3 | -148 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: bread buy 4 @ 1.49, cured meat buy 5 @ 24.8, pasties buy 1 @ 16.1; crew 0.1; est +21 a turn; stock: pasties 1 @ 16.1 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 13.7 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Donaunieder +34, Dortgart +30, Friedwerp +28, Helmgreen +28, Kleinburgh +26
- Donaunieder would trade: cured meat buy 5 @ 22.4, pasties buy 1 @ 13.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bedenis | 566 | 0.17 | 0.50 (55/turn) | cloth 18 (11.13->17.1), garments 10 (30.6->37.43), nets 5 (34.8->38.19), paper 4 (19.53->21.85) | tools 30 (5.62->8.03), wine 34 (5.08->5.75), bricks 10 (5.25->9.36), thread 19 (5.57->6.05) | +307 |
| Vauxvais | 204 | 0.06 | 0.30 (33/turn) | bread 159 (2.54->3.38), flour 2 (21.42->28.88), paper 4 (19.53->22.99), thread 16 (6->6.79) | tools 30 (5.46->8.03), cured meat 4 (24.36->30.2), bricks 4 (4.85->9.36), flax fibres 28 (6.67->7.2) | +293 |
| Rouhomme | 368 | 0.11 | 0.50 (55/turn) | garments 10 (30.6->36.1), yarn 15 (6.56->8.84), cloth 18 (11.13->12.35), wheels 9 (23.31->24.89) | tools 30 (5.78->8.03), bricks 20 (5.46->9.36), flax fibres 15 (5.78->7.2), thread 29 (5.57->6.05) | +266 |
| Etallaen | 774 | 0.23 | 0.20 (22/turn) | garments 10 (30.6->38), cloth 12 (11.13->15.96), nets 6 (34.8->36.48), medicine 1 (135.45->141.55) | tools 30 (5.62->8.03), cured meat 5 (24.57->30.2), flax fibres 13 (5.78->7.2), candles 1 (87.67->90.5) | +260 |
| Kirchwerp | 1072 | 0.40 | 0.50 (55/turn) | glass ingots 1 (66.67->114), paper 4 (19.53->29.07), casks 12 (6.51->9.36), canvas 2 (41.58->52.25) | dyed cloth 5 (11.55->16.53), cookware 5 (21->24.13), acid 1 (140.7->148.2), tools 30 (7.4->8.03) | +258 |

**Best:** Bedenis at about +307 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 7 @ min 3.4 | makes 19.3, uses 19.2, holds 82 (keeps 0): sells the surplus + 7/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 9 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 19 = 3.2 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 10) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 74) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.6k (cash + stock at home prices); +89/turn over 6 turns, +15/turn over 24 turns.
- Limits: cash flow >= -326/turn, prestige >= -1.17/turn (values are after 200 tax a turn).
- Today's settings: value -145/turn, cash -142/turn, prestige +1.30/turn.
- Plan: value +26/turn, cash +36/turn, prestige -1.17/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -192 vs -137, -20 vs -137, -259 vs -146.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +5/turn
  - ship Flax Wyrm -> Calange: +4/turn
  - mansion 1 1.00 -> 0.41: +144/turn
  - brewery 1 0.14 -> 0.08: +10/turn
  - spinnery 1 1.65 -> 1.50: +4/turn
  - net maker [make nets 2] 0.00 -> 0.20: +3/turn
  - flax farm 1 4.64 -> 4.47: -0/turn
  - weavery 1 0.50 -> 0.60: -12/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
- Model check over the last 59 turns: predicted -155/turn for the settings we ran, real +21/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.73, thread 4.34, cloth 6.94, flax fibres 5.14, garments 20.08, nets 32.42, beer 3.00, timber 3.42, prestige 62.29, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 6); garments sell 11 (v2 10); grain buy 5 (v2 10); labour buy 64 (v2 74); light armour buy 1 (v2 None)
- Recipe: net maker make nets 3 -> make nets 2 at 0.20, worth +1/turn.
- Ship linen snake: Grandgues -> Etallaen (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Calange (+5/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +85/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 86/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
