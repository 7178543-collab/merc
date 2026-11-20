# v2 shadow report

Turn 14158, 2026-11-20 07:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,811, prestige 3,751 (631 free, +125.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 33 | 32 | 19 | 0 | 0 | stop 63, buy 32, buy @ 4.78 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 2, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 531 | 0 | 33 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.58 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.58 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 33 labour expired last turn (~71 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 3 (fish)**: hold banquet 3 (fish) costs 61.4 coin per prestige at mansion, vs 73.3 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 3 (pies)**: hold banquet 3 (pies) costs 60.6 coin per prestige at mansion, vs 73.3 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 119 over real use lately; planning 532, not 651
- labour expiry guard: 33 bought labour expired last turn, buy 31 (not 32) this turn

## Prestige spending, cheapest coin per prestige first

243 turns left: prestige gained now converts 70.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 51.0 | 51.3 | needs a arena (build cost 29,847); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.6 | 53.3 | needs a arena (build cost 29,847); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.8 | 55.2 | needs a arena (build cost 29,847); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.6 | 58.4 | needs a arena (build cost 29,847); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 60.6 | 60.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 60.6 | 60.6 | thin at home: wine, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.8 | 60.8 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 61.4 | 61.4 |  |
| hold banquet 2 (pies) | mansion | 7 | 61.5 | 61.5 | thin at home: wine |
| hold banquet 4 (premium) | mansion | 20 | 63.0 | 63.0 | thin at home: wine, stockfish |
| maintain 1 | park | 0.5 | 63.6 | 63.6 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 63.8 | 63.8 | thin at home: beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 12 | 151802239 | 0.12 | - | cured meat 2, pasties 5 | -119 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 7 @ 74.5, cured meat buy 6 @ 19.6, pasties buy 4 @ 16.4; crew 0.1; est +147 a turn; stock: candles 7 @ 74.5 (keep 12); stock: pasties 4 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: candles buy 9 @ 74.0, cured meat buy 4 @ 22.8; crew 0.1; est +146 a turn; stock: candles 9 @ 74.0 (keep 12)
- best towns now: Chatgnan +405, Fulkirch +380, Dortgart +356, Disscester +327, Bedenis +317
- Chatgnan would trade: beer buy 19 @ 3.36, candles buy 7 @ 74.0, cured meat buy 6 @ 22.6, furniture buy 21 @ 13.8, pasties buy 4 @ 13.8; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~134 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.48 | 0.60 (80/turn) | looms 1 (819->897.75), furniture 9 (16.48->24.32), nets 6 (39->42.94), harnesses 1 (47.67->57.95) | cured meat 6 (20.27->26.8), dyed cloth 5 (15.75->21.85), garments 2 (24.15->34.4), cookware 6 (19.43->22.99) | +300 |
| Grandgues | 152 | 0.05 | 0.90 (120/turn) | bread 239 (2.98->3.8), thread 78 (6.05->6.84), tiles 3 (4.14->11.59), firewood 38 (2.71->4.71) | cured meat 6 (20.27->26.8) | +294 |
| Angefont | 686 | 0.24 | 0.30 (40/turn) | thread 78 (6.05->7.03), cloth 26 (12.92->14.34), raw cloth 7 (10.4->14.25), flax fibres 5 (6.4->10.83) | cured meat 6 (24.57->26.8), beer 19 (3.86->4.84), wine 15 (6.46->7.17), tools 13 (6.41->6.98) | +188 |
| Caillechâtel | 488 | 0.17 | 0.20 (27/turn) | lathes 1 (181.65->248.9), harnesses 1 (47.67->55.1), rope 1 (76->79.33), leather 1 (23.52->24.89) | premium ham 2 (218.4->237.5), cloth 24 (11.13->12.3), cured meat 4 (23.52->26.8), tools 13 (6.3->6.98) | +170 |
| Heilegg | 826 | 0.30 | 0.20 (27/turn) | looms 1 (819->897.75), harnesses 1 (47.67->58.42), flour 4 (22.05->26.79), beer 2 (4.78->7.36) | cloth 24 (11.03->12.3), garments 2 (29.4->34.4), cured meat 6 (25.2->26.8), tools 13 (6.41->6.98) | +154 |

**Best:** Kirchwerp at about +300 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 39 @ ?, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 33 = 1.7 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| candles | 2 @ 76.0, stop 6 |  | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 3) |
| cured meat | 11 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 16 = 2.6 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 34 |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 31) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 38.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 74.0) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 1 = 2.3 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.8k (cash + stock at home prices); -767/turn over 6 turns, -93/turn over 24 turns.
- Limits: cash flow >= -284/turn, prestige >= -1.38/turn (values are after 200 tax a turn).
- Today's settings: value -153/turn, cash -164/turn, prestige +137.20/turn.
- Plan: value +493/turn, cash +259/turn, prestige +125.00/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -479 vs -137, -707 vs -176, -374 vs -155 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> no route: -26/turn
  - ship Flax Wyrm -> no route: -11/turn
  - mansion 1 1.00 -> 0.00: +232/turn
  - park 1 16.00 -> 0.00: +62/turn
  - weavery 1 0.50 -> 1.47: +27/turn
  - spinnery 1 1.65 -> 2.68: +81/turn
  - sewing shop 1 0.30 -> 0.36: +26/turn
  - net maker 0.00 -> 0.29: +22/turn
  - flax farm 1 4.64 -> 8.11: +21/turn
  - retting pit 1 0.91 -> 1.60: +133/turn
- Model check over the last 58 turns: predicted -22/turn for the settings we ran, real -9/turn.
- Worth of one more unit per turn: labour 1.38, thread 3.47, cloth 5.54, flax fibres 4.13, garments 16.01, nets 25.64, beer 3.08, timber 4.34, prestige 0.00, cash 0.00
- Orders it would set: candles buy 2 (v2 3); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 31); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.04, worth +7/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.14, worth +12/turn.
- Ship linen snake: Grandgues -> no route (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +69/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 424 (+135 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.42 |
| ret | 3 | 0.91 | 0.88 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 101/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.58; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
