# v2 shadow report

Turn 13787, 2026-11-04 20:05. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,954, prestige 3,317 (197 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 104 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

614 turns left: prestige gained now converts 95.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.8 | 46.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.0 | 51.0 | thin at home: hop beer, stockfish, pies |
| hold banquet 2 (pies) | mansion | 7 | 52.3 | 52.3 | thin at home: pasties, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 52.7 | 52.7 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 53.2 | 53.2 |  |
| jousting 3 | arena | 230 | 53.5 | 53.7 | needs a arena (build cost 25,057); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 53.9 | 53.9 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 55.1 | 55.1 | thin at home: pasties, hop beer, pies |
| hold banquet 4 (premium) | mansion | 20 | 56.1 | 56.1 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 56.6 | 56.6 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 57.1 | 57.1 |  |
| jousting 2 | arena | 210 | 58.6 | 58.8 | needs a arena (build cost 25,057); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 6 @ 14.2; crew 0.1; est +18 a turn; stock: pasties 6 @ 14.2 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.4 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Clairas +27, Boistot +24, Clairlond +24, Orlesailles +24, Essenbrucke +23
- Clairas would trade: pasties buy 6 @ 12.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.40 (39/turn) | cured fish 7 (22.68->29.07), bread 151 (2.39->2.68), timber 25 (7.09->8.22), thread 13 (4.66->5.22) | bricks 2 (7.46->8.6), premium cheese 3 (31.08->31.54), salt 4 (4.68->4.84) | +111 |
| Fontaux | 411 | 0.11 | 0.50 (49/turn) | timber 19 (7.09->10.54), wine 14 (5.83->7.74), cheese 15 (5.99->6.79), nets 4 (34.8->36.86) | grindstones 1 (239.4->266), belts 1 (22.26->28.88), garments 2 (23.1->24) | +107 |
| Briclives | 1041 | 0.33 | 0.20 (19/turn) | wrought iron 8 (14.49->21.47), ham 1 (72.98->80.75), rope 1 (81->88.35), blades 3 (15.12->17.48) | grindstones 1 (241.5->266), garments 2 (20.27->24), malt 5 (3.51->4.8), furniture 1 (12.6->15.3) | +105 |
| Hanstein | 380 | 0.10 | 0.30 (29/turn) | timber 14 (7.09->10.26), garments 10 (18.25->19.95), axes 1 (14.07->17.39), firewood 1 (1.68->4.66) | thread 61 (4.24->4.74), flax fibres 24 (4.49->5.2), premium cheese 3 (29.4->31.54), garments 2 (22.26->24) | +90 |
| Karlmoor | 787 | 0.20 | 0.20 (19/turn) | belts 3 (32.34->40.28), nets 4 (34.8->38.95), rope 1 (81->91.2), limestone 1 (16.48->33.63) | garments 2 (20.37->24), furniture 1 (13.55->15.3), yarn 3 (4.16->4.75), hop beer 1 (8.98->9.59) | +70 |

**Best:** Grandgues at about +111 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 22.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 89, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 18.0k (cash + stock at home prices); -390/turn over 6 turns, -55/turn over 24 turns.
- Limits: cash flow >= -165/turn, prestige >= +4.30/turn (values are after 200 tax a turn).
- Today's settings: value +92/turn, cash +100/turn, prestige -0.99/turn - breaks the prestige floor.
- Plan: value -135/turn, cash -125/turn, prestige +3.21/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +72 vs +77, -117 vs +72, +150 vs +69.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +12/turn
  - ship Flax Wyrm -> Unterhufe: +2/turn
  - net maker 0.00 -> 0.29: +6/turn
  - sewing shop 1 0.30 -> 0.36: -2/turn
  - weavery 1 0.50 -> 0.62: +6/turn
  - spinnery 1 1.65 -> 1.99: -5/turn
  - flax farm 1 4.64 -> 5.70: -9/turn
  - retting pit 1 0.91 -> 1.13: +13/turn
  - brewery 1 0.14 -> 0.27: -19/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.30: -24/turn
- HAND-OVER: goal planner: model check failed 3 runs in a row, ships handed back to the old rules.
- Model check over the last 60 turns: predicted +97/turn for the settings we ran, real +43/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.56, thread 3.92, cloth 6.26, flax fibres 4.64, garments 18.11, nets 28.34, beer 2.81, timber 3.04, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +15/turn.
- Ship linen snake: Grandgues -> Angefont (+12/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Unterhufe (+2/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 480 (+191 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.90 |
| ret | 3 | 0.91 | 1.18 |
| spin | 4 | 1.65 | 2.08 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 344/228, cloth 73/128

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 33.8, home ask 32.2; our bid is already at/over the ask (sellers too thin)
