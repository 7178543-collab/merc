# v2 shadow report

Turn 14012, 2026-11-14 05:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,494, prestige 3,516 (396 free, +2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 107 | 27 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 548 | 0 | 16 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.28 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.28 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 16 labour expired last turn (~29 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +5 crew for linen snake (crew 0.10, no projection from the game)
- labour: projection runs 99 over real use lately; planning 548, not 637

## Prestige spending, cheapest coin per prestige first

389 turns left: prestige gained now converts 85.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 55.8 | 55.8 | running |
| jousting 3 | arena | 230 | 56.7 | 57.0 | needs a arena (build cost 28,448); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.3 | 58.3 | thin at home: pasties, pies |
| hold banquet 4 (pies) | mansion | 18 | 59.7 | 59.7 | thin at home: pasties, hop beer, ham, stockfish, glassware |
| hold banquet 2 (fish) | mansion | 6.8 | 61.0 | 61.0 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 61.5 | 61.5 | thin at home: cured fish |
| hold banquet 4 (premium) | mansion | 20 | 61.5 | 61.5 | thin at home: hop beer, ham, stockfish, glassware |
| hold banquet 3 (pies) | mansion | 8 | 62.0 | 62.0 | thin at home: pasties, hop beer, pies |
| jousting 2 | arena | 210 | 62.1 | 62.5 | needs a arena (build cost 28,448); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 63.2 | 63.2 | thin at home: hop beer, ham, stockfish, glassware |
| hold banquet 2 (meat) | mansion | 6.8 | 63.3 | 63.3 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 65.0 | 65.0 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0 | - | cured meat 6, pasties 2 | -169 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.1 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.4 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Kirchwerp +28, Großmühle +17, Gottweiler +15
- Kirchwerp would trade: cured meat buy 6 @ 20.4, pasties buy 3 @ 16.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.60 (69/turn) | timber 25 (8.09->11.88), firewood 35 (3.44->6.08), pasties 3 (13.97->15.2), beer 3 (3.66->4.08) | cloth 10 (7.93->9.3), cured meat 6 (23.94->25.4), candles 1 (84.53->88.5), garments 2 (22.47->23.6) | +153 |
| Coburgbaum | 619 | 0.19 | 0.70 (81/turn) | bread 123 (2.58->4.08) | cured meat 5 (23.52->25.4), cloth 6 (8.14->9.3), tackles 1 (163.8->170.05), cheese 6 (5.78->6.65) | +135 |
| Blanans | 297 | 0.09 | 0.60 (69/turn) | timber 39 (8.09->11.59), limestone 3 (18.9->24.89), cheese 11 (7.82->8.41), honey 3 (8.56->9.59) | cloth 15 (7.56->9.3), candles 1 (86.62->88.5), garments 2 (22.89->23.6) | +129 |
| Friedwerp | 684 | 0.21 | 0.30 (35/turn) | acid 1 (118.65->140.6), nets 2 (38.8->41.42) | grindstones 1 (226.8->266), cloth 11 (7.72->9.3), furniture 18 (15.12->16.81), candles 1 (84->88.5) | +92 |
| Orlesailles | 1178 | 0.48 | 0.20 (23/turn) | tapestries 1 (761.25->798), premium ham 1 (258.3->286.9), dyed cloth 5 (10.82->13.87), acid 1 (118.65->121.6) | cloth 19 (8.4->9.3), candles 1 (86.1->88.5), cured meat 6 (24.36->25.4), garments 2 (22.89->23.6) | +89 |

**Best:** Grandgues at about +153 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 107 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 10 = 1.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.5 | goal planner: sells 2 a turn at 5.5, keeps 85 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 48) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.8) |
| pasties |  | 1 @ min 12.5 | goal planner: sells 1 a turn at 12.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.8k (cash + stock at home prices); -208/turn over 6 turns, -60/turn over 24 turns.
- Limits: cash flow >= -354/turn, prestige >= -0.40/turn (values are after 200 tax a turn).
- Today's settings: value -179/turn, cash -149/turn, prestige +2.03/turn.
- Plan: value -13/turn, cash +1/turn, prestige -0.40/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -237 vs -161, -70 vs -168, -352 vs -158.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship Flax Wyrm -> Kirchwerp: +11/turn
  - mansion 1 1.00 -> 0.42: +151/turn
  - spinnery 1 1.65 -> 1.36: +3/turn
  - retting pit 1 0.91 -> 0.84: +2/turn
  - flax farm 1 4.64 -> 4.22: +4/turn
  - net maker 0.00 -> 0.29: -1/turn
  - ropewalk 1 0.25 -> 0.00: -11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.32: +12/turn
  - weavery 1 0.50 -> 0.36: -14/turn
  - sewing shop 1 0.30 -> 0.21: +18/turn
- Model check over the last 60 turns: predicted +13/turn for the settings we ran, real +41/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.29, beer 3.19, timber 3.83, prestige 59.99, cash 0.00
- Orders it would set: bread buy 5 (v2 7); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax fibres sell 2 (v2 none); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 48); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.32, worth +11/turn.
- Ship linen snake: stays on Grandgues (worth +8/turn).
- Ship Flax Wyrm: Caillechâtel -> Kirchwerp (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 422 (+133 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.30 |
| ret | 3 | 0.91 | 0.86 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 110/77, thread 1055/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.28; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1055 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.2 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
