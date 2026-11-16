# v2 shadow report

Turn 14066, 2026-11-16 11:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,038, prestige 3,644 (524 free, -3.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.02 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.02 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

335 turns left: prestige gained now converts 81.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.3 | 51.8 | needs a arena (build cost 27,981); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 52.5 | 52.5 | running |
| jousting 2 | arena | 210 | 56.2 | 56.7 | needs a arena (build cost 27,981); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.7 | 60.7 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 60.9 | 60.9 | thin at home: wine, pies |
| hold banquet 1 (meat) | mansion | 4.2 | 61.6 | 61.6 |  |
| hold banquet 3 (pies) | mansion | 8 | 62.9 | 62.9 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 63.2 | 63.2 | thin at home: hop beer, wine, stockfish, pies |
| hold banquet 2 (meat) | mansion | 6.8 | 63.4 | 63.4 | thin at home: wine |
| hold banquet 4 (premium) | mansion | 20 | 64.1 | 64.1 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 60.1 | 64.1 | needs a cathedral (build cost 312,885); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.6 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.0 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +70, Brunnham +67, Clairlond +49, Hanbrücken +17
- Hofkirchen would trade: candles buy 6 @ 78.0, pasties buy 2 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (99/turn) | timber 48 (7.72->12.44), firewood 34 (3.17->6.41), windows 1 (656.25->712.5), charcoal 19 (3.02->5.46) | swords 2 (231->258.4), spinning wheels 1 (208.95->220.4), tools 5 (4.62->6.03), cloth 4 (8.61->9.5) | +439 |
| Clairlond | 1288 | 0.52 | 0.30 (33/turn) | windows 1 (656.25->850.25), rope 1 (72.5->78.85), premium ham 1 (247.8->250.8), casks 3 (6.04->7.5) | swords 2 (231->258.4), garments 19 (24.99->26.6), silver bars 1 (302.4->321.1), cookware 4 (22.89->24.51) | +299 |
| Heilegg | 826 | 0.25 | 0.60 (66/turn) | windows 1 (656.25->703), charcoal 19 (3.02->6.03), nets 6 (35.8->37.62), flour 2 (17.85->23.56) | garments 19 (22.89->26.6), swords 2 (231->258.4), cloth 24 (7.82->9.5), cookware 7 (23.52->24.51) | +263 |
| Amsdermund | 1111 | 0.42 | 0.30 (33/turn) | windows 1 (656.25->760), premium ham 1 (247.8->266), cured fish 8 (26.88->28.12), malt 2 (7.3->9.12) | swords 2 (231->258.4), garments 19 (24.57->26.6), cloth 24 (7.98->9.5), tools 17 (4.83->6.03) | +259 |
| Hofkirchen | 991 | 0.35 | 0.30 (33/turn) | windows 1 (656.25->688.75), premium ham 1 (247.8->260.3), lead ore 2 (7.4->12.82), flour 2 (17.85->21.66) | garments 19 (21.63->26.6), swords 2 (231->258.4), cloth 24 (7.82->9.5), silver bars 1 (308.7->321.1) | +257 |

**Best:** Grandgues at about +439 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.2) |
| grain | 6 @ 3.7, stop 22 |  | goal planner: buys 6 a turn for today's rates, keeps up to 22 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34 | goal planner: sells 9 at 34 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 70.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.0k (cash + stock at home prices); -451/turn over 6 turns, -77/turn over 24 turns.
- Limits: cash flow >= -168/turn, prestige >= -0.93/turn (values are after 200 tax a turn).
- Today's settings: value +84/turn, cash +66/turn, prestige -3.33/turn - breaks the prestige floor.
- Plan: value -11/turn, cash -1/turn, prestige -0.93/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -160 vs +33, -282 vs +45, +331 vs +48.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanbrücken: +11/turn
  - ship Flax Wyrm -> Rotterburg: +0/turn
  - net maker 0.00 -> 0.29: +10/turn
  - ropewalk 1 0.25 -> 0.20: +6/turn
  - spinnery 1 1.65 -> 1.51: +4/turn
  - flax farm 1 4.64 -> 4.72: -1/turn
  - sewing shop 1 0.30 -> 0.38: -12/turn
  - weavery 1 0.50 -> 0.62: +17/turn
  - mansion 1 0.00 -> 0.57: -132/turn
- Model check over the last 59 turns: predicted -44/turn for the settings we ran, real -111/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.75, thread 4.40, cloth 7.02, flax fibres 5.21, garments 20.32, nets 31.79, beer 3.30, timber 3.31, prestige 61.37, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Hanbrücken (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Rotterburg (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.9/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 420 (+131 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.14 |
| ret | 3 | 0.91 | 0.83 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.29 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 122/78, thread 1050/228, cloth 73/129

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.4 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.46 (ask 3.4, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.02; ask over the cap 2.1 (60 coin per prestige)
