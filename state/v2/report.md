# v2 shadow report

Turn 14122, 2026-11-18 19:42. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,561, prestige 3,591 (471 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.88 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.88 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~36 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

279 turns left: prestige gained now converts 75.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 54.7 | 55.3 | needs a arena (build cost 28,154); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.4 | 58.4 |  |
| maintain 1 | park | 0.5 | 59.1 | 59.1 | running |
| jousting 2 | arena | 210 | 59.9 | 60.5 | needs a arena (build cost 28,154); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 61.2 | 61.2 | thin at home: cheese |
| hold mass 2 (premium) | cathedral | 360 | 56.0 | 61.2 | needs a cathedral (build cost 302,240); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 1 (meat) | mansion | 4.2 | 63.1 | 63.1 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 64.5 | 64.5 | thin at home: cheese |
| hold banquet 4 (pies) | mansion | 18 | 65.4 | 65.4 | thin at home: stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 65.4 | 65.4 | thin at home: stockfish |
| hold banquet 2 (pies) | mansion | 7 | 65.9 | 65.9 | thin at home: cheese, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 68.8 | 68.8 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: candles buy 3 @ 77.5; crew 0.1; est +25 a turn; stock: candles 3 @ 77.5 (keep 12)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.0 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- best towns now: Amsdermund +635, Cobholme +330, Clairlond +311, Disscester +282, Chribruck +275
- Amsdermund would trade: furniture buy 59 @ 13.7, pasties buy 3 @ 15.4; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~125 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (112/turn) | timber 28 (9.08->12.35), firewood 32 (3.02->6.22), charcoal 18 (2.39->5.75), bread 158 (2.69->3.04) | garments 2 (31.5->40.6), dyed cloth 3 (10.08->13.87), wrought iron 4 (16.7->17.67), beer 4 (3.74->3.96) | +262 |
| Hofkirchen | 991 | 0.39 | 0.20 (25/turn) | glassware 5 (83.48->114), tackles 1 (160.65->171), tallow 1 (18.59->19.76) | garments 2 (26.25->40.6), cloth 24 (9.55->10.9), cheese 4 (6.3->8.84), dyed cloth 3 (12.6->13.87) | +224 |
| Heidlowe | 662 | 0.22 | 0.10 (12/turn) | hides 2 (11.34->12.25) | looms 1 (540.75->608), tapestries 1 (651->703), garments 2 (27.93->40.6), cloth 24 (9.66->10.9) | +177 |
| Amsdermund | 1111 | 0.47 | 0.50 (62/turn) | tackles 1 (160.65->190), grain 2 (3.02->4.16) | cloth 24 (7.35->10.9), garments 2 (26.25->40.6), wrought iron 4 (13.23->17.67), paper 6 (21->23.94) | +175 |
| Heilegg | 826 | 0.28 | 0.20 (25/turn) | wrought iron 8 (20.16->27.55), nets 5 (35.4->37.43), butter 6 (87.67->89.3), hides 2 (11.34->12.82) | cloth 24 (8.66->10.9), garments 2 (28.77->40.6), cheese 4 (6.3->8.84), pies 2 (20.37->22.42) | +156 |

**Best:** Grandgues at about +262 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 4.14, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 10 @ min 21 | goal planner: sells 10 at 21 (v2 had 10 at 35.0) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.3k (cash + stock at home prices); +261/turn over 6 turns, +109/turn over 24 turns.
- Limits: cash flow >= -440/turn, prestige >= -0.71/turn (values are after 200 tax a turn).
- Today's settings: value +109/turn, cash +85/turn, prestige -2.57/turn - breaks the prestige floor.
- Plan: value +39/turn, cash +50/turn, prestige -0.71/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +183 vs +49, +287 vs +60, +114 vs +78.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +2/turn
  - ship Flax Wyrm -> Marmont: +0/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - net maker 0.00 -> 0.28: +3/turn
  - ropewalk 1 0.25 -> 0.31: +2/turn
  - flax farm 1 4.64 -> 4.01: -1/turn
  - retting pit 1 0.91 -> 0.80: +2/turn
  - spinnery 1 1.65 -> 1.41: +8/turn
  - sewing shop 1 0.30 -> 0.25: -21/turn
  - weavery 1 0.50 -> 0.40: -4/turn
- Model check over the last 60 turns: predicted +127/turn for the settings we ran, real +122/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.78, beer 3.26, timber 3.89, prestige 60.27, cash 0.00
- Orders it would set: bread buy 5 (v2 8); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Angefont (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Marmont (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +84/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 7.8/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 427 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.72 |
| ret | 3 | 0.91 | 0.94 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 74/77, thread 1050/227, cloth 72/127

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.88; ask over the cap 2.1 (60 coin per prestige)
- R7 stale ask: limestone ask 16.4 over the market for 6 turns: the town trades ~4 a turn at 16.1, we sold 0 with 46 over what we keep; floor 21.73 (config sell_floor / unit cost) is at or over the market: Taylor's call
