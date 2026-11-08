# v2 shadow report

Turn 13866, 2026-11-08 03:07. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,541, prestige 3,496 (376 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 69 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.28 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 5 | 6 | 6 | 3 | 0 | stop 19, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 512 | 0 | 17 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **grain**: brewery 1 ran short of grain (buy is live (5 @ 3.7), 6 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.6 turns of grain left and buying 5 (need 18) -> v2: buy 18
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 17 labour expired last turn (~28 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 512, not 610

## Prestige spending, cheapest coin per prestige first

535 turns left: prestige gained now converts 93.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| jousting 3 | arena | 230 | 53.6 | 53.8 | needs a arena (build cost 24,712); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 54.7 | 54.7 | thin at home: hop beer, wine, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.2 | 55.2 |  |
| hold banquet 4 (premium) | mansion | 20 | 56.9 | 56.9 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.7 | 57.7 | thin at home: wine, hop beer, ham, stockfish, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 57.9 | 57.9 |  |
| jousting 2 | arena | 210 | 58.7 | 59.0 | needs a arena (build cost 24,712); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 62.3 | 62.3 | thin at home: hop beer, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 63.1 | 63.1 | thin at home: wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 63.3 | 63.3 | thin at home: hop beer, cheese |
| jousting 1 | arena | 170 | 63.0 | 63.3 | needs a arena (build cost 24,712); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Chatgnan +33
- Chatgnan would trade: pasties buy 8 @ 13.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (97/turn) | timber 23 (7.56->10.54), firewood 34 (2.23->4.31), bread 150 (2.67->2.93), grain 61 (2.81->3.06) | cheese 3 (7.56->10.45), blades 5 (17.32->17.86), cloth 7 (9.45->9.8), raw cloth 1 (8.19->10.16) | +142 |
| Hofkirchen | 991 | 0.34 | 0.70 (76/turn) | grain 99 (2.81->4.12), yarn 5 (3.74->4.45), hides 1 (10.61->11.88), leather 1 (23.73->25.46) | cloth 24 (8.03->9.8), cheese 3 (5.78->10.45), candles 1 (71.4->81), copper ingots 1 (12.81->18.52) | +140 |
| Hanstein | 380 | 0.11 | 0.40 (43/turn) | timber 13 (7.56->9.79), malt 1 (6.41->13.01), charcoal 15 (2.71->3.8), wine 4 (6.72->7.27) | cloth 24 (8.35->9.8), thread 44 (4.47->5.3), cheese 3 (7.14->10.45), flax fibres 17 (5.17->5.9) | +118 |
| Etallaen | 774 | 0.22 | 0.90 (97/turn) | grain 99 (2.81->3.55), cured fish 6 (24.57->28.69), clay 3 (4.91->19), beer 9 (3.26->4.8) | cheese 3 (7.61->10.45), candles 1 (73.5->81), raw cloth 2 (8.19->10.16), cloth 6 (9.35->9.8) | +107 |
| Neuborn | 780 | 0.23 | 1.00 (108/turn) | cookware 6 (24.78->28.69), timber 18 (7.56->11.88), beer 6 (3.26->4.45), seeds 9 (2.6->3.32) | cloth 17 (8.09->9.8), cheese 2 (5.41->10.45), thread 12 (4.68->5.3), blades 3 (17.12->17.86) | +107 |

**Best:** Grandgues at about +142 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.4) |
| grain | 6 @ 3.7, stop 24 |  | goal planner: buys 6 a turn for today's rates, keeps up to 24 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 12) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.2k (cash + stock at home prices); -576/turn over 6 turns, -23/turn over 24 turns.
- Limits: cash flow >= -189/turn, prestige >= -0.32/turn (values are after 200 tax a turn).
- Today's settings: value +76/turn, cash +61/turn, prestige -1.89/turn - breaks the prestige floor.
- Plan: value +12/turn, cash +15/turn, prestige -0.32/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -6 vs +52, +1 vs +46, -38 vs +58.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +10/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - flax farm 1 4.64 -> 4.02: -5/turn
  - retting pit 1 0.91 -> 0.80: +2/turn
  - spinnery 1 1.65 -> 1.41: +6/turn
  - weavery 1 0.50 -> 0.41: -12/turn
  - sewing shop 1 0.30 -> 0.24: -3/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.32: -15/turn
  - ropewalk 1 0.25 -> 0.00: +20/turn
- Model check over the last 61 turns: predicted +103/turn for the settings we ran, real +13/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 30.01, beer 2.91, timber 3.24, prestige 56.53, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 18); labour buy 29 (v2 12); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.32, worth +13/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+14/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 597/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.9 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
- R5: tar buy not filling: bid 11 under the home ask 12.6 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
