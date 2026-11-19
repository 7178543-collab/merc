# v2 shadow report

Turn 14143, 2026-11-19 16:24. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,582, prestige 3,646 (526 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 47 | 12 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 47, buy 12, buy @ 3.48 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 501 | 0 | 63 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.66 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.66 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.70 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 63 labour expired last turn (~123 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 3.18 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.70 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 502, not 602
- labour expiry guard: 63 bought labour expired last turn, buy 2 (not 2) this turn

## Prestige spending, cheapest coin per prestige first

258 turns left: prestige gained now converts 72.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.0 | 50.3 | needs a arena (build cost 28,005); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.7 | 54.0 | needs a arena (build cost 28,005); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.3 | 54.8 | needs a arena (build cost 28,005); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.8 | 57.8 |  |
| maintain 1 | park | 0.5 | 58.5 | 58.5 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 59.5 | 59.5 |  |
| jousting 2 | arena | 210 | 59.4 | 60.1 | needs a arena (build cost 28,005); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 60.4 | 60.4 | thin at home: candles |
| hold banquet 3 (pies) | mansion | 8 | 60.9 | 60.9 | thin at home: hop beer, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 61.3 | 61.3 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 61.8 | 61.8 | thin at home: hop beer, stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 57.2 | 63.3 | needs a cathedral (build cost 303,990); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 3 @ 24.4, pasties buy 14 @ 16.2; crew 0.1; est +30 a turn; stock: pasties 14 @ 16.2 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 11.1 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Angefont +544, Cobholme +364, Fulkirch +327, Brunnham +285, Clairas +248
- Angefont would trade: cured meat buy 3 @ 24.2, furniture buy 49 @ 14.6, pasties buy 2 @ 13.7; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~124 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.70 (87/turn) | glassware 8 (88.73->104.5), bread 198 (3.34->4.01), timber 42 (9.5->12.54), thread 92 (5.5->6.27) | paper 3 (21->24.32), cured meat 3 (25.2->26), flax fibres 3 (7.61->7.95), hop beer 3 (8.77->9.12) | +470 |
| Fontaux | 411 | 0.14 | 1.00 (124/turn) | thread 92 (5.5->7.27), garments 10 (32.6->34.58), timber 39 (9.5->11.88), salt 6 (6.2->7.79) | swords 2 (228.9->237.5), cured meat 3 (24.99->26), pasties 5 (12.6->13.11), raw cloth 1 (11.34->12.06) | +228 |
| Bordetes | 831 | 0.29 | 0.10 (12/turn) | glassware 5 (88.73->108.3), dyed cloth 16 (19.32->23.37), garments 10 (32.6->38), flax fibres 1 (7.6->9.31) | leather 1 (28.77->30.78), salt 3 (4.94->5.56) | +210 |
| Angefont | 686 | 0.23 | 0.30 (37/turn) | thread 92 (5.5->6.55), garments 10 (32.6->37.24), dyed cloth 10 (19.32->20.71), flax fibres 4 (7.6->9.59) | candles 6 (73.5->75.52), cloth 23 (11.65->12.1), furniture 1 (15.33->17.9), cured meat 3 (25.2->26) | +168 |
| Hofkirchen | 991 | 0.39 | 0.40 (50/turn) | blades 2 (21->33.25), nets 6 (36.8->41.23), dyed cloth 17 (19.32->20.33), jewellery 3 (108.15->109.25) | cloth 24 (10.08->12.1), flax fibres 23 (6.3->7.95), candles 10 (73.5->75.52), coats 4 (81.9->84.55) | +159 |

**Best:** Grandgues at about +470 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 12 @ 3.52, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 47 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 31.8) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 34 |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 2) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.5k (cash + stock at home prices); +115/turn over 6 turns, +51/turn over 24 turns.
- Limits: cash flow >= -441/turn, prestige >= -0.94/turn (values are after 200 tax a turn).
- Today's settings: value -154/turn, cash -158/turn, prestige +1.37/turn.
- Plan: value +26/turn, cash +29/turn, prestige -0.94/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +9 vs -133, +137 vs -136, -244 vs -151.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +13/turn
  - ship Flax Wyrm -> Bordees: +3/turn
  - mansion 1 1.00 -> 0.45: +134/turn
  - brewery 1 0.14 -> 0.01: +20/turn
  - net maker 0.00 -> 0.29: +8/turn
  - spinnery 1 1.65 -> 1.39: +3/turn
  - retting pit 1 0.91 -> 0.80: +2/turn
  - flax farm 1 4.64 -> 4.02: +7/turn
- Model check over the last 59 turns: predicted +44/turn for the settings we ran, real +78/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.71, beer 3.36, timber 3.69, prestige 63.37, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); labour buy 64 (v2 2); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Ship linen snake: Grandgues -> Amsdermund (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordees (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 90/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.66; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
