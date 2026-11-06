# v2 shadow report

Turn 13835, 2026-11-06 20:32. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,975, prestige 3,396 (276 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 32 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 500 | 0 | 29 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.40 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.40 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.80 x22, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~48 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 517, not 617

## Prestige spending, cheapest coin per prestige first

566 turns left: prestige gained now converts 94.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.0 | 54.0 |  |
| jousting 3 | arena | 230 | 54.4 | 54.6 | needs a arena (build cost 26,459); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 55.1 | 55.1 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 55.4 | 55.4 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 55.5 | 55.5 | thin at home: hop beer, wine, ham, stockfish, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 57.1 | 57.1 | thin at home: hop beer |
| hold banquet 1 (meat) | mansion | 4.2 | 57.4 | 57.4 |  |
| hold banquet 4 | mansion | 17.5 | 58.5 | 58.5 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 59.7 | 59.7 | thin at home: hop beer, wine, ham, stockfish |
| jousting 2 | arena | 210 | 59.6 | 59.8 | needs a arena (build cost 26,459); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.3 | 60.3 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0.108 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.168 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: pasties buy 11 @ 15.0; crew 0.1; est +32 a turn; stock: pasties 11 @ 15.0 (keep 14)
- best towns now: Rouhomme +56, Orlesailles +50, Grandgues +38, Bordees +36, Bordetes +33
- Rouhomme would trade: pasties buy 12 @ 13.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.24 | 0.20 (22/turn) | nets 6 (32.2->35.72), glass ingots 1 (51.87->58.42), wheels 1 (17.12->22.42), wool 1 (6.25->8.74) | dyed cloth 14 (11.23->19.95), cloth 24 (7.77->10.1), garments 2 (26.04->28.6), candles 1 (79.28->83.5) | +218 |
| Rotterburg | 1056 | 0.38 | 0.20 (22/turn) | paper 3 (20.06->21.85), glass ingots 1 (51.87->55.1), wheels 1 (17.12->19.95), wool 1 (6.25->7.5) | dyed cloth 14 (13.55->19.95), cloth 24 (7.19->10.1), garments 2 (24.15->28.6), candles 1 (76.12->83.5) | +170 |
| Kirchwerp | 1072 | 0.39 | 0.40 (43/turn) | thread 61 (4.26->4.8), wool 1 (6.25->8.22), nets 6 (32.2->33.06), spirits 2 (10.29->11.21) | dyed cloth 14 (13.65->19.95), cloth 24 (7.56->10.1), garments 2 (23.1->28.6), candles 1 (78.75->83.5) | +165 |
| Grandgues | 152 | 0.04 | 0.80 (86/turn) | firewood 33 (3.57->6.46), timber 23 (7.4->10.07), bread 151 (2.33->2.64), logs 1 (3.95->7.79) | wine 2 (6.83->8.22), candles 1 (81.9->83.5), bricks 4 (7.98->8.98), slaked lime 2 (10.5->10.83) | +142 |
| Fontaux | 411 | 0.12 | 0.70 (75/turn) | timber 23 (7.4->11.49), thread 61 (4.26->4.8), charcoal 17 (3.38->5.46), furniture 12 (15.23->16.25) | dyed cloth 2 (13.55->19.95), candles 1 (78.23->83.5), flax fibres 5 (4.94->6), wine 2 (6.83->8.22) | +140 |

**Best:** Heilegg at about +218 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 32 = 7.5 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 16.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 27.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 17) |
| light armour | 1 @ 94.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.4/turn (observed), makes 0.0, holds 1 = 2.7 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.3k (cash + stock at home prices); -594/turn over 6 turns, -5/turn over 24 turns.
- Limits: cash flow >= -249/turn, prestige >= +1.01/turn (values are after 200 tax a turn).
- Today's settings: value +74/turn, cash +64/turn, prestige -1.59/turn - breaks the prestige floor.
- Plan: value -37/turn, cash +85/turn, prestige +1.01/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +127 vs +81, +3 vs +80, +64 vs +68.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Dortgart: +2/turn
  - ship Flax Wyrm -> Karlmoor: +6/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: +3/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.10: +14/turn
  - weavery 1 0.50 -> 0.61: -8/turn
  - sewing shop 1 0.30 -> 0.36: +9/turn
  - brewery 1 0.14 -> 0.20: -13/turn
  - spinnery 1 1.65 -> 0.99: -14/turn
  - retting pit 1 0.91 -> 0.56: +5/turn
- HAND-OVER: goal planner: model check failed 3 runs in a row, rates handed back to the old rules.
- Model check over the last 62 turns: predicted +99/turn for the settings we ran, real +28/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 3.96, cloth 6.33, flax fibres 4.69, garments 18.30, nets 28.49, beer 2.95, timber 3.17, prestige 55.96, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 17); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.10, worth +7/turn.
- Ship linen snake: Grandgues -> Dortgart (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Karlmoor (+6/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 436 (+147 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.89 |
| ret | 3 | 0.91 | 0.98 |
| spin | 4 | 1.65 | 1.73 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 558/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.4; ask over the cap 2.1 (60 coin per prestige)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.0 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
