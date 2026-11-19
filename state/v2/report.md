# v2 shadow report

Turn 14134, 2026-11-19 07:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,964, prestige 3,653 (533 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 29 | 11 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 47, buy 24, buy @ 3.78 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 528 | 0 | 36 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.7 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.80 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.80 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 36 labour expired last turn (~69 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 116 over real use lately; planning 528, not 634

## Prestige spending, cheapest coin per prestige first

267 turns left: prestige gained now converts 73.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.3 | 50.6 | needs a arena (build cost 27,897); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.0 | 54.3 | needs a arena (build cost 27,897); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.4 | 54.9 | needs a arena (build cost 27,897); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 57.9 | 57.9 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.5 | 58.5 |  |
| hold banquet 4 (pies) | mansion | 18 | 60.1 | 60.1 | thin at home: stockfish, pies |
| jousting 2 | arena | 210 | 59.6 | 60.2 | needs a arena (build cost 27,897); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 60.4 | 60.4 |  |
| hold banquet 2 (pies) | mansion | 7 | 61.1 | 61.1 | thin at home: pies |
| hold banquet 3 (pies) | mansion | 8 | 61.5 | 61.5 | thin at home: pies |
| hold mass 2 (premium) | cathedral | 360 | 56.5 | 62.4 | needs a cathedral (build cost 311,870); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 16.0 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Amsdermund +745, Fulkirch +373, Cobholme +322, Brunnham +311, Birkeningen +274
- Amsdermund would trade: candles buy 4 @ 76.5, cured meat buy 1 @ 22.8, furniture buy 64 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~124 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.60 (74/turn) | bread 165 (2.71->3.76), timber 39 (9.24->12.35), charcoal 19 (2.81->4.99), garments 10 (26.4->29.64) | beer 11 (3.51->3.78), hop beer 2 (8.77->9.88), wax 4 (27.51->27.74), garments 2 (34.02->34.2) | +316 |
| Fontaux | 411 | 0.14 | 0.70 (86/turn) | thread 91 (4.98->7.27), garments 10 (26.4->34.01), timber 33 (9.24->12.25), flour 1 (16.38->21.47) | candles 1 (79.28->83), cured meat 3 (24.36->25.2), cloth 10 (11.65->11.9) | +313 |
| Marmont | 638 | 0.21 | 0.10 (12/turn) | garments 10 (26.4->36.1), raw cloth 7 (9.24->15.58), thread 12 (4.98->6.79), flour 2 (16.38->19.76) | furniture 8 (15.65->21.28), paper 1 (21.21->22.61), blades 1 (16.28->16.81) | +202 |
| Bordetes | 831 | 0.28 | 0.20 (25/turn) | garments 10 (26.4->38), lathes 1 (182.7->207.1), raw cloth 6 (9.24->11.69), tin ingots 2 (33.81->39.9) | furniture 8 (18.17->21.28), paper 5 (21.21->22.61), dyed cloth 8 (16.38->17) | +200 |
| Kirchwerp | 1072 | 0.44 | 0.60 (74/turn) | thread 91 (4.98->6.32), nails 19 (7.88->8.79), slaked lime 1 (6.93->11.4), lead ore 2 (7.72->10.45) | dyed cloth 16 (13.23->17), furniture 8 (15.75->21.28), garments 2 (28.35->34.2), wax 7 (26.25->27.74) | +200 |

**Best:** Grandgues at about +316 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 21 @ 3.96, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 29 = 2.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 5 @ 3.7, stop 19 |  | goal planner: buys 5 a turn for today's rates, keeps up to 19 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 28) |
| light armour | 1 @ 100, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.2k (cash + stock at home prices); -150/turn over 6 turns, +2/turn over 24 turns.
- Limits: cash flow >= -457/turn, prestige >= -0.97/turn (values are after 200 tax a turn).
- Today's settings: value -156/turn, cash -147/turn, prestige +1.33/turn.
- Plan: value +8/turn, cash +17/turn, prestige -0.97/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -118 vs -150, +142 vs -144, +87 vs -159.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Pontmont: +22/turn
  - ship Flax Wyrm -> Amsdermund: +2/turn
  - mansion 1 1.00 -> 0.45: +133/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.28: +3/turn
  - spinnery 1 1.65 -> 1.40: -2/turn
  - retting pit 1 0.91 -> 0.79: +4/turn
  - flax farm 1 4.64 -> 3.97: +8/turn
  - weavery 1 0.50 -> 0.41: -16/turn
- Model check over the last 59 turns: predicted +85/turn for the settings we ran, real +76/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.75, beer 3.27, timber 3.58, prestige 62.75, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 28); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Pontmont (+29/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Amsdermund (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 74/77, thread 1049/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 28.6 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 24 @ 3.78, home ask 3.78; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.8; ask over the cap 2.1 (60 coin per prestige)
