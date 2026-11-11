# v2 shadow report

Turn 13946, 2026-11-11 11:17. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,616, prestige 3,483 (363 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.50 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~79 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.50 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: projection runs 100 over real use lately; planning 490, not 590

## Prestige spending, cheapest coin per prestige first

455 turns left: prestige gained now converts 89.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.5 | 52.5 | running |
| jousting 3 | arena | 230 | 55.8 | 56.1 | needs a arena (build cost 28,292); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.5 | 56.5 | thin at home: beer |
| hold banquet 4 (pies) | mansion | 18 | 57.8 | 57.8 | thin at home: wine, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 60.1 | 60.1 | thin at home: wine, ham, stockfish, premium cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 60.4 | 60.4 | thin at home: beer, cured meat |
| hold banquet 4 | mansion | 17.5 | 61.0 | 61.0 | thin at home: wine, ham, stockfish |
| jousting 2 | arena | 210 | 61.2 | 61.5 | needs a arena (build cost 28,292); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 65.2 | 65.2 | thin at home: pies |
| hold banquet 3 (fish) | mansion | 7.6 | 65.7 | 65.7 | thin at home: cheese |
| jousting 1 | arena | 170 | 65.6 | 66.0 | needs a arena (build cost 28,292); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 67.6 | 67.6 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.7 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Donaunieder +323, Marmont +316, Vauxvais +307, Brebronn +300, Angefont +276
- Donaunieder would trade: furniture buy 25 @ 12.8, garments sell 1 @ 26.6, pasties buy 5 @ 14.0; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.39 | 0.60 (66/turn) | thread 92 (4.76->6.65), arms 10 (30.45->40.28), looms 1 (588->617.5), flax fibres 6 (6.4->8.26) | cloth 24 (7.56->8.85), glassware 2 (52.5->59.38), tools 16 (5.02->5.61), copper ingots 1 (17.12->19.57) | +306 |
| Fontaux | 411 | 0.12 | 0.40 (44/turn) | thread 91 (4.76->5.65), garments 10 (23.2->25.84), charcoal 19 (2.73->4.73), flax fibres 6 (6.4->7.89) | windows 1 (614.25->736.25), copper ingots 1 (17.12->19.57), tin ingots 1 (35.91->36.29) | +236 |
| Heilegg | 826 | 0.25 | 0.60 (66/turn) | arms 10 (30.45->37.24), beer 65 (3.46->4.62), lead ore 9 (9.35->12.06), thread 48 (4.76->5.22) | cheese 8 (7.19->11.59), cloth 24 (7.46->8.85), windows 1 (729.75->736.25), candles 1 (87.67->88.5) | +200 |
| Disscester | 1474 | 0.63 | 0.40 (44/turn) | looms 1 (588->698.25), dyed cloth 6 (10.82->12.92), steel ingots 1 (16.07->16.72) | furniture 12 (11.45->16.62), cheese 8 (7.93->11.59), tin ingots 1 (32.13->36.29), cloth 12 (8.19->8.85) | +173 |
| Hofkirchen | 991 | 0.34 | 0.50 (55/turn) | thread 90 (4.76->5.7), looms 1 (588->617.5), arms 10 (30.45->31.92), seeds 7 (2.98->4.31) | cheese 8 (6.83->11.59), furniture 17 (14.49->16.62), nails 6 (6.3->7.12), garments 2 (22.68->24.2) | +154 |

**Best:** Kirchwerp at about +306 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 90.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 10 @ min 19.3 | goal planner: sells 10 at 19.3 (v2 had 10 at 22.6) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 98.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 38.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.2k (cash + stock at home prices); +29/turn over 6 turns, +18/turn over 24 turns.
- Limits: cash flow >= -151/turn, prestige >= -0.26/turn (values are after 200 tax a turn).
- Today's settings: value +15/turn, cash +12/turn, prestige -2.53/turn - breaks the prestige floor.
- Plan: value -49/turn, cash +16/turn, prestige -0.26/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -60 vs -6, +67 vs +14, +150 vs +13.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.09: +12/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: +7/turn
  - spinnery 1 1.65 -> 1.33: +8/turn
  - retting pit 1 0.91 -> 0.79: -4/turn
  - flax farm 1 4.64 -> 3.96: -8/turn
  - mansion 1 0.00 -> 0.54: -99/turn
- Model check over the last 59 turns: predicted +106/turn for the settings we ran, real +106/turn.
- Worth of one more unit per turn: labour 1.58, thread 3.96, cloth 6.32, flax fibres 4.70, garments 18.30, nets 28.76, beer 3.03, timber 3.31, prestige 57.96, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); grain buy 6 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +4/turn.
- Ship linen snake: Grandgues -> Essenbrucke (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +69/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 7.0/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 415 (+126 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.16 |
| ret | 3 | 0.91 | 0.83 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 117/77, thread 1064/226, cloth 73/127

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.36 (ask 3.3, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
