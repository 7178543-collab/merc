# v2 shadow report

Turn 14180, 2026-11-21 05:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,336, prestige 3,732 (612 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 66 | 0 | 12 | 0 | 0 | min_holding 58, sell 15, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 6 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 13 | 9 | 0 | 0 | stop 36, buy 11, buy @ 3.7 |
| labour | 64 | 64 | 519 | 0 | 45 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: home ask 2.64 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~92 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.72 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 519, not 619

## Prestige spending, cheapest coin per prestige first

221 turns left: prestige gained now converts 67.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.7 | 51.1 | needs a arena (build cost 29,062); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.4 | 53.1 | needs a arena (build cost 29,062); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.6 | 55.0 | needs a arena (build cost 29,062); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.4 | 58.2 | needs a arena (build cost 29,062); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 59.3 | 59.3 | thin at home: hop beer, ham, stockfish, cheese, pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 60.7 | 60.7 | thin at home: hop beer, ham, stockfish, candles |
| maintain 1 | park | 0.5 | 61.2 | 61.2 | running |
| hold banquet 3 (pies) | mansion | 8 | 61.7 | 61.7 | thin at home: hop beer, cheese, pies, candles |
| hold mass 2 (premium) | cathedral | 360 | 54.4 | 63.0 | needs a cathedral (build cost 314,640); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 2 (pies) | mansion | 7 | 63.6 | 63.6 | thin at home: cheese, pies, candles |
| hold banquet 4 | mansion | 17.5 | 64.2 | 64.2 | thin at home: hop beer, ham, stockfish, cheese, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 70.6 | 70.6 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: cured meat buy 3 @ 27.0, pasties buy 12 @ 15.6; crew 0.1; est +32 a turn; stock: pasties 12 @ 15.6 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 8 a turn after crew: ship stays at 0
- best towns now: Blanans +232, Vauxvais +187, Angefont +177, Heidlowe +172, Bordees +166
- Blanans would trade: cured meat buy 3 @ 26.0, furniture buy 14 @ 12.7, grain buy 8 @ 2.68, pasties buy 13 @ 16.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~129 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.60 (77/turn) | charcoal 19 (2.77->6.17), firewood 34 (2.77->5.79), thread 92 (6.55->7.03), wine 8 (7.77->9.5) | cured meat 3 (25.2->28.8), wrought iron 4 (16.8->18.24), cloth 5 (11.13->12) | +185 |
| Amsdermund | 1111 | 0.49 | 0.30 (39/turn) | jewellery 3 (98.17->123.5), ploughs 1 (82.42->91.2), casks 6 (6.72->7.84) | cloth 24 (10.92->12), cured meat 3 (24.57->28.8), garments 2 (28.35->31), nails 6 (5.51->6.7) | +117 |
| Unterhufe | 595 | 0.20 | 0.30 (39/turn) | premium ham 1 (243.6->269.8), limestone 2 (19.43->30.4) | thread 49 (6.35->6.95), cloth 24 (11.13->12), wrought iron 4 (14.38->18.24), beer 11 (3.51->4.34) | +96 |
| Hofkirchen | 991 | 0.41 | 0.30 (39/turn) | paper 6 (27.3->30.02), flax fibres 7 (7.2->9.88), tar 2 (11.87->13.59), flax plants 1 (1.44->2.83) | cloth 24 (10.5->12), wrought iron 4 (14.38->18.24), cheese 7 (10.13->11.4), yarn 18 (5.35->6.08) | +90 |
| Pontmont | 341 | 0.12 | 0.60 (77/turn) | cookware 10 (22.89->26.03), timber 26 (8.82->11.3), charcoal 19 (2.77->3.99), lead ore 1 (7.88->11.02) | cheese 7 (7.88->11.4), wrought iron 4 (16.48->18.24), tools 15 (5.78->6.08), wax 1 (22.05->23.75) | +87 |

**Best:** Grandgues at about +185 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.88 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 28.0) |
| grain | 10 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 35 = 3.9 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 19) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 43.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.0k (cash + stock at home prices); +94/turn over 6 turns, -121/turn over 24 turns.
- Limits: cash flow >= -306/turn, prestige >= -1.30/turn (values are after 200 tax a turn).
- Today's settings: value -172/turn, cash -194/turn, prestige +1.14/turn.
- Plan: value +48/turn, cash +49/turn, prestige -1.30/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -65 vs -185, +114 vs -187, +86 vs -188.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Blanans: -5/turn
  - ship Flax Wyrm -> Donaunieder: +13/turn
  - mansion 1 1.00 -> 0.42: +164/turn
  - ropewalk 1 0.25 -> 0.07: +8/turn
  - spinnery 1 1.65 -> 1.21: +27/turn
  - net maker 0.00 -> 0.29: +3/turn
  - retting pit 1 0.91 -> 0.77: +3/turn
  - flax farm 1 4.64 -> 3.86: +8/turn
  - brewery 1 [brew mead 1] 0.00 -> 0.19: -37/turn
  - brewery 1 0.14 -> 0.00: +38/turn
- Model check over the last 59 turns: predicted -116/turn for the settings we ran, real +7/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.61, beer 3.56, timber 3.69, prestige 64.36, cash 0.00
- Orders it would set: bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 19); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.19, worth +12/turn.
- Ship linen snake: Grandgues -> Blanans (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+5/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 418 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.07 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 127/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 0.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.72 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 2.78 (ask 2.72, cap 4.3))
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
