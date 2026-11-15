# v2 shadow report

Turn 14047, 2026-11-15 16:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,537, prestige 3,573 (453 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 14 | 9 | 4 | 0 | 0 | min_holding 60, sell 5, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 46 | 0 | 2 | 0 | 0 | min_holding 30, sell 12, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~77 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

354 turns left: prestige gained now converts 83.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| jousting 3 | arena | 230 | 55.9 | 56.3 | needs a arena (build cost 26,662); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.6 | 56.6 |  |
| hold banquet 3 (pies) | mansion | 8 | 56.8 | 56.8 | thin at home: pasties, hop beer |
| hold banquet 4 (pies) | mansion | 18 | 57.7 | 57.7 | thin at home: hop beer, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 58.4 | 58.4 | thin at home: pasties, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 59.7 | 59.7 | thin at home: hop beer, cured fish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 60.1 | 60.1 | thin at home: cured fish, cheese |
| hold banquet 4 | mansion | 17.5 | 61.3 | 61.3 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 61.6 | 61.6 | thin at home: hop beer, stockfish, premium ham |
| jousting 2 | arena | 210 | 61.2 | 61.6 | needs a arena (build cost 26,662); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 61.7 | 61.7 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 14.3, pasties buy 5 @ 14.9; crew 0.2; est +253 a turn; stock: furniture 21 @ 14.3 (keep 145); stock: pasties 5 @ 14.9 (keep 14)
- **linen snake** on Grandgues: nets sell 2 @ 41.4, pasties buy 14 @ 15.4; crew 0.1; est +50 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Chatgnan +640, Amsdermund +603, Angefont +546, Gotthafen +461, Bedenis +370
- Chatgnan would trade: furniture buy 55 @ 13.8; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | timber 42 (7.88->12.63), firewood 30 (3.02->5.75), furniture 12 (15.12->17.76), bread 145 (2.48->2.81) | rope 2 (81.38->82.65), candles 0 (86.1->88), cheese 3 (6.46->6.93), garments 1 (24.36->25.6) | +345 |
| Hanstein | 380 | 0.11 | 0.40 (43/turn) | timber 11 (7.88->11.3), charcoal 16 (2.69->4.12), wheels 1 (17.12->23.18), nets 3 (34.4->35.15) | looms 1 (556.5->688.75), seeds 11 (1.92->2.58), thread 12 (4.66->5.15), yarn 11 (4.77->5.32) | +180 |
| Fontaux | 411 | 0.12 | 1.00 (106/turn) | thread 23 (4.98->7.27), timber 11 (7.88->12.16), charcoal 11 (2.69->5.98), firewood 16 (3.02->7.5) | flax fibres 6 (5.35->6.2), candles 0 (85.58->88), tools 10 (5.78->5.98), flax plants 0 (1.14->1.49) | +165 |
| Heidlowe | 662 | 0.19 | 0.10 (11/turn) | nets 3 (34.4->37.62), wheels 1 (17.12->21.47), cloth 1 (8.4->8.88), honey 1 (8.35->8.55) | looms 1 (572.25->688.75), cheese 4 (5.46->6.93), yarn 10 (4.96->5.32), candles 1 (86.62->88) | +134 |
| Hanbrücken | 531 | 0.15 | 0.90 (96/turn) | timber 22 (7.88->12.25), charcoal 16 (2.69->4.84), nets 5 (34.4->37.24), bricks 5 (7.04->11.88) | rope 1 (71.92->82.65), candles 1 (85.58->88), thread 6 (4.75->5.15), cheese 4 (6.46->6.93) | +93 |

**Best:** Grandgues at about +345 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 6 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 14 = 3.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat |  | 2 @ min 24.6 | goal planner: trial sale of an idle pile, 2 a turn at 24.6, keeps 0 (14 over) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 12 @ min 21.2 | goal planner: sells 12 at 21.2 (v2 had 12 at 22.8) |
| grain | 6 @ 3.7, stop 23 |  | goal planner: buys 6 a turn for today's rates, keeps up to 23 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 10 @ min 34.0 | sell; ships offer 2 a turn abroad, so home sells 10 (was 9) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.8k (cash + stock at home prices); +83/turn over 6 turns, -20/turn over 24 turns.
- Limits: cash flow >= -231/turn, prestige >= -0.64/turn (values are after 200 tax a turn).
- Today's settings: value +65/turn, cash +61/turn, prestige -2.47/turn - breaks the prestige floor.
- Plan: value +7/turn, cash +36/turn, prestige -0.64/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +100 vs +140, -163 vs +99, +227 vs +102.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +11/turn
  - ship Flax Wyrm -> Rouhomme: +0/turn
  - net maker 0.00 -> 0.24: +8/turn
  - flax farm 1 4.64 -> 4.26: -1/turn
  - retting pit 1 0.91 -> 0.85: -0/turn
  - spinnery 1 1.65 -> 1.35: +5/turn
  - ropewalk 1 0.25 -> 0.00: +8/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.12: +10/turn
  - weavery 1 0.50 -> 0.57: -9/turn
  - mansion 1 0.00 -> 0.44: -99/turn
- Model check over the last 59 turns: predicted -123/turn for the settings we ran, real -92/turn.
- Worth of one more unit per turn: labour 1.70, thread 4.27, cloth 6.82, flax fibres 5.06, garments 19.73, nets 30.85, beer 3.11, timber 3.89, prestige 61.13, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); cured meat sell 2 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); grain buy 6 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.12, worth +5/turn.
- Ship linen snake: Grandgues -> Brunnham (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Rouhomme (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3977 coin: +2/turn, payback 1810 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 8.8/turn (+0.0 exported); plan makes 32.0 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 409 (+121 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.07 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.64 |
| weave | 3 | 0.50 | 1.25 |
| sew | 2 | 0.30 | 0.78 |

Buffers: flax fibres 118/76, thread 1064/224, cloth 72/125

## Self-diagnosis

- R1: arms slot dry: 0.5 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 32.8, home ask 31.4; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
