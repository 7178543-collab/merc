# v2 shadow report

Turn 13922, 2026-11-10 11:17. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,705, prestige 3,460 (340 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 2 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (2.0/turn) but there is NO buy order, stock 0.0 -> v2: add buy 5
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.22 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.22 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~74 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 56
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 486, not 586

## Prestige spending, cheapest coin per prestige first

479 turns left: prestige gained now converts 91.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.2 | 54.2 | thin at home: ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 54.3 | 54.3 | thin at home: cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 54.4 | 54.4 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 55.8 | 55.8 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 56.2 | 56.2 | thin at home: ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 56.6 | 56.6 | thin at home: ham, stockfish |
| jousting 3 | arena | 230 | 56.6 | 56.8 | needs a arena (build cost 26,814); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.4 | 58.4 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 58.6 | 58.6 |  |
| hold mass 2 (premium) | cathedral | 360 | 58.5 | 60.7 | needs a cathedral (build cost 290,270); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 2 (meat) | mansion | 6.8 | 61.3 | 61.3 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 8 @ 15.0; crew 0.1; est +21 a turn; stock: pasties 8 @ 15.0 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 16.4 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Essenbrucke +197, Bedenis +188, Chatgnan +169, Großmühle +169, Herschweig +157
- Essenbrucke would trade: furniture buy 13 @ 12.8, pasties buy 9 @ 14.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.21 | 1.00 (103/turn) | beer 41 (3.49->6.84), bread 118 (2.48->3.23), fleece 2 (8.61->12.92), cured fish 5 (24.57->26.41) | flax fibres 16 (4.94->7.1), sails 0 (840->878.75), wrought iron 2 (15.54->17.2), garments 1 (25.41->26.6) | +229 |
| Grandgues | 152 | 0.04 | 0.80 (82/turn) | firewood 25 (3.38->10.45), charcoal 19 (3.26->4.89), cured fish 7 (24.57->27.55), bread 154 (2.48->2.68) | premium garments 1 (126->129.2), dyed cloth 10 (12.71->12.92), cloth 12 (8.66->8.8), salt 4 (5.3->5.56) | +228 |
| Pontmont | 341 | 0.09 | 0.90 (93/turn) | bread 154 (2.48->3.34), thread 33 (4.66->5.56), bricks 6 (9.45->12.73), beer 54 (3.49->3.8) | cloth 18 (7.88->8.8), garments 2 (25.62->26.6) | +146 |
| Kirchwerp | 1072 | 0.37 | 0.90 (93/turn) | thread 92 (4.66->5.7), beer 54 (3.49->4.71), flour 2 (23.52->27.55), spirits 1 (10.13->11.3) | cloth 24 (7.67->8.8), flax fibres 23 (5.78->7.1), dyed cloth 10 (11.97->12.92), garments 2 (24.15->26.6) | +138 |
| Fontaux | 411 | 0.11 | 1.00 (103/turn) | thread 68 (4.66->5.65), bread 120 (2.48->3.13), charcoal 14 (3.26->5.56), spirits 0 (10.13->13.39) | flax plants 2 (1.37->1.69) | +127 |

**Best:** Etallaen at about +229 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 5 @ 3.48, stop 9 |  | uses 2.0/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 84.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 16.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 25.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.9k (cash + stock at home prices); +93/turn over 6 turns, +174/turn over 24 turns.
- Limits: cash flow >= -321/turn, prestige >= -0.17/turn (values are after 200 tax a turn).
- Today's settings: value +59/turn, cash +17/turn, prestige -2.36/turn - breaks the prestige floor.
- Plan: value -38/turn, cash -34/turn, prestige -0.17/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +88 vs +49, +3 vs +44, -28 vs +34.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +28/turn
  - ship Flax Wyrm -> Essenbrucke: +3/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: -2/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.10: +18/turn
  - spinnery 1 1.65 -> 1.38: -4/turn
  - retting pit 1 0.91 -> 0.78: +3/turn
  - flax farm 1 4.64 -> 3.94: +5/turn
  - sewing shop 1 0.30 -> 0.36: -8/turn
  - weavery 1 0.50 -> 0.60: +11/turn
- Model check over the last 59 turns: predicted +106/turn for the settings we ran, real +134/turn.
- Worth of one more unit per turn: labour 1.62, thread 4.11, cloth 6.54, flax fibres 4.95, garments 18.89, nets 29.69, beer 2.90, timber 3.35, prestige 62.16, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.10, worth +5/turn.
- Ship linen snake: Grandgues -> Donaunieder (+28/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Essenbrucke (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1859 coin: +1/turn, payback 2384 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 35/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.32 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.38 (ask 3.32, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.22; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: flax fibres buy not filling: bid 5.05 under the home ask 7.1 for 6 turns, bought 0.0 of 1, 35.3 held (1.3 turns); raise needs Taylor (ceiling None)
