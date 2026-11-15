# v2 shadow report

Turn 14042, 2026-11-15 11:24. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,951, prestige 3,586 (466 free, -3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 15 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 9, buy 3, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 24.6 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 31, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 484 | 0 | 80 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 35.2 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (15.0/turn) but there is NO buy order, stock 0.0 -> v2: add buy 30
- **firewood**: brewery 1 ran short of firewood (buy is live (3 @ 2.4), but the home ask 2.74 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.74 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 80 labour expired last turn (~133 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

359 turns left: prestige gained now converts 83.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| jousting 3 | arena | 230 | 55.1 | 55.5 | needs a arena (build cost 25,614); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.3 | 56.3 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 57.2 | 57.2 | thin at home: pasties, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 59.2 | 59.2 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 59.3 | 59.3 | thin at home: hop beer, stockfish, candles |
| hold banquet 3 (pies) | mansion | 8 | 60.5 | 60.5 | thin at home: pasties, hop beer, candles |
| jousting 2 | arena | 210 | 60.4 | 60.8 | needs a arena (build cost 25,614); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 58.3 | 61.4 | needs a cathedral (build cost 269,470); thin at home: jewellery, glassware, candles, premium garments |
| hold banquet 4 (premium) | mansion | 20 | 61.9 | 61.9 | thin at home: hop beer, stockfish, candles |
| hold banquet 4 | mansion | 17.5 | 63.1 | 63.1 | thin at home: hop beer, stockfish, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 63.8 | 63.8 | thin at home: hop beer, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 14.2, pasties buy 4 @ 14.9; crew 0.2; est +251 a turn; stock: furniture 21 @ 14.2 (keep 145); stock: pasties 4 @ 14.9 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Friedwerp +399, Bordees +354, Brebronn +316, Essenbrucke +296, Toqueque +292
- Friedwerp would trade: furniture buy 30 @ 13.3, pasties buy 9 @ 14.7; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | timber 45 (7.88->12.35), firewood 31 (2.88->5.7), bread 161 (2.35->2.62), charcoal 19 (2.86->4.2) | tools 8 (4.66->5.7), cloth 6 (8.72->9.65), garments 2 (24.36->27), cheese 5 (6.35->6.6) | +334 |
| Vauxvais | 204 | 0.06 | 0.50 (53/turn) | bread 161 (2.35->2.75), charcoal 19 (2.86->4.75), medicine 1 (138.6->152.95), beer 64 (3.46->3.7) | thread 10 (4.35->5.6), flax fibres 7 (5.35->6.65), garments 2 (23.52->27), logs 1 (4.39->7.22) | +141 |
| Fontaux | 411 | 0.12 | 1.00 (106/turn) | charcoal 13 (2.86->5.84), timber 12 (7.88->11.78), firewood 17 (2.88->7.27), garments 7 (26.6->28.88) | thread 35 (5.04->5.6), flax fibres 6 (5.35->6.65) | +124 |
| Kirchwerp | 1072 | 0.38 | 0.40 (43/turn) | premium ham 2 (268.8->275.5), nets 6 (36.2->37.62), resin 6 (2.48->3.93), arms 1 (29.4->33.25) | cloth 24 (7.56->9.65), ploughs 5 (73.5->81.22), garments 2 (22.68->27), salt 6 (3.89->5.56) | +107 |
| Hanbrücken | 531 | 0.15 | 0.60 (64/turn) | timber 20 (7.88->12.06), ham 2 (99.23->108.3), bricks 4 (5.3->10.16), flax fibres 3 (5.95->6.98) | bellows 1 (237.3->252.7), salt 6 (4.45->5.56), thread 6 (4.79->5.6), garments 2 (25.41->27) | +99 |

**Best:** Grandgues at about +334 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 30 @ 3.46, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 79, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 24.6 | goal planner: sells 11 at 24.6 (v2 had 10 at 27.0) |
| grain | 8 @ 3.7, stop 31 |  | goal planner: buys 8 a turn for today's rates, keeps up to 31 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 35.2 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.3k (cash + stock at home prices); -125/turn over 6 turns, -178/turn over 24 turns.
- Limits: cash flow >= -248/turn, prestige >= -0.69/turn (values are after 200 tax a turn).
- Today's settings: value +142/turn, cash +127/turn, prestige -3.04/turn - breaks the prestige floor.
- Plan: value +50/turn, cash +79/turn, prestige -0.69/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -151 vs -174, -175 vs -170, -93 vs -193.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brebronn: +1/turn
  - ship Flax Wyrm -> Karlmoor: +0/turn
  - net maker 0.00 -> 0.29: +12/turn
  - spinnery 1 1.65 -> 1.47: +3/turn
  - sewing shop 1 0.30 -> 0.36: +1/turn
  - weavery 1 0.50 -> 0.61: +11/turn
  - ropewalk 1 0.25 -> 0.00: -1/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.20: +12/turn
  - mansion 1 0.00 -> 0.56: -133/turn
- Model check over the last 59 turns: predicted -126/turn for the settings we ran, real -84/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.21, cloth 6.70, flax fibres 5.06, garments 19.35, nets 30.21, beer 2.96, timber 3.38, prestige 62.84, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.20, worth +9/turn.
- Ship linen snake: Grandgues -> Brebronn (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Karlmoor (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3594 coin: +4/turn, payback 908 turns, doesn't pay yet (materials thin at home: nails)
  - +1 plot park 1 for ~1686 coin: +1/turn, payback 3257 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 422 (+133 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.32 |
| ret | 3 | 0.91 | 0.86 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 109/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.36 (ask 3.3, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.74; ask over the cap 2.1 (60 coin per prestige)
- R1: prestige rate -3.04 a turn vs 12-turn median -0.50; likely: dry slot: beer, firewood
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
