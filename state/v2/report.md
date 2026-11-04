# v2 shadow report

Turn 13768, 2026-11-04 01:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,876, prestige 3,181 (61 free, -0.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 6 | 0 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 29, short of ~35 needed -> v2: buy 35

## Notes

- labour: projection runs 100 over real use lately; planning 535, not 635

## Prestige spending, cheapest coin per prestige first

633 turns left: prestige gained now converts 95.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.1 | 51.1 | thin at home: hop beer, stockfish, candles |
| jousting 3 | arena | 230 | 52.8 | 53.0 | needs a arena (build cost 24,774); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 53.8 | 53.8 | thin at home: hop beer, ham, stockfish, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| hold banquet 3 (pies) | mansion | 8 | 54.5 | 54.5 | thin at home: hop beer, pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 54.6 | 54.6 | thin at home: hop beer, stockfish, candles |
| hold banquet 2 (pies) | mansion | 7 | 55.7 | 55.7 | thin at home: pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 55.9 | 55.9 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 56.3 | 56.3 |  |
| jousting 2 | arena | 210 | 57.8 | 58.0 | needs a arena (build cost 24,774); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| jousting 1 | arena | 170 | 58.3 | 58.6 | needs a arena (build cost 24,774); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 134102075 | 0.54 | - | furniture 27, pasties 2 | -384 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 19 @ 13.8, pasties buy 6 @ 14.4; crew 0.2; est +246 a turn; stock: furniture 19 @ 13.8 (keep 145); stock: pasties 6 @ 14.4 (keep 14)
- **linen snake** on Grandgues: pasties buy 6 @ 14.0; crew 0.1; est +19 a turn; stock: pasties 6 @ 14.0 (keep 14)
- best towns now: Pontmont +345, Hofkirchen +326, Bedenis +323, Chatgnan +318, Donaunieder +318
- Pontmont would trade: furniture buy 26 @ 14.2, pasties buy 10 @ 14.1; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Corstoft | 1496 | 0.59 | 0.20 (20/turn) | cloth 1 (6.35->7.79), yarn 3 (3.8->4.56), wool 1 (7.51->8.6) | looms 1 (525->722), cookware 8 (23.1->24.13), gears 1 (63.53->65.08) | +192 |
| Heilegg | 826 | 0.23 | 0.50 (50/turn) | cured fish 7 (22.68->25.65), wrought iron 15 (14.49->15.58), charcoal 19 (2.31->4.33), logs 1 (3.86->10.26) | looms 1 (656.25->722), cloth 24 (7.14->8.4), cookware 8 (22.68->24.13), thread 46 (4.62->5.05) | +151 |
| Rouhomme | 368 | 0.10 | 0.20 (20/turn) | charcoal 19 (2.31->3.5), cloth 1 (6.35->7.6), grain 2 (2.52->2.98), yarn 3 (3.8->4.16) | looms 1 (630->722), cookware 8 (21->24.13), flax fibres 13 (4.94->5.95), garments 2 (22.05->24) | +149 |
| Gotthafen | 964 | 0.30 | 0.20 (20/turn) | wool 1 (7.51->7.84) | looms 1 (603.75->722), cookware 8 (21.84->24.13), cloth 24 (7.51->8.4), garments 2 (21.42->24) | +144 |
| Kirchwerp | 1072 | 0.36 | 0.30 (30/turn) | furniture 12 (15.86->19.95), light armour 2 (91.35->93.57), pickaxes 2 (9.87->10.83), wool 1 (7.51->8.07) | looms 1 (651->722), cloth 24 (7.04->8.4), garments 2 (20.37->24), jewellery 3 (76.12->77.42) | +139 |

**Best:** Corstoft at about +192 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.1 | goal planner: sells 1 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 22.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 30 @ 2.2, stop - |  | goal planner: buys 30 for today's rates (v2 had 35) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.4k (cash + stock at home prices); +157/turn over 6 turns, +159/turn over 24 turns.
- Limits: cash flow >= -161/turn, prestige >= +9.96/turn (values are after 200 tax a turn).
- Today's settings: value +106/turn, cash +104/turn, prestige -0.31/turn - breaks the prestige floor.
- Plan: value -126/turn, cash -122/turn, prestige +3.89/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -36 vs +102, +82 vs +112, -278 vs +111 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Herschweig: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - flax farm 1 4.64 -> 4.45: +1/turn
  - spinnery 1 1.65 -> 1.58: +0/turn
  - sewing shop 1 0.30 -> 0.37: -7/turn
  - weavery 1 0.50 -> 0.61: +9/turn
  - ropewalk 1 0.25 -> 0.00: -14/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.30: +15/turn
  - brewery 1 0.14 -> 0.27: -17/turn
- Model check over the last 59 turns: predicted +69/turn for the settings we ran, real +96/turn.
- Worth of one more unit per turn: labour 1.61, thread 4.04, cloth 6.46, flax fibres 4.79, garments 18.69, nets 29.05, beer 2.79, timber 3.02, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 30 (v2 35); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +13/turn.
- Ship linen snake: Grandgues -> Herschweig (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.3/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 493 (+205 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.21 |
| ret | 3 | 0.91 | 1.24 |
| spin | 4 | 1.65 | 2.19 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 281/228, cloth 81/128

## Self-diagnosis

Nothing found this run.
