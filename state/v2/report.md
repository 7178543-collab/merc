# v2 shadow report

Turn 14022, 2026-11-14 15:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,460, prestige 3,602 (482 free, +75.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 107 | 27 | 14 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 24, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 534 | 0 | 30 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.64 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.64 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 30 labour expired last turn (~51 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 534, not 628

## Prestige spending, cheapest coin per prestige first

379 turns left: prestige gained now converts 85.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| jousting 3 | arena | 230 | 55.7 | 56.1 | needs a arena (build cost 26,596); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.0 | 58.0 | thin at home: pasties, wine |
| hold banquet 4 (pies) | mansion | 18 | 59.7 | 59.7 | thin at home: pasties, hop beer, wine, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 60.5 | 60.5 | thin at home: pasties, hop beer |
| jousting 2 | arena | 210 | 61.0 | 61.4 | needs a arena (build cost 26,596); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 62.8 | 62.8 | thin at home: hop beer, wine, ham, stockfish, premium ham |
| hold banquet 1 (fish) | mansion | 4.2 | 63.2 | 63.2 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 63.4 | 63.4 | thin at home: wine |
| hold banquet 4 | mansion | 17.5 | 63.4 | 63.4 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 63.6 | 63.6 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 63.8 | 63.8 | thin at home: wine, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.5 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.5 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Amsdermund +718, Gotthafen +450, Vauxvais +318, Fulkirch +304, Cobholme +300
- Amsdermund would trade: furniture buy 65 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (108/turn) | timber 43 (8.03->12.16), firewood 29 (3.82->6.6), lathes 1 (182.7->226.1), bread 157 (2.54->2.72) | tackles 1 (156.45->164.35), cured meat 4 (24.15->25.2), garments 2 (22.47->23), tools 19 (6.46->6.55) | +267 |
| Blanans | 297 | 0.09 | 0.70 (75/turn) | timber 43 (8.03->12.44), cheese 13 (7.77->11.78), axes 6 (21.84->22.8), limestone 1 (18.27->24.89) | dyed cloth 10 (10.71->12.63), cloth 13 (7.88->8.55), cured fish 11 (25.62->25.84), garments 2 (22.68->23) | +226 |
| Fontaux | 411 | 0.12 | 1.00 (108/turn) | thread 65 (4.68->5.65), lathes 0 (182.7->224.2), charcoal 15 (2.73->5.18), salt 5 (4.6->7.79) | cured fish 15 (24.57->25.84), cured meat 3 (23.31->25.2), cloth 6 (8.35->8.55), dyed yarn 0 (4.79->5.08) | +185 |
| Rouhomme | 368 | 0.10 | 0.10 (11/turn) | windows 2 (813.75->855), lathes 1 (182.7->220.4), leather 1 (22.68->24.7), tin ingots 1 (36.12->38.57) | tools 19 (5.02->6.55), cloth 12 (8.14->8.55), dyed cloth 8 (12.39->12.63), garments 2 (22.68->23) | +155 |
| Cobholme | 1564 | 0.67 | 0.20 (22/turn) | garments 10 (22.8->27.74), lathes 1 (182.7->212.8), nets 1 (36.6->39.9), leather 1 (22.68->25.27) | tapestries 1 (582.75->650.75) | +134 |

**Best:** Grandgues at about +267 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 15 @ 3.88, stop 57 |  | uses 14.2/turn (household upkeep), makes 0.0, holds 107 = 7.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 81.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 | off | a building is stalled on cured meat: no sell until it runs again |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.2) |
| grain | 6 @ 3.7, stop 24 |  | goal planner: buys 6 a turn for today's rates, keeps up to 24 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 34) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 35.6) |
| pasties |  | 1 @ min 12.3 | goal planner: sells 1 a turn at 12.3, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 82.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 2.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.3k (cash + stock at home prices); -566/turn over 6 turns, -247/turn over 24 turns.
- Limits: cash flow >= -311/turn, prestige >= -0.76/turn (values are after 200 tax a turn).
- Today's settings: value -171/turn, cash -150/turn, prestige +87.20/turn.
- Plan: value +396/turn, cash +270/turn, prestige +75.00/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -280 vs -164, -30 vs -164, -197 vs -156.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> no route: -4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.00: +249/turn
  - park 1 16.00 -> 0.00: +50/turn
  - flax farm 1 4.64 -> 8.56: +19/turn
  - retting pit 1 0.91 -> 1.69: +49/turn
  - net maker [make nets 1] 0.00 -> 0.38: +17/turn
  - sewing shop 1 0.30 -> 0.36: +8/turn
  - weavery 1 0.50 -> 0.72: +21/turn
  - spinnery 1 1.65 -> 2.85: +48/turn
- Model check over the last 58 turns: predicted -37/turn for the settings we ran, real -43/turn.
- Worth of one more unit per turn: labour 0.96, thread 2.41, cloth 3.85, flax fibres 2.88, garments 11.12, nets 18.04, beer 2.50, timber 3.44, prestige 0.00, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 64 (v2 34); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 1.00, worth +37/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +20/turn.
- Ship linen snake: Grandgues -> no route (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +48/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~4665 coin: +14/turn, payback 336 turns, doesn't pay yet (materials thin at home: nails)
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.38 |
| ret | 3 | 0.91 | 0.88 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 104/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.64; ask over the cap 2.1 (60 coin per prestige)
