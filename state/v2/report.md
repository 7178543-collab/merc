# v2 shadow report

Turn 13852, 2026-11-07 13:26. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,649, prestige 3,367 (247 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 9 | 0 | 0 | 0 | 0 | min_holding 60, sell 3, sell @ 3.06; stop 26, buy 9, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 505 | 0 | 24 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.58 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.58 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.30 x9, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 24 labour expired last turn (~41 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 607

## Prestige spending, cheapest coin per prestige first

549 turns left: prestige gained now converts 93.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.4 | 54.4 | thin at home: pasties, wine, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 54.5 | 54.7 | needs a arena (build cost 25,853); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.1 | 55.1 |  |
| hold banquet 4 (premium) | mansion | 20 | 56.3 | 56.3 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.4 | 57.4 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 59.7 | 59.7 | thin at home: wine, cheese |
| jousting 2 | arena | 210 | 59.7 | 59.9 | needs a arena (build cost 25,853); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 60.0 | 60.0 |  |
| hold banquet 3 (pies) | mansion | 8 | 60.0 | 60.0 | thin at home: pasties, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 62.0 | 62.0 | thin at home: pasties, wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 14.2 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 8 @ 15.8 (keep 14); best orders clear only 14 a turn after crew: ship stays at 0
- best towns now: Orlesailles +29, Rouhomme +25, Chatgnan +22, Bordees +22, Toqueque +21
- Orlesailles would trade: pasties buy 8 @ 13.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.12 | 1.00 (106/turn) | garments 8 (18.83->26.6), timber 20 (7.4->12.06), firewood 17 (2.71->7.46), hides 0 (11.03->11.4) | candles 0 (76.65->84.5), cloth 1 (7.25->9.15), gears 0 (67.2->71.72), flax plants 2 (1.11->1.57) | +161 |
| Marmont | 638 | 0.18 | 0.10 (11/turn) | garments 10 (18.83->30.78), hinges 1 (37.59->42.18), premium steel 1 (37.59->39.14), axes 1 (18.48->18.9) | tapestries 1 (619.5->636.5), acid 1 (114.45->124.45), candles 1 (79.8->84.5), varnish 1 (14.38->16.25) | +160 |
| Hanstein | 380 | 0.11 | 0.30 (32/turn) | garments 10 (18.83->22.99), timber 14 (7.4->11.59), mouldboards 1 (38.22->40.28), salt 4 (4.37->4.73) | cloth 23 (7.19->9.15), thread 43 (4.91->5.4), cheese 4 (6.83->9.17), seeds 13 (1.86->2.32) | +154 |
| Etallaen | 774 | 0.22 | 0.40 (42/turn) | garments 10 (18.83->25.84), nets 4 (33.6->38.38), cured fish 6 (25.41->28.5), honey 4 (8.14->12.25) | candles 1 (78.23->84.5), thread 7 (4.73->5.4), gears 1 (69.3->71.72), cloth 8 (8.77->9.15) | +136 |
| Chatgnan | 728 | 0.21 | 0.10 (11/turn) | garments 10 (18.83->27.93), tackles 1 (202.65->222.3) | cloth 16 (8.29->9.15), cheese 4 (7.19->9.17), candles 1 (79.8->84.5), gears 1 (68.78->71.72) | +132 |

**Best:** Fontaux at about +161 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 13, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.3k (cash + stock at home prices); +154/turn over 6 turns, -40/turn over 24 turns.
- Limits: cash flow >= -319/turn, prestige >= +2.21/turn (values are after 200 tax a turn).
- Today's settings: value +80/turn, cash +66/turn, prestige -1.94/turn - breaks the prestige floor.
- Plan: value -131/turn, cash -123/turn, prestige +2.21/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +155 vs +75, +132 vs +69, +6 vs +67.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +6/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - ropewalk 1 0.25 -> 0.33: +3/turn
  - spinnery 1 1.65 -> 1.34: -8/turn
  - retting pit 1 0.91 -> 0.76: +4/turn
  - flax farm 1 4.64 -> 3.78: +7/turn
  - weavery 1 0.50 -> 0.30: -48/turn
  - sewing shop 1 0.30 -> 0.17: -10/turn
  - mansion 1 0.00 -> 0.99: -163/turn
- Model check over the last 61 turns: predicted +103/turn for the settings we ran, real +73/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.00, beer 3.00, timber 3.17, prestige 58.00, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Brunnham (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 438 (+149 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.95 |
| ret | 3 | 0.91 | 0.99 |
| spin | 4 | 1.65 | 1.75 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 545/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.58; ask over the cap 2.1 (60 coin per prestige)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.1 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
