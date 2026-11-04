# v2 shadow report

Turn 13782, 2026-11-04 15:38. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,525, prestige 3,322 (202 free, +100.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 29, short of ~130 needed -> v2: buy 130

## Prestige spending, cheapest coin per prestige first

619 turns left: prestige gained now converts 95.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.7 | 51.7 | thin at home: pasties, hop beer, stockfish, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 |  |
| hold banquet 4 | mansion | 17.5 | 54.2 | 54.2 | thin at home: hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 54.1 | 54.2 | needs a arena (build cost 24,782); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 54.4 | 54.4 | thin at home: pasties, pies |
| hold banquet 4 (premium) | mansion | 20 | 55.2 | 55.2 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 56.2 | 56.2 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 56.6 | 56.6 | thin at home: pasties, hop beer, pies |
| hold banquet 2 (meat) | mansion | 6.8 | 56.7 | 56.7 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 59.0 | 59.0 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.052 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 4 @ 77.5, pasties buy 3 @ 16.2; crew 0.1; est +48 a turn; stock: candles 4 @ 77.5 (keep 12); stock: pasties 3 @ 16.2 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 13.6 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Clarfranche +79, Blanans +74, Gottweiler +68, Hanstein +66, Orlesailles +65
- Clarfranche would trade: candles buy 4 @ 74.0, pasties buy 4 @ 12.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (49/turn) | bread 153 (2.16->2.66), timber 26 (7.04->9.03), thread 13 (4.48->5.22), harnesses 1 (34.02->41.61) | bricks 3 (6.41->9.59), yarn 3 (4.77->5.27), varnish 1 (15.65->15.96) | +131 |
| Fontaux | 411 | 0.11 | 0.90 (88/turn) | garments 10 (18.32->24.51), wine 18 (5.78->7.74), bread 148 (2.16->2.66), timber 17 (7.04->9.03) | leather 1 (26.04->28.12), yarn 3 (4.73->5.27), hinges 1 (36.96->37.62) | +130 |
| Hanstein | 380 | 0.10 | 0.30 (29/turn) | timber 14 (7.04->10.64), grindstones 1 (224.7->247), garments 10 (18.32->19.76), harnesses 1 (34.02->37.81) | thread 62 (4.14->4.6), flax fibres 27 (5.21->5.8), yarn 3 (4.16->5.27), bricks 3 (6.77->9.59) | +109 |
| Heilegg | 826 | 0.22 | 1.00 (98/turn) | grindstones 0 (224.7->296.4), bread 127 (2.16->3), nets 5 (34.8->37.24), wine 13 (5.78->6.37) | garments 1 (18.9->22.4), yarn 2 (4.73->5.27) | +103 |
| Rouhomme | 368 | 0.10 | 0.60 (59/turn) | bread 153 (2.16->2.72), harnesses 1 (34.02->42.94), firewood 1 (1.71->6.27), beer 15 (3.3->3.59) | flax fibres 12 (4.94->5.8), bricks 3 (6.51->9.59), tools 16 (4.51->4.75), garments 2 (21.63->22.4) | +71 |

**Best:** Grandgues at about +131 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.0 turns |
| cloth |  | 2 @ min 7.05 | goal planner: sells 2 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 1 @ min 1.27 | goal planner: sells 1 a turn at 1.27, keeps 219 (no one offered it) |
| furniture | 2 @ 15.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 21.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 130) |
| light armour | 1 @ 92, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 79.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 2.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.8k (cash + stock at home prices); +172/turn over 6 turns, +87/turn over 24 turns.
- Limits: cash flow >= -147/turn, prestige >= +4.09/turn (values are after 200 tax a turn).
- Today's settings: value +80/turn, cash +72/turn, prestige +108.00/turn.
- Plan: value +385/turn, cash +251/turn, prestige +100.00/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +71 vs +82, +202 vs +74, +72 vs +77.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +3/turn
  - ship Flax Wyrm -> Briclives: +1/turn
  - park 1 16.00 -> 0.00: +46/turn
  - net maker [make nets 1] 0.00 -> 0.38: +18/turn
  - flax farm 1 4.64 -> 8.00: +18/turn
  - retting pit 1 0.91 -> 1.59: +31/turn
  - spinnery 1 1.65 -> 2.81: +95/turn
  - weavery 1 0.50 -> 0.68: +13/turn
  - sewing shop 1 0.30 -> 0.41: +41/turn
  - ropewalk 1 0.25 -> 0.00: -35/turn
- Model check over the last 60 turns: predicted +104/turn for the settings we ran, real +101/turn.
- Worth of one more unit per turn: labour 0.86, thread 2.18, cloth 3.47, flax fibres 2.60, garments 10.04, nets 16.28, beer 2.07, timber 3.02, prestige 0.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 2 (v2 none); firewood buy 4 (v2 5); flax plants sell 1 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 130); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 1.00, worth +37/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +23/turn.
- Ship linen snake: Grandgues -> Vauxvais (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Briclives (+1/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +43/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 478 (+189 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.85 |
| ret | 3 | 0.91 | 1.17 |
| spin | 4 | 1.65 | 2.07 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 354/228, cloth 74/128

## Self-diagnosis

Nothing found this run.
