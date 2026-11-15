# v2 shadow report

Turn 14051, 2026-11-15 20:14. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,103, prestige 3,563 (443 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 9 | 4 | 0 | 0 | min_holding 60, sell 5, sell @ 3.26; stop 26, buy 9, buy @ 3.16 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 40 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.04 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.04 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~78 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.13, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

350 turns left: prestige gained now converts 82.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| jousting 3 | arena | 230 | 54.8 | 55.2 | needs a arena (build cost 26,539); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.7 | 55.7 |  |
| hold banquet 4 (pies) | mansion | 18 | 57.0 | 57.0 | thin at home: pasties, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 59.3 | 59.3 |  |
| hold banquet 3 (pies) | mansion | 8 | 59.6 | 59.6 | thin at home: pasties |
| hold banquet 2 (pies) | mansion | 7 | 59.7 | 59.7 | thin at home: pasties |
| hold banquet 4 | mansion | 17.5 | 60.0 | 60.0 | thin at home: ham, stockfish |
| jousting 2 | arena | 210 | 60.0 | 60.4 | needs a arena (build cost 26,539); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 |  |
| hold banquet 4 (premium) | mansion | 20 | 61.6 | 61.6 | thin at home: ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 61.9 | 61.9 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 14.1, pasties buy 3 @ 14.6; crew 0.2; est +250 a turn; stock: furniture 21 @ 14.1 (keep 145); stock: pasties 3 @ 14.6 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Amsdermund +581, Gotthafen +456, Vauxvais +400, Bordees +326, Boistot +301
- Amsdermund would trade: furniture buy 56 @ 14.3; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (107/turn) | timber 39 (7.88->12.63), nets 3 (15.61->36.29), firewood 28 (3.19->6.22), charcoal 15 (2.75->5.22) | candles 0 (85.58->89.5), dyed cloth 4 (11.97->12.73), rope 1 (78.75->80.27), hop beer 0 (8.4->9.88) | +367 |
| Hofkirchen | 991 | 0.34 | 0.40 (43/turn) | nets 5 (15.61->34.77), steel ingots 12 (19.32->24.7) | ploughs 5 (77.17->83.12), cloth 24 (7.82->8.65), glassware 2 (95.55->99.75), dyed cloth 5 (10.92->12.73) | +204 |
| Kirchwerp | 1072 | 0.39 | 0.40 (43/turn) | nets 5 (15.61->35.53), steel ingots 6 (19.32->23.18), furniture 9 (14.49->17), honey 7 (8.24->9.59) | cloth 24 (7.56->8.65), ploughs 3 (73.5->83.12), dyed cloth 5 (10.92->12.73), garments 2 (23.73->25) | +193 |
| Gottweiler | 1135 | 0.42 | 0.20 (21/turn) | nets 6 (15.61->38.38), tapestries 1 (782.25->807.5), wheels 1 (17.12->23.37) | cloth 9 (7.35->8.65), garments 2 (22.47->25), cheese 9 (5.72->6.46), dyed cloth 5 (11.76->12.73) | +183 |
| Essenbrucke | 584 | 0.17 | 0.20 (21/turn) | nets 4 (15.61->35.53), dyed cloth 12 (14.6->17.39), garments 11 (24->26.41), beer 28 (3.15->4.14) | ploughs 2 (72.45->83.12), thread 4 (4.64->5.3), cloth 4 (8.19->8.65), raw cloth 1 (7.09->7.27) | +172 |

**Best:** Grandgues at about +367 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 14.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21.2 | goal planner: sells 11 at 21.2 (v2 had 10 at 23.4) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.6k (cash + stock at home prices); +5/turn over 6 turns, -24/turn over 24 turns.
- Limits: cash flow >= -254/turn, prestige >= -0.60/turn (values are after 200 tax a turn).
- Today's settings: value +60/turn, cash +27/turn, prestige -2.43/turn - breaks the prestige floor.
- Plan: value +9/turn, cash +31/turn, prestige -0.60/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +227 vs +102, +91 vs +52, -6 vs +44.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Chatgnan: +3/turn
  - ship Flax Wyrm -> Pontmont: +0/turn
  - flax farm 1 4.64 -> 3.88: -8/turn
  - retting pit 1 0.91 -> 0.77: +6/turn
  - ropewalk 1 0.25 -> 0.00: -10/turn
  - weavery 1 0.50 -> 0.58: +5/turn
  - spinnery 1 1.65 -> 1.22: -6/turn
  - mansion 1 0.00 -> 0.44: -70/turn
- Model check over the last 58 turns: predicted -122/turn for the settings we ran, real -109/turn.
- Worth of one more unit per turn: labour 1.57, thread 3.96, cloth 6.32, flax fibres 4.70, garments 18.29, nets 15.84, beer 2.91, timber 3.38, prestige 57.93, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.05, worth +2/turn.
- Ship linen snake: Grandgues -> Chatgnan (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Pontmont (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~4723 coin: +16/turn, payback 304 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 9.2/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 411 (+122 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.01 |
| ret | 3 | 0.91 | 0.80 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 125/77, thread 1064/225, cloth 72/126

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.04; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
