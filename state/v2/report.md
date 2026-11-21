# v2 shadow report

Turn 14189, 2026-11-21 14:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,088, prestige 3,715 (595 free, +0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 58 | 0 | 19 | 0 | 0 | min_holding 58, sell 15, sell @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 3 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 5 | 5 | 0 | 0 | stop 42, buy 14, buy @ 2.32 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 9 | 9 | 0 | 0 | stop 36, buy 10, buy @ 3.7 |
| labour | 64 | 64 | 543 | 0 | 21 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.72 is above our ceiling 2.40 and last turn bought 3 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.50 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 21 labour expired last turn (~42 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 3.00 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **cured meat**: home ask 30.80 is above our ceiling 29.00 and last turn bought 6 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.50 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 114 over real use lately; planning 543, not 626

## Prestige spending, cheapest coin per prestige first

212 turns left: prestige gained now converts 65.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.4 | 52.2 | needs a arena (build cost 29,602); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 56.3 | 57.2 | needs a arena (build cost 29,602); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.4 | 60.4 | thin at home: wine, stockfish, candles |
| hold banquet 4 (pies) | mansion | 18 | 60.6 | 60.6 | thin at home: wine, stockfish, candles |
| maintain 1 | park | 0.5 | 60.6 | 60.6 | running |
| hold mass 2 (premium) | cathedral | 360 | 52.6 | 61.2 | needs a cathedral (build cost 285,670); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 1 (fish) | mansion | 4.2 | 64.6 | 64.6 |  |
| hold banquet 4 | mansion | 17.5 | 65.5 | 65.5 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 3 (pies) | mansion | 8 | 65.6 | 65.6 | thin at home: cheese, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 67.8 | 67.8 | thin at home: wine, cheese, pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 73.6 | 73.6 | thin at home: wine, cheese |
| jousting 1 | arena | 170 | 72.6 | 73.6 | needs a arena (build cost 29,602); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.4 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 12 a turn after crew: ship stays at 0
- best towns now: Heidlowe +120, Blanans +111, Clairlond +76, Bordees +75, Briclives +70
- Heidlowe would trade: cured meat buy 6 @ 26.8, furniture buy 6 @ 13.4, pasties buy 5 @ 12.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~127 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.46 | 0.70 (89/turn) | glassware 5 (79.28->114), windows 1 (698.25->793.25), thread 45 (7->9.5), butter 3 (75.08->82.65) | cheese 6 (10.13->13.3), garments 2 (29.19->32.4), nails 6 (5.35->6.84), cloth 17 (10.5->11) | +476 |
| Rouhomme | 368 | 0.12 | 1.00 (127/turn) | beer 113 (4.37->5.79), windows 0 (698.25->802.75), lathes 0 (180.6->199.5), nets 3 (45.8->48.92) | tools 13 (5.25->6.37), cheese 5 (11.97->13.3), cookware 5 (20.48->21.28), wrought iron 0 (15.65->16.15) | +308 |
| Hofkirchen | 991 | 0.40 | 0.20 (25/turn) | windows 1 (698.25->883.5), nets 6 (45.8->48.92), flax fibres 5 (7.2->8.98), varnish 3 (17.12->19.19) | cheese 6 (8.98->13.3), garments 2 (28.56->32.4), cured meat 6 (29.4->30.8), cloth 24 (10.5->11) | +248 |
| Grandgues | 152 | 0.05 | 0.60 (76/turn) | firewood 37 (2.86->8.07), charcoal 19 (2.79->5.94), windows 1 (698.25->726.75), lead ore 1 (7.77->10.45) | cured meat 6 (27.72->30.8), cloth 6 (8.98->11), cheese 6 (12.29->13.3), grain 8 (3.61->3.8) | +247 |
| Rotterburg | 1056 | 0.45 | 0.20 (25/turn) | windows 1 (698.25->760), yarn 20 (7.25->8.55), hides 2 (13.55->17.1), dyed yarn 1 (5.46->6.89) | cloth 24 (6.93->11), cured meat 6 (26.67->30.8), ham 1 (87.15->101.65), cheese 6 (11.65->13.3) | +210 |

**Best:** Kirchwerp at about +476 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 5 @ 2.5, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| furniture | 2 @ 17.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 10 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 35 = 4.0 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 43) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 44.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.1k (cash + stock at home prices); +196/turn over 6 turns, +102/turn over 24 turns.
- Limits: cash flow >= -337/turn, prestige >= -1.23/turn (values are after 200 tax a turn).
- Today's settings: value -171/turn, cash -186/turn, prestige +0.93/turn.
- Plan: value +28/turn, cash +31/turn, prestige -1.23/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +220 vs -201, -24 vs -189, +72 vs -191.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Großmühle: +3/turn
  - ship Flax Wyrm -> Blanans: +9/turn
  - mansion 1 1.00 -> 0.49: +152/turn
  - ropewalk 1 0.25 -> 0.12: +12/turn
  - spinnery 1 1.65 -> 1.21: +14/turn
  - retting pit 1 0.91 -> 0.77: +4/turn
  - flax farm 1 4.64 -> 3.88: +1/turn
  - net maker 0.00 -> 0.29: +3/turn
  - weavery 1 0.50 -> 0.40: -14/turn
  - sewing shop 1 0.30 -> 0.25: +2/turn
- Model check over the last 59 turns: predicted -130/turn for the settings we ran, real +3/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.66, beer 3.50, timber 4.41, prestige 67.76, cash 0.00
- Orders it would set: bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 43); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.23, worth +12/turn.
- Ship linen snake: Grandgues -> Großmühle (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2051 coin: +1/turn, payback 2728 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 418 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.07 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 126/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: firewood buy not filling: bid 2.4 under the home ask 2.72 for 6 turns, bought 3.0 of 4, 5.1 held (1.3 turns); raise needs Taylor (ceiling 2.4)
