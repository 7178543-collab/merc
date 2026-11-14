# v2 shadow report

Turn 14026, 2026-11-14 19:14. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,780, prestige 3,600 (480 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 69 | 0 | 12 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 528 | 0 | 36 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.40 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.40 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 36 labour expired last turn (~62 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 529, not 628
- labour expiry guard: 36 bought labour expired last turn, buy 29 (not 29) this turn

## Prestige spending, cheapest coin per prestige first

375 turns left: prestige gained now converts 84.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.1 | 55.1 |  |
| jousting 3 | arena | 230 | 54.8 | 55.2 | needs a arena (build cost 26,251); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 57.3 | 57.3 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 57.4 | 57.4 |  |
| jousting 2 | arena | 210 | 60.0 | 60.4 | needs a arena (build cost 26,251); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 61.3 | 61.3 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 61.7 | 61.7 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 62.2 | 62.2 |  |
| hold banquet 3 (pies) | mansion | 8 | 62.6 | 62.6 | thin at home: hop beer |
| hold mass 2 (premium) | cathedral | 360 | 60.4 | 63.6 | needs a cathedral (build cost 294,730); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 64.0 | 64.0 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 3 @ 23.0, pasties buy 7 @ 15.4, rope sell 1 @ 83.0; crew 0.1; est +23 a turn; stock: pasties 7 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.5 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- best towns now: Amsdermund +671, Hofkirchen +663, Chatgnan +491, Gotthafen +441, Disscester +317
- Amsdermund would trade: furniture buy 65 @ 14.4; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (98/turn) | timber 36 (7.98->12.25), nets 4 (16.6->35.53), firewood 28 (3.57->6.65), bread 157 (2.5->2.75) | cloth 6 (8.24->10.3), tools 8 (5.78->6.98), cured meat 3 (23.73->24.4), garments 2 (22.47->23.4) | +311 |
| Nürnnieder | 520 | 0.15 | 0.20 (22/turn) | looms 1 (588->741), nets 3 (16.6->37.43), thread 70 (4.62->5.22), cheese 4 (7.4->13.3) | cloth 6 (9.08->10.3), furniture 1 (14.28->17.1), flax plants 4 (0.81->1.32), flax fibres 3 (6.14->6.6) | +293 |
| Brunnham | 1281 | 0.52 | 0.30 (33/turn) | nets 6 (16.6->39.14), looms 1 (588->665), garments 10 (23.2->27.17), wax 11 (22.68->24.32) | cloth 12 (7.72->10.3), candles 1 (80.85->88.5), tools 16 (6.35->6.98) | +289 |
| Blanans | 297 | 0.09 | 0.70 (77/turn) | timber 43 (7.98->11.88), cheese 14 (7.4->11.78), nets 3 (16.6->34.39), jewellery 5 (96.6->99.75) | cloth 13 (7.93->10.3), tools 16 (6.09->6.98), dyed cloth 6 (11.55->12.25), garments 2 (22.68->23.4) | +287 |
| Hofkirchen | 991 | 0.34 | 0.30 (33/turn) | nets 6 (16.6->37.43), wax 10 (22.68->24.7), lead bars 8 (15.44->16.62), acid 1 (115.5->120.65) | cloth 24 (7.35->10.3), tools 16 (6.04->6.98), cookware 7 (23.1->24.13), dyed cloth 7 (11.13->12.25) | +243 |

**Best:** Grandgues at about +311 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 12 @ 3.64, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 69 = 5.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 90.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 17.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 29) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| pasties |  | 1 @ min 12.3 | goal planner: sells 1 a turn at 12.3, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 10 @ min 69.5 | goal planner: sells 10 at 69.5 (v2 had 10 at 75.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 2.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.3k (cash + stock at home prices); -394/turn over 6 turns, -212/turn over 24 turns.
- Limits: cash flow >= -324/turn, prestige >= -0.75/turn (values are after 200 tax a turn).
- Today's settings: value -190/turn, cash -177/turn, prestige +1.60/turn.
- Plan: value -35/turn, cash +53/turn, prestige -0.75/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -197 vs -156, +309 vs -163, +108 vs -167.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +9/turn
  - ship Flax Wyrm -> Clairlond: +3/turn
  - mansion 1 1.00 -> 0.44: +142/turn
  - spinnery 1 1.65 -> 1.07: -4/turn
  - retting pit 1 0.91 -> 0.69: -8/turn
  - weavery 1 0.50 -> 0.61: -3/turn
  - sewing shop 1 0.30 -> 0.36: +11/turn
  - flax farm 1 4.64 -> 3.47: +10/turn
  - ropewalk 1 0.25 -> 0.00: -16/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.26: +19/turn
- Model check over the last 59 turns: predicted -49/turn for the settings we ran, real -48/turn.
- Worth of one more unit per turn: labour 1.65, thread 4.16, cloth 6.64, flax fibres 4.93, garments 19.21, nets 16.63, beer 3.10, timber 3.42, prestige 59.30, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 29); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.26, worth +7/turn.
- Ship linen snake: Grandgues -> Brunnham (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Clairlond (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~4691 coin: +36/turn, payback 131 turns, doesn't pay yet (materials thin at home: bricks, nails)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 426 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.54 |
| ret | 3 | 0.91 | 0.91 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 93/77, thread 1049/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.4; ask over the cap 2.1 (60 coin per prestige)
