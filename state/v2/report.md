# v2 shadow report

Turn 13861, 2026-11-07 22:35. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,489, prestige 3,505 (385 free, +150.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 59 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.42 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 30 | 8 | 9 | 0 | 0 | stop 32, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 99 over real use lately; planning 520, not 618

## Prestige spending, cheapest coin per prestige first

540 turns left: prestige gained now converts 93.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| jousting 3 | arena | 230 | 54.3 | 54.6 | needs a arena (build cost 25,229); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 54.8 | 54.8 | thin at home: pasties, wine, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.2 | 55.2 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 56.7 | 56.7 |  |
| hold banquet 4 | mansion | 17.5 | 57.8 | 57.8 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.8 | 57.8 | thin at home: wine, ham, stockfish, premium cheese |
| jousting 2 | arena | 210 | 59.5 | 59.8 | needs a arena (build cost 25,229); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.0 | 60.0 | thin at home: wine, cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 60.8 | 60.8 | thin at home: wine, cheese |
| hold banquet 3 (pies) | mansion | 8 | 61.2 | 61.2 | thin at home: pasties, cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.8 | 61.8 | thin at home: pasties, wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clairlond | 1288 | 0.50 | 0.10 (10/turn) | premium ham 1 (258.3->326.8), garments 10 (23->25.84), salt 5 (4.37->6.6), hop beer 2 (10.61->14.72) | candles 1 (75.08->83.5), cheese 5 (6.77->8.93), cloth 11 (8.51->9.55), furniture 1 (13.02->15.7) | +129 |
| Etallaen | 774 | 0.22 | 0.20 (21/turn) | cured fish 6 (24.36->30.4), beer 15 (3->5.22), cured meat 4 (22.68->25.46), nets 1 (33.6->40.09) | candles 1 (73.5->83.5), nails 3 (6.14->6.84), pickaxes 1 (9.19->9.88) | +84 |
| Fontaux | 411 | 0.12 | 1.00 (105/turn) | firewood 22 (2.33->7.46), charcoal 17 (2.79->4.58), beer 15 (3->3.91), flax fibres 2 (6.35->7.36) | cloth 8 (8.45->9.55), candles 1 (77.17->83.5), flax plants 3 (0.73->1.68), wool 1 (9.35->11.21) | +76 |
| Kirchwerp | 1072 | 0.38 | 0.30 (31/turn) | thread 60 (4.66->5.7), hides 1 (10.82->12.35) | cloth 24 (8.45->9.55), cheese 5 (6.2->8.93), candles 1 (76.65->83.5), wool 1 (10.71->11.21) | +76 |
| Nürnnieder | 520 | 0.14 | 0.10 (10/turn) | garments 10 (23->25.65) | tapestries 1 (640.5->665), candles 1 (75.08->83.5), thread 30 (4.91->5.3), flax fibres 11 (5.78->6.5) | +70 |

**Best:** Clairlond at about +129 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 15 @ min 3.38 |  |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 13 |  | goal planner: buys 4 a turn for today's rates, keeps up to 13 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.4) |
| grain | 2 @ 3.7, stop 7 |  | goal planner: buys 2 a turn for today's rates, keeps up to 7 (v2 had 13) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 20) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.7k (cash + stock at home prices); -513/turn over 6 turns, -29/turn over 24 turns.
- Limits: cash flow >= -187/turn, prestige >= -0.35/turn (values are after 200 tax a turn).
- Today's settings: value +69/turn, cash +52/turn, prestige +158.00/turn.
- Plan: value +407/turn, cash +261/turn, prestige +150.00/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +24 vs +68, -1460 vs +63, -2439 vs +54 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +6/turn
  - ship Flax Wyrm -> Chatgnan: +2/turn
  - park 1 16.00 -> 0.00: +47/turn
  - flax farm 1 4.64 -> 8.04: +28/turn
  - retting pit 1 0.91 -> 1.57: +32/turn
  - spinnery 1 1.65 -> 2.77: +61/turn
  - weavery 1 0.50 -> 1.30: +101/turn
  - net maker [make nets 1] 0.00 -> 0.38: +29/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
  - brewery 1 0.14 -> 0.03: +16/turn
- Model check over the last 61 turns: predicted +104/turn for the settings we ran, real +15/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.07, thread 2.69, cloth 4.30, flax fibres 3.20, garments 12.43, nets 20.15, beer 2.35, timber 3.31, prestige 0.00, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 2 (v2 13); labour buy 29 (v2 20); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.34, worth +41/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +17/turn.
- Ship linen snake: Grandgues -> Etallaen (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+2/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +53/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 439 (+150 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.97 |
| ret | 3 | 0.91 | 0.99 |
| spin | 4 | 1.65 | 1.75 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 541/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.5 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
