# v2 shadow report

Turn 13916, 2026-11-10 05:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,058, prestige 3,472 (352 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 23 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 500 | 0 | 29 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~43 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 503, not 603

## Prestige spending, cheapest coin per prestige first

485 turns left: prestige gained now converts 91.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.7 | 44.7 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 53.6 | 53.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.2 | 54.2 | thin at home: pasties, hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 54.8 | 55.1 | needs a arena (build cost 25,528); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 55.4 | 55.4 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 55.8 | 55.8 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.4 | 56.4 | thin at home: hop beer, cheese |
| hold banquet 4 | mansion | 17.5 | 56.5 | 56.5 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 59.6 | 59.6 | thin at home: pasties, hop beer, pies |
| jousting 2 | arena | 210 | 60.1 | 60.3 | needs a arena (build cost 25,528); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 60.6 | 60.6 | thin at home: pasties, cheese, pies |
| hold feast 2 | townhouse | 2.6 | 56.1 | 63.8 | needs a townhouse (build cost 9,234) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 13 @ 14.6; crew 0.1; est +46 a turn; stock: pasties 13 @ 14.6 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.0 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Vauxvais +83, Clairlond +73, Friedwerp +72, Marmont +70, Chatgnan +67
- Vauxvais would trade: pasties buy 14 @ 12.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (87/turn) | firewood 31 (3.11->10.07), beer 57 (3.55->5.98), charcoal 19 (2.75->5.42), bread 154 (2.18->2.53) | cured meat 4 (26.25->27.74), bricks 1 (9.4->15.67), nails 3 (7.46->7.98), yarn 2 (4.81->4.99) | +422 |
| Fontaux | 411 | 0.11 | 1.00 (96/turn) | thread 69 (5.15->7.27), bread 108 (2.18->3.4), beer 41 (3.55->4.69), tapestries 0 (614.25->665) | cloth 6 (8.4->8.8), bricks 0 (11.45->15.67), jewellery 1 (103.43->104.5), flax plants 3 (1.52->1.88) | +363 |
| Etallaen | 774 | 0.20 | 1.00 (96/turn) | bread 90 (2.18->3.74), beer 33 (3.55->5.61), tapestries 0 (614.25->665), charcoal 11 (2.75->5.61) | cloth 3 (7.72->8.8), bricks 0 (8.61->15.67), nails 1 (7.61->7.98), flax plants 4 (1.44->1.88) | +203 |
| Rouhomme | 368 | 0.10 | 0.50 (48/turn) | bread 154 (2.18->3.04), tapestries 1 (614.25->646), thread 22 (5.15->6.27), grain 2 (2.4->3.4) | cloth 24 (7.25->8.8), bricks 1 (6.98->15.67), candles 1 (81.9->84.5), tools 17 (4.89->5.18) | +196 |
| Kleinburgh | 1440 | 0.54 | 0.10 (10/turn) | tapestries 1 (614.25->807.5), honey 1 (8.09->10.36), nets 3 (39.2->41.04), cloth 1 (6.24->8.03) | - | +193 |

**Best:** Grandgues at about +422 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 5 @ 3.54, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 23 = 5.5 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 13.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 3) |
| light armour | 1 @ 106, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 38.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.3k (cash + stock at home prices); +148/turn over 6 turns, +190/turn over 24 turns.
- Limits: cash flow >= -336/turn, prestige >= -0.22/turn (values are after 200 tax a turn).
- Today's settings: value +85/turn, cash +63/turn, prestige -1.97/turn - breaks the prestige floor.
- Plan: value +1/turn, cash +5/turn, prestige -0.22/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -17 vs +72, +89 vs +75, +74 vs +68.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +31/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +9/turn
  - flax farm 1 4.64 -> 5.38: -4/turn
  - retting pit 1 0.91 -> 1.05: -0/turn
  - spinnery 1 1.65 -> 1.86: +7/turn
  - sewing shop 1 0.30 -> 0.36: -8/turn
  - weavery 1 0.50 -> 0.60: +12/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.18: -16/turn
  - ropewalk 1 0.25 -> 0.00: +26/turn
- Model check over the last 59 turns: predicted +105/turn for the settings we ran, real +69/turn.
- Worth of one more unit per turn: labour 1.49, thread 3.75, cloth 5.98, flax fibres 4.44, garments 17.30, nets 27.30, beer 2.85, timber 3.35, prestige 64.86, cash 0.00
- Orders it would set: arms buy 1 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 3); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.18, worth +12/turn.
- Ship linen snake: Grandgues -> Donaunieder (+32/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +75/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1741 coin: +4/turn, payback 427 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 1020/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.6 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
