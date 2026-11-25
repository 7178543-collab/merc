# v2 shadow report

Turn 14282, 2026-11-25 11:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,191, prestige 3,718 (598 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 3 | 0 | 12 | 0 | 0 | sell 15, sell @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 519 | 0 | 45 | buy 64, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~90 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.62 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 526, not 626
- labour expiry guard: 45 bought labour expired last turn, buy 20 (not 26) this turn

## Prestige spending, cheapest coin per prestige first

119 turns left: prestige gained now converts 45.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.7 | 51.7 | needs a arena (build cost 30,802); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.4 | 55.5 | needs a arena (build cost 30,802); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 59.4 | 59.4 | running |
| jousting 3 | arena | 230 | 59.0 | 60.8 | needs a arena (build cost 30,802); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 61.2 | 61.2 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 61.5 | 61.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 62.3 | 62.3 |  |
| hold banquet 4 (pies) | mansion | 18 | 63.8 | 63.8 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 65.3 | 65.3 | thin at home: hop beer, stockfish, sculptures |
| jousting 2 | arena | 210 | 64.6 | 66.6 | needs a arena (build cost 30,802); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 67.2 | 67.2 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 67.8 | 67.8 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 7 @ 14.9; crew 0.1; est +16 a turn; stock: pasties 7 @ 14.9 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- best towns now: Orlesailles +65, Heilegg +54, Großmühle +54, Friedwerp +50, Dortdorf +44
- Orlesailles would trade: cured meat buy 3 @ 24.8, pasties buy 11 @ 11.7; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~125 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Arnsreuth | 921 | 0.35 | 0.20 (25/turn) | leather 8 (29.82->32.49), dyed cloth 6 (20.48->23.37), glass ingots 2 (70.88->74.58), spinning wheels 1 (346.5->353.4) | sculptures 1 (2478->2736), fleece 7 (9.4->12.06), cured meat 3 (23.73->28.4), cloth 4 (11.03->12) | +328 |
| Pontmont | 341 | 0.11 | 0.60 (75/turn) | timber 35 (9.03->15.58), cookware 8 (28.35->32.87), paper 14 (27.93->30.4), garments 10 (31.6->34.58) | fleece 7 (8.87->12.06), thread 19 (5.25->5.9), bricks 8 (5.25->8.03), tools 14 (5.78->6.03) | +305 |
| Angefont | 686 | 0.23 | 0.20 (25/turn) | garments 10 (31.6->32.87), casks 3 (6.51->7.6) | sculptures 1 (2478->2736), thread 49 (5.35->5.9), seeds 12 (1.78->2.58), chisels 1 (11.34->12.06) | +282 |
| Hofkirchen | 991 | 0.40 | 0.50 (63/turn) | glass ingots 3 (70.88->95.95), jewellery 3 (97.12->109.25), ploughs 5 (81.9->92.15), furniture 15 (16.48->18.71) | cloth 17 (9.35->12), varnish 7 (18.69->21.85), fleece 7 (10.19->12.06), wrought iron 3 (11.97->15.01) | +246 |
| Grandgues | 152 | 0.05 | 0.50 (63/turn) | charcoal 20 (2.54->6.74), flour 4 (20.27->29.64), beer 7 (3.94->7.08), bread 182 (2.75->3) | medicine 1 (143.85->157.7), fleece 5 (9.45->12.06), cured meat 3 (27.72->28.4), flax fibres 1 (6.51->6.65) | +240 |

**Best:** Arnsreuth at about +328 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.84 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.95 | goal planner: sells 2 a turn at 0.95, keeps 219 (no one offered it) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 20) |
| light armour | 1 @ 100, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.4k (cash + stock at home prices); -39/turn over 6 turns, -7/turn over 24 turns.
- Limits: cash flow >= -300/turn, prestige >= -1.24/turn (values are after 200 tax a turn).
- Today's settings: value -171/turn, cash -166/turn, prestige +1.21/turn.
- Plan: value +24/turn, cash +30/turn, prestige -1.24/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +118 vs -155, +129 vs -141, -10 vs -162.
- Route sales counted at most (what the ships really sold, a turn): beer 2.1, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bremcop: +12/turn
  - ship Flax Wyrm -> Donaunieder: +14/turn
  - mansion 1 1.00 -> 0.42: +174/turn
  - spinnery 1 1.65 -> 1.36: +5/turn
  - retting pit 1 0.91 -> 0.80: +3/turn
  - flax farm 1 4.64 -> 3.98: +8/turn
  - net maker 0.00 -> 0.28: -4/turn
  - sewing shop 1 0.30 -> 0.23: -9/turn
  - weavery 1 0.50 -> 0.36: +6/turn
- Model check over the last 59 turns: predicted -145/turn for the settings we ran, real -28/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 33.21, beer 3.27, timber 3.69, prestige 66.91, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 20); light armour buy 1 (v2 None); meat buy 0 (v2 None)
- Ship linen snake: Grandgues -> Bremcop (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 86/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 2.6 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 4.22 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 39 @ 4.3 (ask 4.22, cap 14.4))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
