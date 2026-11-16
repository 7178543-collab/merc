# v2 shadow report

Turn 14056, 2026-11-16 01:14. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,289, prestige 3,551 (431 free, -2.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 13 | 9 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 1 | 1 | 1 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 36 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), 1 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: only 0.5 turns of firewood left and buying 1 (need 5) -> v2: buy 5
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~76 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 506, not 606
- labour expiry guard: 45 bought labour expired last turn, buy 0 (not 6) this turn

## Prestige spending, cheapest coin per prestige first

345 turns left: prestige gained now converts 82.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.4 | 55.4 | thin at home: beer, cured fish |
| jousting 3 | arena | 230 | 56.9 | 57.2 | needs a arena (build cost 26,188); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 59.3 | 59.3 | thin at home: hop beer |
| hold banquet 1 (meat) | mansion | 4.2 | 59.6 | 59.6 | thin at home: beer |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.5 | 60.5 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 61.1 | 61.1 |  |
| hold banquet 4 (pies) | mansion | 18 | 61.6 | 61.6 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 62.2 | 62.2 | thin at home: hop beer, ham, stockfish |
| jousting 2 | arena | 210 | 62.3 | 62.7 | needs a arena (build cost 26,188); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 62.8 | 62.8 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0.388 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.168 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 22 @ 14.0, pasties buy 2 @ 14.3; crew 0.2; est +261 a turn; stock: furniture 22 @ 14.0 (keep 145); stock: pasties 2 @ 14.3 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Chatgnan +642, Amsdermund +566, Disscester +384, Fulkirch +300, Boistot +295
- Chatgnan would trade: furniture buy 54 @ 13.9, garments sell 6 @ 26.2, pasties buy 4 @ 16.3; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | timber 46 (7.82->12.63), firewood 35 (2.35->5.98), charcoal 19 (3.07->5.32), bread 162 (2.37->2.6) | swords 1 (231->340.1), candles 1 (77.17->83.5), cheese 5 (6.72->7.36), cloth 4 (8.72->9.1) | +474 |
| Heilegg | 826 | 0.24 | 1.00 (106/turn) | beer 122 (3.15->4.41), charcoal 17 (3.07->6.03), nets 5 (34.6->37.62), wine 10 (7.04->7.84) | swords 0 (231->340.1), cloth 21 (7.72->9.1), tools 13 (5.02->5.94), cheese 4 (5.78->7.36) | +281 |
| Hanbrücken | 531 | 0.15 | 0.80 (85/turn) | timber 25 (7.82->12.06), nets 3 (34.6->36.48), bricks 5 (5.57->9.26), garments 10 (24.4->24.7) | swords 1 (208.95->340.1), cloth 24 (8.45->9.1), cheese 5 (6.67->7.36), cured fish 3 (21->22.04) | +211 |
| Calange | 218 | 0.06 | 0.10 (11/turn) | dyed cloth 13 (14.28->16.05), cured fish 4 (24.57->26.79), tin ingots 1 (31.5->35.91), wool 3 (10.29->10.54) | swords 1 (200.55->340.1), cloth 10 (7.77->9.1), copper ore 1 (26.04->28.88), tiles 3 (3.95->5.08) | +189 |
| Kirchwerp | 1072 | 0.38 | 0.40 (42/turn) | honey 10 (8.24->9.59), chisels 3 (11.45->12.06), fleece 1 (6.67->7.22), resin 6 (3.15->3.93) | swords 1 (231->340.1), cloth 24 (7.56->9.1), ploughs 5 (73.5->80.27), salt 8 (3.89->5.56) | +183 |

**Best:** Grandgues at about +474 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 7 @ ?, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 13 = 3.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 7 |  | goal planner: buys 2 a turn for today's rates, keeps up to 7 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21.2 | goal planner: sells 11 at 21.2 (v2 had 10 at 23.8) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.5/turn (observed), makes 0.0, holds 1 = 2.1 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.3k (cash + stock at home prices); +110/turn over 6 turns, +24/turn over 24 turns.
- Limits: cash flow >= -262/turn, prestige >= -0.55/turn (values are after 200 tax a turn).
- Today's settings: value +61/turn, cash +31/turn, prestige -2.33/turn - breaks the prestige floor.
- Plan: value +21/turn, cash +29/turn, prestige -0.55/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +136 vs +26, +187 vs +44, +20 vs +31.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +6/turn
  - ship Flax Wyrm -> Marmont: +0/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.29: +10/turn
  - ropewalk 1 0.25 -> 0.00: +10/turn
  - spinnery 1 1.65 -> 1.31: +3/turn
  - sewing shop 1 0.30 -> 0.35: +3/turn
  - weavery 1 0.50 -> 0.59: +9/turn
  - retting pit 1 0.91 -> 0.83: +1/turn
  - flax farm 1 4.64 -> 4.15: +5/turn
- HAND-OVER: goal planner: model check held 12 runs, it now runs 'buys' live.
- Model check over the last 59 turns: predicted -105/turn for the settings we ran, real -107/turn.
- Worth of one more unit per turn: labour 1.68, thread 4.22, cloth 6.74, flax fibres 5.01, garments 19.51, nets 30.71, beer 2.96, timber 3.35, prestige 60.71, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 5); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.05, worth +3/turn.
- Ship linen snake: Grandgues -> Vauxvais (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Marmont (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3681 coin: +1/turn, payback 3611 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 9.6/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 411 (+121 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.92 |
| ret | 3 | 0.91 | 0.78 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 134/77, thread 1064/226, cloth 72/127

## Self-diagnosis

- R1: firewood slot dry: 1.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.24; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
