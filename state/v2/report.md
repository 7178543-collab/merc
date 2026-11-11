# v2 shadow report

Turn 13944, 2026-11-11 09:05. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,399, prestige 3,488 (368 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.18 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.18 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.70 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~79 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.70 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.13, no projection from the game)
- labour: projection runs 100 over real use lately; planning 490, not 590

## Prestige spending, cheapest coin per prestige first

457 turns left: prestige gained now converts 89.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.5 | 52.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 56.0 | 56.0 | thin at home: beer |
| jousting 3 | arena | 230 | 56.0 | 56.3 | needs a arena (build cost 28,488); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.1 | 58.1 | thin at home: wine, ham, stockfish, cheese, pies |
| hold banquet 4 (premium) | mansion | 20 | 60.1 | 60.1 | thin at home: wine, ham, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 61.1 | 61.1 | thin at home: wine, ham, stockfish, cheese |
| jousting 2 | arena | 210 | 61.3 | 61.7 | needs a arena (build cost 28,488); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 61.8 | 61.8 | thin at home: beer |
| hold banquet 3 (fish) | mansion | 7.6 | 65.3 | 65.3 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 65.6 | 65.6 | thin at home: cheese, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 66.5 | 66.5 | thin at home: wine, cheese |
| jousting 1 | arena | 170 | 67.2 | 67.6 | needs a arena (build cost 28,488); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 18 @ 12.8, pasties buy 9 @ 15.5; crew 0.2; est +254 a turn; stock: furniture 18 @ 12.8 (keep 145); stock: pasties 9 @ 15.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Marmont +318, Vauxvais +297, Brebronn +290, Dortgart +270, Briclives +266
- Marmont would trade: furniture buy 25 @ 13.1, pasties buy 2 @ 15.1; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (55/turn) | bread 154 (2.46->3.63), cured fish 7 (24.57->30.4), charcoal 19 (2.77->4.1), timber 27 (7.77->8.74) | cheese 9 (8.98->11.4), tiles 5 (3.89->5.98), cloth 11 (7.61->8.25), honey 1 (8.82->10.73) | +267 |
| Fontaux | 411 | 0.12 | 1.00 (109/turn) | thread 91 (4.92->7.27), flax fibres 5 (6.15->7.6), bricks 4 (7.04->10.54), flax plants 1 (1.37->2.83) | cheese 8 (11.13->11.4), tallow 1 (22.26->23.37), honey 1 (10.13->10.73), pasties 1 (16.38->16.81) | +211 |
| Etallaen | 774 | 0.23 | 0.50 (55/turn) | garments 10 (22.6->29.26), spinning wheels 2 (237.3->254.6), nets 5 (37.8->40.85), charcoal 19 (2.77->5.08) | cheese 9 (7.09->11.4), cookware 3 (20.37->24.13), fleece 2 (6.25->6.79), honey 1 (10.19->10.73) | +183 |
| Vauxvais | 204 | 0.06 | 0.30 (33/turn) | bread 143 (2.46->3.61), flax fibres 5 (6.15->6.27) | tiles 4 (3.82->5.98), honey 1 (8.66->10.73), seeds 11 (2.14->2.32), dyed cloth 3 (10.71->10.83) | +146 |
| Darmwald | 1022 | 0.36 | 0.50 (55/turn) | beer 64 (3.91->5.89), garments 10 (22.6->24.89) | cheese 7 (7.82->11.4), axes 1 (15.44->17.76), honey 1 (8.98->10.73), tar 3 (10.5->11.4) | +126 |

**Best:** Grandgues at about +267 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 89, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 10 @ min 19.3 | goal planner: sells 10 at 19.3 (v2 had 10 at 22.8) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 99.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.7k (cash + stock at home prices); -92/turn over 6 turns, +14/turn over 24 turns.
- Limits: cash flow >= -142/turn, prestige >= -0.28/turn (values are after 200 tax a turn).
- Today's settings: value +20/turn, cash +14/turn, prestige -2.55/turn - breaks the prestige floor.
- Plan: value -50/turn, cash +15/turn, prestige -0.28/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +589 vs -70, +45 vs -70, -60 vs -6.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gottweiler: +4/turn
  - brewery 1 0.14 -> 0.09: +11/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: +8/turn
  - spinnery 1 1.65 -> 1.34: +8/turn
  - retting pit 1 0.91 -> 0.77: -4/turn
  - flax farm 1 4.64 -> 3.87: -9/turn
  - mansion 1 0.00 -> 0.54: -102/turn
- Model check over the last 60 turns: predicted +105/turn for the settings we ran, real +114/turn.
- Worth of one more unit per turn: labour 1.57, thread 3.96, cloth 6.32, flax fibres 4.70, garments 18.29, nets 28.70, beer 2.91, timber 3.31, prestige 59.22, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); grain buy 6 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +4/turn.
- Ship linen snake: Grandgues -> Gottweiler (+5/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +3/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +68/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.5/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 415 (+126 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.20 |
| ret | 3 | 0.91 | 0.84 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 111/77, thread 1064/225, cloth 73/126

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.8 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.86 (ask 3.8, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.18; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
