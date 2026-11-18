# v2 shadow report

Turn 14111, 2026-11-18 08:30. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,376, prestige 3,620 (500 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 5 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 22 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 521 | 0 | 8 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.76 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.76 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Tuning

- **candles**: home ask 83.50 is above our ceiling 76.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 521, not 618

## Prestige spending, cheapest coin per prestige first

290 turns left: prestige gained now converts 76.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 53.0 | 53.5 | needs a arena (build cost 26,917); thin at home: swords, protection, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.0 | 54.0 | running |
| jousting 2 | arena | 210 | 58.1 | 58.6 | needs a arena (build cost 26,917); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.9 | 58.9 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 61.0 | 61.0 |  |
| hold mass 2 (premium) | cathedral | 360 | 56.8 | 61.6 | needs a cathedral (build cost 296,300); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 61.9 | 61.9 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 63.1 | 63.1 |  |
| hold banquet 2 (pies) | mansion | 7 | 63.7 | 63.7 |  |
| hold banquet 4 (premium) | mansion | 20 | 64.8 | 64.8 | thin at home: hop beer, ham, stockfish, premium ham |
| hold banquet 3 (pies) | mansion | 8 | 65.8 | 65.8 | thin at home: hop beer |
| hold banquet 3 (fish) | mansion | 7.6 | 66.0 | 66.0 | thin at home: hop beer, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 21 | 134102075 | 0.344 | - | candles 2, furniture 20, pasties 1 | -466 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.4 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: candles 2 @ 78.0 (keep 12); best orders clear only 12 a turn after crew: ship stays at 0
- best towns now: Gotthafen +447, Clairlond +290, Fulkirch +286, Donaunieder +285, Cobholme +262
- Gotthafen would trade: furniture buy 42 @ 14.5, pasties buy 4 @ 14.9; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.80 (92/turn) | timber 31 (7.88->12.44), firewood 35 (2.9->6.32), charcoal 19 (2.96->4.99), limestone 5 (17.43->24.7) | spinning wheels 1 (245.7->266), bricks 4 (7.19->11.59), cloth 6 (9.45->10.8), candles 1 (80.85->83.5) | +307 |
| Kirchwerp | 1072 | 0.41 | 0.60 (69/turn) | thread 91 (5.5->6.32), honey 7 (9.5->13.11), jewellery 13 (102.9->104.5), nails 13 (8.19->9.5) | spinning wheels 1 (243.6->266), ham 2 (130.2->134.9), wax 7 (26.25->27.74), flax fibres 12 (5.99->7.4) | +153 |
| Birkeningen | 1006 | 0.37 | 0.50 (57/turn) | beer 62 (3.91->6.41), nets 4 (35->40.47), dyed cloth 2 (12.18->13.87), tackles 1 (152.25->156.75) | hop beer 2 (9.5->11.88), garments 2 (29.4->30.2), wax 1 (27.3->27.74) | +143 |
| Amsdermund | 1111 | 0.43 | 0.20 (23/turn) | wine 17 (7.61->9.12), light armour 2 (98.7->101.65), nets 3 (35->36.86), tackles 1 (152.25->155.8) | cloth 24 (7.35->10.8), spinning wheels 1 (245.7->266), hop beer 2 (7.77->11.88), garments 2 (27.3->30.2) | +133 |
| Etallaen | 774 | 0.24 | 0.10 (11/turn) | garments 10 (26.4->33.63), cloth 10 (11.34->13.11), tackles 1 (152.25->165.3), dyed cloth 2 (12.18->15.2) | gold ore 1 (135.45->147.25), hop beer 2 (9.61->11.88), yarn 3 (3.84->5.51), thread 7 (5.04->5.75) | +132 |

**Best:** Grandgues at about +307 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 5 @ 3.9, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 10 = 6.3 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 10 @ min 21 | goal planner: sells 10 at 21 (v2 had 10 at 25.8) |
| grain | 0 @ 3.7, stop 19 |  | goal planner: buys 0 a turn for today's rates, keeps up to 19 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 21) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 71.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 0.7 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.1k (cash + stock at home prices); -116/turn over 6 turns, +80/turn over 24 turns.
- Limits: cash flow >= -349/turn, prestige >= -0.83/turn (values are after 200 tax a turn).
- Today's settings: value +85/turn, cash +66/turn, prestige -2.71/turn - breaks the prestige floor.
- Plan: value +12/turn, cash +26/turn, prestige -0.83/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +70 vs +82, -716 vs +79, -451 vs +86 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +22/turn
  - ship Flax Wyrm -> Essenbrucke: +2/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.28: +4/turn
  - spinnery 1 1.65 -> 1.46: +3/turn
  - retting pit 1 0.91 -> 0.85: +1/turn
  - flax farm 1 4.64 -> 4.26: +3/turn
  - mansion 1 0.00 -> 0.45: -101/turn
- Model check over the last 60 turns: predicted +126/turn for the settings we ran, real +39/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.80, thread 4.52, cloth 7.22, flax fibres 5.36, garments 20.90, nets 32.70, beer 3.35, timber 3.38, prestige 59.96, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); grain buy 5 (v2 0); labour buy 29 (v2 21); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Donaunieder (+22/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Essenbrucke (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +85/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 5.7/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 77/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.76; ask over the cap 2.1 (60 coin per prestige)
