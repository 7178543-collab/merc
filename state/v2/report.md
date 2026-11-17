# v2 shadow report

Turn 14101, 2026-11-17 22:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,118, prestige 3,597 (477 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.98 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.98 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~33 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

300 turns left: prestige gained now converts 77.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.8 | 51.3 | needs a arena (build cost 27,990); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.9 | 54.9 | running |
| jousting 2 | arena | 210 | 55.7 | 56.2 | needs a arena (build cost 27,990); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 58.7 | 58.7 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 58.8 | 58.8 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 60.5 | 60.5 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 60.9 | 60.9 |  |
| hold banquet 2 (pies) | mansion | 7 | 61.1 | 61.1 |  |
| hold banquet 3 (pies) | mansion | 8 | 61.6 | 61.6 | thin at home: hop beer |
| hold banquet 1 (meat) | mansion | 4.2 | 62.2 | 62.2 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 62.5 | 62.5 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 63.3 | 63.3 | thin at home: hop beer, stockfish, premium cheese, premium ham |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.3 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +709, Cobholme +266, Fulkirch +255, Clairlond +240, Marmont +224
- Amsdermund would trade: furniture buy 65 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.70 (81/turn) | timber 25 (8.45->12.73), firewood 33 (3.13->6.27), charcoal 19 (2.56->4.37), cured fish 8 (24.57->25.27) | acid 1 (131.25->147.25), bricks 3 (7.56->10.83), candles 1 (84->89), tools 8 (5.46->5.94) | +217 |
| Kirchwerp | 1072 | 0.42 | 0.50 (58/turn) | light armour 5 (98.7->112.1), lead ore 8 (6.25->10.45), wine 9 (7.04->7.6), hides 2 (11.65->12.54) | flax fibres 28 (5.62->7.35), acid 1 (131.25->147.25), tools 20 (5.02->5.94), rope 5 (78.75->81.22) | +168 |
| Hofkirchen | 991 | 0.37 | 0.70 (81/turn) | lead ore 3 (6.25->11.78), lead bars 5 (13.12->14.54), wine 6 (7.04->8.12), nets 5 (34.2->35.15) | flax fibres 28 (5.62->7.35), dyed cloth 9 (12.6->15.86), acid 1 (133.35->147.25), rope 5 (78.75->81.22) | +150 |
| Pontmont | 341 | 0.11 | 1.00 (116/turn) | firewood 24 (3.13->8.41), timber 17 (8.45->12.73), garments 4 (29.4->33.82), premium garments 0 (120.75->138.7) | acid 0 (130.2->147.25), tools 9 (5.46->5.94), candles 0 (87.67->89), furniture 0 (16.38->18.1) | +144 |
| Amsdermund | 1111 | 0.44 | 0.30 (35/turn) | wine 9 (7.04->9.5), chisels 4 (12.92->17.1), paper 2 (28.77->30.21) | cloth 24 (7.98->10.9), nails 6 (6.2->8.22), rope 5 (78.75->81.22), acid 1 (139.65->147.25) | +140 |

**Best:** Grandgues at about +217 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.94, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 28.6) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 83.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.3k (cash + stock at home prices); +176/turn over 6 turns, +89/turn over 24 turns.
- Limits: cash flow >= -338/turn, prestige >= -0.74/turn (values are after 200 tax a turn).
- Today's settings: value +96/turn, cash +75/turn, prestige -2.60/turn - breaks the prestige floor.
- Plan: value +21/turn, cash +27/turn, prestige -0.74/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +230 vs +82, +104 vs +70, +376 vs +70.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +7/turn
  - ship Flax Wyrm -> Amsdermund: +0/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.28: +4/turn
  - spinnery 1 1.65 -> 1.39: +1/turn
  - retting pit 1 0.91 -> 0.82: +2/turn
  - flax farm 1 4.64 -> 4.14: +3/turn
  - sewing shop 1 0.30 -> 0.25: -24/turn
  - weavery 1 0.50 -> 0.40: -4/turn
  - mansion 1 0.00 -> 0.44: -74/turn
- Model check over the last 58 turns: predicted +127/turn for the settings we ran, real +43/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.70, beer 3.21, timber 3.49, prestige 60.41, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Brunnham (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Amsdermund (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 81/77, thread 1049/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.98; ask over the cap 2.1 (60 coin per prestige)
