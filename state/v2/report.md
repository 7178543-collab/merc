# v2 shadow report

Turn 14184, 2026-11-21 09:12. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,416, prestige 3,724 (604 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 59 | 0 | 14 | 0 | 0 | min_holding 58, sell 15, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 537 | 0 | 27 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), 4 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: home ask 2.62 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 27 labour expired last turn (~57 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 3.00 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.30 is above our ceiling 11.00 and last turn bought 1 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 569, not 669

## Prestige spending, cheapest coin per prestige first

217 turns left: prestige gained now converts 66.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.8 | 53.6 | needs a arena (build cost 29,840); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.9 | 58.7 | needs a arena (build cost 29,840); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 61.4 | 61.4 | thin at home: hop beer, stockfish, candles |
| hold banquet 4 (pies) | mansion | 18 | 61.8 | 61.8 | thin at home: hop beer, stockfish, cheese, candles |
| maintain 1 | park | 0.5 | 63.0 | 63.0 | running |
| hold mass 2 (premium) | cathedral | 360 | 54.1 | 63.1 | needs a cathedral (build cost 316,930); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 66.5 | 66.5 | thin at home: hop beer, cheese, candles |
| hold banquet 4 | mansion | 17.5 | 67.1 | 67.1 | thin at home: hop beer, stockfish, cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 68.2 | 68.2 | thin at home: cheese, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 70.3 | 70.3 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 72.9 | 72.9 | running |
| jousting 1 | arena | 170 | 75.1 | 76.1 | needs a arena (build cost 29,840); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 12 | 134102075 | 0 | - | cured meat 2, pasties 11 | -230 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 12 @ 14.6, pasties buy 3 @ 16.0; crew 0.1; est +137 a turn; stock: furniture 12 @ 14.6 (keep 145); stock: pasties 3 @ 16.0 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -0 a turn after crew: ship stays at 0
- best towns now: Blanans +175, Caillechâtel +137, Donaunieder +130, Boistot +124, Disscester +120
- Blanans would trade: cured meat buy 4 @ 27.0, furniture buy 12 @ 12.7, grain buy 8 @ 2.58, pasties buy 3 @ 16.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~133 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (120/turn) | bread 258 (3.15->4.14), firewood 35 (2.75->6.84), charcoal 19 (2.79->6.46), thread 78 (6.7->7.03) | cured meat 4 (26.46->28.8), cloth 3 (11.34->12.4) | +412 |
| Kirchwerp | 1072 | 0.48 | 0.60 (80/turn) | garments 10 (31.6->37.62), thread 38 (6.7->8.41), honey 4 (8.82->13.21), furniture 8 (16.48->19.95) | cloth 24 (10.5->12.4), cookware 7 (21->22.99), chisels 4 (8.4->9.79) | +212 |
| Amsdermund | 1111 | 0.51 | 0.40 (53/turn) | - | cloth 24 (7.35->12.4), cured meat 4 (21->28.8), cheese 6 (9.03->13.01), cookware 7 (21.21->22.99) | +182 |
| Angefont | 686 | 0.24 | 0.20 (27/turn) | thread 57 (6.7->8.22), garments 10 (31.6->38), swords 1 (245.7->252.7), lathes 1 (180.6->183.35) | cloth 24 (11.87->12.4), seeds 18 (1.78->2.58) | +155 |
| Rouhomme | 368 | 0.13 | 0.10 (13/turn) | thread 34 (6.7->7.41), lathes 1 (180.6->199.5), nets 2 (45.8->49.4), grain 2 (3.4->4.43) | cloth 23 (10.82->12.4), cheese 6 (7.56->13.01), wrought iron 2 (15.65->17), wool 2 (11.65->12.25) | +115 |

**Best:** Grandgues at about +412 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 15 @ min 3.88 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 6 = 1.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.8) |
| grain | 11 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 33 = 3.7 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 69) |
| light armour | 1 @ 111, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 44.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 1 = 2.3 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.9k (cash + stock at home prices); +163/turn over 6 turns, +100/turn over 24 turns.
- Limits: cash flow >= -309/turn, prestige >= -1.27/turn (values are after 200 tax a turn).
- Today's settings: value -160/turn, cash -183/turn, prestige +0.88/turn.
- Plan: value +54/turn, cash +58/turn, prestige -1.27/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +86 vs -188, +156 vs -198, -212 vs -179.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +27/turn
  - ship Flax Wyrm -> Blanans: +7/turn
  - mansion 1 1.00 -> 0.49: +150/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +14/turn
  - spinnery 1 1.65 -> 1.18: +24/turn
  - retting pit 1 0.91 -> 0.75: +2/turn
  - flax farm 1 4.64 -> 3.79: +3/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.06: +1/turn
  - weavery 1 0.50 -> 0.44: -13/turn
- Model check over the last 59 turns: predicted -130/turn for the settings we ran, real -0/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.63, beer 3.49, timber 3.76, prestige 65.98, cash 0.00
- Orders it would set: arms buy 1 (v2 None); bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); fish buy 0 (v2 None); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 69); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.21, worth +15/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.06, worth +1/turn.
- Ship linen snake: Grandgues -> Amsdermund (+13/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+7/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +89/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 416 (+127 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.97 |
| ret | 3 | 0.91 | 0.79 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 134/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
