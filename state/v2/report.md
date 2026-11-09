# v2 shadow report

Turn 13888, 2026-11-09 01:13. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,117, prestige 3,527 (407 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 8 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 19 | 9 | 9 | 0 | 0 | stop 36, buy 18, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.50 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.50 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

513 turns left: prestige gained now converts 92.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 56.3 | 56.3 | thin at home: ham, stockfish |
| jousting 3 | arena | 230 | 56.0 | 56.3 | needs a arena (build cost 27,682); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 58.3 | 58.3 | thin at home: ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 58.5 | 58.5 | thin at home: ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.0 | 59.0 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 61.6 | 61.6 | thin at home: cured fish |
| jousting 2 | arena | 210 | 61.4 | 61.7 | needs a arena (build cost 27,682); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 63.2 | 63.2 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 63.6 | 63.6 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 63.8 | 63.8 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.0 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- best towns now: Gotthafen +350, Calange +319, Essenbrucke +296, Brunnham +290, Clairlond +271
- Gotthafen would trade: furniture buy 31 @ 13.8, pasties buy 2 @ 15.8; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.11 | 0.70 (82/turn) | bread 155 (2.69->3.57), charcoal 19 (2.62->5.51), malt 9 (5.46->9.69), flour 1 (24.15->28.69) | thread 31 (4.94->5.6), cloth 7 (10.24->11.97), cookware 6 (23.31->25.08), tools 17 (4.51->5.18) | +225 |
| Grandgues | 152 | 0.05 | 0.80 (93/turn) | timber 30 (7.61->11.21), firewood 38 (2.58->4.99), charcoal 19 (2.62->4.75), wine 30 (6.77->7.03) | cloth 7 (10.08->11.97), thread 21 (5.19->5.6), tools 9 (4.79->5.18), flax fibres 12 (6.3->6.4) | +197 |
| Blanans | 297 | 0.09 | 0.50 (58/turn) | timber 33 (7.61->10.64), lead ore 6 (12.6->19.19), honey 2 (9.4->9.79), malt 2 (5.46->6.22) | cloth 7 (8.29->11.97), salt 9 (4.96->5.56), cookware 6 (24.57->25.08), tools 17 (4.94->5.18) | +135 |
| Hanbrücken | 531 | 0.17 | 0.60 (70/turn) | timber 18 (7.61->12.06), wine 19 (6.77->8.55), garments 10 (23.4->25.27), nets 3 (37->38.57) | cloth 7 (8.72->11.97), salt 9 (4.66->5.56), thread 6 (4.7->5.6), varnish 1 (15.44->15.77) | +125 |
| Kirchwerp | 1072 | 0.42 | 0.50 (58/turn) | thread 85 (4.64->5.7), wine 23 (6.77->9.5), chisels 5 (9.97->11.69), nets 6 (37->38.57) | garments 2 (24.15->26.2) | +116 |

**Best:** Rouhomme at about +225 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.42) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 82.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 18 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 19 = 2.1 turns |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.0k (cash + stock at home prices); +270/turn over 6 turns, +83/turn over 24 turns.
- Limits: cash flow >= -297/turn, prestige >= -0.44/turn (values are after 200 tax a turn).
- Today's settings: value +49/turn, cash +9/turn, prestige -2.04/turn - breaks the prestige floor.
- Plan: value -4/turn, cash +29/turn, prestige -0.44/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -28 vs +16, +74 vs +22, -115 vs +20.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Cobholme: +7/turn
  - ship Flax Wyrm -> no route: +0/turn
  - ropewalk 1 0.25 -> 0.00: +13/turn
  - net maker 0.00 -> 0.29: +9/turn
  - weavery 1 0.50 -> 0.60: +2/turn
  - sewing shop 1 0.30 -> 0.36: +4/turn
  - brewery 1 0.14 -> 0.00: -6/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.19: +1/turn
  - spinnery 1 1.65 -> 1.17: -7/turn
  - retting pit 1 0.91 -> 0.67: +7/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real -22/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.65, thread 4.18, cloth 6.64, flax fibres 5.02, garments 19.19, nets 29.95, beer 2.88, timber 3.26, prestige 60.87, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.19, worth +14/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +3/turn.
- Ship linen snake: Grandgues -> Cobholme (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/77, thread 844/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.4 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
