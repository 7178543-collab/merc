# v2 shadow report

Turn 14248, 2026-11-24 01:01. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,649, prestige 3,694 (574 free, +1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 27 | 0 | 19 | 0 | 0 | none |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 11 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 7 | 7 | 7 | 2 | 0 | stop 25, buy 7, buy @ 3.7 |
| labour | 64 | 64 | 550 | 0 | 14 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (19.2/turn) but there is NO buy order, stock 27.5 -> v2: add buy 39
- **grain**: brewery 1 ran short of grain (buy is live (7 @ 3.7), 7 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.8 turns of grain left and buying 7 (need 18) -> v2: buy 18

## Tuning

- **cured meat**: home ask 29.20 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 56.2 coin per prestige at mansion, vs 66.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 109 over real use lately; planning 556, not 665

## Prestige spending, cheapest coin per prestige first

153 turns left: prestige gained now converts 53.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 47.7 | 48.8 | needs a arena (build cost 26,601); thin at home: swords, protection, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| jousting 2 | arena | 210 | 52.3 | 53.5 | needs a arena (build cost 26,601); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.1 | 55.1 | thin at home: beer |
| hold banquet 2 (fish) | mansion | 6.8 | 56.2 | 56.2 |  |
| hold banquet 2 (pies) | mansion | 7 | 60.1 | 60.1 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 64.0 | 64.0 | thin at home: hop beer, stockfish, glassware |
| hold banquet 5 | mansion | 22 | 64.9 | 64.9 | thin at home: hop beer, stockfish, sculptures, glassware |
| hold banquet 2 (meat) | mansion | 6.8 | 65.1 | 65.1 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 66.5 | 66.5 | running; thin at home: beer |
| hold banquet 4 (premium) | mansion | 20 | 67.5 | 67.5 | thin at home: hop beer, stockfish, premium cheese, glassware |
| hold banquet 4 | mansion | 17.5 | 67.8 | 67.8 | thin at home: hop beer, stockfish, glassware |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | beer 3 | cured meat 6 | -131 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: cured meat buy 4 @ 26.2, pasties buy 7 @ 13.8; crew 0.1; est +44 a turn; stock: pasties 7 @ 13.8 (keep 14)
- **linen snake** on Grandgues: beer sell 2 @ 5.3, cured meat buy 6 @ 24.4; crew 0.1; est +32 a turn
- best towns now: Darmwald +53, Donaunieder +49, Chatgnan +44, Rouhomme +44, Caillechâtel +44
- Darmwald would trade: cured meat buy 6 @ 21.4, pasties buy 7 @ 16.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Pontmont | 341 | 0.10 | 0.70 (74/turn) | timber 40 (8.03->13.21), tiles 7 (3.23->7.08), nails 10 (8.19->9.5), wrought iron 2 (20.37->26.6) | bricks 13 (6.3->10.07), cured meat 6 (28.35->30.8), thread 6 (5.57->6.1), tools 20 (5.78->5.98) | +260 |
| Rouhomme | 368 | 0.10 | 0.60 (64/turn) | garments 10 (27.6->33.06), yarn 10 (5.83->7.22), wine 17 (6.41->7.03), wheels 8 (23.73->24.89) | bricks 23 (5.04->10.07), cured meat 6 (27.09->30.8), tools 20 (5.3->5.98), cookware 5 (24.99->27.36) | +223 |
| Kirchwerp | 1072 | 0.38 | 0.50 (53/turn) | canvas 5 (42.63->52.25), casks 11 (6.51->9.36), lead bars 3 (12.5->19), light armour 4 (94.5->99.75) | jewellery 6 (74.03->81.22), dyed cloth 4 (14.7->16.81), garments 2 (24.15->28), wrought iron 3 (15.44->17.39) | +213 |
| Donaunieder | 985 | 0.33 | 0.20 (21/turn) | garments 10 (27.6->35.15), cloth 9 (9.55->16.15), nets 3 (37->39.33), glass ingots 2 (62.48->64.6) | cured meat 6 (24.57->30.8), wool 6 (10.4->11.21), pies 1 (17.22->18.9), tools 20 (5.62->5.98) | +176 |
| Vauxvais | 204 | 0.06 | 0.50 (53/turn) | grain 95 (2.94->3.74), bread 158 (2.31->2.77), thread 14 (6->7.03), charcoal 19 (2.09->2.98) | cured meat 5 (27.93->30.8), tools 20 (5.46->5.98), bricks 5 (7.3->10.07), flax fibres 6 (5.78->6.4) | +174 |

**Best:** Pontmont at about +260 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 39 @ 3.94, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 27 = 1.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 10 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 17 = 2.8 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.0) |
| grain | 7 @ 3.7, stop 25 |  | goal planner: buys 7 a turn for today's rates, keeps up to 25 (v2 had 18) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 56) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.2k (cash + stock at home prices); -70/turn over 6 turns, -10/turn over 24 turns.
- Limits: cash flow >= -360/turn, prestige >= -1.14/turn (values are after 200 tax a turn).
- Today's settings: value -126/turn, cash -120/turn, prestige +1.34/turn.
- Plan: value +42/turn, cash +47/turn, prestige -1.14/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -77 vs -124, +40 vs -117, -369 vs -132.
- Route sales counted at most (what the ships really sold, a turn): beer 2.1, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Darmwald: +12/turn
  - ship Flax Wyrm -> Grandgues: +3/turn
  - mansion 1 1.00 -> 0.41: +147/turn
  - net maker [make nets 1] 0.00 -> 0.38: +5/turn
  - spinnery 1 1.65 -> 1.60: +2/turn
  - flax farm 1 4.64 -> 2.95: +1/turn
  - sewing shop 1 0.30 -> 0.36: -6/turn
  - weavery 1 0.50 -> 0.60: +10/turn
- Model check over the last 59 turns: predicted -156/turn for the settings we ran, real +22/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.70, thread 4.27, cloth 6.82, flax fibres 5.06, garments 19.74, nets 31.98, beer 2.99, timber 3.26, prestige 61.39, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 6); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 7 (v2 18); labour buy 65 (v2 56); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +2/turn.
- Ship linen snake: Grandgues -> Darmwald (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +84/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 87/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 27.5 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.76 -> **buy 39 @ 3.82 (ask 3.76, cap 14.4)** (ok)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: cured meat buy not filling: bid 29 under the home ask 29.2 for 3 turns, bought 0.0 of 3, 17.0 held (2.8 turns); raise needs Taylor (ceiling 29.0)
