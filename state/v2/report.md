# v2 shadow report

Turn 14201, 2026-11-22 02:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,924, prestige 3,708 (588 free, +1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 101 | 0 | 19 | 0 | 0 | min_holding 58, sell 17, sell @ 3.86 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 564 | 0 | 0 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 5 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 64, short of ~75 needed -> v2: buy 75

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 65.6 coin per prestige at mansion, vs 78.2 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.70 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 88 over real use lately; planning 575, not 664

## Prestige spending, cheapest coin per prestige first

200 turns left: prestige gained now converts 63.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 47.6 | 48.0 | needs a arena (build cost 28,678); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 51.1 | 51.6 | needs a arena (build cost 28,678); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.8 | 53.7 | needs a arena (build cost 28,678); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.9 | 58.8 | needs a arena (build cost 28,678); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 2 | park | 2 | 59.4 | 59.4 | thin at home: sculptures |
| hold banquet 5 | mansion | 22 | 60.7 | 60.7 | thin at home: hop beer, wine, stockfish, sculptures |
| maintain 1 | park | 0.5 | 61.2 | 61.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 63.3 | 63.3 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 53.8 | 64.4 | needs a cathedral (build cost 306,595); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 (premium) | mansion | 20 | 65.0 | 65.0 | thin at home: hop beer, wine, stockfish, premium ham |
| hold banquet 1 (fish) | mansion | 4.2 | 65.6 | 65.6 |  |
| hold banquet 2 (pies) | mansion | 7 | 65.9 | 65.9 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.4 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.3 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Pontmont +68, Birkeningen +46, Amsdermund +42, Kirchwerp +36, Calange +26
- Pontmont would trade: cured meat buy 6 @ 24.6, pasties buy 7 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~130 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (130/turn) | bread 260 (2.88->5.7), firewood 43 (2.27->11.78), charcoal 17 (2.71->6.6), furniture 8 (15.65->18.71) | cloth 7 (11.65->13), garments 1 (28.35->32.4) | +1200 |
| Kirchwerp | 1072 | 0.47 | 0.70 (91/turn) | thread 91 (6.7->9.5), nets 6 (40.2->45.41), furniture 9 (15.65->20.33), varnish 2 (18.79->26.6) | cloth 24 (10.5->13), cured meat 6 (27.93->33.6), cookware 6 (21->24.13), garments 2 (24.15->32.4) | +447 |
| Rouhomme | 368 | 0.13 | 0.90 (117/turn) | bread 287 (2.88->4.07), lathes 1 (183.75->220.4), honey 6 (9.24->11.59), cheese 18 (12.81->13.3) | cloth 15 (11.76->13), tools 16 (4.73->5.7) | +327 |
| Heilegg | 826 | 0.30 | 0.40 (52/turn) | candles 7 (81.38->84.55), lathes 1 (183.75->199.5), furniture 9 (15.65->17.95), malt 2 (8.29->13.3) | cloth 24 (10.45->13), garments 2 (25.41->32.4), tools 16 (4.62->5.7), dyed cloth 7 (14.7->16.25) | +194 |
| Hofkirchen | 991 | 0.41 | 0.40 (52/turn) | windows 2 (840->855), thread 72 (6.7->7.27), nets 3 (40.2->43.89), paper 3 (27.09->30.02) | cloth 24 (9.24->13), coats 4 (81.9->86.92), cookware 6 (22.26->24.13), dyed cloth 7 (14.7->16.25) | +189 |

**Best:** Grandgues at about +1200 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 4 @ min 3.6 | makes 19.3, uses 19.2, holds 101 (keeps 58): sells the surplus + 4/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 79.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 11) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 2 @ 16.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 75) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 39.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 83.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.6k (cash + stock at home prices); +33/turn over 6 turns, +114/turn over 24 turns.
- Limits: cash flow >= -372/turn, prestige >= -1.20/turn (values are after 200 tax a turn).
- Today's settings: value -197/turn, cash -178/turn, prestige +0.97/turn.
- Plan: value +4/turn, cash +21/turn, prestige -1.20/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +93 vs -184, -138 vs -162, -89 vs -177.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: +24/turn
  - ship Flax Wyrm -> Donaunieder: +9/turn
  - mansion 1 1.00 -> 0.48: +170/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.07: -3/turn
  - spinnery 1 1.65 -> 1.23: +13/turn
  - retting pit 1 0.91 -> 0.78: +2/turn
  - flax farm 1 4.64 -> 3.92: +9/turn
- Model check over the last 59 turns: predicted -130/turn for the settings we ran, real +38/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.80, thread 4.57, cloth 7.27, flax fibres 5.48, garments 21.00, nets 32.82, beer 3.53, timber 3.80, prestige 75.62, cash 0.00
- Orders it would set: bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 11); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 64 (v2 75); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Calange (+23/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+9/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2052 coin: +5/turn, payback 430 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 422 (+133 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.29 |
| ret | 3 | 0.91 | 0.86 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 111/77, thread 1050/228, cloth 73/128

## Self-diagnosis

Nothing found this run.
