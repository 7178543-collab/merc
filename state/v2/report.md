# v2 shadow report

Turn 14127, 2026-11-19 00:04. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 15,131, prestige 3,583 (463 free, -0.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 11 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 39, buy @ 3.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 2, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 538 | 0 | 26 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 2 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.44 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.44 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 12 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 26 labour expired last turn (~50 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: +5 crew for linen snake (crew 0.10, no projection from the game)
- labour: projection runs 100 over real use lately; planning 538, not 631

## Prestige spending, cheapest coin per prestige first

274 turns left: prestige gained now converts 74.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 54.0 | 54.6 | needs a arena (build cost 28,524); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.1 | 58.1 |  |
| maintain 1 | park | 0.5 | 58.8 | 58.8 | running |
| jousting 2 | arena | 210 | 59.2 | 59.8 | needs a arena (build cost 28,524); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.0 | 60.0 |  |
| hold banquet 2 (pies) | mansion | 7 | 62.4 | 62.4 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 63.3 | 63.3 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 63.7 | 63.7 |  |
| hold banquet 4 (pies) | mansion | 18 | 64.7 | 64.7 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 65.0 | 65.0 | thin at home: hop beer, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 65.6 | 65.6 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 65.7 | 65.7 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 12 | 134102075 | 0.008 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 12 | 151802239 | 0 | - | pasties 2 | -32 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 22 @ 14.3; crew 0.2; est +241 a turn; stock: furniture 22 @ 14.3 (keep 145)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.4 (keep 14); best orders clear only -7 a turn after crew: ship stays at 0
- best towns now: Gotthafen +459, Hofkirchen +432, Vauxvais +321, Cobholme +297, Friedwerp +263
- Gotthafen would trade: cured meat buy 3 @ 21.4, furniture buy 42 @ 14.0, pasties buy 1 @ 15.1; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~125 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Chatgnan | 728 | 0.24 | 0.20 (25/turn) | thread 17 (5.5->6.84), furniture 8 (14.38->15.58), ploughs 1 (88.2->92.62), malt 1 (6.25->7.31) | tapestries 1 (630->893), garments 2 (36.75->38.8), leather 1 (26.46->30.02), yarn 6 (6.67->7.46) | +289 |
| Grandgues | 152 | 0.05 | 0.90 (112/turn) | firewood 32 (3.19->7.12), timber 29 (8.77->12.16), bread 162 (2.69->3.27), charcoal 19 (2.79->5.61) | dyed cloth 6 (13.97->15.2), yarn 4 (6.51->7.46), beer 11 (3.49->3.62), cheese 3 (6.41->6.6) | +287 |
| Kleinburgh | 1440 | 0.69 | 0.10 (12/turn) | nets 5 (35.4->37.62) | tapestries 1 (640.5->893), cookware 5 (21.21->24.13), garments 2 (36.12->38.8) | +268 |
| Heidlowe | 662 | 0.22 | 0.20 (25/turn) | candles 1 (78.75->87.88), nets 5 (35.4->37.62), malt 1 (6.25->7.55), slaked lime 1 (6.72->7.89) | tapestries 1 (834.75->893), cloth 24 (10.19->11.7), garments 2 (28.98->38.8), cookware 5 (22.05->24.13) | +149 |
| Kirchwerp | 1072 | 0.45 | 0.20 (25/turn) | candles 3 (78.75->85.5), wine 24 (6.72->7.22) | tapestries 1 (861->893), dyed cloth 12 (12.6->15.2), cookware 5 (19.43->24.13), garments 2 (27.72->38.8) | +148 |

**Best:** Chatgnan at about +289 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 24 @ 3.96, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 16 = 1.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 37.2) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 38) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.5k (cash + stock at home prices); +302/turn over 6 turns, +103/turn over 24 turns.
- Limits: cash flow >= -464/turn, prestige >= -0.68/turn (values are after 200 tax a turn).
- Today's settings: value -111/turn, cash -104/turn, prestige +1.68/turn.
- Plan: value +56/turn, cash +64/turn, prestige -0.68/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +306 vs +85, +316 vs +75, +159 vs -140.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Karlmoor: +5/turn
  - ship Flax Wyrm -> Gotthafen: +4/turn
  - mansion 1 1.00 -> 0.44: +133/turn
  - brewery 1 0.14 -> 0.08: +16/turn
  - spinnery 1 1.65 -> 1.41: +5/turn
  - net maker 0.00 -> 0.28: +1/turn
  - retting pit 1 0.91 -> 0.80: +1/turn
  - flax farm 1 4.64 -> 4.02: +8/turn
  - ropewalk 1 0.25 -> 0.31: -1/turn
  - sewing shop 1 0.30 -> 0.25: -6/turn
- Model check over the last 60 turns: predicted +118/turn for the settings we ran, real +126/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.71, beer 3.37, timber 3.53, prestige 60.82, cash 0.00
- Orders it would set: bread buy 5 (v2 6); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 38); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Karlmoor (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Gotthafen (+1/turn over staying).
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

Buffers: flax fibres 71/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 16.5 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 39 @ 3.94, home ask 3.78; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.44; ask over the cap 2.1 (60 coin per prestige)
