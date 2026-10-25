# v2 shadow report

Turn 13529, 2026-10-25 02:43. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,807, prestige 3,570 (450 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 82, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 10 | 0 | 6 | 0 | 0 | stop 16, buy 3, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 7, sell @ 17.8 |
| grain | 33 | 10 | 29 | 0 | 0 | stop 115, buy 29, buy @ 3.7 |
| labour | 1 | 20 | 519 | 0 | 1 | buy 1, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 13 | 13 | 11 | 0 | 2 | buy 13, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 17/turn) -> v2: check the step that makes it
- **labour**: buying 1, short of ~119 needed -> v2: buy 119

## Tuning

- **firewood**: we make 0/turn more than we use but there is no sell order -> v2: sell 0
- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 43

## Prestige spending, cheapest coin per prestige first

872 turns left: prestige gained now converts 98.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| hold banquet 3 (pies) | mansion | 8 | 49.2 | 49.2 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 49.4 | 49.4 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.0 | 50.0 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 52.7 | 52.8 | needs a arena (build cost 24,505); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 53.0 | 53.0 | thin at home: wine, hop beer, stockfish |
| hold prayer 2 | chapel | 13 | 50.2 | 53.2 | needs a chapel (build cost 31,402); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.7 | 53.7 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 53.8 | 53.8 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 54.5 | 54.5 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 54.5 | 54.5 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 52.0 | 54.6 | needs a church (build cost 64,925); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Amsdermund +32, Vauxvais +25, Marmont +23, Briclives +20, Fontaux +20
- Amsdermund would trade: rope sell 3 @ 83.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Großaue | 1136 | 0.38 | 1.00 (96/turn) | bread 77 (2.14->4.27), rope 1 (68.5->71.72), scythes 0 (24.99->26.03) | candles 0 (68.25->73.5), cheese 5 (4.41->5.61), flax fibres 8 (4.96->6.05), beer 5 (2.69->3.5) | +91 |
| Unterhufe | 595 | 0.15 | 0.10 (10/turn) | grindstones 1 (258.3->288.8), rope 3 (68.5->71.25), garments 6 (17.8->18.43) | lathes 1 (170.1->193.8), candles 1 (67.2->73.5), gears 1 (58.8->61.75), flax fibres 5 (5.57->6.05) | +68 |
| Grandgues | 152 | 0.04 | 0.60 (58/turn) | firewood 28 (1.89->4.31), timber 17 (7.51->8.88), charcoal 11 (2.01->2.94), rope 3 (68.5->69.83) | candles 1 (69.3->73.5), mouldboards 2 (30.87->32.3), pasties 2 (12.08->13.3), furniture 1 (13.65->14.6) | +62 |
| Bordetes | 831 | 0.22 | 0.30 (29/turn) | raw cloth 6 (7.51->11.49), rope 3 (68.5->70.77), malt 1 (5.62->9.07), wrought iron 5 (14.07->14.82) | lathes 1 (184.8->193.8), spinning wheels 1 (210->218.5), candles 1 (69.3->73.5), cloth 14 (7.25->7.5) | +52 |
| Amsdermund | 1111 | 0.37 | 0.20 (19/turn) | rope 3 (68.5->85.5) | flax fibres 19 (5.25->6.05), mouldboards 1 (31.08->32.3), nails 10 (5.62->5.98), tools 1 (4.2->4.62) | +51 |

**Best:** Großaue at about +91 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 56 @ min 2.98 | goal planner: sells 56 at 2.98 (v2 had 55 at 3.38) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 1) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 0 @ 2.4, stop 13 | 1 @ min 1.75 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 10 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 7 @ min 17.8 | goal planner: sells 7 at 17.8 (v2 had 6 at 20.0) |
| grain | 29 @ 3.7, stop 115 |  | goal planner: buys 29 a turn for today's rates, keeps up to 115 (v2 had 58) |
| labour | 20 @ 2.2, stop - |  | goal planner: buys 20 for today's rates (v2 had 119) |
| light armour | 1 @ 86, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 12 @ min 34 | goal planner: sells 12 at 34 (v2 had 12 at 34.6) |
| pasties | 4 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 11 = 3.9 turns |
| porterage | 11 @ 1.1, stop - |  | goal planner: buys 11 for today's rates (v2 had 11) |
| rope |  | 4 @ min 66.5 | makes 2.0, uses 0.2, holds 23 (keeps 0): sells the surplus + 2/turn of the excess |
| thread |  | 11 @ min 4.1 | goal planner: sells 11 a turn at 4.1, keeps 221 (no one offered it) |
| tools | 2 @ 6.2, stop 13 |  | uses 1.5/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 199 = 130.0 turns |
| varnish | 1 @ 21.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| wax | 1 @ 20.8, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.3k (cash + stock at home prices); +73/turn over 6 turns, +79/turn over 24 turns.
- Limits: cash flow >= +91/turn, prestige >= -0.63/turn (values are after 240 tax a turn).
- Today's settings: value +15/turn, cash +99/turn, prestige -0.61/turn.
- Plan: value +35/turn, cash +91/turn, prestige -0.63/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +293 vs -37, +303 vs -59, +514 vs -53.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Magdeach: +2/turn
  - net maker 0.50 -> 0.60: +4/turn
  - ropewalk 1 0.50 -> 0.00: +1/turn
  - ropewalk 1 [make rope 2] 0.00 -> 0.38: +9/turn
  - logging camp w/ tool 5.00 -> 4.87: +0/turn
  - flax farm 1 3.55 -> 3.69: -1/turn
  - weavery 1 0.33 -> 0.22: -6/turn
  - sewing shop 1 0.21 -> 0.10: +3/turn
- Model check over the last 34 turns: predicted +116/turn for the settings we ran, real +60/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.65, thread 4.05, cloth 6.52, flax fibres 4.65, garments 18.94, nets 30.10, beer 2.93, timber 3.04, prestige 57.94, cash 0.06
- Orders it would set: beer sell 56 (v2 55); garments sell 7 (v2 6); grain buy 29 (v2 58); labour buy 20 (v2 119); light armour buy 1 (v2 None); thread sell 11 (v2 none)
- Recipe: ropewalk 1 make rope 1 -> make rope 2 at 0.38, worth +5/turn.
- Ship linen snake: Grandgues -> Magdeach (+2/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +10/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +20/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +18/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 7.8/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 409, chain may buy 0 -> chain allowance 91, chain plan 94 (-116 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.55 | 2.14 |
| ret | 3 | 0.62 | 0.38 |
| spin | 4 | 1.28 | 0.79 |
| weave | 3 | 0.33 | 0.00 |
| sew | 2 | 0.21 | 0.00 |

Buffers: flax fibres 36/47, thread 834/138, cloth 0/0
- chain plan needed 94 labour, budget left 91: cut to 94

## Self-diagnosis

- R5: varnish buy not filling: bid 17.1 under the home ask 20.0 for 6 turns, bought 0.0 of 1, 0.1 held (0.4 turns) (held back: ship trade good (v2 ships own it): finding only)
