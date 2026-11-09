# v2 shadow report

Turn 13898, 2026-11-09 11:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,874, prestige 3,507 (387 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 9 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 6 | 0 | buy 30, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 30, short of ~35 needed -> v2: buy 35

## Notes

- labour: projection runs 100 over real use lately; planning 535, not 635

## Prestige spending, cheapest coin per prestige first

503 turns left: prestige gained now converts 92.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 3 | arena | 230 | 55.4 | 55.7 | needs a arena (build cost 27,006); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 56.0 | 56.0 | thin at home: ham, stockfish, cheese |
| hold banquet 4 | mansion | 17.5 | 57.6 | 57.6 | thin at home: ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.6 | 57.6 | thin at home: ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.0 | 59.0 | thin at home: cured fish |
| jousting 2 | arena | 210 | 60.7 | 61.0 | needs a arena (build cost 27,006); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 61.2 | 61.2 | thin at home: cured fish, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 61.8 | 61.8 | thin at home: cured fish, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 64.0 | 64.0 |  |
| hold banquet 3 (pies) | mansion | 8 | 64.6 | 64.6 | thin at home: pasties, cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 64.7 | 64.7 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 134102075 | 0.32 | - | furniture 20 | -281 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 14.1; crew 0.2; est +225 a turn; stock: furniture 20 @ 14.1 (keep 145)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Heidlowe +381, Gotthafen +354, Clairlond +316, Brunnham +286, Fulkirch +277
- Heidlowe would trade: furniture buy 35 @ 14.6; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (96/turn) | bread 154 (2.33->3.4), charcoal 18 (2.01->6.51), firewood 35 (2.37->5.61), timber 24 (8.45->9.59) | thread 20 (5->5.2), flour 3 (22.89->23.94), flax plants 1 (0.44->1.58), salt 6 (5.35->5.56) | +313 |
| Rouhomme | 368 | 0.10 | 1.00 (107/turn) | bread 85 (2.33->3.74), charcoal 10 (2.01->5.03), firewood 21 (2.37->5.84), grain 1 (2.6->3.86) | thread 25 (4.87->5.2), tools 9 (4.51->5.08), candles 0 (79.28->82), cheese 2 (6.51->7.12) | +142 |
| Hanbrücken | 531 | 0.15 | 0.90 (96/turn) | timber 32 (8.45->13.11), charcoal 13 (2.01->3.93), hides 1 (11.03->11.88), nets 2 (38.4->38.95) | cloth 18 (8.93->10.1), salt 11 (4.37->5.56), furniture 1 (15.96->16.6) | +113 |
| Kirchwerp | 1072 | 0.39 | 0.40 (43/turn) | thread 87 (4.52->5.42), nets 6 (38.4->40.47), leather 1 (24.99->32.3), chisels 2 (9.29->11.69) | cloth 24 (8.45->10.1), salt 11 (4.73->5.56), garments 2 (24.57->26.8) | +105 |
| Clairlond | 1288 | 0.51 | 0.20 (21/turn) | garments 10 (26.2->35.15), nets 6 (38.4->41.42) | pasties 1 (6.04->16.43), cloth 4 (9.24->10.1), furniture 1 (13.23->16.6) | +102 |

**Best:** Grandgues at about +313 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 25.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 30 @ 2.2, stop - |  | goal planner: buys 30 for today's rates (v2 had 35) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 80.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.7k (cash + stock at home prices); +167/turn over 6 turns, +72/turn over 24 turns.
- Limits: cash flow >= -286/turn, prestige >= -0.36/turn (values are after 200 tax a turn).
- Today's settings: value +83/turn, cash +66/turn, prestige -1.94/turn - breaks the prestige floor.
- Plan: value +9/turn, cash +99/turn, prestige -0.36/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -17 vs +35, -269 vs +50, -527 vs +58 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +7/turn
  - ship Flax Wyrm -> Clairas: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - brewery 1 0.14 -> 0.20: -6/turn
  - ropewalk 1 0.25 -> 0.00: -7/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.19: +17/turn
  - weavery 1 0.50 -> 0.60: -9/turn
  - sewing shop 1 0.30 -> 0.36: +10/turn
  - spinnery 1 1.65 -> 1.05: -17/turn
  - retting pit 1 0.91 -> 0.60: +7/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +45/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.62, thread 4.07, cloth 6.50, flax fibres 4.82, garments 18.79, nets 29.26, beer 2.88, timber 3.22, prestige 61.48, cash 0.00
- Orders it would set: arms buy 1 (v2 None); beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 30 (v2 35); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.19, worth +9/turn.
- Ship linen snake: Grandgues -> Corstoft (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Clairas (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/77, thread 875/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.75 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
