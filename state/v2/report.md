# v2 shadow report

Turn 13834, 2026-11-06 19:26. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,912, prestige 3,397 (277 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 36 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
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

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.34 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.34 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~48 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.03, no projection from the game)
- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 503, not 603

## Prestige spending, cheapest coin per prestige first

567 turns left: prestige gained now converts 94.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 53.5 | 53.5 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.0 | 54.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 54.1 | 54.1 | thin at home: wine |
| jousting 3 | arena | 230 | 54.1 | 54.3 | needs a arena (build cost 26,183); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 55.0 | 55.0 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 56.1 | 56.1 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 56.4 | 56.4 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 56.9 | 56.9 | thin at home: hop beer, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 57.1 | 57.1 | thin at home: hop beer |
| hold banquet 1 (meat) | mansion | 4.2 | 57.4 | 57.4 |  |
| hold banquet 2 (pies) | mansion | 7 | 57.5 | 57.5 | thin at home: wine, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: pasties buy 9 @ 15.6; crew 0.1; est +19 a turn; stock: pasties 9 @ 15.6 (keep 14)
- best towns now: Rouhomme +51, Orlesailles +48, Bremcop +40, Grandgues +38, Bordees +36
- Rouhomme would trade: pasties buy 11 @ 13.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.24 | 0.20 (22/turn) | nets 6 (32.2->35.15), yarn 11 (5.21->6.08), wheels 1 (17.12->21.28), lead bars 7 (19.43->19.95) | dyed cloth 25 (10.5->19.76), cloth 24 (7.61->10.7), garments 2 (25.41->29.6), candles 1 (79.28->83.5) | +337 |
| Kirchwerp | 1072 | 0.39 | 0.50 (54/turn) | thread 61 (4.26->4.8), coats 1 (66.67->68.4), spirits 1 (10.29->11.3), nets 6 (32.2->33.06) | dyed cloth 23 (11.03->19.76), cloth 24 (7.35->10.7), garments 2 (23.1->29.6), candles 1 (77.7->83.5) | +295 |
| Rotterburg | 1056 | 0.38 | 0.20 (22/turn) | wheels 1 (17.12->19.95), paper 2 (20.37->21.47) | dyed cloth 25 (13.55->19.76), cloth 24 (7.19->10.7), garments 2 (24.15->29.6), candles 1 (77.17->83.5) | +240 |
| Etallaen | 774 | 0.22 | 0.40 (43/turn) | beer 69 (3.46->4.8), blades 3 (14.07->15.2), wheels 1 (17.12->19.95), nets 4 (32.2->32.87) | dyed cloth 12 (14.18->19.76), cloth 24 (9.45->10.7), candles 1 (79.8->83.5), flax fibres 10 (5.51->6) | +159 |
| Amsdermund | 1111 | 0.41 | 0.60 (65/turn) | wheels 1 (17.12->20.9), charcoal 19 (3.38->6.79), medicine 1 (139.65->142.5) | dyed cloth 19 (13.23->19.76), cloth 8 (7.35->10.7), casks 2 (5.46->6.65), flax fibres 21 (5.17->6) | +148 |

**Best:** Heilegg at about +337 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.06 | goal planner: sells 15 a turn at 3.06, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 28.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 3) |
| light armour | 1 @ 95.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.3k (cash + stock at home prices); -500/turn over 6 turns, -15/turn over 24 turns.
- Limits: cash flow >= -246/turn, prestige >= +0.95/turn (values are after 200 tax a turn).
- Today's settings: value +77/turn, cash +68/turn, prestige -1.59/turn - breaks the prestige floor.
- Plan: value -31/turn, cash +88/turn, prestige +0.95/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +116 vs +72, +127 vs +81, +3 vs +80.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: +3/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.10: +14/turn
  - weavery 1 0.50 -> 0.61: -8/turn
  - sewing shop 1 0.30 -> 0.36: +9/turn
  - brewery 1 0.14 -> 0.20: -13/turn
  - spinnery 1 1.65 -> 0.99: -14/turn
  - retting pit 1 0.91 -> 0.56: +6/turn
- Model check over the last 62 turns: predicted +99/turn for the settings we ran, real +32/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 3.96, cloth 6.33, flax fibres 4.69, garments 18.30, nets 28.48, beer 2.85, timber 3.26, prestige 55.61, cash 0.00
- Orders it would set: beer sell 15 (v2 none); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 3); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.10, worth +7/turn.
- Ship linen snake: Grandgues -> Vauxvais (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/77, thread 547/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.34; ask over the cap 2.1 (60 coin per prestige)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.0 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
