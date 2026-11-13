# v2 shadow report

Turn 13993, 2026-11-13 10:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 15,126, prestige 3,492 (372 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.80 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.80 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 608

## Prestige spending, cheapest coin per prestige first

408 turns left: prestige gained now converts 87.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.7 | 53.7 | running |
| jousting 3 | arena | 230 | 57.1 | 57.4 | needs a arena (build cost 26,973); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.1 | 58.1 | thin at home: hop beer, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.3 | 59.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.4 | 59.4 | thin at home: pasties, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 59.8 | 59.8 |  |
| hold banquet 3 (pies) | mansion | 8 | 59.8 | 59.8 | thin at home: pasties, hop beer, pies |
| hold banquet 4 (premium) | mansion | 20 | 59.9 | 59.9 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 61.4 | 61.4 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 61.5 | 61.5 | thin at home: hop beer, ham, stockfish |
| jousting 2 | arena | 210 | 62.5 | 62.9 | needs a arena (build cost 26,973); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 61.7 | 64.6 | needs a cathedral (build cost 308,840); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.7 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.7 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (98/turn) | timber 42 (7.88->12.35), firewood 48 (2.94->6.65), cured fish 7 (24.99->26.6), flax plants 1 (1.36->2.3) | tin ingots 3 (33.39->35.34), tools 9 (4.91->5.32) | +290 |
| Vauxvais | 204 | 0.06 | 1.00 (109/turn) | beer 62 (3.99->5.42), firewood 51 (2.94->5.7), charcoal 18 (2.39->4.01), malt 1 (8.45->14.06) | tin ingots 1 (32.13->35.34), tools 16 (5.15->5.32), copper ingots 2 (19.21->19.76), furniture 1 (13.97->15.5) | +166 |
| Etallaen | 774 | 0.23 | 0.30 (33/turn) | beer 62 (3.99->6.13), cloth 1 (7.85->9.12), tallow 2 (23.31->23.94) | thread 17 (4.73->5.55), copper ingots 2 (17.64->19.76), raw cloth 1 (6.72->7.17) | +119 |
| Hanstein | 380 | 0.11 | 0.40 (44/turn) | timber 14 (7.88->11.3), charcoal 17 (2.39->4.33), yarn 5 (4.85->5.32), slaked lime 1 (7.61->9.26) | thread 23 (4.89->5.55), seeds 19 (1.75->2.51), cloth 11 (7.3->8.15), candles 1 (81.38->88) | +88 |
| Donaunieder | 985 | 0.34 | 0.10 (11/turn) | cheese 9 (7.61->11.3), ham 1 (87.15->111.15), tin ingots 1 (39.48->39.9) | cloth 24 (7.19->8.15), premium steel 1 (39.69->45.79), candles 1 (82.95->88), copper ingots 2 (18.59->19.76) | +81 |

**Best:** Grandgues at about +290 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 2 @ 90, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.2) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.6) |
| pasties |  | 1 @ min 15.6 | goal planner: sells 1 a turn at 15.6, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 80.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.9k (cash + stock at home prices); +243/turn over 6 turns, +59/turn over 24 turns.
- Limits: cash flow >= -464/turn, prestige >= -0.30/turn (values are after 200 tax a turn).
- Today's settings: value +50/turn, cash +51/turn, prestige -2.57/turn - breaks the prestige floor.
- Plan: value -61/turn, cash -45/turn, prestige -0.30/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +138 vs +68, +229 vs +70, +190 vs +52.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +14/turn
  - brewery 1 0.14 -> 0.09: +11/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.30: -1/turn
  - retting pit 1 0.91 -> 0.82: +2/turn
  - flax farm 1 4.64 -> 4.14: -4/turn
  - weavery 1 0.50 -> 0.42: -11/turn
  - sewing shop 1 0.30 -> 0.25: -8/turn
  - mansion 1 0.00 -> 0.54: -107/turn
- Model check over the last 59 turns: predicted +106/turn for the settings we ran, real -17/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.18, beer 3.07, timber 3.38, prestige 65.66, cash 0.00
- Orders it would set: bread buy 5 (v2 7); candles buy 2 (v2 None); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Angefont (+14/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +0/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1923 coin: +2/turn, payback 1009 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.3/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 415 (+126 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.91 |
| ret | 3 | 0.91 | 0.78 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 138/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.8 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.86 (ask 3.8, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.8; ask over the cap 2.1 (60 coin per prestige)
