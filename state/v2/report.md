# v2 shadow report

Turn 14205, 2026-11-22 06:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,420, prestige 3,704 (584 free, -3.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 120 | 0 | 4 | 0 | 0 | min_holding 58, sell 3, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 24 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 510 | 0 | 54 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), but the home ask 33.20 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: home ask 2.54 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 54 labour expired last turn (~106 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 33.20 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 62.2 coin per prestige at mansion, vs 76.7 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 100 over real use lately; planning 529, not 629
- labour expiry guard: 54 bought labour expired last turn, buy 10 (not 29) this turn

## Prestige spending, cheapest coin per prestige first

196 turns left: prestige gained now converts 62.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.0 | 51.9 | needs a arena (build cost 28,232); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 55.9 | 56.8 | needs a arena (build cost 28,232); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 58.5 | 58.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 62.2 | 62.2 |  |
| hold banquet 5 | mansion | 22 | 62.5 | 62.5 | thin at home: hop beer, wine, stockfish, sculptures |
| hold banquet 4 (pies) | mansion | 18 | 62.7 | 62.7 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 64.5 | 64.5 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold mass 2 (premium) | cathedral | 360 | 53.6 | 64.5 | needs a cathedral (build cost 301,820); thin at home: furniture, jewellery, glassware, premium garments |
| hold banquet 2 (pies) | mansion | 7 | 65.4 | 65.4 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 66.5 | 66.5 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 67.7 | 67.7 | thin at home: wine, hop beer, stockfish |
| hold mass 3 | cathedral | 460 | 59.3 | 67.8 | needs a cathedral (build cost 301,820); thin at home: coats, jewellery, glassware, candles, windows, sculptures, furniture, tapestries, books |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 20 @ 5.1, pasties buy 8 @ 16.1; crew 0.1; est +33 a turn; stock: pasties 8 @ 16.1 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.4 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Heilegg +76, Bordetes +41, Heidlowe +37, Clairas +36, Pontmont +35
- Heilegg would trade: beer sell 20 @ 6.75, pasties buy 8 @ 14.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~124 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (124/turn) | bread 267 (2.86->4.2), firewood 29 (2.25->11.4), beer 18 (3.62->5.18), furniture 9 (14.38->17.39) | cloth 4 (8.87->11.9), garments 1 (28.35->30.8), bricks 6 (7.4->8.64), raw cloth 0 (10.08->10.64) | +670 |
| Rouhomme | 368 | 0.12 | 1.00 (124/turn) | bread 294 (2.86->4.75), flour 2 (22.89->26.22), resin 3 (2.33->2.93), flax fibres 5 (7.25->7.55) | tools 16 (4.73->6.13), bricks 16 (5.51->8.64), cookware 7 (24.15->24.32) | +487 |
| Amsdermund | 1111 | 0.47 | 0.40 (50/turn) | windows 2 (840->883.5), flour 2 (22.89->29.64), varnish 1 (19.74->25.08), hides 2 (13.23->16.25) | cloth 24 (9.55->11.9), wool 11 (8.72->11.59), garments 2 (25.2->30.8), tools 16 (5.04->6.13) | +205 |
| Kirchwerp | 1072 | 0.45 | 0.40 (50/turn) | glassware 5 (77.17->89.77), butter 2 (76.12->94.05), nets 6 (39.4->44.08), hides 2 (13.23->15.48) | cloth 24 (10.5->11.9), tools 16 (4.62->6.13), garments 2 (24.15->30.8), nails 6 (5.46->6.51) | +188 |
| Heilegg | 826 | 0.28 | 0.40 (50/turn) | beer 20 (3.62->6.84), nets 6 (39.4->44.08), malt 3 (8.29->15.58), flour 2 (22.89->29.26) | cloth 24 (10.5->11.9), tools 16 (5.04->6.13), garments 2 (26.46->30.8), hop beer 3 (9.5->11.69) | +174 |

**Best:** Grandgues at about +670 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 19 @ min 3.52 | makes 19.3, uses 4.2, holds 120 (keeps 58): sells the surplus + 4/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 80.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 2 @ 14, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.6) |
| grain | 8 @ 3.7, stop 29 |  | goal planner: buys 8 a turn for today's rates, keeps up to 29 (v2 had 15) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 10) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 38.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.6k (cash + stock at home prices); -5/turn over 6 turns, +106/turn over 24 turns.
- Limits: cash flow >= -393/turn, prestige >= -1.18/turn (values are after 200 tax a turn).
- Today's settings: value -176/turn, cash -151/turn, prestige +0.96/turn.
- Plan: value +9/turn, cash +30/turn, prestige -1.18/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -89 vs -177, +159 vs -178, +121 vs -170.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Clairas: +5/turn
  - ship Flax Wyrm -> Blanans: +0/turn
  - mansion 1 1.00 -> 0.49: +163/turn
  - spinnery 1 1.65 -> 1.34: +10/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - flax farm 1 4.64 -> 4.24: +4/turn
  - net maker 0.00 -> 0.29: -4/turn
  - sewing shop 1 0.30 -> 0.23: -9/turn
  - weavery 1 0.50 -> 0.38: +19/turn
- Model check over the last 59 turns: predicted -133/turn for the settings we ran, real +34/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.84, beer 3.46, timber 3.69, prestige 74.85, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 15); labour buy 64 (v2 10); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Clairas (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1985 coin: +4/turn, payback 462 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.39 |
| ret | 3 | 0.91 | 0.88 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 104/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 33.2 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 33.8 (ask 33.2, cap 42.0))
- R1: prestige rate -3.24 a turn vs 12-turn median +0.51; likely: dry slot: cured meat; mansion 1 projected 0 (cured meat)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
