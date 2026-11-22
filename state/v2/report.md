# v2 shadow report

Turn 14219, 2026-11-22 20:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,264, prestige 3,688 (568 free, +1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 59 | 0 | 19 | 0 | 0 | min_holding 58, sell 10, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 20 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 537 | 0 | 27 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: only 0.0 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 27 labour expired last turn (~47 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 32.00 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 56.1 coin per prestige at mansion, vs 71.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 106 over real use lately; planning 537, not 602

## Prestige spending, cheapest coin per prestige first

182 turns left: prestige gained now converts 59.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.4 | 49.9 | needs a arena (build cost 27,028); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 49.2 | 50.1 | needs a arena (build cost 27,028); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| jousting 2 (premium) | arena | 400 | 53.1 | 53.6 | needs a arena (build cost 27,028); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 53.9 | 54.9 | needs a arena (build cost 27,028); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.1 | 56.1 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 60.7 | 60.7 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 63.9 | 63.9 | thin at home: wine, pies |
| hold banquet 4 (pies) | mansion | 18 | 64.8 | 64.8 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 66.3 | 66.3 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 54.4 | 68.1 | needs a cathedral (build cost 306,300); thin at home: furniture, jewellery, glassware, windows, premium garments |
| hold banquet 4 | mansion | 17.5 | 68.4 | 68.4 | thin at home: wine, hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.9 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.4 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Karlmoor +73, Bedenis +64, Chatgnan +62, Briclives +57, Dortgart +55
- Karlmoor would trade: furniture buy 4 @ 8.75, pasties buy 2 @ 12.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (109/turn) | beer 67 (3.4->7.6), firewood 29 (2.02->11.4), bread 199 (2.48->3.76), timber 30 (8.4->11.59) | bricks 7 (7.72->10.45), cloth 5 (8.56->10), copper ingots 0 (17.32->23.94), garments 1 (24.36->27.8) | +976 |
| Kirchwerp | 1072 | 0.39 | 0.50 (54/turn) | thread 78 (6->9.5), nets 6 (37.4->42.94), glass ingots 1 (63->82.65), flax fibres 3 (6.9->9.03) | tools 18 (4.62->5.75), lathes 2 (220.5->229.9), garments 2 (24.15->27.8), jewellery 1 (73.5->81.22) | +351 |
| Bordetes | 831 | 0.25 | 1.00 (109/turn) | beer 32 (3.4->6.7), bread 95 (2.48->4.01), cured fish 1 (24.57->30.97), wine 2 (6.51->9.5) | copper ingots 0 (17.85->23.94), garments 0 (24.36->27.8), dyed cloth 4 (14.7->15.29) | +197 |
| Heilegg | 826 | 0.25 | 0.60 (65/turn) | beer 81 (3.4->4.58), wrought iron 3 (15.65->27.55), nets 3 (37.4->43.51), resin 3 (2.35->6.7) | cloth 15 (9.45->10), garments 2 (25.2->27.8), tools 18 (5.25->5.75), copper ingots 1 (19.84->23.94) | +159 |
| Rouhomme | 368 | 0.11 | 1.00 (109/turn) | bread 113 (2.48->3.42), firewood 21 (2.02->6.74), seeds 3 (2.39->3.15), nets 2 (37.4->37.81) | bricks 10 (5.25->10.45), tools 8 (4.73->5.75), garments 0 (24.36->27.8), copper ingots 0 (17.64->23.94) | +154 |

**Best:** Grandgues at about +976 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 2 @ 82.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.0) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 37) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.3k (cash + stock at home prices); -308/turn over 6 turns, +36/turn over 24 turns.
- Limits: cash flow >= -428/turn, prestige >= -1.12/turn (values are after 200 tax a turn).
- Today's settings: value -175/turn, cash -177/turn, prestige +1.37/turn.
- Plan: value +19/turn, cash +21/turn, prestige -1.12/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -254 vs -177, -97 vs -192, +90 vs -176.
- Route sales counted at most (what the ships really sold, a turn): beer 1.2.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Karlmoor: +14/turn
  - ship Flax Wyrm -> Donaunieder: +15/turn
  - mansion 1 1.00 -> 0.41: +177/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.57: +4/turn
  - retting pit 1 0.91 -> 0.96: -1/turn
  - flax farm 1 4.64 -> 4.82: +2/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +15/turn
  - ropewalk 1 0.25 -> 0.00: -16/turn
- Model check over the last 59 turns: predicted -147/turn for the settings we ran, real +78/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.70, thread 4.27, cloth 6.82, flax fibres 5.07, garments 19.74, nets 31.27, beer 3.02, timber 3.60, prestige 70.65, cash 0.00
- Orders it would set: bread buy 5 (v2 7); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 37); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +11/turn.
- Ship linen snake: Grandgues -> Karlmoor (+14/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +85/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1896 coin: +4/turn, payback 495 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 87/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 32.0 -> **buy 12 @ 32.6 (ask 32.0, cap 42.0)** (ok)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.4 for 5 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
