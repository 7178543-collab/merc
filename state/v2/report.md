# v2 shadow report

Turn 14054, 2026-11-15 23:20. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,082, prestige 3,556 (436 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 12 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 26, buy 9, buy @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 38 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.00 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.00 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~77 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 12.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 490, not 590

## Prestige spending, cheapest coin per prestige first

347 turns left: prestige gained now converts 82.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| jousting 3 | arena | 230 | 54.6 | 55.0 | needs a arena (build cost 27,304); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.5 | 55.5 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 59.2 | 59.2 |  |
| jousting 2 | arena | 210 | 59.8 | 60.3 | needs a arena (build cost 27,304); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.7 | 60.7 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 60.8 | 60.8 | thin at home: pasties, hop beer, ham, stockfish, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 62.5 | 62.5 | thin at home: hop beer, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 63.1 | 63.1 |  |
| hold banquet 2 (pies) | mansion | 7 | 63.2 | 63.2 | thin at home: pasties, pies |
| hold banquet 3 (pies) | mansion | 8 | 63.2 | 63.2 | thin at home: pasties, hop beer, pies |
| hold banquet 4 (premium) | mansion | 20 | 63.3 | 63.3 | thin at home: hop beer, ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 14.0, pasties buy 4 @ 14.0; crew 0.2; est +259 a turn; stock: furniture 21 @ 14.0 (keep 145); stock: pasties 4 @ 14.0 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Amsdermund +640, Chatgnan +528, Gotthafen +468, Bedenis +447, Vauxvais +379
- Amsdermund would trade: furniture buy 58 @ 13.7; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (107/turn) | timber 42 (7.82->12.82), firewood 32 (3.15->6.32), bread 145 (2.37->2.83), charcoal 17 (2.92->5.13) | candles 0 (70.35->89.5), cheese 7 (6.62->7.08), wax 1 (28.14->29.26), cloth 4 (8.66->8.85) | +364 |
| Heilegg | 826 | 0.24 | 1.00 (107/turn) | beer 120 (3.15->4.01), charcoal 17 (2.92->6.03), nets 5 (34.8->37.43), cured fish 6 (24.57->26.22) | cloth 21 (7.4->8.85), cheese 7 (5.78->7.08), candles 0 (84.53->89.5), garments 1 (23.31->24) | +126 |
| Vauxvais | 204 | 0.06 | 1.00 (107/turn) | bread 114 (2.37->2.75), charcoal 13 (2.92->4.89), firewood 38 (3.15->5.32), beer 50 (3.15->3.55) | candles 0 (64.58->89.5), acid 0 (116.55->121.6), flax fibres 5 (5.62->6.15), thread 8 (4.7->5.05) | +107 |
| Calange | 218 | 0.06 | 0.50 (53/turn) | tapestries 1 (777->817), beer 97 (3.15->3.44), bread 160 (2.37->2.64), limestone 1 (16.59->22.23) | cloth 11 (7.19->8.85), flax fibres 17 (5.83->6.15), yarn 3 (3.42->4.45), blades 1 (15.12->15.29) | +100 |
| Hanbrücken | 531 | 0.15 | 0.70 (75/turn) | timber 30 (7.82->12.06), nets 5 (34.8->39.9), steel ingots 1 (19.74->20.52) | cloth 24 (8.45->8.85), candles 1 (87.67->89.5), cheese 8 (6.67->7.08), salt 4 (5.06->5.56) | +95 |

**Best:** Grandgues at about +364 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21.2 | goal planner: sells 11 at 21.2 (v2 had 10 at 22.6) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.4k (cash + stock at home prices); +87/turn over 6 turns, +22/turn over 24 turns.
- Limits: cash flow >= -253/turn, prestige >= -0.57/turn (values are after 200 tax a turn).
- Today's settings: value +68/turn, cash +44/turn, prestige -2.39/turn - breaks the prestige floor.
- Plan: value +32/turn, cash +46/turn, prestige -0.57/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +105 vs +27, -262 vs +34, +136 vs +26.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +9/turn
  - ship Flax Wyrm -> Pontmont: +0/turn
  - brewery 1 0.14 -> 0.01: +26/turn
  - net maker 0.00 -> 0.29: +10/turn
  - ropewalk 1 0.25 -> 0.00: +9/turn
  - weavery 1 0.50 -> 0.59: +1/turn
  - sewing shop 1 0.30 -> 0.35: +15/turn
  - spinnery 1 1.65 -> 1.31: +1/turn
  - retting pit 1 0.91 -> 0.82: -1/turn
  - flax farm 1 4.64 -> 4.12: -6/turn
- Model check over the last 59 turns: predicted -116/turn for the settings we ran, real -102/turn.
- Worth of one more unit per turn: labour 1.70, thread 4.27, cloth 6.82, flax fibres 5.07, garments 19.74, nets 31.23, beer 3.00, timber 3.35, prestige 59.30, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.05, worth +3/turn.
- Ship linen snake: Grandgues -> Vauxvais (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Pontmont (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3795 coin: +1/turn, payback 5453 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 9.5/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 411 (+121 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.96 |
| ret | 3 | 0.91 | 0.79 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 130/77, thread 1064/226, cloth 72/126

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.0; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
