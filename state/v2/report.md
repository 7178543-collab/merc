# v2 shadow report

Turn 14053, 2026-11-15 22:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,946, prestige 3,558 (438 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 7 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 39 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 7.2 -> v2: add buy 5
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.94 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.94 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~77 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

348 turns left: prestige gained now converts 82.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| jousting 3 | arena | 230 | 54.5 | 54.9 | needs a arena (build cost 26,316); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.4 | 55.4 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 59.7 | 59.7 | thin at home: cured meat |
| jousting 2 | arena | 210 | 59.7 | 60.1 | needs a arena (build cost 26,316); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.5 | 60.5 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 61.1 | 61.1 | thin at home: pasties, hop beer, ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 62.3 | 62.3 | thin at home: hop beer, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 63.4 | 63.4 | thin at home: cured meat |
| hold banquet 4 (premium) | mansion | 20 | 63.4 | 63.4 | thin at home: hop beer, ham, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 59.8 | 63.5 | needs a cathedral (build cost 307,120); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 63.9 | 63.9 | thin at home: hop beer, ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 14.0, pasties buy 3 @ 14.1; crew 0.2; est +254 a turn; stock: furniture 21 @ 14.0 (keep 145); stock: pasties 3 @ 14.1 (keep 14)
- **linen snake** on Grandgues: pasties buy 12 @ 15.5; crew 0.1; est +30 a turn; stock: pasties 12 @ 15.5 (keep 14)
- best towns now: Amsdermund +570, Chatgnan +524, Vauxvais +406, Bedenis +388, Bordees +323
- Amsdermund would trade: furniture buy 55 @ 14.3; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | timber 41 (7.82->12.82), firewood 31 (3.09->5.79), charcoal 17 (3.04->5.27), lathes 0 (180.6->197.6) | spinning wheels 0 (241.5->254.6), candles 0 (81.9->88.5), dyed cloth 4 (11.76->12.44), tiles 3 (3.89->4.99) | +329 |
| Kirchwerp | 1072 | 0.38 | 0.20 (21/turn) | arms 9 (32.97->40.28), honey 7 (8.24->9.79), chisels 4 (11.23->12.16), resin 6 (3.07->3.93) | cloth 24 (7.56->9.05), spinning wheels 1 (237.3->254.6), dyed cloth 5 (10.92->12.44), garments 2 (21.63->24.4) | +128 |
| Darmwald | 1022 | 0.35 | 0.60 (63/turn) | charcoal 19 (3.04->7.22), nets 3 (34.8->35.91), wool 1 (8.98->9.5) | spinning wheels 1 (214.2->254.6), cloth 24 (7.35->9.05), candles 1 (82.95->88.5), wax 3 (30.66->31.92) | +110 |
| Vauxvais | 204 | 0.06 | 1.00 (106/turn) | bread 113 (2.37->2.75), firewood 38 (3.09->5.32), charcoal 13 (3.04->4.75), beer 50 (3.15->3.55) | candles 0 (64.58->88.5), thread 8 (4.7->5.25), wax 2 (30.24->31.92), spinning wheels 0 (249.9->254.6) | +110 |
| Essenbrucke | 584 | 0.17 | 0.10 (11/turn) | dyed cloth 13 (13.97->20.14), garments 10 (24.2->25.65), malt 1 (6.83->8.22) | tools 15 (5.99->6.46), ploughs 2 (71.92->75.52), cloth 2 (8.35->9.05), pasties 3 (14.38->15.2) | +104 |

**Best:** Grandgues at about +329 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.14, stop 9 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 7 = 1.7 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21.2 | goal planner: sells 11 at 21.2 (v2 had 10 at 23.6) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.0k (cash + stock at home prices); +29/turn over 6 turns, -5/turn over 24 turns.
- Limits: cash flow >= -248/turn, prestige >= -0.58/turn (values are after 200 tax a turn).
- Today's settings: value +52/turn, cash +26/turn, prestige -2.40/turn - breaks the prestige floor.
- Plan: value +10/turn, cash +28/turn, prestige -0.58/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -6 vs +44, +105 vs +27, -262 vs +34.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +26/turn
  - ship Flax Wyrm -> Pontmont: +0/turn
  - brewery 1 0.14 -> 0.01: +26/turn
  - net maker 0.00 -> 0.28: +9/turn
  - ropewalk 1 0.25 -> 0.00: +6/turn
  - weavery 1 0.50 -> 0.59: +1/turn
  - sewing shop 1 0.30 -> 0.35: +15/turn
  - spinnery 1 1.65 -> 1.30: +0/turn
  - retting pit 1 0.91 -> 0.82: -2/turn
  - flax farm 1 4.64 -> 4.10: -6/turn
- Model check over the last 59 turns: predicted -121/turn for the settings we ran, real -111/turn.
- Worth of one more unit per turn: labour 1.69, thread 4.29, cloth 6.82, flax fibres 5.15, garments 19.70, nets 31.34, beer 3.00, timber 3.35, prestige 61.79, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +4/turn.
- Ship linen snake: Grandgues -> Vauxvais (+26/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Pontmont (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3786 coin: +1/turn, payback 4851 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 9.4/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 412 (+122 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.98 |
| ret | 3 | 0.91 | 0.80 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 128/77, thread 1064/226, cloth 72/126

## Self-diagnosis

- R1: beer slot dry: 7.2 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.0 -> **buy 9 @ 3.06 (ask 3.0, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.94; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
