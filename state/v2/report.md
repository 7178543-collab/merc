# v2 shadow report

Turn 13776, 2026-11-04 09:02. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,895, prestige 3,225 (105 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 6 | 0 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 29, short of ~135 needed -> v2: buy 135

## Prestige spending, cheapest coin per prestige first

625 turns left: prestige gained now converts 95.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.7 | 49.7 | thin at home: hop beer, stockfish, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.4 | 51.4 | thin at home: pies |
| hold banquet 4 | mansion | 17.5 | 52.8 | 52.8 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 53.2 | 53.2 | thin at home: hop beer, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 53.5 | 53.5 |  |
| jousting 3 | arena | 230 | 53.4 | 53.6 | needs a arena (build cost 25,284); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 53.7 | 53.7 | thin at home: hop beer, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 54.1 | 54.1 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 56.9 | 56.9 | thin at home: hop beer |
| jousting 2 | arena | 210 | 58.5 | 58.7 | needs a arena (build cost 25,284); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 59.5 | 59.5 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 19 | 134102075 | 0.332 | - | furniture 20, pasties 1 | -277 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 7 @ 14.6, pasties buy 2 @ 13.7; crew 0.1; est +83 a turn; stock: furniture 7 @ 14.6 (keep 145); stock: pasties 2 @ 13.7 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 13.9 (keep 14); best orders clear only 0 a turn after crew: ship stays at 0
- best towns now: Chatgnan +97, Toqueque +94, Clairlond +93, Donaunieder +89, Neuborn +89
- Chatgnan would trade: furniture buy 7 @ 12.4, pasties buy 2 @ 14.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (49/turn) | charcoal 19 (2.35->6.98), bread 153 (2.18->2.66), timber 25 (6.98->8.88), wine 12 (5.99->6.7) | bricks 5 (6.46->9.07), cloth 7 (7.67->8.2), leather 1 (26.88->27.36) | +203 |
| Chatgnan | 728 | 0.19 | 0.10 (10/turn) | raw cloth 9 (7.04->7.89), bellows 1 (204.75->207.1), premium cheese 1 (26.46->27.17), cloth 1 (6.22->6.74) | tapestries 1 (567->655.5), cloth 24 (7.67->8.2), garments 2 (21.42->25), furniture 1 (12.81->15.2) | +115 |
| Fontaux | 411 | 0.11 | 1.00 (99/turn) | charcoal 17 (2.35->6.22), bread 143 (2.18->2.66), timber 16 (6.98->9.79), beer 15 (2.66->3.25) | mouldboards 1 (30.24->37.62), cloth 8 (7.77->8.2), leather 1 (26.04->27.36) | +110 |
| Bordetes | 831 | 0.23 | 0.50 (49/turn) | charcoal 19 (2.35->6.41), bellows 1 (204.75->212.8), premium cheese 1 (26.46->27.36), beer 15 (2.66->3.13) | cloth 24 (7.25->8.2), garments 2 (20.37->25), dyed cloth 1 (10.5->10.92) | +77 |
| Hanstein | 380 | 0.10 | 0.50 (49/turn) | timber 14 (6.98->10.26), salt 8 (5.99->8.26), charcoal 15 (2.35->3.36), cloth 1 (6.22->7.65) | tackles 2 (177.45->186.2), garments 2 (22.05->25), bricks 5 (6.46->9.07) | +75 |

**Best:** Grandgues at about +203 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 7.1 | goal planner: sells 1 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 23.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 30 @ 2.2, stop - |  | goal planner: buys 30 for today's rates (v2 had 135) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 78.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 19.7k (cash + stock at home prices); -121/turn over 6 turns, +90/turn over 24 turns.
- Limits: cash flow >= -121/turn, prestige >= +8.11/turn (values are after 200 tax a turn).
- Today's settings: value +114/turn, cash +106/turn, prestige -0.93/turn - breaks the prestige floor.
- Plan: value -114/turn, cash -102/turn, prestige +3.27/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -116 vs +88, +13 vs +96, -121 vs +99 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Chatgnan: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - flax farm 1 4.64 -> 4.16: +0/turn
  - retting pit 1 0.91 -> 0.85: -1/turn
  - spinnery 1 1.65 -> 1.50: +3/turn
  - ropewalk 1 0.25 -> 0.00: -4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.22: +11/turn
  - sewing shop 1 0.30 -> 0.36: -4/turn
  - weavery 1 0.50 -> 0.61: +7/turn
- Model check over the last 59 turns: predicted +83/turn for the settings we ran, real +85/turn.
- Worth of one more unit per turn: labour 1.59, thread 3.99, cloth 6.38, flax fibres 4.73, garments 18.45, nets 28.82, beer 2.85, timber 2.99, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 30 (v2 135); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.22, worth +11/turn.
- Ship linen snake: Grandgues -> Chatgnan (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 477 (+188 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.84 |
| ret | 3 | 0.91 | 1.17 |
| spin | 4 | 1.65 | 2.06 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 357/228, cloth 78/128

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 26.4, home ask 29.6 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 1 @ 30.2 (ask 29.6, cap 48.0))
