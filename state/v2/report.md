# v2 shadow report

Turn 14238, 2026-11-23 15:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,616, prestige 3,680 (560 free, +1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 73 | 0 | 19 | 0 | 0 | min_holding 58, sell 1, sell @ 3.16 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 9 | 4 | 3 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 7 | 5 | 5 | 4 | 0 | stop 27, buy 7, buy @ 3.7 |
| labour | 64 | 64 | 562 | 0 | 2 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **grain**: brewery 1 ran short of grain (buy is live (7 @ 3.7), 5 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.8 turns of grain left and buying 7 (need 18) -> v2: buy 18
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.90 x15, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 56.7 coin per prestige at mansion, vs 68.3 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 98 over real use lately; planning 562, not 659

## Prestige spending, cheapest coin per prestige first

163 turns left: prestige gained now converts 56.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| jousting 3 (premium) | arena | 420 | 50.2 | 50.7 | needs a arena (build cost 25,731); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 50.2 | 51.1 | needs a arena (build cost 25,731); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.8 | 54.4 | needs a arena (build cost 25,731); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.9 | 56.0 | needs a arena (build cost 25,731); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.7 | 56.7 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.6 | 59.6 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 63.9 | 63.9 | thin at home: wine, pies |
| hold banquet 4 (pies) | mansion | 18 | 64.1 | 64.1 | thin at home: hop beer, wine, stockfish |
| hold banquet 5 | mansion | 22 | 65.1 | 65.1 | thin at home: hop beer, wine, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 66.8 | 66.8 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 67.3 | 67.3 | thin at home: wine, hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0 | - | cured meat 3 | -81 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | - | cured meat 6 | -121 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 20.8, pasties buy 4 @ 16.4; crew 0.1; est +52 a turn; stock: pasties 4 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: cured meat buy 4 @ 27.4, pasties buy 3 @ 12.9; crew 0.1; est +16 a turn; stock: pasties 3 @ 12.9 (keep 14)
- best towns now: Grandgues +52, Gottweiler +51, Heidlowe +26, Friedwerp +25, Hanbrücken +22
- Grandgues would trade: cured meat buy 6 @ 20.8, pasties buy 4 @ 16.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.06 | 0.50 (52/turn) | grain 98 (3->4.24), thread 30 (3.92->4.89), charcoal 19 (2.1->3.13), bread 165 (2.5->2.7) | bricks 16 (6.35->9.79), flax fibres 6 (5.78->8.25), flax plants 8 (1.68->2.41), copper ingots 3 (19.53->20.9) | +220 |
| Pontmont | 341 | 0.10 | 0.60 (62/turn) | timber 40 (7.61->11.11), cookware 5 (28.35->33.63), paper 4 (28.77->30.4), clay 1 (3.57->11.97) | flax fibres 8 (5.78->8.25), wool 5 (7.93->11.02), bricks 11 (7.35->9.79), cloth 4 (8.93->10.3) | +169 |
| Neuborn | 780 | 0.22 | 1.00 (104/turn) | grain 18 (3->5.94), bread 31 (2.5->4.46), firewood 7 (2.18->12.73), timber 6 (7.61->14.25) | cloth 1 (7.88->10.3), garments 0 (24.36->27.6), cheese 1 (5.78->6.74), copper ingots 0 (20.27->20.9) | +166 |
| Grandgues | 152 | 0.04 | 0.30 (31/turn) | charcoal 19 (2.1->4.26), timber 28 (7.61->9.12), thread 15 (3.92->4.89), logs 2 (5.21->7.98) | cured meat 6 (21.42->29.4), bricks 10 (6.51->9.79), cloth 9 (9.97->10.3), flax plants 8 (1.93->2.41) | +164 |
| Rouhomme | 368 | 0.10 | 0.50 (52/turn) | glassware 2 (78.75->108.3), cookware 5 (28.35->28.5), hides 1 (14.6->14.91) | flax fibres 19 (5.78->8.25), bricks 19 (5.57->9.79), tools 19 (4.73->5.7), copper ingots 4 (19.64->20.9) | +161 |

**Best:** Vauxvais at about +220 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 22 @ 3.86, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 73 = 3.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 9 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 19 = 3.2 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.6) |
| grain | 6 @ 3.7, stop 23 |  | goal planner: buys 6 a turn for today's rates, keeps up to 23 (v2 had 18) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 62) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 41.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.1k (cash + stock at home prices); +52/turn over 6 turns, -85/turn over 24 turns.
- Limits: cash flow >= -401/turn, prestige >= -1.08/turn (values are after 200 tax a turn).
- Today's settings: value -113/turn, cash -123/turn, prestige +1.41/turn.
- Plan: value +49/turn, cash +51/turn, prestige -1.08/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -126 vs -165, -238 vs -174, -368 vs -114.
- Route sales counted at most (what the ships really sold, a turn): beer 2.0, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship Flax Wyrm -> Bedenis: +2/turn
  - mansion 1 1.00 -> 0.41: +130/turn
  - net maker 0.00 -> 0.29: +10/turn
  - brewery 1 0.14 -> 0.09: +8/turn
  - spinnery 1 1.65 -> 1.43: +3/turn
  - retting pit 1 0.91 -> 0.85: +2/turn
  - flax farm 1 4.64 -> 4.25: +1/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +16/turn
- Model check over the last 59 turns: predicted -157/turn for the settings we ran, real +53/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.63, thread 4.10, cloth 6.54, flax fibres 4.86, garments 18.93, nets 33.60, beer 2.96, timber 3.26, prestige 55.30, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 7); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 18); labour buy 65 (v2 62); light armour buy 1 (v2 None)
- Ship linen snake: stays on Grandgues (worth +19/turn).
- Ship Flax Wyrm: Caillechâtel -> Bedenis (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 84/77, thread 1058/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1058 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
