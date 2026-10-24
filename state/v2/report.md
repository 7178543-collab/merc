# v2 shadow report

Turn 13514, 2026-10-24 11:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,239, prestige 3,581 (461 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 72 | 0 | 7 | 0 | 0 | min_holding 60, sell 82, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 7 | 0 | 8 | 0 | 0 | stop 6, buy 2, buy @ 2.4; sell 1, sell @ 1.67 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 59 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 17.9 |
| grain | 84 | 38 | 41 | 0 | 0 | stop 149, buy 38, buy @ 3.7 |
| labour | 73 | 73 | 566 | 0 | 7 | buy 73, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 12 | 12 | 12 | 0 | 0 | buy 12, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **varnish**: net maker152202386007001 ran short of varnish (no buy order); labour need rises ~6/turn when they restart -> v2: add a varnish buy
- **varnish**: needed (0.1/turn) but there is NO buy order, stock 0.0 -> v2: add buy 1

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57
- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 566, not 636

## Prestige spending, cheapest coin per prestige first

887 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.3 | 45.3 | running |
| hold banquet 4 (pies) | mansion | 18 | 48.6 | 48.6 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.9 | 49.9 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.8 | 50.8 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 51.7 | 51.7 | thin at home: wine, hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 51.6 | 51.7 | needs a arena (build cost 24,058); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 50.0 | 52.8 | needs a chapel (build cost 30,660); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.0 | 53.0 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 53.0 | 53.0 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 54.0 | 54.0 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 54.1 | 54.1 | thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 51.5 | 54.2 | needs a church (build cost 65,012); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~95 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.10 | 0.30 (28/turn) | thread 64 (4.34->5.65), glassware 2 (50.82->57.95), charcoal 12 (1.87->3.55), garments 5 (17.8->18.62) | wax 7 (20.68->21.47), furniture 1 (14.38->14.9), raw cloth 2 (6.41->6.65) | +104 |
| Birkeningen | 1006 | 0.31 | 0.80 (76/turn) | beer 50 (2.98->4.89), garments 5 (17.8->24.7), wine 5 (6.2->7.08), cloth 3 (6.95->7.98) | gears 2 (59.85->61.27) | +102 |
| Hanbrücken | 531 | 0.13 | 0.10 (9/turn) | looms 1 (656.25->698.25), rope 2 (73->76.95), ham 1 (57.23->60.32), garments 5 (17.8->18.14) | lathes 1 (189->205.2), tackles 1 (153.3->161.5), fleece 1 (5.1->5.98), furniture 1 (13.65->14.9) | +73 |
| Dedlowe | 1146 | 0.38 | 0.10 (9/turn) | windows 1 (598.5->655.5), rope 1 (73->79.33), light armour 1 (80.33->85.02), wine 3 (6.2->7.84) | blades 1 (14.8->15.86), wax 2 (21->21.47) | +71 |
| Darmwald | 1022 | 0.32 | 0.60 (57/turn) | beer 79 (2.98->3.84), leather 1 (30.24->38), ham 1 (57.23->62.22), cured fish 4 (25.2->26.6) | lathes 1 (174.3->205.2), blades 1 (14.28->15.86) | +66 |

**Best:** Fontaux at about +104 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 82 @ min 2.98 | goal planner: sells 82 at 2.98 (v2 had 82 at 3.38) |
| cloth |  | 1 @ min 7 | goal planner: sells 1 a turn at 7, keeps 33 (no one offered it) |
| cured meat | 1 @ 29.0, stop 4 |  | uses 0.9/turn (mansion 1), makes 0.0, holds 4 = 4.2 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 6 | 1 @ min 1.71 | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 2) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 10 @ min 17.8 | goal planner: sells 10 at 17.8 (v2 had 10 at 20.0) |
| grain | 38 @ 3.7, stop 150 |  | goal planner: buys 38 a turn for today's rates, keeps up to 150 (v2 had 82) |
| labour | 73 @ 2.2, stop - |  | goal planner: buys 73 for today's rates (v2 had 66) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 12 @ 1.1, stop - |  | goal planner: buys 12 for today's rates (v2 had 12) |
| rope |  | 5 @ min 71.0 | makes 2.9, uses 0.0, holds 29 (keeps 0): sells the surplus + 2/turn of the excess |
| tar | 2 @ 11.0, stop 3 |  | uses 0.6/turn (ropewalk 1), makes 0.0, holds 1 = 0.9 turns |
| thread |  | 6 @ min 4.34 | goal planner: sells 6 a turn at 4.34, keeps 225 (no one offered it) |
| tools | 2 @ 6.2, stop 13 |  | uses 1.5/turn (retting pit 1), makes 0.0, holds 200 = 131.4 turns |
| varnish | 1 @ 17.1, stop 1 |  | uses 0.1/turn (observed), makes 0.0, holds 0 = 0.0 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.9k (cash + stock at home prices); +94/turn over 6 turns, +73/turn over 24 turns.
- Limits: cash flow >= +115/turn, prestige >= -0.67/turn (values are after 240 tax a turn).
- Today's settings: value +11/turn, cash +5/turn, prestige -0.66/turn - breaks the cash floor.
- Plan: value +63/turn, cash +119/turn, prestige -0.67/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -62 vs +118, -10 vs +142, -127 vs +35 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +3/turn
  - ship Flax Wyrm -> Bedenis: +1/turn
  - net maker 0.25 -> 0.58: +21/turn
  - brewery 1 0.63 -> 0.58: +8/turn
  - logging camp w/ tool 5.00 -> 0.00: +4/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 4.01: +3/turn
  - flax farm 1 4.60 -> 4.44: +1/turn
  - spinnery 1 1.70 -> 1.61: +1/turn
  - weavery 1 0.23 -> 0.16: -3/turn
  - sewing shop 1 0.14 -> 0.08: +6/turn
- Model check over the last 19 turns: predicted +149/turn for the settings we ran, real +86/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.52, thread 3.79, cloth 6.07, flax fibres 4.45, garments 17.60, nets 28.18, beer 2.72, timber 5.32, prestige 55.51, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); grain buy 38 (v2 82); labour buy 73 (v2 66); light armour buy 1 (v2 None); pasties buy 3 (v2 4); thread sell 6 (v2 none); wax buy 1 (v2 None)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 4.01, worth +3/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.66, worth +25/turn.
- Ship linen snake: Grandgues -> Essenbrucke (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bedenis (+0/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +76/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +20/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +17/turn (tax 20 saved).
- Trim: donate weavery 1: +15/turn (tax 18 saved).
- Trim: donate sewing shop 1: +11/turn (tax 12 saved).

## Chain sizing

Mode HOLD, garments sold 2.8/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 432, chain may buy 0 -> chain allowance 68, chain plan 109 (-131 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.47 |
| ret | 3 | 0.76 | 0.44 |
| spin | 4 | 1.70 | 0.91 |
| weave | 3 | 0.23 | 0.00 |
| sew | 2 | 0.14 | 0.00 |

Buffers: flax fibres 38/51, thread 637/151, cloth 34/0
- chain plan needed 109 labour, budget left 68: cut to 109

## Self-diagnosis

Nothing found this run.
