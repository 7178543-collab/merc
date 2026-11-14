# v2 shadow report

Turn 14025, 2026-11-14 18:09. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,672, prestige 3,601 (481 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 88 | 20 | 12 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 528 | 0 | 36 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.40 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.40 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 36 labour expired last turn (~60 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 529, not 628
- labour expiry guard: 36 bought labour expired last turn, buy 29 (not 29) this turn

## Prestige spending, cheapest coin per prestige first

376 turns left: prestige gained now converts 84.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| jousting 3 | arena | 230 | 54.5 | 54.8 | needs a arena (build cost 26,093); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 58.0 | 58.0 | thin at home: pies |
| hold banquet 3 (pies) | mansion | 8 | 58.4 | 58.4 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 59.1 | 59.1 | thin at home: hop beer, ham, stockfish |
| jousting 2 | arena | 210 | 59.7 | 60.1 | needs a arena (build cost 26,093); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.4 | 60.4 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 62.0 | 62.0 | thin at home: hop beer, cured fish |
| hold banquet 4 (premium) | mansion | 20 | 62.1 | 62.1 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 62.2 | 62.2 | running |
| hold banquet 4 | mansion | 17.5 | 63.1 | 63.1 | thin at home: hop beer, ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.5 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.4 (keep 14); best orders clear only 15 a turn after crew: ship stays at 0
- best towns now: Amsdermund +717, Hofkirchen +652, Chatgnan +477, Gotthafen +466, Bedenis +375
- Amsdermund would trade: furniture buy 65 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (98/turn) | timber 42 (7.98->12.06), firewood 29 (3.57->6.65), bread 157 (2.5->2.74), charcoal 19 (2.69->3.53) | tools 25 (6.41->7.03), cloth 6 (8.51->9.5), beer 11 (3.46->3.7), cheese 5 (6.62->7.12) | +255 |
| Rouhomme | 368 | 0.11 | 0.60 (65/turn) | windows 2 (813.75->855), bread 157 (2.5->2.96), flour 2 (21.84->26.03), tin ingots 1 (34.86->37.43) | tools 46 (5.02->7.03), cloth 9 (8.19->9.5), butter 1 (75.6->77.9), cookware 5 (24.99->25.46) | +214 |
| Blanans | 297 | 0.09 | 0.60 (65/turn) | timber 42 (7.98->12.44), cheese 10 (8.09->10.92), jewellery 3 (97.65->100.7), limestone 1 (18.27->24.89) | cloth 13 (7.56->9.5), dyed cloth 6 (11.23->12.16), garments 2 (22.68->22.8) | +202 |
| Kirchwerp | 1072 | 0.39 | 0.50 (54/turn) | thread 91 (4.66->5.61), wax 12 (22.89->24.7), honey 6 (9.03->10.26), resin 5 (2.5->3.93) | tools 46 (5.83->7.03), cloth 13 (7.51->9.5), cookware 5 (24.36->25.46), cheese 5 (6.2->7.12) | +144 |
| Angefont | 686 | 0.20 | 0.30 (33/turn) | jewellery 3 (97.65->99.75), rope 1 (78->83.6), resin 5 (2.5->3.38), salt 4 (4.73->4.94) | tools 46 (5.15->7.03), flax fibres 28 (5.04->6.6), cloth 13 (8.51->9.5), cheese 5 (6.04->7.12) | +138 |

**Best:** Grandgues at about +255 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 12 @ 3.88, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 88 = 7.5 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 90.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 29) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 35.8) |
| pasties |  | 1 @ min 12.3 | goal planner: sells 1 a turn at 12.3, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 76.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.6k (cash + stock at home prices); -476/turn over 6 turns, -207/turn over 24 turns.
- Limits: cash flow >= -320/turn, prestige >= -0.75/turn (values are after 200 tax a turn).
- Today's settings: value -183/turn, cash -167/turn, prestige +1.60/turn.
- Plan: value -28/turn, cash -17/turn, prestige -0.75/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -30 vs -164, -197 vs -156, +309 vs -163.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bremcop: +7/turn
  - ship Flax Wyrm -> Vauxvais: +2/turn
  - mansion 1 1.00 -> 0.44: +142/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.33: +1/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - flax farm 1 4.64 -> 4.19: +4/turn
  - sewing shop 1 0.30 -> 0.22: -13/turn
  - weavery 1 0.50 -> 0.38: +11/turn
- Model check over the last 59 turns: predicted -44/turn for the settings we ran, real -37/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.14, beer 3.11, timber 3.42, prestige 59.42, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 29); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Bremcop (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 425 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.50 |
| ret | 3 | 0.91 | 0.90 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 96/77, thread 1049/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.4; ask over the cap 2.1 (60 coin per prestige)
- R1: prestige rate -0.50 a turn vs 12-turn median +1.63; likely: dry slot: firewood
