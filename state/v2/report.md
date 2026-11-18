# v2 shadow report

Turn 14105, 2026-11-18 03:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,511, prestige 3,586 (466 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 1 | 1 | 1 | 1 | 0 | stop 7, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 40 | 0 | 2 | 0 | 0 | min_holding 75, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), 1 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: only 0.5 turns of firewood left and buying 2 (need 5) -> v2: buy 5

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 83.50 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

296 turns left: prestige gained now converts 77.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.1 | 52.6 | needs a arena (build cost 27,362); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.0 | 54.0 | running |
| jousting 2 | arena | 210 | 57.1 | 57.6 | needs a arena (build cost 27,362); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 |  |
| hold banquet 3 (pies) | mansion | 8 | 60.8 | 60.8 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 61.0 | 61.0 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 61.4 | 61.4 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 61.6 | 61.6 |  |
| hold mass 2 (premium) | cathedral | 360 | 57.0 | 61.8 | needs a cathedral (build cost 303,610); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 1 (meat) | mansion | 4.2 | 63.4 | 63.4 |  |
| hold banquet 4 (premium) | mansion | 20 | 64.2 | 64.2 | thin at home: hop beer, stockfish, premium ham |
| hold banquet 2 (meat) | mansion | 6.8 | 64.3 | 64.3 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.3 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +714, Gotthafen +463, Vauxvais +420, Cobholme +340, Boistot +298
- Amsdermund would trade: furniture buy 65 @ 13.7, pasties buy 1 @ 16.1; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Gotthafen | 964 | 0.35 | 0.30 (34/turn) | nets 3 (34.2->35.72) | tapestries 2 (640.5->798), garments 19 (26.88->28.69), ham 2 (127.05->134.9), yarn 4 (5.83->8.03) | +374 |
| Grandgues | 152 | 0.05 | 1.00 (115/turn) | timber 28 (7.93->12.44), firewood 34 (2.39->6.03), bread 161 (2.5->2.83), charcoal 19 (3.04->4.39) | ham 3 (118.65->134.9), bricks 3 (8.14->10.36), yarn 2 (6.41->8.03), cloth 3 (10.61->11) | +303 |
| Fontaux | 411 | 0.13 | 0.70 (80/turn) | beer 64 (3.91->5.89), timber 24 (7.93->11.97), thread 44 (5.05->5.65), nets 5 (34.2->35.15) | ham 3 (126->134.9), flax fibres 5 (6.41->7.5), flour 4 (19.21->21.28), yarn 1 (6.3->8.03) | +222 |
| Kirchwerp | 1072 | 0.41 | 1.00 (115/turn) | beer 61 (3.91->5.22), jewellery 12 (101.85->104.5), thread 82 (5.05->5.7), steel ingots 8 (19.21->21.28) | garments 17 (26.67->28.69), flax fibres 25 (5.62->7.5), ham 0 (127.05->134.9), dyed cloth 4 (13.23->14.91) | +191 |
| Amsdermund | 1111 | 0.44 | 0.40 (46/turn) | jewellery 14 (101.85->104.5), paper 1 (24.57->26.6), wine 2 (7.61->9.12) | cloth 24 (7.35->11), ham 2 (121.8->134.9), garments 19 (27.3->28.69), tools 21 (4.83->5.61) | +168 |

**Best:** Gotthafen at about +374 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 4.02, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 7 |  | goal planner: buys 2 a turn for today's rates, keeps up to 7 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 12.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.0) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.8k (cash + stock at home prices); +151/turn over 6 turns, +60/turn over 24 turns.
- Limits: cash flow >= -396/turn, prestige >= -0.69/turn (values are after 200 tax a turn).
- Today's settings: value +105/turn, cash +85/turn, prestige -2.51/turn - breaks the prestige floor.
- Plan: value +29/turn, cash +36/turn, prestige -0.69/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +526 vs +75, +273 vs +74, +66 vs +80.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +6/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.28: +4/turn
  - ropewalk 1 0.25 -> 0.33: +3/turn
  - flax farm 1 4.64 -> 4.73: -1/turn
  - weavery 1 0.50 -> 0.59: -7/turn
  - sewing shop 1 0.30 -> 0.36: +10/turn
  - mansion 1 0.00 -> 0.43: -102/turn
- Model check over the last 60 turns: predicted +125/turn for the settings we ran, real +53/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.80, thread 4.52, cloth 7.22, flax fibres 5.36, garments 20.90, nets 32.46, beer 3.16, timber 3.38, prestige 61.55, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Hofkirchen (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 39.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 510 (+221 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.52 |
| ret | 3 | 0.91 | 1.10 |
| spin | 4 | 1.65 | 1.95 |
| weave | 3 | 0.50 | 1.55 |
| sew | 2 | 0.30 | 0.97 |

Buffers: flax fibres 78/87, thread 1049/255, cloth 72/155
- chain plan needed 557 labour, budget left 510: cut to 510 (sewing capped at 0.97)

## Self-diagnosis

- R1: firewood slot dry: 1.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.26; our bid is already at/over the ask (sellers too thin)
