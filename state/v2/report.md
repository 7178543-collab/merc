# v2 shadow report

Turn 14061, 2026-11-16 06:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,438, prestige 3,663 (543 free, +125.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 7, buy @ 3.6 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.98 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.98 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.90 x10, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~76 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **candles**: home ask 78.00 is above our ceiling 76.00 and last turn bought 7 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 501, not 601
- labour expiry guard: 45 bought labour expired last turn, buy 0 (not 1) this turn

## Prestige spending, cheapest coin per prestige first

340 turns left: prestige gained now converts 81.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 3 | arena | 230 | 50.1 | 50.5 | needs a arena (build cost 27,721); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.9 | 55.3 | needs a arena (build cost 27,721); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.8 | 58.8 | thin at home: beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 59.4 | 59.4 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 59.4 | 59.4 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 61.7 | 61.7 | thin at home: hop beer, stockfish, pies |
| hold banquet 3 (pies) | mansion | 8 | 62.2 | 62.2 | thin at home: hop beer, pies |
| hold banquet 2 (meat) | mansion | 6.8 | 62.3 | 62.3 |  |
| hold banquet 4 (premium) | mansion | 20 | 62.9 | 62.9 | thin at home: hop beer, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 63.0 | 63.0 | thin at home: beer |
| hold mass 2 (premium) | cathedral | 360 | 59.5 | 63.4 | needs a cathedral (build cost 310,780); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0.364 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 22 @ 13.1, pasties buy 1 @ 15.3; crew 0.2; est +276 a turn; stock: furniture 22 @ 13.1 (keep 145); stock: pasties 1 @ 15.3 (keep 14)
- **linen snake** on Grandgues: beer buy 4 @ 3.28, candles buy 4 @ 77.5, pasties buy 4 @ 15.9; crew 0.1; est +53 a turn; stock: candles 4 @ 77.5 (keep 12); stock: pasties 4 @ 15.9 (keep 14)
- best towns now: Heidlowe +558, Chatgnan +482, Amsdermund +479, Bedenis +351, Boistot +329
- Heidlowe would trade: furniture buy 48 @ 13.9; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (104/turn) | timber 42 (7.77->12.54), firewood 35 (3.13->5.84), charcoal 19 (2.52->5.18), bread 164 (2.33->2.66) | beer 75 (3.38->4.16), dyed cloth 4 (11.45->13.39), cloth 4 (8.66->9.3), yarn 5 (4.75->4.99) | +385 |
| Brebronn | 862 | 0.26 | 0.10 (10/turn) | swords 1 (281.4->324.9), garments 10 (22.4->26.79), leather 1 (23.1->26.03) | cloth 10 (8.03->9.3), salt 10 (4.54->5.56), cheese 9 (5.78->6.7), dyed cloth 4 (12.39->13.39) | +114 |
| Hofkirchen | 991 | 0.33 | 0.90 (93/turn) | lead ore 10 (9.19->13.01), wine 9 (6.46->7.5), flax plants 1 (1.5->3.89), leather 1 (23.1->25.65) | cloth 24 (7.82->9.3), beer 75 (3.36->4.16), tools 16 (5.15->6.13), flax fibres 23 (5.78->6.8) | +114 |
| Amsdermund | 1111 | 0.39 | 0.30 (31/turn) | wine 12 (6.46->9.5), pasties 4 (14.91->19.76), flour 2 (21.21->27.55), leather 1 (23.1->26.79) | cloth 24 (7.35->9.3), tools 16 (4.83->6.13), flax fibres 14 (5.78->6.8), hop beer 1 (8.51->9.45) | +112 |
| Heilegg | 826 | 0.24 | 0.50 (52/turn) | charcoal 19 (2.52->6.03), nets 6 (34->36.1), garments 10 (22.4->22.99), leather 1 (23.1->26.79) | cloth 24 (7.72->9.3), cheese 9 (5.78->6.7), tools 16 (5.51->6.13), dyed cloth 4 (11.97->13.39) | +106 |

**Best:** Grandgues at about +385 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 8 @ ?, stop 16 |  | uses 4.0/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| candles | 2 @ 76.0, stop 6 |  | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 3) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 21.8) |
| grain | 0 @ 3.7, stop 6 |  | goal planner: buys 0 a turn for today's rates, keeps up to 6 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.4/turn (observed), makes 0.0, holds 1 = 2.4 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.9k (cash + stock at home prices); -559/turn over 6 turns, -125/turn over 24 turns.
- Limits: cash flow >= -185/turn, prestige >= -1.01/turn (values are after 200 tax a turn).
- Today's settings: value +67/turn, cash +39/turn, prestige +133.00/turn.
- Plan: value +409/turn, cash +260/turn, prestige +125.00/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -670 vs +27, -328 vs +31, -328 vs +30 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bordetes: +0/turn
  - ship Flax Wyrm -> Pontmont: +0/turn
  - park 1 16.00 -> 0.00: +48/turn
  - flax farm 1 4.64 -> 7.33: +24/turn
  - retting pit 1 0.91 -> 1.44: +28/turn
  - net maker [make nets 1] 0.00 -> 0.38: +21/turn
  - spinnery 1 1.65 -> 2.40: +19/turn
  - weavery 1 0.50 -> 1.18: +84/turn
  - sewing shop 1 0.30 -> 0.72: +75/turn
  - brewery 1 0.14 -> 0.03: +20/turn
- Model check over the last 59 turns: predicted -77/turn for the settings we ran, real -146/turn.
- Worth of one more unit per turn: labour 0.96, thread 2.42, cloth 3.86, flax fibres 2.89, garments 11.16, nets 18.10, beer 2.47, timber 3.31, prestige 0.00, cash 0.00
- Orders it would set: candles buy 2 (v2 3); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 2 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.09, worth +12/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +24/turn.
- Ship linen snake: Grandgues -> Bordetes (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Pontmont (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +48/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~4596 coin: +15/turn, payback 298 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - new leatherworks (make leather armour 1) for ~3755 coin: +11/turn, payback 329 turns, doesn't pay yet (materials thin at home: nails)
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 11.1/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 417 (+128 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.02 |
| ret | 3 | 0.91 | 0.80 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 130/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.98; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
