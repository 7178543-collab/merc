# v2 shadow report

Turn 14109, 2026-11-18 06:19. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,544, prestige 3,577 (457 free, -2.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 3 | 3 | 1 | 0 | stop 11, buy 3, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 75 | 0 | 2 | 0 | 0 | min_holding 75, sell 11, sell @ 21 |
| grain | 34 | 0 | 2 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 507 | 0 | 22 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (3 @ 2.4), but the home ask 2.70 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 3 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 3 (need 8) -> v2: buy 8
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~39 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 84.00 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 604

## Prestige spending, cheapest coin per prestige first

292 turns left: prestige gained now converts 76.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.9 | 52.4 | needs a arena (build cost 27,052); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| jousting 2 | arena | 210 | 56.9 | 57.4 | needs a arena (build cost 27,052); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 60.8 | 60.8 |  |
| hold mass 2 (premium) | cathedral | 360 | 56.9 | 61.7 | needs a cathedral (build cost 296,800); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 62.3 | 62.3 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 63.6 | 63.6 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 63.7 | 63.7 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 64.6 | 64.6 | thin at home: hop beer, ham, stockfish, premium ham |
| hold banquet 3 (pies) | mansion | 8 | 64.7 | 64.7 | thin at home: hop beer, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 64.8 | 64.8 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0.376 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 14.6, pasties buy 2 @ 16.3; crew 0.2; est +218 a turn; stock: furniture 20 @ 14.6 (keep 145); stock: pasties 2 @ 16.3 (keep 14)
- **linen snake** on Grandgues: candles buy 6 @ 78.0; crew 0.1; est +60 a turn; stock: candles 6 @ 78.0 (keep 12)
- best towns now: Hofkirchen +516, Cobholme +323, Fulkirch +323, Clairlond +312, Helmgreen +274
- Hofkirchen would trade: candles buy 6 @ 76.5, furniture buy 37 @ 13.7, pasties buy 8 @ 14.6; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.12 | 0.90 (102/turn) | timber 41 (7.88->11.78), beer 65 (4.03->5.56), thread 43 (5.5->7.27), salt 4 (5.35->7.79) | spinning wheels 1 (245.7->266), flax fibres 2 (5.51->7.8), cheese 4 (6.41->7.03), garments 2 (30.87->32.2) | +278 |
| Grandgues | 152 | 0.05 | 0.80 (91/turn) | timber 29 (7.88->12.44), firewood 35 (2.84->5.7), charcoal 19 (2.92->4.99), limestone 4 (17.96->24.7) | spinning wheels 1 (243.6->266), dyed cloth 3 (10.08->14.91), bricks 4 (7.4->10.07), candles 1 (81.38->84) | +268 |
| Hofkirchen | 991 | 0.36 | 0.50 (57/turn) | honey 4 (9.71->10.45), grain 2 (2.88->3.61) | flax fibres 28 (5.62->7.8), cloth 24 (9.4->10.9), cookware 8 (20.48->24.13), spinning wheels 1 (239.4->266) | +169 |
| Kirchwerp | 1072 | 0.41 | 0.40 (45/turn) | lead ore 7 (5.88->10.45), honey 6 (9.71->12.63), nails 18 (8.66->9.5), leather 2 (30.03->32.3) | flax fibres 18 (5.62->7.8), spinning wheels 1 (243.6->266), garments 2 (26.25->32.2), cookware 8 (22.47->24.13) | +130 |
| Birkeningen | 1006 | 0.37 | 0.50 (57/turn) | beer 61 (4.03->5.94), malt 3 (6.83->12.25), nets 2 (35->40.47), wine 6 (7.98->8.46) | cookware 5 (21.84->24.13), garments 2 (29.82->32.2) | +106 |

**Best:** Fontaux at about +278 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 4.02, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 6 = 3.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 31.2) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 2) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.2k (cash + stock at home prices); +38/turn over 6 turns, +136/turn over 24 turns.
- Limits: cash flow >= -398/turn, prestige >= -0.65/turn (values are after 200 tax a turn).
- Today's settings: value +100/turn, cash +79/turn, prestige -2.29/turn - breaks the prestige floor.
- Plan: value +39/turn, cash +46/turn, prestige -0.65/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +66 vs +80, -5 vs +82, +70 vs +82.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.07: +14/turn
  - spinnery 1 1.65 -> 1.56: +4/turn
  - net maker 0.00 -> 0.28: +4/turn
  - ropewalk 1 0.25 -> 0.33: +3/turn
  - flax farm 1 4.64 -> 4.54: +0/turn
  - mansion 1 0.00 -> 0.39: -88/turn
- Model check over the last 59 turns: predicted +125/turn for the settings we ran, real +61/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.77, thread 4.45, cloth 7.10, flax fibres 5.28, garments 20.55, nets 32.16, beer 3.15, timber 3.38, prestige 59.00, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 2); labour buy 29 (v2 7); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Hofkirchen (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 7.7/turn (+0.0 exported); plan makes 34.9 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 451 (+162 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.95 |
| ret | 3 | 0.91 | 0.99 |
| spin | 4 | 1.65 | 1.75 |
| weave | 3 | 0.50 | 1.35 |
| sew | 2 | 0.30 | 0.85 |

Buffers: flax fibres 75/80, thread 1062/235, cloth 72/135

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1062 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
