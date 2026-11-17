# v2 shadow report

Turn 14093, 2026-11-17 14:29. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,532, prestige 3,618 (498 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 14 | 9 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 510 | 0 | 19 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.80 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.80 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 19 labour expired last turn (~34 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 521, not 621

## Prestige spending, cheapest coin per prestige first

308 turns left: prestige gained now converts 78.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.2 | 51.6 | needs a arena (build cost 29,311); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| jousting 2 | arena | 210 | 56.0 | 56.6 | needs a arena (build cost 29,311); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.9 | 58.9 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 59.9 | 59.9 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 60.5 | 60.5 | thin at home: pasties, hop beer, candles |
| hold banquet 4 (premium) | mansion | 20 | 61.1 | 61.1 | thin at home: hop beer, ham, stockfish, candles, premium ham |
| hold banquet 2 (fish) | mansion | 6.8 | 61.4 | 61.4 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 61.5 | 61.5 | thin at home: hop beer |
| hold banquet 1 (meat) | mansion | 4.2 | 61.7 | 61.7 |  |
| hold banquet 2 (pies) | mansion | 7 | 63.0 | 63.0 | thin at home: pasties, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 63.1 | 63.1 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 21 | 134102075 | 0.312 | - | furniture 18, pasties 1 | -283 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +662, Hofkirchen +457, Gotthafen +448, Vauxvais +394, Bordees +376
- Amsdermund would trade: furniture buy 61 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~112 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (101/turn) | firewood 37 (2.94->7.12), timber 26 (8.45->12.63), bread 160 (2.77->3.13), charcoal 19 (2.9->4.94) | tapestries 2 (792.75->798), bricks 3 (10.92->13.59), beer 4 (3.44->3.76), cloth 3 (10.13->10.5) | +294 |
| Hanbrücken | 531 | 0.16 | 0.70 (79/turn) | nets 6 (35.2->38.76), charcoal 15 (2.9->4.67), timber 19 (8.45->11.02), tiles 1 (2.9->5.46) | tapestries 1 (614.25->798), garments 2 (28.35->35.4), furniture 8 (15.96->17.48), ham 1 (111.3->117.8) | +244 |
| Amsdermund | 1111 | 0.43 | 0.50 (56/turn) | premium cheese 6 (29.4->34.77), slaked lime 2 (8.98->11.4), grain 2 (2.88->3.82) | cloth 24 (6.67->10.5), candles 7 (78.75->83.12), furniture 12 (14.18->17.48), garments 2 (26.25->35.4) | +206 |
| Fontaux | 411 | 0.12 | 0.50 (56/turn) | thread 62 (5->7.27), salt 11 (5.46->7.79), timber 22 (8.45->11.4), premium cheese 2 (29.4->32.11) | bricks 6 (9.03->13.59), ploughs 1 (75.08->77.42), tools 16 (5.83->5.98), flax plants 3 (1.37->1.77) | +202 |
| Angefont | 686 | 0.21 | 0.70 (79/turn) | premium cheese 11 (29.4->34.2), looms 1 (635.25->674.5), charcoal 19 (2.9->5.13), beer 67 (3.95->4.48) | flax fibres 25 (5.04->7.3), garments 2 (27.72->35.4), raw cloth 4 (7.51->9.03), tools 16 (5.51->5.98) | +183 |

**Best:** Grandgues at about +294 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 6 @ 3.94, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 14 = 3.3 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 31.8) |
| grain | 0 @ 3.7, stop 18 |  | goal planner: buys 0 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 21) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 1 = 1.9 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.3k (cash + stock at home prices); +193/turn over 6 turns, +104/turn over 24 turns.
- Limits: cash flow >= -272/turn, prestige >= -0.82/turn (values are after 200 tax a turn).
- Today's settings: value +102/turn, cash +82/turn, prestige -2.70/turn - breaks the prestige floor.
- Plan: value +25/turn, cash +31/turn, prestige -0.82/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +179 vs +95, -156 vs +84, -228 vs +87 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +11/turn
  - ship Flax Wyrm -> Nürnnieder: +4/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.28: +4/turn
  - spinnery 1 1.65 -> 1.57: +4/turn
  - flax farm 1 4.64 -> 4.71: -0/turn
  - weavery 1 0.50 -> 0.58: -7/turn
  - sewing shop 1 0.30 -> 0.36: +11/turn
  - mansion 1 0.00 -> 0.45: -103/turn
- Model check over the last 60 turns: predicted +96/turn for the settings we ran, real +15/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.77, thread 4.45, cloth 7.10, flax fibres 5.26, garments 20.55, nets 32.00, beer 3.16, timber 3.44, prestige 60.45, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 21); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Amsdermund (+14/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Nürnnieder (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 86/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.8; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
