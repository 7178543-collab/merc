# v2 shadow report

Turn 14046, 2026-11-15 15:45. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,310, prestige 3,575 (455 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 19 | 9 | 4 | 0 | 0 | min_holding 60, sell 5, sell @ 3.26; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 48 | 0 | 2 | 0 | 0 | min_holding 30, sell 12, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 21 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 35.2 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.90 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~78 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.90 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

355 turns left: prestige gained now converts 83.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| jousting 3 | arena | 230 | 55.3 | 55.7 | needs a arena (build cost 26,810); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 56.6 | 56.6 | thin at home: pasties, hop beer, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 |  |
| hold banquet 4 (pies) | mansion | 18 | 57.6 | 57.6 | thin at home: hop beer, stockfish, candles |
| hold banquet 2 (pies) | mansion | 7 | 58.5 | 58.5 | thin at home: pasties, cheese, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 59.4 | 59.4 | thin at home: hop beer, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 60.2 | 60.2 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 60.2 | 60.2 | thin at home: hop beer, stockfish, candles |
| jousting 2 | arena | 210 | 60.6 | 61.0 | needs a arena (build cost 26,810); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 61.3 | 61.3 | thin at home: hop beer, stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 58.1 | 61.5 | needs a cathedral (build cost 288,060); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 13.9, pasties buy 4 @ 14.9; crew 0.2; est +257 a turn; stock: furniture 21 @ 13.9 (keep 145); stock: pasties 4 @ 14.9 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Amsdermund +589, Chatgnan +542, Bedenis +437, Gotthafen +429, Bordees +372
- Amsdermund would trade: furniture buy 54 @ 13.7; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (108/turn) | timber 41 (7.88->12.54), furniture 14 (11.97->16.05), bread 146 (2.44->2.79), firewood 31 (3.04->5.18) | cheese 4 (6.35->7.22), garments 1 (24.36->25.6), tiles 2 (3.89->4.35), yarn 1 (5.25->5.32) | +344 |
| Fontaux | 411 | 0.12 | 1.00 (108/turn) | furniture 8 (11.97->17.76), timber 11 (7.88->12.16), charcoal 11 (2.69->5.61), garments 6 (25->27.36) | flax fibres 6 (5.35->6.55), flax plants 13 (1.08->1.5), yarn 1 (5.19->5.32) | +162 |
| Calange | 218 | 0.06 | 0.30 (32/turn) | furniture 16 (11.97->15.11), beer 131 (3.46->3.8), steel ingots 4 (19.43->23.56), cloth 1 (8.3->12.73) | flax fibres 23 (5.35->6.55), yarn 12 (4.96->5.32), seeds 5 (1.94->2.58), garments 2 (25.2->25.6) | +128 |
| Hanbrücken | 531 | 0.15 | 0.90 (97/turn) | timber 21 (7.88->12.25), nets 6 (34.8->39.52), furniture 7 (11.97->15.58), charcoal 16 (2.69->4.84) | cheese 5 (6.51->7.22), thread 6 (4.66->5.15), hop beer 1 (8.98->9.97) | +120 |
| Hofkirchen | 991 | 0.34 | 0.40 (43/turn) | furniture 16 (11.97->15.77), lathes 1 (182.7->197.6), nets 6 (34.8->37.24), pies 5 (18.17->19.95) | jewellery 6 (87.15->90.72), cloth 24 (7.72->8.5), cookware 4 (22.26->24.13), garments 2 (22.26->25.6) | +117 |

**Best:** Grandgues at about +344 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 1 = 2.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat |  | 2 @ min 25.4 | goal planner: trial sale of an idle pile, 2 a turn at 25.4, keeps 0 (14 over) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 12 @ min 21.2 | goal planner: sells 12 at 21.2 (v2 had 12 at 22.6) |
| grain | 0 @ 3.7, stop 24 |  | goal planner: buys 0 a turn for today's rates, keeps up to 24 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.6k (cash + stock at home prices); -10/turn over 6 turns, -27/turn over 24 turns.
- Limits: cash flow >= -221/turn, prestige >= -0.65/turn (values are after 200 tax a turn).
- Today's settings: value +86/turn, cash +102/turn, prestige -2.49/turn - breaks the prestige floor.
- Plan: value +25/turn, cash +55/turn, prestige -0.65/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -320 vs +99, +100 vs +140, -163 vs +99 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Clairlond: +0/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - net maker 0.00 -> 0.29: +10/turn
  - spinnery 1 1.65 -> 1.38: +0/turn
  - ropewalk 1 0.25 -> 0.00: +7/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.14: +9/turn
  - flax farm 1 4.64 -> 4.35: -0/turn
  - weavery 1 0.50 -> 0.57: -8/turn
  - mansion 1 0.00 -> 0.44: -101/turn
- Model check over the last 59 turns: predicted -123/turn for the settings we ran, real -90/turn.
- Worth of one more unit per turn: labour 1.72, thread 4.32, cloth 6.90, flax fibres 5.12, garments 19.97, nets 31.21, beer 3.19, timber 3.87, prestige 62.71, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat sell 2 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); grain buy 6 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.14, worth +5/turn.
- Ship linen snake: Grandgues -> Clairlond (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3943 coin: +2/turn, payback 1895 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 8.7/turn (+0.0 exported); plan makes 32.0 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 409 (+121 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.08 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.64 |
| weave | 3 | 0.50 | 1.24 |
| sew | 2 | 0.30 | 0.78 |

Buffers: flax fibres 116/76, thread 1064/224, cloth 72/124

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
