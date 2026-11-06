# v2 shadow report

Turn 13832, 2026-11-06 17:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,782, prestige 3,400 (280 free, +123.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 44 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 500 | 0 | 29 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~48 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.03, no projection from the game)
- labour: projection runs 100 over real use lately; planning 502, not 602

## Prestige spending, cheapest coin per prestige first

569 turns left: prestige gained now converts 94.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 53.4 | 53.4 | thin at home: hop beer, wine, ham, stockfish, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 54.1 | 54.1 | thin at home: wine |
| jousting 3 | arena | 230 | 54.4 | 54.6 | needs a arena (build cost 26,151); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 54.8 | 54.8 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 56.1 | 56.1 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 56.4 | 56.4 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 56.5 | 56.5 | thin at home: hop beer, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 56.9 | 56.9 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 57.1 | 57.1 | thin at home: wine, pies |
| hold banquet 1 (meat) | mansion | 4.2 | 57.5 | 57.5 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 14 @ 16.0; crew 0.1; est +29 a turn; stock: pasties 14 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.0 (keep 14); best orders clear only 12 a turn after crew: ship stays at 0
- best towns now: Rouhomme +64, Orlesailles +50, Toqueque +38, Bordees +35, Bremcop +31
- Rouhomme would trade: pasties buy 14 @ 13.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~112 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.12 | 0.70 (78/turn) | garments 10 (26->31.73), timber 27 (7.88->11.78), charcoal 17 (3.15->5.37), arms 3 (28.98->32.3) | dyed cloth 3 (13.97->18.81), mouldboards 1 (35.49->44.46), cloth 3 (9.35->12.06), flax fibres 5 (4.94->6.1) | +176 |
| Hanstein | 380 | 0.11 | 0.40 (45/turn) | timber 15 (7.88->11.78), charcoal 19 (3.15->4.14), wine 3 (6.14->6.46), yarn 4 (5.02->5.37) | looms 1 (522.9->593.75), dyed cloth 4 (12.81->18.81), cloth 4 (9.45->12.06), garments 2 (24.78->29.4) | +158 |
| Briclives | 1041 | 0.38 | 0.10 (11/turn) | garments 10 (26->35.15), light armour 1 (96.6->100.7), nets 3 (33->34.77), hop beer 1 (9.5->11.02) | dyed cloth 4 (14.07->18.81), mouldboards 1 (34.65->44.46), cloth 4 (10.5->12.06), candles 1 (78.23->81) | +128 |
| Hanbrücken | 531 | 0.16 | 0.50 (56/turn) | tapestries 1 (750.75->802.75), timber 19 (7.88->10.73), nets 2 (33->34.2), yarn 4 (5.02->5.56) | looms 1 (551.25->593.75), cloth 4 (9.13->12.06), dyed cloth 1 (14.07->18.81), mouldboards 1 (42.42->44.46) | +121 |
| Heilegg | 826 | 0.25 | 0.10 (11/turn) | nets 6 (33->35.34), lead bars 7 (18.69->19.95), hides 1 (11.03->12.44), wine 3 (6.14->6.74) | dyed cloth 14 (13.76->18.81), cloth 4 (7.19->12.06), garments 2 (26.04->29.4), flax fibres 7 (5.19->6.1) | +115 |

**Best:** Fontaux at about +176 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 a turn at 3.06, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 25.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 2) |
| light armour | 1 @ 94, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.3k (cash + stock at home prices); +88/turn over 6 turns, +151/turn over 24 turns.
- Limits: cash flow >= -241/turn, prestige >= +0.81/turn (values are after 200 tax a turn).
- Today's settings: value +82/turn, cash +81/turn, prestige +123.39/turn.
- Plan: value +461/turn, cash +218/turn, prestige +115.39/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +192 vs +71, -292 vs +77, +116 vs +72.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +17/turn
  - ship Flax Wyrm -> no route: +0/turn
  - park 1 16.00 -> 0.00: +49/turn
  - weavery 1 0.50 -> 1.46: +84/turn
  - spinnery 1 1.65 -> 2.64: +54/turn
  - flax farm 1 4.64 -> 7.62: +22/turn
  - retting pit 1 0.91 -> 1.49: +125/turn
  - sewing shop 1 0.30 -> 0.36: +20/turn
  - net maker 0.00 -> 0.19: +11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.13: -12/turn
- Model check over the last 62 turns: predicted +98/turn for the settings we ran, real +62/turn.
- Worth of one more unit per turn: labour 1.42, thread 3.58, cloth 5.71, flax fibres 4.24, garments 16.54, nets 25.95, beer 2.79, timber 3.08, prestige 0.00, cash 0.00
- Orders it would set: beer sell 16 (v2 none); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 2); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.13, worth +10/turn.
- Ship linen snake: Grandgues -> Vauxvais (+26/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +71/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 442 (+153 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.05 |
| ret | 3 | 0.91 | 1.01 |
| spin | 4 | 1.65 | 1.78 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 524/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.1 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
