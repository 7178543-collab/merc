# v2 shadow report

Turn 14084, 2026-11-17 05:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,855, prestige 3,644 (524 free, +47.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 5, buy @ 3.6 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.70 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~33 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 604

## Prestige spending, cheapest coin per prestige first

317 turns left: prestige gained now converts 79.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.6 | 50.0 | needs a arena (build cost 28,404); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.3 | 54.3 | running |
| jousting 2 | arena | 210 | 54.3 | 54.8 | needs a arena (build cost 28,404); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.9 | 57.9 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 61.5 | 61.5 | thin at home: wine, cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 63.1 | 63.1 |  |
| hold banquet 2 (pies) | mansion | 7 | 63.3 | 63.3 | thin at home: pasties, wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 64.5 | 64.5 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 64.7 | 64.7 | thin at home: pasties, hop beer, pies |
| hold banquet 4 (premium) | mansion | 20 | 64.9 | 64.9 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 60.5 | 65.0 | needs a cathedral (build cost 318,680); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 (pies) | mansion | 18 | 65.1 | 65.1 | thin at home: hop beer, wine, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.3 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 8 @ 16.0 (keep 14); best orders clear only 12 a turn after crew: ship stays at 0
- best towns now: Amsdermund +684, Hofkirchen +482, Gotthafen +441, Chatgnan +389, Heidlowe +382
- Amsdermund would trade: furniture buy 63 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.13 | 0.50 (58/turn) | thread 46 (5.1->7.27), garments 10 (26.4->34.2), furniture 8 (16.48->21.28), flour 2 (18.38->30.4) | tools 15 (5.15->6.51), ploughs 1 (70.35->83.12), dyed cloth 4 (15.23->17.76), bricks 8 (9.82->13.11) | +293 |
| Grandgues | 152 | 0.05 | 0.80 (93/turn) | timber 30 (8.03->12.35), firewood 31 (2.84->6.65), bread 161 (2.56->3.06), furniture 8 (16.48->16.91) | candles 1 (81.9->89.5), garments 2 (26.46->28.6), dyed cloth 6 (17.32->17.76), flax fibres 4 (7.19->7.8) | +258 |
| Kirchwerp | 1072 | 0.42 | 0.60 (70/turn) | honey 9 (8.56->11.11), thread 91 (5.1->5.7), lead ore 9 (7.88->10.45), chisels 3 (11.03->12.06) | cloth 24 (7.51->11.3), flax fibres 28 (5.78->7.8), dyed cloth 7 (13.76->17.76), tools 15 (5.57->6.51) | +204 |
| Amsdermund | 1111 | 0.44 | 0.30 (35/turn) | flour 2 (18.38->24.89), chisels 3 (11.03->13.3), hides 1 (11.03->12.25) | cloth 24 (6.67->11.3), dyed cloth 7 (13.44->17.76), medicine 1 (131.25->157.7), candles 1 (78.75->89.5) | +188 |
| Pontmont | 341 | 0.11 | 1.00 (116/turn) | firewood 26 (2.84->9.5), bread 80 (2.56->3.1), honey 3 (8.56->10.83), tiles 2 (3.91->8.55) | bricks 6 (9.55->13.11), tools 7 (5.35->6.51), butter 0 (72.45->78.85), cookware 1 (21->22.61) | +146 |

**Best:** Fontaux at about +293 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.56, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.9k (cash + stock at home prices); -111/turn over 6 turns, -22/turn over 24 turns.
- Limits: cash flow >= -286/turn, prestige >= -0.93/turn (values are after 200 tax a turn).
- Today's settings: value +89/turn, cash +75/turn, prestige +47.17/turn.
- Plan: value +476/turn, cash +311/turn, prestige +39.17/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +164 vs +69, +101 vs +73, +160 vs +66.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +4/turn
  - ship Flax Wyrm -> Brunnham: +0/turn
  - park 1 16.00 -> 0.00: +52/turn
  - flax farm 1 4.64 -> 8.23: +27/turn
  - retting pit 1 0.91 -> 1.62: +53/turn
  - weavery 1 0.50 -> 1.28: +21/turn
  - spinnery 1 1.65 -> 2.73: +143/turn
  - net maker [make nets 1] 0.00 -> 0.38: +47/turn
  - sewing shop 1 0.30 -> 0.37: +12/turn
  - brewery 1 0.14 -> 0.00: +15/turn
- Model check over the last 60 turns: predicted +47/turn for the settings we ran, real -11/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.26, thread 3.19, cloth 5.08, flax fibres 3.80, garments 14.70, nets 23.84, beer 2.86, timber 3.44, prestige 0.00, cash 0.00
- Orders it would set: bread buy 5 (v2 6); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.04, worth +2/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.32, worth +29/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +14/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brunnham (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +63/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~5675 coin: +20/turn, payback 284 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - new leatherworks (make leather armour 1) for ~4240 coin: +8/turn, payback 539 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate park 1: +96/turn (tax 96 saved).

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

Buffers: flax fibres 83/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.7; ask over the cap 2.1 (60 coin per prestige)
