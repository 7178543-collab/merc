# v2 shadow report

Turn 14129, 2026-11-19 02:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,666, prestige 3,582 (462 free, -0.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 12 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 39, buy @ 3.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 1 | 1 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 502 | 0 | 62 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.76 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.76 is above our ceiling 2.40 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 5) -> v2: buy 5
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.80 x4, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 62 labour expired last turn (~123 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618
- labour expiry guard: 62 bought labour expired last turn, buy 3 (not 18) this turn

## Prestige spending, cheapest coin per prestige first

272 turns left: prestige gained now converts 74.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 47.0 | 47.3 | needs a arena (build cost 28,752); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 50.6 | 50.9 | needs a arena (build cost 28,752); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 53.7 | 54.3 | needs a arena (build cost 28,752); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 |  |
| jousting 2 | arena | 210 | 58.8 | 59.4 | needs a arena (build cost 28,752); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 59.4 | 59.4 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 59.5 | 59.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 62.2 | 62.2 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 64.0 | 64.0 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 64.5 | 64.5 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 64.6 | 64.6 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 64.6 | 64.6 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0.336 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 13.5, pasties buy 2 @ 16.4; crew 0.2; est +238 a turn; stock: furniture 20 @ 13.5 (keep 145); stock: pasties 2 @ 16.4 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.3 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Friedwerp +265, Amsdermund +248, Gotthafen +244, Clairlond +241, Caillechâtel +238
- Friedwerp would trade: cured meat buy 3 @ 23.4, furniture buy 22 @ 13.8, pasties buy 3 @ 16.3; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~126 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (126/turn) | bread 144 (2.88->4.2), firewood 30 (2.9->9.21), timber 35 (8.61->12.16), charcoal 17 (2.77->5.27) | garments 1 (32.13->37.4), flax fibres 3 (7.4->9.85), yarn 1 (7.4->10.16), candles 0 (79.28->83) | +524 |
| Großaue | 1136 | 0.50 | 0.40 (50/turn) | raw cloth 16 (8.82->13.96), nets 2 (35.6->38.19) | flax fibres 20 (5.88->9.85), cloth 24 (9.77->12.7), yarn 9 (6.25->10.16), dyed cloth 7 (13.86->16.62) | +265 |
| Hofkirchen | 991 | 0.40 | 0.40 (50/turn) | lathes 1 (182.7->214.7) | flax fibres 23 (6.14->9.85), books 1 (614.25->665), cloth 24 (10.61->12.7), garments 2 (27.3->37.4) | +238 |
| Fontaux | 411 | 0.14 | 0.80 (101/turn) | thread 48 (5.35->7.27), timber 32 (8.61->12.35), dyed cloth 3 (19.53->22.8), cloth 1 (12.3->16.25) | flax fibres 19 (7.04->9.85), candles 1 (79.8->83), yarn 1 (6.83->10.16), cured meat 3 (24.36->25.2) | +213 |
| Heilegg | 826 | 0.29 | 0.30 (38/turn) | casks 15 (6.67->9.17), nets 6 (35.6->37.62), varnish 8 (17.12->18.24) | cloth 24 (10.24->12.7), books 1 (624.75->665), yarn 9 (6.35->10.16), flax fibres 6 (6.41->9.85) | +213 |

**Best:** Grandgues at about +524 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 24 @ 3.96, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 16 = 1.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 7 |  | goal planner: buys 2 a turn for today's rates, keeps up to 7 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 35.0) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 3) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.9k (cash + stock at home prices); +257/turn over 6 turns, +116/turn over 24 turns.
- Limits: cash flow >= -444/turn, prestige >= -0.68/turn (values are after 200 tax a turn).
- Today's settings: value -135/turn, cash -128/turn, prestige +1.72/turn.
- Plan: value +42/turn, cash +50/turn, prestige -0.68/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +159 vs -140, -503 vs -104, +39 vs -122.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Karlmoor: +6/turn
  - ship Flax Wyrm -> Donaunieder: +7/turn
  - mansion 1 1.00 -> 0.43: +140/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.41: +9/turn
  - net maker 0.00 -> 0.28: +1/turn
  - retting pit 1 0.91 -> 0.80: +0/turn
  - flax farm 1 4.64 -> 4.02: +7/turn
  - ropewalk 1 0.25 -> 0.31: -1/turn
  - sewing shop 1 0.30 -> 0.25: -6/turn
- Model check over the last 60 turns: predicted +110/turn for the settings we ran, real +118/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.66, beer 3.26, timber 3.53, prestige 62.69, cash 0.00
- Orders it would set: bread buy 5 (v2 8); cloth sell 1 (v2 none); firewood buy 2 (v2 5); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 3); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Ship linen snake: Grandgues -> Karlmoor (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+2/turn over staying).
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

Buffers: flax fibres 73/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 16.1 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 39 @ 3.94, home ask 3.78; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.76; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
