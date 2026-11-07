# v2 shadow report

Turn 13857, 2026-11-07 18:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,129, prestige 3,360 (240 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 12 | 5 | 4 | 0 | 0 | min_holding 60, sell 3, sell @ 3.06; stop 17, buy 8, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 2 | 2 | 2 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 31, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 507 | 0 | 22 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), 2 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: only 0.6 turns of firewood left and buying 2 (need 7) -> v2: buy 7
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~36 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 607

## Prestige spending, cheapest coin per prestige first

544 turns left: prestige gained now converts 93.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 53.2 | 53.2 | thin at home: hop beer, wine, ham, stockfish, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 53.7 | 53.7 | thin at home: wine, cheese |
| jousting 3 | arena | 230 | 53.9 | 54.1 | needs a arena (build cost 25,407); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 54.6 | 54.6 | thin at home: hop beer, cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 55.1 | 55.1 | thin at home: wine, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.3 | 55.3 | thin at home: beer |
| hold banquet 3 (meat) | mansion | 7.6 | 55.9 | 55.9 | thin at home: hop beer, cheese |
| hold banquet 3 (pies) | mansion | 8 | 55.9 | 55.9 | thin at home: pasties, hop beer, pies, candles |
| hold banquet 4 | mansion | 17.5 | 55.9 | 55.9 | thin at home: wine, hop beer, ham, stockfish, candles |
| hold banquet 2 (pies) | mansion | 7 | 56.1 | 56.1 | thin at home: pasties, wine, cheese, pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 57.2 | 57.2 | thin at home: hop beer, wine, ham, stockfish, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 9 @ 15.9; crew 0.1; est +16 a turn; stock: pasties 9 @ 15.9 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.0 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Hanstein +27, Rouhomme +26, Blanans +22, Grandgues +16, Herschweig +15
- Hanstein would trade: beer buy 4 @ 3.14, pasties buy 9 @ 15.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.11 | 0.40 (42/turn) | timber 15 (7.25->11.59), charcoal 18 (2.44->3.55), axes 1 (15.12->16.05), salt 5 (4.81->4.99) | cloth 24 (7.25->8.95), thread 43 (4.89->5.3), beer 4 (3.23->3.94), bricks 3 (6.83->9.79) | +105 |
| Caillechâtel | 488 | 0.14 | 0.20 (21/turn) | medicine 2 (158.55->184.3), nets 3 (33.6->34.2), raw cloth 2 (6.93->7.41) | tapestries 1 (614.25->660.25), thread 18 (4.79->5.3), jewellery 3 (86.1->87.4), flax fibres 10 (5.78->6.25) | +103 |
| Etallaen | 774 | 0.22 | 0.10 (11/turn) | nets 6 (33.6->38.76), cured meat 8 (22.89->25.08), cheese 3 (6.2->9.12), rope 1 (80->87.4) | cloth 16 (7.35->8.95), chisels 1 (7.09->8.17), flax fibres 6 (5.67->6.25), thread 7 (4.96->5.3) | +84 |
| Grandgues | 152 | 0.04 | 0.30 (32/turn) | timber 26 (7.25->9.31), charcoal 18 (2.44->4.33), logs 1 (3.97->7.6), rope 1 (80->81.7) | bricks 5 (8.35->9.79), casks 2 (6.04->6.13), fleece 1 (9.4->9.45) | +71 |
| Vauxvais | 204 | 0.06 | 0.20 (21/turn) | beer 52 (4.14->4.94), cheese 3 (6.2->6.46), limestone 2 (16.8->19.76), axes 1 (15.12->15.58) | bricks 5 (5.72->9.79), thread 15 (4.96->5.3), cloth 10 (8.56->8.95), flax fibres 7 (5.67->6.25) | +68 |

**Best:** Hanstein at about +105 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 7 @ 3.94, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 12 = 2.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 74.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 13 |  | goal planner: buys 4 a turn for today's rates, keeps up to 13 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.2) |
| grain | 8 @ 3.7, stop 31 |  | goal planner: buys 8 a turn for today's rates, keeps up to 31 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.0k (cash + stock at home prices); +164/turn over 6 turns, +116/turn over 24 turns.
- Limits: cash flow >= -339/turn, prestige >= +2.50/turn (values are after 200 tax a turn).
- Today's settings: value +85/turn, cash +68/turn, prestige -1.33/turn - breaks the prestige floor.
- Plan: value -97/turn, cash -91/turn, prestige +2.50/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +70 vs +66, +158 vs +61, +124 vs +62.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanbrücken: +2/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - ropewalk 1 0.25 -> 0.33: +3/turn
  - spinnery 1 1.65 -> 1.35: -7/turn
  - retting pit 1 0.91 -> 0.77: +3/turn
  - flax farm 1 4.64 -> 3.87: +6/turn
  - weavery 1 0.50 -> 0.31: -40/turn
  - sewing shop 1 0.30 -> 0.18: -10/turn
  - mansion 1 0.00 -> 0.91: -142/turn
- Model check over the last 61 turns: predicted +103/turn for the settings we ran, real +77/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 29.84, beer 2.89, timber 3.08, prestige 55.03, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 7); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Hanbrücken (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 440 (+151 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.00 |
| ret | 3 | 0.91 | 1.00 |
| spin | 4 | 1.65 | 1.76 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 535/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 2.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 4 @ 2.4, home ask 2.26; our bid is already at/over the ask (sellers too thin)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.3 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
