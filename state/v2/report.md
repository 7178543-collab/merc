# v2 shadow report

Turn 14194, 2026-11-21 19:36. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,964, prestige 3,709 (589 free, +1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 51 | 0 | 19 | 0 | 0 | min_holding 58, sell 15, sell @ 3.5 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 2 | 3 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 33 | 9 | 6 | 0 | 0 | stop 35, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 547 | 0 | 17 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (4 @ 2.4), but the home ask 2.80 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.80 is above our ceiling 2.40 and last turn bought 2 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.90 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 17 labour expired last turn (~34 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.74 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.90 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 103 over real use lately; planning 547, not 636

## Prestige spending, cheapest coin per prestige first

207 turns left: prestige gained now converts 64.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.5 | 50.9 | needs a arena (build cost 28,506); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 53.2 | 54.0 | needs a arena (build cost 28,506); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.3 | 54.8 | needs a arena (build cost 28,506); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 58.3 | 59.1 | needs a arena (build cost 28,506); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 60.0 | 60.0 | running |
| hold banquet 4 (premium) | mansion | 20 | 61.6 | 61.6 | thin at home: hop beer, wine, stockfish, candles |
| hold banquet 4 (pies) | mansion | 18 | 62.2 | 62.2 | thin at home: hop beer, wine, stockfish, cheese, candles |
| hold mass 2 (premium) | cathedral | 360 | 53.8 | 63.6 | needs a cathedral (build cost 305,675); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 67.2 | 67.2 | thin at home: wine, hop beer, stockfish, cheese, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 67.3 | 67.3 |  |
| hold banquet 3 (pies) | mansion | 8 | 68.9 | 68.9 | thin at home: hop beer, cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 70.0 | 70.0 | thin at home: wine, cheese, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 29.8, pasties buy 8 @ 16.4; crew 0.1; est +25 a turn; stock: pasties 8 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: pasties buy 6 @ 12.8; crew 0.1; est +24 a turn; stock: pasties 6 @ 12.8 (keep 14)
- best towns now: Chatgnan +70, Blanans +69, Orlesailles +68, Bordees +60, Bordetes +55
- Chatgnan would trade: furniture buy 3 @ 14.6, pasties buy 10 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~125 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (125/turn) | bread 261 (2.88->4.26), firewood 46 (2.94->8.69), charcoal 19 (2.44->7.74), lead ore 1 (7.82->10.73) | cheese 10 (11.03->13.96), cured meat 6 (30.87->32.6), garments 2 (32.13->34.8), dyed yarn 1 (6.14->6.51) | +660 |
| Kirchwerp | 1072 | 0.45 | 0.80 (100/turn) | thread 104 (6.95->9.5), butter 3 (71.4->82.65), garments 10 (34.4->37.62), casks 9 (6.83->9.36) | cheese 10 (11.87->13.96), jewellery 2 (73.5->80.27), tools 16 (5.25->6.32), chisels 3 (8.4->9.07) | +366 |
| Rouhomme | 368 | 0.12 | 1.00 (125/turn) | beer 117 (4.22->5.7), bread 237 (2.88->3.8), grain 1 (3.24->5.13), resin 3 (2.27->2.93) | tools 14 (5.04->6.32), cookware 5 (22.89->23.94), dyed cloth 2 (15.65->16.91), cheese 9 (13.76->13.96) | +309 |
| Amsdermund | 1111 | 0.48 | 0.30 (38/turn) | windows 1 (840->878.75), wheels 1 (23.1->24.89) | cloth 24 (7.35->11.5), cheese 10 (8.4->13.96), garments 2 (21->34.8), cookware 6 (21.21->23.94) | +235 |
| Heilegg | 826 | 0.28 | 1.00 (125/turn) | beer 92 (4.22->5.7), casks 6 (6.83->11.3), garments 7 (34.4->37.05), furniture 6 (15.75->19.19) | cloth 17 (10.5->11.5), tools 11 (5.25->6.32) | +203 |

**Best:** Grandgues at about +660 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 33 @ 4.22, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 51 = 2.7 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 11 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 14 = 2.3 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 2 @ 15.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 33.4) |
| grain | 9 @ 3.7, stop 35 |  | goal planner: buys 9 a turn for today's rates, keeps up to 35 (v2 had 6) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 47) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 44.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.7k (cash + stock at home prices); +133/turn over 6 turns, +126/turn over 24 turns.
- Limits: cash flow >= -373/turn, prestige >= -1.21/turn (values are after 200 tax a turn).
- Today's settings: value -153/turn, cash -151/turn, prestige +0.96/turn.
- Plan: value +38/turn, cash +44/turn, prestige -1.21/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +228 vs -186, +165 vs -160, +114 vs -168.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanstein: +25/turn
  - ship Flax Wyrm -> Angefont: +5/turn
  - mansion 1 1.00 -> 0.48: +161/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.29: -7/turn
  - retting pit 1 0.91 -> 0.81: +2/turn
  - flax farm 1 4.64 -> 4.09: +6/turn
  - sewing shop 1 0.30 -> 0.23: -10/turn
  - weavery 1 0.50 -> 0.37: +18/turn
- Model check over the last 59 turns: predicted -128/turn for the settings we ran, real +46/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.75, beer 3.37, timber 3.78, prestige 71.79, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 6); labour buy 65 (v2 47); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Hanstein (+13/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+5/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1998 coin: +3/turn, payback 723 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 420 (+131 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.20 |
| ret | 3 | 0.91 | 0.84 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 118/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 4 @ 2.4, home ask 2.8; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
