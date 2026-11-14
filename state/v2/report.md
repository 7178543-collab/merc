# v2 shadow report

Turn 14014, 2026-11-14 07:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,131, prestige 3,520 (400 free, +2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 27 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 519 | 0 | 45 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: only 0.7 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.28 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.28 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~83 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 99 over real use lately; planning 519, not 607
- labour expiry guard: 45 bought labour expired last turn, buy 19 (not 19) this turn

## Prestige spending, cheapest coin per prestige first

387 turns left: prestige gained now converts 85.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 54.6 | 54.6 | running |
| jousting 3 | arena | 230 | 55.3 | 55.7 | needs a arena (build cost 27,566); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.4 | 58.4 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 60.5 | 60.5 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 60.7 | 60.7 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 60.9 | 60.9 | thin at home: hop beer, stockfish, glassware |
| jousting 2 | arena | 210 | 60.6 | 61.0 | needs a arena (build cost 27,566); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 62.6 | 62.6 |  |
| hold banquet 4 (premium) | mansion | 20 | 62.9 | 62.9 | thin at home: hop beer, stockfish, glassware |
| hold banquet 1 (meat) | mansion | 4.2 | 64.0 | 64.0 | running |
| hold banquet 4 | mansion | 17.5 | 64.4 | 64.4 | thin at home: hop beer, stockfish, glassware |
| hold banquet 3 (pies) | mansion | 8 | 64.7 | 64.7 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 1 @ 13.9, pasties buy 4 @ 15.1; crew 0.1; est +16 a turn; stock: furniture 1 @ 13.9 (keep 145); stock: pasties 4 @ 15.1 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 16.1 (keep 14); best orders clear only 14 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +35, Großmühle +28, Heidlowe +28, Unterhufe +27, Gosschweig +26
- Hofkirchen would trade: cured meat buy 6 @ 22.8, furniture buy 1 @ 14.3, pasties buy 5 @ 14.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.41 | 0.30 (34/turn) | windows 1 (677.25->817), resin 4 (2.9->3.93) | cloth 9 (7.35->9.4), ploughs 3 (73.5->80.27), cheese 15 (5.41->6.32), cured meat 6 (23.1->25) | +182 |
| Grandgues | 152 | 0.05 | 0.60 (69/turn) | timber 25 (8.09->11.78), firewood 31 (3.55->6.22), windows 1 (677.25->712.5), acid 1 (115.5->116.85) | cloth 9 (7.93->9.4), cured meat 6 (23.94->25), jewellery 2 (100.8->103.55), candles 1 (86.62->88.5) | +180 |
| Herschweig | 775 | 0.24 | 0.10 (11/turn) | windows 1 (677.25->793.25), acid 1 (115.5->148.2), wine 8 (6.35->6.93), beer 3 (3.66->4.5) | cloth 9 (7.98->9.4), cured meat 6 (23.94->25) | +164 |
| Clairas | 374 | 0.11 | 0.60 (69/turn) | windows 1 (677.25->779), timber 27 (8.09->10.83), charcoal 19 (2.58->4.16), tools 26 (5.67->5.98) | cloth 6 (7.82->9.4), candles 1 (86.62->88.5), garments 2 (22.26->23.6), pies 1 (17.43->17.86) | +160 |
| Hanstein | 380 | 0.12 | 0.30 (34/turn) | windows 1 (677.25->788.5), charcoal 15 (2.58->4.69), timber 9 (8.09->10.83), tools 8 (5.67->5.79) | seeds 14 (1.81->2.58), cured meat 6 (24.36->25), flax fibres 8 (5.15->5.6) | +150 |

**Best:** Kirchwerp at about +182 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 108 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 4 = 0.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.5 | goal planner: sells 2 a turn at 5.5, keeps 85 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 19) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.4) |
| pasties |  | 1 @ min 12.5 | goal planner: sells 1 a turn at 12.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.4k (cash + stock at home prices); -192/turn over 6 turns, -77/turn over 24 turns.
- Limits: cash flow >= -339/turn, prestige >= -0.42/turn (values are after 200 tax a turn).
- Today's settings: value -171/turn, cash -143/turn, prestige +2.01/turn.
- Plan: value -8/turn, cash +5/turn, prestige -0.42/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -237 vs -161, -70 vs -168, -352 vs -158.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Caillechâtel: -4/turn
  - ship Flax Wyrm -> Etallaen: +3/turn
  - mansion 1 1.00 -> 0.42: +149/turn
  - spinnery 1 1.65 -> 1.37: +3/turn
  - retting pit 1 0.91 -> 0.85: +1/turn
  - flax farm 1 4.64 -> 4.24: +4/turn
  - net maker 0.00 -> 0.29: -0/turn
  - ropewalk 1 0.25 -> 0.00: -13/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.35: +14/turn
  - sewing shop 1 0.30 -> 0.20: -15/turn
- Model check over the last 60 turns: predicted +8/turn for the settings we ran, real +34/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.26, beer 3.19, timber 3.46, prestige 60.00, cash 0.00
- Orders it would set: bread buy 5 (v2 6); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax fibres sell 2 (v2 none); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 19); light armour buy 1 (v2 None); pasties sell 1 (v2 none); rope sell 2 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.35, worth +12/turn.
- Ship linen snake: Grandgues -> Caillechâtel (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Etallaen (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 422 (+133 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.30 |
| ret | 3 | 0.91 | 0.86 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 110/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.28; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.1 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
