# v2 shadow report

Turn 14215, 2026-11-22 16:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,835, prestige 3,683 (563 free, +0.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 17 | 0 | 0 | min_holding 58, sell 15, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 0 | 0 | 0 | 0 | stop 42, buy 14, buy @ 2.26 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 20 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 558 | 0 | 6 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (12 @ 33.6), but the home ask 35.20 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **cured meat**: home ask 35.20 is above our ceiling 29.00 and last turn bought 5 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 56.8 coin per prestige at mansion, vs 74.2 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 103 over real use lately; planning 561, not 664

## Prestige spending, cheapest coin per prestige first

186 turns left: prestige gained now converts 60.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.7 | 50.1 | needs a arena (build cost 27,657); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 51.0 | 51.8 | needs a arena (build cost 27,657); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| jousting 2 (premium) | arena | 400 | 53.3 | 53.8 | needs a arena (build cost 27,657); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 |  |
| jousting 2 | arena | 210 | 55.8 | 56.8 | needs a arena (build cost 27,657); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 62.7 | 62.7 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 63.4 | 63.4 | thin at home: hop beer, stockfish, pies |
| hold banquet 2 (pies) | mansion | 7 | 63.6 | 63.6 | thin at home: pies |
| hold banquet 5 | mansion | 22 | 64.0 | 64.0 | thin at home: pies, hop beer, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 65.3 | 65.3 | thin at home: hop beer, stockfish, premium cheese |
| hold mass 2 (premium) | cathedral | 360 | 54.3 | 67.0 | needs a cathedral (build cost 304,560); thin at home: furniture, jewellery, glassware, windows, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 2 @ 6.0, cured meat buy 5 @ 32.6, pasties buy 4 @ 16.0; crew 0.1; est +20 a turn; stock: pasties 4 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 14.3 (keep 14); best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Gottweiler +54, Heilegg +48, Großaue +44, Clairlond +42, Fulkirch +40
- Gottweiler would trade: cured meat buy 5 @ 26.4, pasties buy 4 @ 13.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (113/turn) | bread 208 (2.54->4.69), firewood 38 (2.04->11.69), timber 29 (9.03->12.16), thread 75 (6.7->7.03) | cloth 4 (6.88->11.7), bricks 7 (8.09->10.45), flax fibres 5 (8.61->10.4), canvas 0 (54.6->62.22) | +947 |
| Heilegg | 826 | 0.26 | 0.40 (45/turn) | wrought iron 14 (16.59->27.55), flour 10 (19.11->26.79), nets 5 (37.4->45.03), wine 11 (6.62->7.41) | cloth 24 (9.92->11.7), tools 18 (5.04->6.79), cured meat 5 (30.03->35.2), thread 32 (6.25->6.75) | +383 |
| Hofkirchen | 991 | 0.36 | 0.70 (79/turn) | nets 6 (37.4->42.94), swords 3 (258.3->264.1), glass ingots 2 (60.9->66.97), wine 8 (6.62->7.6) | thread 55 (5.62->6.75), cloth 24 (10.29->11.7), flax fibres 27 (8.77->10.4), tools 18 (5.15->6.79) | +239 |
| Heidlowe | 662 | 0.20 | 0.40 (45/turn) | nets 6 (37.4->40.47), beer 2 (3.33->4.84), cured fish 6 (24.57->25.27) | flax fibres 28 (6.41->10.4), cured meat 5 (31.08->35.2), tackles 1 (154.35->171.95), cloth 24 (10.82->11.7) | +228 |
| Angefont | 686 | 0.21 | 0.40 (45/turn) | garments 10 (28.2->29.45), flour 4 (19.11->22.61), fleece 2 (7.56->8.6), nets 6 (37.4->38.19) | flax fibres 23 (5.78->10.4), thread 62 (5.88->6.75), tools 18 (5.78->6.79), cloth 12 (10.45->11.7) | +204 |

**Best:** Grandgues at about +947 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 39.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 10 @ min 3.38 | sell; ships offer 2 a turn abroad, so home sells 10 (was 15) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 86, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 6 = 1.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.4) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 9) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 61) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 85.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 33.3k (cash + stock at home prices); +275/turn over 6 turns, +128/turn over 24 turns.
- Limits: cash flow >= -451/turn, prestige >= -1.10/turn (values are after 200 tax a turn).
- Today's settings: value -173/turn, cash -171/turn, prestige +1.09/turn.
- Plan: value +23/turn, cash -35/turn, prestige -1.10/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +224 vs -179, -44 vs -176, -100 vs -186.
- Route sales counted at most (what the ships really sold, a turn): beer 1.2.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gottweiler: +30/turn
  - ship Flax Wyrm -> Blanans: +6/turn
  - mansion 1 1.00 -> 0.48: +163/turn
  - flax farm 1 4.64 -> 7.28: +6/turn
  - retting pit 1 0.91 -> 1.00: +15/turn
  - net maker 0.00 -> 0.29: +4/turn
  - weavery 1 0.50 -> 0.61: -7/turn
  - sewing shop 1 0.30 -> 0.36: +11/turn
  - ropewalk 1 0.25 -> 0.00: -16/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.35: +18/turn
- Model check over the last 59 turns: predicted -143/turn for the settings we ran, real +40/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.73, thread 4.35, cloth 6.94, flax fibres 5.16, garments 20.09, nets 31.90, beer 3.10, timber 3.69, prestige 74.08, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); fish buy 0 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 61); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.35, worth +11/turn.
- Ship linen snake: Grandgues -> Gottweiler (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1928 coin: +5/turn, payback 379 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 84/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: fish slot dry: 3.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy 14 @ 2.26, home ask 2.22; our bid is already at/over the ask (sellers too thin)
