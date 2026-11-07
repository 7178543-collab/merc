# v2 shadow report

Turn 13850, 2026-11-07 11:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,511, prestige 3,371 (251 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 4, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 517 | 0 | 12 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.32 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.32 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Notes

- labour: projection runs 100 over real use lately; planning 517, not 617

## Prestige spending, cheapest coin per prestige first

551 turns left: prestige gained now converts 93.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.2 | 54.2 | thin at home: pasties, wine, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 54.1 | 54.3 | needs a arena (build cost 26,618); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 56.2 | 56.2 | thin at home: wine, ham, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 57.2 | 57.2 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 59.0 | 59.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.3 | 59.3 | thin at home: wine, cheese |
| jousting 2 | arena | 210 | 59.3 | 59.5 | needs a arena (build cost 26,618); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 59.7 | 59.7 | thin at home: pasties, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 59.9 | 59.9 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.5 | 61.5 | thin at home: pasties, wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.072 | - | pasties 1 | -15 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.108 | - | pasties 3 | -47 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 14.9 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.9 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Rouhomme +20, Toqueque +18, Orlesailles +17, Bremcop +16, Clarfranche +16
- Rouhomme would trade: pasties buy 6 @ 13.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.21 | 0.40 (41/turn) | beer 69 (3.46->5.84), garments 10 (18.74->25.65), cured fish 6 (25.41->28.12), cured meat 4 (24.57->26.6) | candles 1 (77.17->84.5), bellows 1 (256.2->260.3), thread 7 (4.73->5.35), flax fibres 4 (5->5.9) | +253 |
| Hofkirchen | 991 | 0.33 | 0.70 (72/turn) | beer 69 (3.46->6.08), garments 10 (18.74->22.61), nets 5 (33.6->41.04), light armour 8 (98.7->100.7) | cheese 5 (5.78->8.98), dyed cloth 9 (10.24->11.11), candles 1 (79.8->84.5), jewellery 10 (87.15->87.88) | +252 |
| Kleinburgh | 1440 | 0.57 | 0.20 (21/turn) | cloth 13 (8.82->17.1), garments 10 (18.74->26.22), nets 3 (33.6->39.52) | cheese 5 (6.25->8.98), candles 1 (76.65->84.5), jewellery 1 (81.38->87.88) | +207 |
| Amsdermund | 1111 | 0.39 | 0.30 (31/turn) | nets 6 (33.6->43.32), garments 10 (18.74->19.95), spirits 1 (10.29->17), rope 1 (80->85.5) | jewellery 10 (81.9->87.88), candles 1 (74.55->84.5), cheese 5 (6.72->8.98), thread 20 (4.51->5.35) | +160 |
| Darmwald | 1022 | 0.34 | 0.10 (10/turn) | garments 10 (18.74->31.35), gears 1 (55.65->60.8), spirits 1 (10.29->14.82), hides 1 (11.13->12.35) | cheese 5 (6.46->8.98) | +141 |

**Best:** Etallaen at about +253 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 4 @ min 3.06 | goal planner: sells 4 a turn at 3.06, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 12.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 17) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.8k (cash + stock at home prices); +154/turn over 6 turns, -40/turn over 24 turns.
- Limits: cash flow >= -313/turn, prestige >= +2.05/turn (values are after 200 tax a turn).
- Today's settings: value +82/turn, cash +69/turn, prestige -1.96/turn - breaks the prestige floor.
- Plan: value -124/turn, cash -121/turn, prestige +2.05/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +139 vs +69, +145 vs +76, +155 vs +75.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - spinnery 1 1.65 -> 1.31: -9/turn
  - retting pit 1 0.91 -> 0.74: +5/turn
  - flax farm 1 4.64 -> 3.75: -1/turn
  - weavery 1 0.50 -> 0.32: -37/turn
  - sewing shop 1 0.30 -> 0.18: -15/turn
  - mansion 1 0.00 -> 0.95: -159/turn
- Model check over the last 61 turns: predicted +103/turn for the settings we ran, real +72/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.20, cloth 6.68, flax fibres 5.05, garments 19.30, nets 29.96, beer 2.92, timber 3.26, prestige 57.64, cash 0.00
- Orders it would set: beer sell 4 (v2 none); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 17); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Amsdermund (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 438 (+150 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.96 |
| ret | 3 | 0.91 | 0.99 |
| spin | 4 | 1.65 | 1.75 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 545/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.36 (ask 3.3, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.32; ask over the cap 2.1 (60 coin per prestige)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.9 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
