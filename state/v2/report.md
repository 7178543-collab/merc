# v2 shadow report

Turn 14221, 2026-11-22 22:01. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,353, prestige 3,685 (565 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 72 | 0 | 12 | 0 | 0 | min_holding 58, sell 10, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 20 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 526 | 0 | 38 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (12 @ 32.6), but the home ask 34.00 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 38 labour expired last turn (~64 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 34.00 is above our ceiling 29.00 and last turn bought 3 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.4 coin per prestige at mansion, vs 73.3 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 106 over real use lately; planning 526, not 629

## Prestige spending, cheapest coin per prestige first

180 turns left: prestige gained now converts 59.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.3 | 49.8 | needs a arena (build cost 26,988); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 49.1 | 50.0 | needs a arena (build cost 26,988); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| jousting 2 (premium) | arena | 400 | 53.0 | 53.5 | needs a arena (build cost 26,988); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 53.8 | 54.7 | needs a arena (build cost 26,988); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.4 | 57.4 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 60.1 | 60.1 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 63.6 | 63.6 | thin at home: wine, pies |
| hold banquet 4 (pies) | mansion | 18 | 64.7 | 64.7 | thin at home: hop beer, wine, stockfish |
| hold banquet 5 | mansion | 22 | 65.3 | 65.3 | thin at home: hop beer, wine, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 66.6 | 66.6 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 53.9 | 67.8 | needs a cathedral (build cost 305,080); thin at home: furniture, jewellery, glassware, windows, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 8 @ 6.95; crew 0.1; est +18 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 16.0 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Bedenis +115, Chatgnan +111, Brebronn +96, Dortgart +96, Briclives +95
- Bedenis would trade: furniture buy 7 @ 13.0, pasties buy 6 @ 13.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (107/turn) | bread 237 (2.48->4.08), firewood 35 (1.97->11.4), timber 27 (8.29->11.59), beer 8 (3.13->7.6) | bricks 9 (7.25->10.36), garments 2 (24.36->26.6), furniture 1 (15.86->17.2) | +925 |
| Kirchwerp | 1072 | 0.39 | 0.50 (53/turn) | thread 76 (6.35->9.5), nets 6 (37.4->42.94), flax fibres 4 (5.29->10.64), glass ingots 1 (63->80.75) | tools 18 (4.3->5.61), cured meat 3 (30.66->33.6), garments 2 (24.15->26.6), nails 7 (5.78->6.6) | +324 |
| Rouhomme | 368 | 0.10 | 1.00 (107/turn) | bread 112 (2.48->3.42), firewood 20 (1.97->6.93), nets 2 (37.4->39.33), grain 0 (2.84->3.82) | bricks 10 (5.25->10.36), tools 8 (4.73->5.61), garments 0 (24.99->26.6) | +155 |
| Darmwald | 1022 | 0.35 | 0.60 (64/turn) | yarn 16 (6.83->8.88), charcoal 19 (2.35->6.51), nets 1 (37.4->41.8), wine 1 (6.51->6.93) | thread 34 (5.19->6.55), cured meat 3 (22.05->33.6), flax fibres 9 (5.88->7.45), tin ingots 2 (32.34->33.06) | +132 |
| Donaunieder | 985 | 0.33 | 0.10 (11/turn) | garments 10 (26.4->30.4), candles 4 (87.15->94.52), nets 6 (37.4->40.66) | premium ham 1 (235.2->250.8), cured meat 3 (28.98->33.6), tools 18 (5.17->5.61), nails 1 (5.21->6.6) | +112 |

**Best:** Grandgues at about +925 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 10 @ min 3.46 | sell; ships offer 8 a turn abroad, so home sells 10 (was 15) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 26) |
| light armour | 1 @ 110, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 87.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.7k (cash + stock at home prices); -239/turn over 6 turns, +48/turn over 24 turns.
- Limits: cash flow >= -431/turn, prestige >= -1.10/turn (values are after 200 tax a turn).
- Today's settings: value -191/turn, cash -190/turn, prestige +1.37/turn.
- Plan: value +13/turn, cash +14/turn, prestige -1.10/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -254 vs -177, -97 vs -192, +90 vs -176.
- Route sales counted at most (what the ships really sold, a turn): beer 1.2.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +15/turn
  - ship Flax Wyrm -> Grandgues: +2/turn
  - mansion 1 1.00 -> 0.41: +185/turn
  - net maker 0.00 -> 0.29: +9/turn
  - spinnery 1 1.65 -> 1.56: +4/turn
  - flax farm 1 4.64 -> 4.78: -1/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +16/turn
- Model check over the last 59 turns: predicted -148/turn for the settings we ran, real +79/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.68, thread 4.22, cloth 6.74, flax fibres 5.00, garments 19.51, nets 30.95, beer 2.99, timber 3.53, prestige 73.25, cash 0.00
- Orders it would set: bread buy 5 (v2 6); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 26); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Hofkirchen (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +84/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1885 coin: +5/turn, payback 347 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 90/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
