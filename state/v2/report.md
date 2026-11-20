# v2 shadow report

Turn 14157, 2026-11-20 06:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,185, prestige 3,624 (504 free, +0.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 32 | 14 | 14 | 5 | 0 | stop 63, buy 32, buy @ 4.78 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 506 | 0 | 58 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.06 is above it); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.06 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.90 x3, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 58 labour expired last turn (~123 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 526, not 626
- labour expiry guard: 58 bought labour expired last turn, buy 7 (not 26) this turn

## Prestige spending, cheapest coin per prestige first

244 turns left: prestige gained now converts 70.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 48.6 | 48.9 | needs a arena (build cost 29,519); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 52.3 | 52.7 | needs a arena (build cost 29,519); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.6 | 53.3 | needs a arena (build cost 29,519); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.6 | 58.3 | needs a arena (build cost 29,519); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 61.5 | 61.5 | thin at home: beer |
| hold banquet 4 (pies) | mansion | 18 | 61.6 | 61.6 | thin at home: wine, stockfish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 62.5 | 62.5 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 64.0 | 64.0 | thin at home: wine, stockfish |
| maintain 1 | park | 0.5 | 64.2 | 64.2 | running |
| hold mass 2 (premium) | cathedral | 360 | 58.0 | 65.1 | needs a cathedral (build cost 320,840); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 65.4 | 65.4 | thin at home: cheese |
| hold banquet 4 | mansion | 17.5 | 66.3 | 66.3 | thin at home: wine, stockfish, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 3 @ 20.4, pasties buy 8 @ 16.0; crew 0.1; est +26 a turn; stock: pasties 8 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Angefont +537, Cobholme +354, Fulkirch +312, Chatgnan +257, Disscester +240
- Angefont would trade: cured meat buy 3 @ 22.6, furniture buy 46 @ 14.3, pasties buy 8 @ 15.8; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~134 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.48 | 0.40 (54/turn) | glassware 7 (87.15->142.5), furniture 9 (16.8->24.89), looms 1 (840->897.75), nets 6 (38->42.94) | cheese 7 (5.1->9.88), cookware 7 (19.43->22.42), cured meat 3 (20.27->25.6), candles 1 (79.8->86) | +598 |
| Amsdermund | 1111 | 0.51 | 0.40 (54/turn) | flour 4 (22.05->29.83), nets 6 (38->40.66), slaked lime 1 (8.77->11.4) | cloth 24 (9.77->12.3), axes 6 (17.85->21.85), cheese 7 (6.67->9.88), candles 1 (73.5->86) | +157 |
| Großmühle | 751 | 0.27 | 0.20 (27/turn) | harnesses 1 (56.7->66.02), nets 2 (38->39.14), dyed yarn 1 (4.96->5.51) | cloth 21 (8.19->12.3), thread 19 (5.17->7.1), cheese 7 (6.83->9.88), candles 1 (81.38->86) | +145 |
| Hofkirchen | 991 | 0.42 | 0.20 (27/turn) | looms 1 (840->902.5), nets 6 (38->42.94), chisels 3 (12.29->13.3) | cheese 7 (6.3->9.88), cured meat 3 (22.05->25.6), axes 5 (20.16->21.85), candles 1 (81.38->86) | +130 |
| Neuborn | 780 | 0.28 | 1.00 (134/turn) | firewood 11 (3.21->15.2), looms 0 (840->940.5), charcoal 7 (2.39->5.98), nets 2 (38->41.61) | cheese 2 (5.25->9.88), cured meat 1 (22.05->25.6), beer 5 (3.7->4.68), candles 0 (80.85->86) | +130 |

**Best:** Kirchwerp at about +598 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 39 @ 4.9, stop 77 |  | uses 19.2/turn (household upkeep), makes 0.0, holds 32 = 1.7 turns |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 14 = 2.3 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 33.2) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 34 |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 7) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 37.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 1 = 4.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.9k (cash + stock at home prices); +32/turn over 6 turns, +113/turn over 24 turns.
- Limits: cash flow >= -299/turn, prestige >= -0.85/turn (values are after 200 tax a turn).
- Today's settings: value -140/turn, cash -155/turn, prestige +1.48/turn.
- Plan: value +50/turn, cash +53/turn, prestige -0.85/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -547 vs -110, -479 vs -137, -707 vs -176 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: -7/turn
  - ship Flax Wyrm -> Kirchwerp: +18/turn
  - mansion 1 1.00 -> 0.45: +129/turn
  - ropewalk 1 0.25 -> 0.12: +14/turn
  - spinnery 1 1.65 -> 1.31: +15/turn
  - net maker 0.00 -> 0.29: +6/turn
  - brewery 1 0.14 -> 0.00: +8/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.06: +8/turn
  - retting pit 1 0.91 -> 0.82: +2/turn
  - flax farm 1 4.64 -> 4.12: +7/turn
- Model check over the last 59 turns: predicted -18/turn for the settings we ran, real +88/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.68, beer 4.68, timber 3.92, prestige 62.40, cash 0.00
- Orders it would set: bread buy 5 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 7); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.06, worth +9/turn.
- Ship linen snake: Grandgues -> Donaunieder (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Kirchwerp (+8/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +86/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 424 (+136 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.45 |
| ret | 3 | 0.91 | 0.89 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 99/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 32.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 32 @ 4.78, home ask 4.68; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.06; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
