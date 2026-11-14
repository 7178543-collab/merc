# v2 shadow report

Turn 14019, 2026-11-14 12:31. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,967, prestige 3,525 (405 free, +1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 107 | 27 | 17 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 540 | 0 | 24 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 4 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.66 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.66 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 24 labour expired last turn (~42 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 540, not 626

## Prestige spending, cheapest coin per prestige first

382 turns left: prestige gained now converts 85.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| jousting 3 | arena | 230 | 55.2 | 55.6 | needs a arena (build cost 26,843); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.9 | 59.9 | thin at home: wine, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 60.1 | 60.1 | thin at home: wine |
| jousting 2 | arena | 210 | 60.5 | 60.9 | needs a arena (build cost 26,843); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 61.7 | 61.7 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 62.7 | 62.7 | thin at home: hop beer, wine, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 62.8 | 62.8 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 63.0 | 63.0 | thin at home: wine |
| hold mass 2 (premium) | cathedral | 360 | 61.1 | 64.3 | needs a cathedral (build cost 296,605); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 65.1 | 65.1 | thin at home: wine, hop beer, ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 5 @ 23.4, pasties buy 7 @ 15.6; crew 0.1; est +20 a turn; stock: pasties 7 @ 15.6 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.1 (keep 14); best orders clear only 12 a turn after crew: ship stays at 0
- best towns now: Großmühle +43, Hofkirchen +37, Heilegg +35, Herschweig +32, Unterhufe +31
- Großmühle would trade: cured meat buy 5 @ 22.6, pasties buy 7 @ 12.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (99/turn) | timber 42 (8.09->11.69), firewood 29 (3.84->6.51), lathes 1 (233.1->260.3), charcoal 20 (2.73->3.44) | cloth 7 (8.35->8.85), cured meat 5 (24.15->24.8), garments 2 (22.47->23) | +208 |
| Blanans | 297 | 0.09 | 0.70 (77/turn) | timber 42 (8.09->12.44), cheese 11 (7.72->9.88), bricks 6 (5.78->8.46), flour 2 (17.96->21.09) | dyed cloth 10 (10.71->12.54), cloth 13 (7.56->8.85), dyed yarn 1 (4.73->4.89), flax fibres 2 (5.93->6.15) | +193 |
| Bordetes | 831 | 0.25 | 0.40 (44/turn) | cured fish 6 (24.57->30.78), charcoal 20 (2.73->5.94), leather 1 (23.31->24.32) | butter 1 (56.7->83.12), cloth 23 (7.56->8.85), tools 28 (5.15->6.08), dyed cloth 10 (10.71->12.54) | +144 |
| Hofkirchen | 991 | 0.35 | 0.40 (44/turn) | thread 23 (4.72->5.22), flax fibres 2 (5.7->6.51) | jewellery 5 (84->91.67), cloth 24 (7.35->8.85), dyed cloth 10 (9.97->12.54), cheese 15 (5.25->6.41) | +123 |
| Fontaux | 411 | 0.12 | 0.70 (77/turn) | thread 79 (4.72->5.65), charcoal 20 (2.73->4.99), garments 10 (21.2->22.04), timber 18 (8.09->10.16) | cured meat 4 (23.31->24.8), flax fibres 5 (5.35->6.15), seeds 3 (2.5->3.23), cloth 5 (8.72->8.85) | +118 |

**Best:** Grandgues at about +208 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 17 @ 3.88, stop 67 |  | uses 16.7/turn (household upkeep), makes 0.0, holds 107 = 6.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 86, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 | off | a building is stalled on cured meat: no sell until it runs again |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 40) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.2) |
| pasties |  | 1 @ min 12.5 | goal planner: sells 1 a turn at 12.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 82.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.7k (cash + stock at home prices); -117/turn over 6 turns, -154/turn over 24 turns.
- Limits: cash flow >= -332/turn, prestige >= -0.44/turn (values are after 200 tax a turn).
- Today's settings: value -183/turn, cash -164/turn, prestige +1.98/turn.
- Plan: value -18/turn, cash -8/turn, prestige -0.44/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -155 vs -159, +27 vs -150, +125 vs -158.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Heidlowe: +6/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.42: +149/turn
  - net maker 0.00 -> 0.29: +6/turn
  - flax farm 1 4.64 -> 4.13: -0/turn
  - spinnery 1 1.65 -> 1.33: -0/turn
  - retting pit 1 0.91 -> 0.83: +7/turn
  - weavery 1 0.50 -> 0.39: -9/turn
  - sewing shop 1 0.30 -> 0.23: +10/turn
- Model check over the last 59 turns: predicted -20/turn for the settings we ran, real +1/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.38, beer 3.21, timber 3.46, prestige 60.40, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 40); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Heidlowe (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 422 (+133 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.30 |
| ret | 3 | 0.91 | 0.86 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 110/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.66; ask over the cap 2.1 (60 coin per prestige)
