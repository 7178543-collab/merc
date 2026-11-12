# v2 shadow report

Turn 13974, 2026-11-12 15:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,768, prestige 3,536 (416 free, -2.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 1 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 36 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 4.12 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 4.12 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.00 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~77 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 12.00 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for Flax Wyrm (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 485, not 585

## Prestige spending, cheapest coin per prestige first

427 turns left: prestige gained now converts 88.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 53.7 | 53.7 | thin at home: ham, stockfish |
| jousting 3 | arena | 230 | 55.7 | 56.0 | needs a arena (build cost 26,607); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 56.2 | 56.2 | thin at home: ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 57.8 | 57.8 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 58.0 | 58.0 | thin at home: pasties, pies |
| hold banquet 3 (pies) | mansion | 8 | 58.1 | 58.1 | thin at home: pasties, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 58.4 | 58.4 | thin at home: cured fish |
| hold banquet 4 (premium) | mansion | 20 | 58.6 | 58.6 | thin at home: ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 58.8 | 58.8 | thin at home: cured fish |
| jousting 2 | arena | 210 | 61.0 | 61.3 | needs a arena (build cost 26,607); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 59.3 | 66.5 | needs a chapel (build cost 34,162); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 6 @ 14.2; crew 0.1; est +63 a turn; stock: furniture 6 @ 14.2 (keep 145)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Disscester +69, Gotthafen +65, Nürnnieder +63, Bordees +63, Caillechâtel +63
- Disscester would trade: furniture buy 6 @ 13.3, garments sell 6 @ 24.6; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Chatgnan | 728 | 0.20 | 0.20 (21/turn) | limestone 2 (18.06->33.44), flax fibres 4 (5.04->5.98), garments 10 (21.6->21.85) | tapestries 1 (598.5->688.75), gold ore 1 (135.45->172.9), furniture 17 (15.96->17.48) | +153 |
| Vauxvais | 204 | 0.06 | 0.10 (11/turn) | wax 11 (26.25->27.17), hop beer 3 (10.45->11.02), wine 10 (6.77->6.89), grain 2 (2.72->2.91) | tapestries 1 (598.5->688.75), furniture 17 (15.96->17.48), flour 1 (17.64->21.09), cloth 14 (7.56->7.75) | +130 |
| Grandgues | 152 | 0.04 | 0.70 (74/turn) | firewood 37 (4.33->6.65), cured fish 6 (25.2->28.12), premium steel 1 (30.45->39.9), charcoal 19 (4.07->4.6) | furniture 17 (15.75->17.48), cured meat 3 (23.94->25.27), beer 4 (3.51->3.8), flax fibres 5 (6.83->6.95) | +110 |
| Helmgreen | 1354 | 0.54 | 0.30 (32/turn) | tin ingots 1 (28.77->35.15), dyed yarn 1 (5.15->5.84) | tapestries 1 (614.25->688.75), gold ore 1 (147->172.9), furniture 9 (15.12->17.48), blades 1 (14.38->15.2) | +98 |
| Fontaux | 411 | 0.12 | 0.20 (21/turn) | thread 77 (4.96->5.65), cookware 5 (30.03->33.82), wine 16 (6.77->7.74), flax fibres 5 (5.04->6.32) | ham 2 (82.42->87.88), cured meat 3 (24.36->25.27), nails 2 (7.3->7.5), tallow 1 (19.21->19.76) | +92 |

**Best:** Chatgnan at about +153 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 7 @ 3.98, stop 9 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 1 = 0.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 90, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.0) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 38.4) |
| pasties |  | 2 @ min 12.1 | goal planner: trial sale of an idle pile, 2 a turn at 12.1, keeps 0 (14 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.5k (cash + stock at home prices); +106/turn over 6 turns, -39/turn over 24 turns.
- Limits: cash flow >= -365/turn, prestige >= -0.48/turn (values are after 200 tax a turn).
- Today's settings: value +48/turn, cash +22/turn, prestige -2.29/turn - breaks the prestige floor.
- Plan: value -36/turn, cash -32/turn, prestige -0.48/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +161 vs -8, +150 vs +2, +88 vs +15.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Nürnnieder: +0/turn
  - ship Flax Wyrm -> Friedwerp: +1/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.35: +1/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - flax farm 1 4.64 -> 4.22: -0/turn
  - weavery 1 0.50 -> 0.43: -11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.24: -18/turn
  - ropewalk 1 0.25 -> 0.00: +22/turn
- Model check over the last 61 turns: predicted +105/turn for the settings we ran, real +16/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.20, beer 3.05, timber 3.29, prestige 67.32, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); pasties sell 2 (v2 none); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.24, worth +9/turn.
- Ship linen snake: Grandgues -> Nürnnieder (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Friedwerp (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1796 coin: +3/turn, payback 659 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 408 (+118 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.72 |
| ret | 3 | 0.91 | 0.74 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 149/77, thread 1064/227, cloth 73/127

## Self-diagnosis

- R1: beer slot dry: 0.6 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy 9 @ 3.76, home ask 3.8 -> **buy 9 @ 3.86 (ask 3.8, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 4.12; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
