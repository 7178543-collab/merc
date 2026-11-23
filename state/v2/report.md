# v2 shadow report

Turn 14236, 2026-11-23 13:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,222, prestige 3,678 (558 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 85 | 0 | 4 | 0 | 0 | min_holding 58, sell 1, sell @ 3.16 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 8 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 8 | 7 | 7 | 2 | 0 | stop 29, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 525 | 0 | 39 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (12 @ 32.2), but the home ask 32.60 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **grain**: brewery 1 ran short of grain (buy is live (8 @ 3.7), 7 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.9 turns of grain left and buying 8 (need 18) -> v2: buy 18

## Waste (money lost now)

- **labour**: 39 labour expired last turn (~63 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 32.60 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 54.8 coin per prestige at mansion, vs 70.1 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 57.9 coin per prestige at mansion, vs 70.1 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 106 over real use lately; planning 556, not 662
- labour expiry guard: 39 bought labour expired last turn, buy 25 (not 56) this turn

## Prestige spending, cheapest coin per prestige first

165 turns left: prestige gained now converts 56.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| maintain 2 | park | 2 | 48.6 | 48.6 | thin at home: sculptures |
| jousting 3 (premium) | arena | 420 | 52.2 | 52.7 | needs a arena (build cost 25,816); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 54.8 | 54.8 |  |
| jousting 3 | arena | 230 | 54.4 | 55.3 | needs a arena (build cost 25,816); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 56.0 | 56.5 | needs a arena (build cost 25,816); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 57.9 | 57.9 |  |
| hold banquet 5 | mansion | 22 | 59.6 | 59.6 | thin at home: hop beer, stockfish, sculptures |
| jousting 2 | arena | 210 | 59.6 | 60.6 | needs a arena (build cost 25,816); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 63.8 | 63.8 |  |
| hold banquet 4 (pies) | mansion | 18 | 63.8 | 63.8 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 65.4 | 65.4 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 12.2 (keep 14); best orders clear only 3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Bordetes +55
- Bordetes would trade: beer sell 13 @ 8.25, pasties buy 2 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.60 (63/turn) | bread 193 (2.52->3.34), timber 28 (7.72->9.88), beer 13 (2.92->4.75), charcoal 19 (2.48->4.05) | cured meat 9 (20.68->30.59), thread 60 (5.46->6.1), bricks 10 (7.4->9.36), dyed cloth 6 (15.96->16.34) | +385 |
| Vauxvais | 204 | 0.06 | 0.50 (53/turn) | grain 97 (3.02->4.29), bread 164 (2.52->3.23), rope 1 (72.5->86.92), beer 13 (2.92->3.72) | cloth 11 (7.88->11.2), thread 6 (3.23->6.1), flax fibres 7 (6.3->8.25), cured meat 5 (28.77->30.59) | +322 |
| Hanstein | 380 | 0.11 | 1.00 (105/turn) | timber 16 (7.72->11.69), charcoal 18 (2.48->4.94), firewood 16 (2.18->6.89), rope 1 (72.5->79.8) | cloth 17 (10.03->11.2), flax fibres 8 (5.93->8.25), thread 20 (5.25->6.1), cured meat 5 (27.72->30.59) | +187 |
| Angefont | 686 | 0.19 | 0.30 (32/turn) | thread 80 (5.7->6.27), rope 1 (72.5->87.88), beer 13 (2.92->3.65), logs 2 (5.3->11.3) | flax fibres 28 (5.57->8.25), cloth 20 (9.08->11.2), tin ingots 3 (35.07->35.91), fleece 3 (8.14->8.74) | +158 |
| Neuborn | 780 | 0.22 | 1.00 (105/turn) | bread 31 (2.52->4.56), grain 20 (3.02->5.18), firewood 6 (2.18->12.54), timber 6 (7.72->14.25) | cloth 1 (7.67->11.2), garments 0 (24.36->28.4), flax fibres 0 (6.67->8.25), raw cloth 0 (7.14->7.65) | +150 |

**Best:** Grandgues at about +385 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 15 @ 3.12, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 85 = 5.7 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.0) |
| grain | 5 @ 3.7, stop 19 |  | goal planner: buys 5 a turn for today's rates, keeps up to 19 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 25) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 41.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 70.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.6k (cash + stock at home prices); +52/turn over 6 turns, -67/turn over 24 turns.
- Limits: cash flow >= -426/turn, prestige >= -1.07/turn (values are after 200 tax a turn).
- Today's settings: value -173/turn, cash -174/turn, prestige +1.40/turn.
- Plan: value +26/turn, cash +34/turn, prestige -1.07/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +175 vs -141, +188 vs -170, -126 vs -165.
- Route sales counted at most (what the ships really sold, a turn): beer 2.0, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bordetes: +6/turn
  - ship Flax Wyrm -> Calange: +6/turn
  - mansion 1 1.00 -> 0.41: +169/turn
  - net maker 0.00 -> 0.29: +10/turn
  - brewery 1 0.14 -> 0.07: +5/turn
  - spinnery 1 1.65 -> 1.47: +4/turn
  - flax farm 1 4.64 -> 4.39: -2/turn
  - weavery 1 0.50 -> 0.60: -9/turn
  - sewing shop 1 0.30 -> 0.36: +13/turn
- Model check over the last 59 turns: predicted -157/turn for the settings we ran, real +63/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.62, thread 4.07, cloth 6.50, flax fibres 4.83, garments 18.81, nets 29.85, beer 2.96, timber 3.31, prestige 70.64, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 18); labour buy 64 (v2 25); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Bordetes (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Calange (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1849 coin: +5/turn, payback 368 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 85/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 7.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 12 @ 32.2, home ask 32.6 (held back: acted on cured meat at turn 14235 (one action per 2 turns))
- R1: prestige rate -2.80 a turn vs 12-turn median +1.03; likely: dry slot: cured meat
