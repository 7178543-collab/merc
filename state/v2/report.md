# v2 shadow report

Turn 13867, 2026-11-08 04:13. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,630, prestige 3,494 (374 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.28 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 3 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 6 | 5 | 5 | 4 | 0 | stop 24, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 510 | 0 | 19 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.68 is above our ceiling 2.40 and last turn bought 4 of ~3 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **grain**: brewery 1 ran short of grain (buy is live (6 @ 3.7), 5 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.7 turns of grain left and buying 6 (need 18) -> v2: buy 18
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 19 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 512, not 612

## Prestige spending, cheapest coin per prestige first

534 turns left: prestige gained now converts 93.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| jousting 3 | arena | 230 | 53.7 | 53.9 | needs a arena (build cost 24,868); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 54.6 | 54.6 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.4 | 55.4 |  |
| hold banquet 4 (premium) | mansion | 20 | 56.9 | 56.9 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.3 | 57.3 | thin at home: wine, ham, stockfish, cheese |
| jousting 2 | arena | 210 | 58.8 | 59.1 | needs a arena (build cost 24,868); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 59.5 | 59.5 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 61.3 | 61.3 | thin at home: wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 61.6 | 61.6 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 61.7 | 61.7 | thin at home: cheese |
| jousting 1 | arena | 170 | 62.8 | 63.1 | needs a arena (build cost 24,868); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Bordetes +24, Pontmont +20
- Bordetes would trade: pasties buy 14 @ 16.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.34 | 0.70 (76/turn) | grain 99 (2.77->4.12), paper 9 (23.1->23.94), nets 5 (33.6->34.96), hides 1 (10.61->11.88) | tapestries 1 (703.5->736.25), cloth 24 (8.03->9.4), cheese 4 (5.78->9.17), candles 1 (71.4->81) | +151 |
| Kleinburgh | 1440 | 0.60 | 0.10 (11/turn) | arms 3 (29.61->34.2), salt 4 (5.1->7.6) | tapestries 1 (640.5->736.25), cheese 4 (6.09->9.17), blades 3 (14.28->17.86), candles 1 (77.7->81) | +133 |
| Chatgnan | 728 | 0.21 | 0.10 (11/turn) | tackles 1 (174.3->175.75), axes 1 (19.11->19.76), flax plants 1 (1.31->1.77) | tapestries 1 (609->736.25), candles 1 (77.17->81), pasties 3 (14.8->15.96), cheese 4 (8.72->9.17) | +133 |
| Helmgreen | 1354 | 0.55 | 0.10 (11/turn) | hides 1 (10.61->12.06) | tapestries 1 (603.75->736.25), raw cloth 5 (7.4->8.55), candles 1 (79.28->81), cheese 4 (8.61->9.17) | +133 |
| Grandgues | 152 | 0.04 | 0.90 (97/turn) | timber 22 (8.29->10.73), firewood 34 (2.81->4.45), grain 64 (2.77->3.02), bread 151 (2.77->2.93) | tapestries 1 (703.5->736.25), cloth 8 (8.19->9.4), cheese 4 (7.46->9.17), candles 1 (78.23->81) | +121 |

**Best:** Hofkirchen at about +151 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.4) |
| grain | 7 @ 3.7, stop 27 |  | goal planner: buys 7 a turn for today's rates, keeps up to 27 (v2 had 18) |
| labour | 30 @ 2.2, stop - |  | goal planner: buys 30 for today's rates (v2 had 12) |
| light armour | 1 @ 93, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.3k (cash + stock at home prices); -572/turn over 6 turns, -44/turn over 24 turns.
- Limits: cash flow >= -193/turn, prestige >= -0.31/turn (values are after 200 tax a turn).
- Today's settings: value +78/turn, cash +61/turn, prestige -1.88/turn - breaks the prestige floor.
- Plan: value +13/turn, cash +14/turn, prestige -0.31/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +1 vs +46, -38 vs +58, +90 vs +61.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +5/turn
  - spinnery 1 1.65 -> 1.39: -6/turn
  - retting pit 1 0.91 -> 0.79: +3/turn
  - flax farm 1 4.64 -> 3.94: +6/turn
  - weavery 1 0.50 -> 0.42: -11/turn
  - sewing shop 1 0.30 -> 0.25: -5/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.30: -16/turn
  - ropewalk 1 0.25 -> 0.00: +19/turn
- Model check over the last 61 turns: predicted +103/turn for the settings we ran, real +10/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 30.06, beer 2.92, timber 3.24, prestige 57.73, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 7); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 7 (v2 18); labour buy 30 (v2 12); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +12/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+10/turn over staying).
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

Buffers: flax fibres 27/77, thread 609/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.85 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
