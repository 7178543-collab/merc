# v2 shadow report

Turn 14221, 2026-11-22 22:38. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,353, prestige 3,685 (565 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 72 | 0 | 12 | 0 | 0 | min_holding 58, sell 10, sell @ 3.46 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 20 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 526 | 0 | 38 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), but the home ask 34.00 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 3 (need 12) -> v2: buy 12

## Waste (money lost now)

- **labour**: 38 labour expired last turn (~64 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 34.00 is above our ceiling 29.00 and last turn bought 3 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 58.6 coin per prestige at mansion, vs 74.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 103 over real use lately; planning 531, not 634
- labour expiry guard: 38 bought labour expired last turn, buy 27 (not 31) this turn

## Prestige spending, cheapest coin per prestige first

180 turns left: prestige gained now converts 59.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.3 | 49.8 | needs a arena (build cost 27,012); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 49.1 | 50.0 | needs a arena (build cost 27,012); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| jousting 2 (premium) | arena | 400 | 53.0 | 53.6 | needs a arena (build cost 27,012); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 53.8 | 54.7 | needs a arena (build cost 27,012); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 60.1 | 60.1 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 63.6 | 63.6 | thin at home: wine, pies |
| hold banquet 4 (pies) | mansion | 18 | 64.7 | 64.7 | thin at home: hop beer, wine, stockfish |
| hold banquet 5 | mansion | 22 | 65.3 | 65.3 | thin at home: hop beer, wine, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 66.6 | 66.6 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 53.9 | 67.9 | needs a cathedral (build cost 305,160); thin at home: furniture, jewellery, glassware, windows, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: cured meat buy 3 @ 31.2, pasties buy 6 @ 15.1; crew 0.1; est +21 a turn; stock: pasties 6 @ 15.1 (keep 14)
- **linen snake** on Grandgues: beer sell 8 @ 7.2; crew 0.1; est +16 a turn
- best towns now: Karlmoor +121, Bedenis +113, Chatgnan +109, Dortgart +106, Clairlond +102
- Karlmoor would trade: furniture buy 6 @ 8.75, pasties buy 4 @ 12.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (107/turn) | firewood 36 (2.39->11.4), bread 237 (2.75->3.76), timber 28 (8.24->10.83), beer 8 (3.56->7.98) | bricks 10 (7.46->10.36), garments 2 (24.36->26.6), furniture 1 (15.86->17.8), leather 1 (30.24->30.59) | +668 |
| Kirchwerp | 1072 | 0.39 | 0.40 (43/turn) | thread 77 (6.35->9.5), nets 6 (37.4->43.13), glass ingots 1 (63->80.27), honey 3 (10.61->13.21) | tools 18 (4.3->5.79), jewellery 2 (73.5->78.85), cured meat 3 (30.87->34), garments 2 (24.15->26.6) | +318 |
| Heilegg | 826 | 0.24 | 0.20 (21/turn) | wrought iron 5 (15.54->27.55), nets 6 (37.4->44.46), beer 8 (3.56->5.18), casks 9 (6.83->7.89) | cloth 24 (9.55->10.3), cured meat 3 (29.61->34), tools 18 (5.25->5.79), dyed cloth 11 (14.7->15.29) | +161 |
| Darmwald | 1022 | 0.35 | 0.60 (64/turn) | charcoal 19 (2.35->6.79), nets 3 (37.4->46.17), yarn 8 (6.25->7.17), honey 1 (10.61->14.82) | thread 19 (4.45->6.65), cured meat 3 (22.05->34), flax fibres 17 (6.04->7.4), wool 4 (9.35->11.11) | +153 |
| Bordetes | 831 | 0.25 | 1.00 (107/turn) | bread 112 (2.75->4.43), beer 3 (3.56->7.6), charcoal 9 (2.35->5.22), cured fish 1 (26.46->27.74) | cured meat 1 (31.71->34), dyed cloth 5 (14.7->15.29), garments 0 (24.36->26.6), casks 1 (5.25->5.89) | +135 |

**Best:** Grandgues at about +668 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 10 @ min 3.46 | sell; ships offer 8 a turn abroad, so home sells 10 (was 15) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 24.4) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 27) |
| light armour | 1 @ 110, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 87.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.8k (cash + stock at home prices); -249/turn over 6 turns, +47/turn over 24 turns.
- Limits: cash flow >= -431/turn, prestige >= -1.10/turn (values are after 200 tax a turn).
- Today's settings: value -190/turn, cash -191/turn, prestige +1.37/turn.
- Plan: value +11/turn, cash +12/turn, prestige -1.10/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -254 vs -177, -97 vs -192, +90 vs -176.
- Route sales counted at most (what the ships really sold, a turn): beer 1.2.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +25/turn
  - ship Flax Wyrm -> Karlmoor: +9/turn
  - mansion 1 1.00 -> 0.41: +181/turn
  - net maker 0.00 -> 0.29: +9/turn
  - spinnery 1 1.65 -> 1.55: +4/turn
  - flax farm 1 4.64 -> 4.74: -1/turn
  - weavery 1 0.50 -> 0.60: -11/turn
  - sewing shop 1 0.30 -> 0.36: +16/turn
- Model check over the last 59 turns: predicted -150/turn for the settings we ran, real +78/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.68, thread 4.22, cloth 6.74, flax fibres 5.00, garments 19.51, nets 30.95, beer 3.00, timber 3.56, prestige 71.43, cash 0.00
- Orders it would set: bread buy 5 (v2 6); cloth sell 1 (v2 none); firewood buy 4 (v2 8); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 27); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Donaunieder (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Karlmoor (+9/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +84/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1887 coin: +5/turn, payback 418 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 90/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
