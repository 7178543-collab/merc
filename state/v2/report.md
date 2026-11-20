# v2 shadow report

Turn 14160, 2026-11-20 09:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,170, prestige 3,748 (628 free, -0.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 2 | 16 | 4 | 0 | stop 63, buy 32, buy @ 4.78 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 1 | 1 | 1 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 548 | 0 | 16 | buy 64, buy @ 2.2 |
| meat | 0 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), 1 bought last turn); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: only 0.5 turns of firewood left and buying 1 (need 4) -> v2: buy 4

## Waste (money lost now)

- **labour**: 16 labour expired last turn (~36 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.00 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +5 crew for Flax Wyrm (crew 0.10, no projection from the game)
- labour: +5 crew for linen snake (crew 0.10, no projection from the game)
- labour: projection runs 120 over real use lately; planning 548, not 614

## Prestige spending, cheapest coin per prestige first

241 turns left: prestige gained now converts 70.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.9 | 51.3 | needs a arena (build cost 29,660); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.5 | 53.1 | needs a arena (build cost 29,660); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.7 | 55.1 | needs a arena (build cost 29,660); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.5 | 58.2 | needs a arena (build cost 29,660); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.3 | 58.3 | thin at home: wine, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 58.4 | 58.4 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 58.6 | 58.6 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 58.9 | 58.9 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 |  |
| hold banquet 4 (premium) | mansion | 20 | 60.3 | 60.3 | thin at home: wine, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 60.7 | 60.7 | thin at home: wine |
| hold banquet 4 | mansion | 17.5 | 62.1 | 62.1 | thin at home: wine, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 13 | 134102075 | 0 | - | candles 4, cured meat 2 | -342 |
| linen snake | 0.1 / 0.10 | 13 | 151802239 | 0 | - | pasties 1 | -15 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 2 @ 74.5, cured meat buy 4 @ 19.8, pasties buy 1 @ 16.4; crew 0.1; est +41 a turn; stock: candles 2 @ 74.5 (keep 12); stock: pasties 1 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: beer buy 15 @ 4.34, candles buy 2 @ 78.0; crew 0.1; est +22 a turn; stock: candles 2 @ 78.0 (keep 12)
- best towns now: Gotthafen +260, Angefont +250, Disscester +241, Bedenis +232, Clairlond +205
- Gotthafen would trade: beer buy 15 @ 3.96, candles buy 2 @ 75.0, cured meat buy 4 @ 21.8, furniture buy 20 @ 13.9, pasties buy 1 @ 14.7; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~136 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.06 | 0.90 (123/turn) | beer 86 (5.62->7.98), bread 241 (2.98->3.76), glassware 5 (87.15->104.5), tiles 3 (4.14->12.54) | cured meat 4 (20.48->25.2), cheese 7 (6.77->7.79), cloth 4 (11.23->12.9) | +537 |
| Rouhomme | 368 | 0.13 | 0.30 (41/turn) | beer 86 (5.62->7.98), lathes 1 (190.05->220.4), candles 2 (59.85->66.02), cloth 21 (13.55->14.15) | tools 20 (6.3->6.98), cheese 7 (7.25->7.79), cookware 4 (20.48->21.47), garments 2 (32.13->34) | +279 |
| Heilegg | 826 | 0.31 | 0.50 (68/turn) | beer 86 (5.62->7.69), candles 2 (59.85->70.3), flour 4 (22.05->26.79) | cloth 24 (10.71->12.9), garments 2 (29.4->34), cheese 7 (6.3->7.79), tools 20 (6.41->6.98) | +221 |
| Kirchwerp | 1072 | 0.49 | 0.40 (54/turn) | furniture 9 (16.7->24.89), nets 6 (39->42.94), candles 2 (59.85->66.97), lead bars 2 (13.76->20.9) | dyed cloth 9 (15.75->20.71), garments 2 (24.15->34), cured meat 4 (20.27->25.2), cheese 7 (5.1->7.79) | +210 |
| Hofkirchen | 991 | 0.43 | 0.30 (41/turn) | casks 12 (8.19->14.25), candles 2 (59.85->74.58), arms 9 (33.6->35.34), nets 6 (39->40.85) | dyed cloth 9 (15.75->20.71), beer 15 (3.89->5.35), cured meat 4 (22.05->25.2), cheese 7 (6.3->7.79) | +181 |

**Best:** Grandgues at about +537 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer | 39 @ 5.65, stop 77 |  | uses 19.2/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 10 = 6.3 turns |
| cured meat | 5 @ 29.0, stop 19 |  | uses 4.6/turn (observed), makes 0.0, holds 18 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 4) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 31.6) |
| grain | 0 @ 3.7, stop 19 |  | goal planner: buys 0 a turn for today's rates, keeps up to 19 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 48) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 39.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 74.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.5k (cash + stock at home prices); -682/turn over 6 turns, -64/turn over 24 turns.
- Limits: cash flow >= -257/turn, prestige >= -1.37/turn (values are after 200 tax a turn).
- Today's settings: value -120/turn, cash -129/turn, prestige +0.89/turn.
- Plan: value +70/turn, cash +82/turn, prestige -1.37/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -479 vs -137, -707 vs -176, -374 vs -155 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship Flax Wyrm -> Marmont: +1/turn
  - mansion 1 1.00 -> 0.46: +127/turn
  - ropewalk 1 0.25 -> 0.13: +15/turn
  - spinnery 1 1.65 -> 1.29: +20/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - retting pit 1 0.91 -> 0.81: +2/turn
  - flax farm 1 4.64 -> 4.09: +2/turn
  - net maker 0.00 -> 0.29: +6/turn
- Model check over the last 59 turns: predicted -24/turn for the settings we ran, real +3/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.76, beer 3.57, timber 4.30, prestige 57.65, cash 0.00
- Orders it would set: arms buy 1 (v2 None); firewood buy 2 (v2 4); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 48); light armour buy 1 (v2 None)
- Ship linen snake: stays on Grandgues (worth +5/turn).
- Ship Flax Wyrm: Caillechâtel -> Marmont (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 425 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.50 |
| ret | 3 | 0.91 | 0.90 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 96/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 32 @ 4.78, home ask 5.4 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 39 @ 5.5 (ask 5.4, cap 14.4))
- R1: firewood slot dry: 1.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.32; our bid is already at/over the ask (sellers too thin)
