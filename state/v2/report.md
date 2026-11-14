# v2 shadow report

Turn 14024, 2026-11-14 17:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,362, prestige 3,601 (481 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 20 | 12 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 24, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 528 | 0 | 36 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.60 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.60 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 36 labour expired last turn (~61 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 529, not 628
- labour expiry guard: 36 bought labour expired last turn, buy 29 (not 29) this turn

## Prestige spending, cheapest coin per prestige first

377 turns left: prestige gained now converts 85.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| jousting 3 | arena | 230 | 55.2 | 55.5 | needs a arena (build cost 26,156); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.1 | 58.1 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 58.5 | 58.5 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 59.6 | 59.6 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 59.7 | 59.7 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 60.0 | 60.0 | thin at home: wine, cured fish |
| jousting 2 | arena | 210 | 60.4 | 60.8 | needs a arena (build cost 26,156); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 62.3 | 62.3 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 62.3 | 62.3 | thin at home: hop beer, cured fish |
| hold banquet 4 (premium) | mansion | 20 | 62.4 | 62.4 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 62.9 | 62.9 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 13.8 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 16.0 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Amsdermund +718, Chatgnan +470, Gotthafen +469, Cobholme +325, Clairlond +311
- Amsdermund would trade: furniture buy 65 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.12 | 0.60 (64/turn) | thread 78 (4.66->7.27), timber 17 (7.98->10.73), salt 4 (5.51->7.79), flax fibres 1 (5.55->7.55) | glassware 1 (102.38->108.3), cloth 4 (8.4->9.25), cured meat 3 (24.36->25.6), ploughs 3 (81.38->83.12) | +240 |
| Grandgues | 152 | 0.04 | 0.80 (86/turn) | timber 43 (7.98->12.16), firewood 29 (3.91->6.6), charcoal 20 (2.69->3.4), looms 1 (588->593.75) | cloth 6 (8.45->9.25), cured meat 3 (24.15->25.6), tools 21 (6.51->6.7), beer 11 (3.51->3.7) | +219 |
| Darmwald | 1022 | 0.36 | 0.80 (86/turn) | medicine 1 (138.6->189.05), charcoal 20 (2.69->7.79), garments 10 (22->26.41), wool 2 (10.71->13.77) | cloth 24 (7.35->9.25), cheese 6 (6.3->6.84), cured meat 3 (24.57->25.6) | +185 |
| Hofkirchen | 991 | 0.34 | 0.40 (43/turn) | thread 43 (4.66->5.22), leather 1 (25.2->28.69), acid 1 (115.5->116.85), nets 6 (36.6->37.43) | jewellery 6 (84->96.9), cloth 24 (7.35->9.25), cheese 16 (5.25->6.84), ploughs 3 (73.5->83.12) | +185 |
| Blanans | 297 | 0.09 | 0.60 (64/turn) | timber 43 (7.98->12.44), limestone 1 (18.27->24.89), casks 5 (7.19->7.69), raw cloth 1 (6.46->7.12) | cloth 13 (7.88->9.25), dyed cloth 5 (10.71->12.73), garments 2 (22.68->22.8) | +167 |

**Best:** Fontaux at about +240 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 | off | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 29) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 35.6) |
| pasties |  | 1 @ min 12.3 | goal planner: sells 1 a turn at 12.3, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 82.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.3k (cash + stock at home prices); -547/turn over 6 turns, -225/turn over 24 turns.
- Limits: cash flow >= -307/turn, prestige >= -0.75/turn (values are after 200 tax a turn).
- Today's settings: value -180/turn, cash -163/turn, prestige +1.59/turn.
- Plan: value -23/turn, cash -10/turn, prestige -0.75/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -280 vs -164, -30 vs -164, -197 vs -156.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +2/turn
  - ship Flax Wyrm -> Friedwerp: +1/turn
  - mansion 1 1.00 -> 0.44: +143/turn
  - net maker 0.00 -> 0.29: +6/turn
  - flax farm 1 4.64 -> 4.17: -0/turn
  - spinnery 1 1.65 -> 1.33: -1/turn
  - retting pit 1 0.91 -> 0.83: +6/turn
  - weavery 1 0.50 -> 0.38: -10/turn
  - sewing shop 1 0.30 -> 0.23: +10/turn
- Model check over the last 59 turns: predicted -39/turn for the settings we ran, real -41/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.33, beer 3.12, timber 3.42, prestige 59.86, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 2 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 29); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Etallaen (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Friedwerp (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 424 (+136 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.46 |
| ret | 3 | 0.91 | 0.89 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 99/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.6; ask over the cap 2.1 (60 coin per prestige)
- R1: prestige rate -0.51 a turn vs 12-turn median +1.98; likely: dry slot: firewood
