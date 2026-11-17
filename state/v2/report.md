# v2 shadow report

Turn 14083, 2026-11-17 04:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,695, prestige 3,646 (526 free, +50.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 5, buy @ 3.6 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 1 | 1 | 1 | 0 | stop 7, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.68 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.68 is above our ceiling 2.40 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 2 (need 5) -> v2: buy 5

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

318 turns left: prestige gained now converts 79.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.8 | 50.3 | needs a arena (build cost 28,394); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.0 | 54.0 | running |
| jousting 2 | arena | 210 | 54.6 | 55.1 | needs a arena (build cost 28,394); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.9 | 57.9 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 59.8 | 59.8 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 61.7 | 61.7 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 62.0 | 62.0 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 62.3 | 62.3 | thin at home: hop beer |
| hold banquet 1 (meat) | mansion | 4.2 | 63.1 | 63.1 |  |
| hold banquet 4 (premium) | mansion | 20 | 63.1 | 63.1 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 (pies) | mansion | 18 | 63.2 | 63.2 | thin at home: hop beer, ham, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 63.5 | 63.5 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.9 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.0 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Amsdermund +673, Hofkirchen +504, Gotthafen +431, Chatgnan +377, Bordees +370
- Amsdermund would trade: furniture buy 62 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (103/turn) | timber 38 (8.35->12.54), firewood 31 (2.81->6.7), bread 161 (2.56->3.06), charcoal 19 (2.86->4.8) | bricks 4 (10.19->13.01), candles 1 (81.9->89.5), garments 2 (27.09->29), dyed cloth 5 (16.48->17.1) | +329 |
| Fontaux | 411 | 0.13 | 0.50 (57/turn) | garments 10 (26.4->38), salt 21 (5.67->7.79), thread 47 (5.1->5.65), furniture 7 (18.48->21.47) | tools 16 (5.35->6.37), bricks 8 (9.97->13.01), candles 1 (87.67->89.5) | +257 |
| Amsdermund | 1111 | 0.43 | 0.20 (23/turn) | flour 3 (18.38->23.37), chisels 4 (12.08->13.3), leather 1 (23.1->26.6) | cloth 24 (6.67->10.8), dyed cloth 8 (13.44->17.1), medicine 1 (131.25->157.7), candles 1 (73.5->89.5) | +181 |
| Kirchwerp | 1072 | 0.41 | 0.60 (69/turn) | thread 91 (5.1->5.7), honey 9 (8.56->10.26), leather 1 (23.1->32.3), lead ore 9 (7.93->10.45) | cloth 24 (7.98->10.8), dyed cloth 8 (13.76->17.1), stockfish 1 (115.5->135.85), ploughs 3 (73.5->83.12) | +178 |
| Pontmont | 341 | 0.10 | 1.00 (114/turn) | firewood 24 (2.81->9.5), bread 76 (2.56->3.42), tiles 1 (3.95->8.98), honey 3 (8.56->10.26) | bricks 5 (9.45->13.01), tools 7 (5.15->6.37), cookware 1 (21->22.61), garments 0 (27.3->29) | +170 |

**Best:** Grandgues at about +329 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.6k (cash + stock at home prices); -129/turn over 6 turns, -32/turn over 24 turns.
- Limits: cash flow >= -279/turn, prestige >= -0.94/turn (values are after 200 tax a turn).
- Today's settings: value +82/turn, cash +66/turn, prestige +58.00/turn.
- Plan: value +461/turn, cash +303/turn, prestige +50.00/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +18 vs +82, +164 vs +69, +101 vs +73.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +13/turn
  - ship Flax Wyrm -> Brebronn: +2/turn
  - park 1 16.00 -> 0.00: +52/turn
  - flax farm 1 4.64 -> 8.24: +30/turn
  - retting pit 1 0.91 -> 1.62: +51/turn
  - net maker [make nets 1] 0.00 -> 0.38: +20/turn
  - weavery 1 0.50 -> 1.28: +8/turn
  - spinnery 1 1.65 -> 2.73: +172/turn
  - sewing shop 1 0.30 -> 0.37: +13/turn
  - brewery 1 0.14 -> 0.00: +15/turn
- Model check over the last 59 turns: predicted +45/turn for the settings we ran, real -16/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.21, thread 3.05, cloth 4.86, flax fibres 3.63, garments 14.05, nets 22.79, beer 2.80, timber 3.53, prestige 0.00, cash 0.00
- Orders it would set: bread buy 5 (v2 7); cloth sell 1 (v2 none); firewood buy 2 (v2 5); garments sell 11 (v2 10); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.04, worth +3/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.32, worth +32/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +16/turn.
- Ship linen snake: Grandgues -> Amsdermund (+13/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brebronn (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +60/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~5686 coin: +21/turn, payback 266 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - new leatherworks (make leather armour 1) for ~4288 coin: +10/turn, payback 428 turns, doesn't pay yet (materials thin at home: bricks, nails)
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

Buffers: flax fibres 84/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.68; ask over the cap 2.1 (60 coin per prestige)
