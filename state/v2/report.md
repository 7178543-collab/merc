# v2 shadow report

Turn 13845, 2026-11-07 06:32. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,900, prestige 3,380 (260 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 8 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 29, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 507 | 0 | 22 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 7.6 -> v2: add buy 5
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.26 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.26 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~35 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 607

## Prestige spending, cheapest coin per prestige first

556 turns left: prestige gained now converts 93.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 |  |
| jousting 3 | arena | 230 | 53.4 | 53.7 | needs a arena (build cost 25,777); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 54.0 | 54.0 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 56.5 | 56.5 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 57.1 | 57.1 | thin at home: pasties, wine, cheese |
| hold banquet 4 | mansion | 17.5 | 57.3 | 57.3 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 57.5 | 57.5 |  |
| hold banquet 3 (pies) | mansion | 8 | 57.9 | 57.9 | thin at home: pasties, cheese |
| hold banquet 4 (premium) | mansion | 20 | 58.1 | 58.1 | thin at home: wine, ham, stockfish |
| jousting 2 | arena | 210 | 58.5 | 58.8 | needs a arena (build cost 25,777); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 59.0 | 59.0 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 14.9 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.7 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Clarfranche +19, Bedenis +16, Rouhomme +15
- Clarfranche would trade: pasties buy 5 @ 13.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.32 | 0.90 (92/turn) | beer 118 (3.46->5.22), glass ingots 1 (51.87->60.32), lead bars 9 (19.74->20.71), lead ore 1 (13.65->18.24) | cheese 8 (5.78->7.46), ham 1 (107.1->114), slaked lime 2 (7.25->10.83), flax fibres 27 (5.17->5.95) | +186 |
| Grandgues | 152 | 0.04 | 0.30 (31/turn) | beer 118 (3.46->4.33), timber 28 (7.14->8.55), glass ingots 1 (51.87->61.27), cured fish 8 (24.15->25.08) | candles 1 (77.7->83.5), cheese 8 (6.67->7.46), thread 10 (5.15->5.35), bricks 3 (7.98->8.93) | +155 |
| Etallaen | 774 | 0.21 | 0.90 (92/turn) | beer 91 (3.46->4.84), cured meat 4 (23.52->28.5), cured fish 6 (24.15->26.79), wool 3 (10.29->11.59) | candles 1 (78.75->83.5), thread 6 (4.73->5.35), cheese 8 (7.09->7.46), chisels 2 (8.09->8.69) | +136 |
| Fontaux | 411 | 0.11 | 1.00 (103/turn) | timber 18 (7.14->11.69), thread 34 (4.66->5.65), beer 38 (3.46->3.89), firewood 14 (3.42->7.22) | - | +104 |
| Dortgart | 1045 | 0.35 | 0.10 (10/turn) | glass ingots 1 (51.87->63.65), nets 2 (32.2->34.2), cloth 1 (8.25->9.17) | tapestries 1 (609->660.25), candles 1 (78.75->83.5), cheese 8 (6.67->7.46), gears 1 (53.55->56.52) | +72 |

**Best:** Hofkirchen at about +186 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.46, stop 9 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 8 = 1.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 12.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.2k (cash + stock at home prices); +20/turn over 6 turns, -39/turn over 24 turns.
- Limits: cash flow >= -288/turn, prestige >= +1.66/turn (values are after 200 tax a turn).
- Today's settings: value +74/turn, cash +56/turn, prestige -1.51/turn - breaks the prestige floor.
- Plan: value -75/turn, cash -68/turn, prestige +1.66/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +52 vs +53, +100 vs +46, +150 vs +60.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.28: +8/turn
  - flax farm 1 4.64 -> 4.33: -0/turn
  - retting pit 1 0.91 -> 0.86: -1/turn
  - spinnery 1 1.65 -> 1.52: +4/turn
  - sewing shop 1 0.30 -> 0.36: -9/turn
  - weavery 1 0.50 -> 0.61: +10/turn
  - mansion 1 0.00 -> 0.75: -165/turn
- Model check over the last 61 turns: predicted +97/turn for the settings we ran, real +73/turn.
- Worth of one more unit per turn: labour 1.64, thread 4.16, cloth 6.62, flax fibres 5.00, garments 19.12, nets 29.65, beer 3.04, timber 3.06, prestige 56.51, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None)
- Ship linen snake: stays on Grandgues (worth +8/turn).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 436 (+147 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.90 |
| ret | 3 | 0.91 | 0.98 |
| spin | 4 | 1.65 | 1.73 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 557/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 7.6 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.36 (ask 3.3, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.26; ask over the cap 2.1 (60 coin per prestige)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.95 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
