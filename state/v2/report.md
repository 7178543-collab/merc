# v2 shadow report

Turn 14208, 2026-11-22 09:30. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,203, prestige 3,694 (574 free, -3.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 0 | 4 | 0 | 0 | min_holding 58, sell 18, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 20 | 7 | 9 | 0 | 0 | stop 29, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 527 | 0 | 37 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), but the home ask 33.80 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 37 labour expired last turn (~69 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 33.80 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 56.9 coin per prestige at mansion, vs 74.4 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 527, not 626

## Prestige spending, cheapest coin per prestige first

193 turns left: prestige gained now converts 62.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.4 | 51.3 | needs a arena (build cost 27,987); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 55.2 | 56.1 | needs a arena (build cost 27,987); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 56.7 | 56.7 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 56.9 | 56.9 |  |
| maintain 2 | park | 2 | 57.9 | 57.9 | thin at home: sculptures |
| hold banquet 5 | mansion | 22 | 60.7 | 60.7 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 4 (pies) | mansion | 18 | 63.4 | 63.4 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 65.1 | 65.1 | thin at home: hop beer, stockfish, premium cheese |
| hold mass 2 (premium) | cathedral | 360 | 54.0 | 65.6 | needs a cathedral (build cost 306,680); thin at home: furniture, jewellery, glassware, premium garments |
| hold mass 3 | cathedral | 460 | 57.8 | 66.9 | needs a cathedral (build cost 306,680); thin at home: coats, jewellery, glassware, candles, sculptures, furniture, tapestries, books |
| hold banquet 2 (fish) | mansion | 6.8 | 67.3 | 67.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 67.3 | 67.3 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 19 @ 5.35, pasties buy 9 @ 15.8; crew 0.1; est +44 a turn; stock: pasties 9 @ 15.8 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 14.5 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Rouhomme +68, Bordetes +60, Heilegg +47, Heidlowe +46, Grandgues +44
- Rouhomme would trade: beer sell 19 @ 5.7, pasties buy 12 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~119 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (119/turn) | bread 277 (2.81->4.2), firewood 36 (2.16->11.59), timber 21 (9.29->11.78), beer 14 (3.59->5.75) | dyed cloth 7 (14.7->22.23), bricks 4 (7.3->10.36), garments 1 (28.35->30.6), wool 3 (11.97->12.16) | +785 |
| Heilegg | 826 | 0.27 | 0.60 (72/turn) | flour 8 (20.68->29.26), cured fish 10 (23.1->28.5), nets 6 (37.8->45.03), beer 19 (3.59->5.75) | dyed cloth 37 (14.7->22.23), cheese 6 (8.45->11.02), tools 17 (5.04->6.13), garments 2 (27.09->30.6) | +541 |
| Rouhomme | 368 | 0.12 | 1.00 (119/turn) | bread 304 (2.81->4.5), beer 13 (3.59->5.51), flour 4 (20.68->24.7), nets 4 (37.8->39.14) | tools 12 (4.73->6.13), bricks 4 (5->10.36) | +480 |
| Amsdermund | 1111 | 0.45 | 0.60 (72/turn) | furniture 16 (13.12->19), nets 5 (37.8->43.89), casks 15 (6.51->7.98), cured fish 6 (23.1->25.08) | dyed cloth 24 (13.33->22.23), wool 6 (8.61->12.16), cheese 6 (7.88->11.02), tools 17 (5.04->6.13) | +383 |
| Brunnham | 1281 | 0.56 | 0.70 (84/turn) | cured fish 13 (23.1->27.17), nets 6 (37.8->43.32), butter 2 (76.12->78.38), slaked lime 1 (8.56->10.45) | dyed cloth 36 (17.12->22.23), lathes 2 (189->209), thread 40 (5.67->6.85), cloth 24 (9.87->11) | +304 |

**Best:** Grandgues at about +785 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 18 @ min 3.38 | makes 19.3, uses 4.2, holds 108 (keeps 58): sells the surplus + 3/turn of the excess |
| bread | 5 @ 2.74, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 29.0, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 2 @ 12.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 28.8) |
| grain | 8 @ 3.7, stop 31 |  | goal planner: buys 8 a turn for today's rates, keeps up to 31 (v2 had 17) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 27) |
| light armour | 1 @ 106, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.1k (cash + stock at home prices); +77/turn over 6 turns, +90/turn over 24 turns.
- Limits: cash flow >= -425/turn, prestige >= -1.14/turn (values are after 200 tax a turn).
- Today's settings: value -180/turn, cash -163/turn, prestige +0.62/turn.
- Plan: value -28/turn, cash -12/turn, prestige -1.14/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +207 vs -150, +355 vs -142, +221 vs -156.
- Route sales counted at most (what the ships really sold, a turn): beer 0.3.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gottweiler: +12/turn
  - ship Flax Wyrm -> Fontaux: +0/turn
  - mansion 1 1.00 -> 0.58: +133/turn
  - spinnery 1 1.65 -> 1.33: +7/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - flax farm 1 4.64 -> 4.20: +3/turn
  - net maker 0.00 -> 0.29: -4/turn
  - sewing shop 1 0.30 -> 0.22: -13/turn
  - weavery 1 0.50 -> 0.36: +24/turn
- Model check over the last 58 turns: predicted -136/turn for the settings we ran, real +14/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.88, beer 3.30, timber 3.69, prestige 75.15, cash 0.00
- Orders it would set: bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 4 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 17); labour buy 64 (v2 27); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Gottweiler (+12/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Fontaux (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1979 coin: +4/turn, payback 445 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 425 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.50 |
| ret | 3 | 0.91 | 0.90 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 96/77, thread 1052/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 0.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.74, home ask 2.68; our bid is already at/over the ask (sellers too thin)
- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 29, home ask 33.8 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 34.4 (ask 33.8, cap 42.0))
- R1: prestige rate -3.58 a turn vs 12-turn median -0.56; likely: dry slot: bread, cured meat; mansion 1 projected 0 (cured meat)
- R2: spinnery 1 blocked by thread space: 1052 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
