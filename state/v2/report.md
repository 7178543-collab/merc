# v2 shadow report

Turn 14222, 2026-11-22 23:47. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,377, prestige 3,682 (562 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 69 | 0 | 4 | 0 | 0 | min_holding 58, sell 10, sell @ 3.46 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 20 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 539 | 0 | 25 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), but the home ask 32.20 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12

## Waste (money lost now)

- **labour**: 25 labour expired last turn (~42 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 32.20 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 59.9 coin per prestige at mansion, vs 74.6 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 103 over real use lately; planning 556, not 659

## Prestige spending, cheapest coin per prestige first

179 turns left: prestige gained now converts 59.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.4 | 49.9 | needs a arena (build cost 27,384); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 3 | arena | 230 | 49.6 | 50.5 | needs a arena (build cost 27,384); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.3 | 53.8 | needs a arena (build cost 27,384); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.3 | 55.3 | needs a arena (build cost 27,384); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 59.9 | 59.9 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 61.0 | 61.0 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 64.1 | 64.1 | thin at home: wine, pies |
| hold banquet 4 (pies) | mansion | 18 | 64.1 | 64.1 | thin at home: hop beer, wine, stockfish |
| hold banquet 5 | mansion | 22 | 64.8 | 64.8 | thin at home: hop beer, wine, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 66.2 | 66.2 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 67.7 | 67.7 | thin at home: wine, hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0 | - | cured meat 3 | -90 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | beer 8 | - | 40 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 10 @ 7.25; crew 0.1; est +19 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.3 (keep 14); best orders clear only 8 a turn after crew: ship stays at 0
- best towns now: Chatgnan +122, Bedenis +113, Clairlond +100, Briclives +91, Großaue +77
- Chatgnan would trade: furniture buy 7 @ 12.9, pasties buy 7 @ 13.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | firewood 36 (2.35->11.4), bread 230 (2.44->3.76), beer 16 (4->7.69), timber 28 (8.24->10.45) | bricks 10 (7.35->10.36), axes 2 (19.95->23.56), coats 1 (74.03->81.22), steel ingots 1 (18.06->19.19) | +793 |
| Boistot | 1230 | 0.47 | 0.30 (32/turn) | nets 6 (37.4->41.61), rope 1 (89.5->95.95), slaked lime 1 (8.77->10.45) | sculptures 1 (2016->2584), thread 10 (5.62->6.65), axes 2 (22.05->23.56), cloth 1 (7.77->10.3) | +594 |
| Heilegg | 826 | 0.24 | 0.30 (32/turn) | casks 11 (6.51->11.3), nets 5 (37.4->43.13), beer 16 (4->5.75), wrought iron 15 (17.22->17.86) | jewellery 5 (77.17->82.17), cloth 24 (9.77->10.3), dyed cloth 10 (14.7->15.2), tools 18 (5.25->5.65) | +150 |
| Kirchwerp | 1072 | 0.38 | 0.20 (21/turn) | nets 6 (37.4->42.94), glass ingots 1 (63->79.33), flax fibres 6 (7.61->9.45), honey 1 (8.98->13.21) | jewellery 5 (73.5->82.17), tools 18 (4.3->5.65), tin ingots 2 (25.41->33.06), nails 11 (5.78->6.6) | +147 |
| Hofkirchen | 991 | 0.34 | 0.30 (32/turn) | nets 3 (37.4->48.92), glass ingots 1 (63->80.27), resin 2 (2.81->7.03), yarn 13 (6.04->6.84) | jewellery 5 (73.5->82.17), glassware 4 (63.53->65.08), nails 11 (5.78->6.6), tools 18 (5.15->5.65) | +136 |

**Best:** Grandgues at about +793 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 10 @ min 4.18 | sell; ships offer 10 a turn abroad, so home sells 10 (was 15) |
| bread | 5 @ 2.38, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 85, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 24.6) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 56) |
| light armour | 1 @ 110, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 87.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 32.0k (cash + stock at home prices); -125/turn over 6 turns, +58/turn over 24 turns.
- Limits: cash flow >= -432/turn, prestige >= -1.09/turn (values are after 200 tax a turn).
- Today's settings: value -183/turn, cash -184/turn, prestige +1.38/turn.
- Plan: value +17/turn, cash +20/turn, prestige -1.09/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -97 vs -192, +90 vs -176, +24 vs -190.
- Route sales counted at most (what the ships really sold, a turn): beer 1.2.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +7/turn
  - ship Flax Wyrm -> Grandgues: +3/turn
  - mansion 1 1.00 -> 0.41: +180/turn
  - net maker 0.00 -> 0.29: +9/turn
  - spinnery 1 1.65 -> 1.54: +4/turn
  - flax farm 1 4.64 -> 4.74: -1/turn
  - sewing shop 1 0.30 -> 0.36: -11/turn
  - weavery 1 0.50 -> 0.60: +15/turn
- Model check over the last 58 turns: predicted -151/turn for the settings we ran, real +78/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.67, thread 4.20, cloth 6.70, flax fibres 4.98, garments 19.39, nets 30.76, beer 2.98, timber 3.96, prestige 70.58, cash 0.00
- Orders it would set: bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 56); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Brunnham (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+5/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1926 coin: +4/turn, payback 455 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 88/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 3.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 32.2 -> **buy 12 @ 32.8 (ask 32.2, cap 42.0)** (ok)
- R1: prestige rate -2.82 a turn vs 12-turn median +0.74; likely: dry slot: cured meat
