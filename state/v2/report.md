# v2 shadow report

Turn 13996, 2026-11-13 13:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 15,128, prestige 3,485 (365 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 39 | 0 | 0 | 15 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 511 | 0 | 53 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.52 is above it); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.52 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 53 labour expired last turn (~98 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 546, not 646
- labour expiry guard: 53 bought labour expired last turn, buy 11 (not 46) this turn

## Prestige spending, cheapest coin per prestige first

405 turns left: prestige gained now converts 86.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 54.6 | 54.6 | running |
| jousting 3 | arena | 230 | 55.6 | 55.9 | needs a arena (build cost 27,812); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 60.2 | 60.2 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.4 | 60.4 | thin at home: cured fish, cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.2 | 61.2 | thin at home: cheese, pies, candles |
| jousting 2 | arena | 210 | 60.9 | 61.2 | needs a arena (build cost 27,812); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 62.2 | 62.2 | thin at home: hop beer, ham, stockfish, pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 62.5 | 62.5 | thin at home: hop beer, ham, stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 61.4 | 64.4 | needs a cathedral (build cost 310,170); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 65.4 | 65.4 | thin at home: hop beer, pies, candles |
| hold banquet 4 | mansion | 17.5 | 65.8 | 65.8 | thin at home: hop beer, ham, stockfish, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 66.1 | 66.1 | thin at home: hop beer, cured fish, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.5 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.5 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~112 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (112/turn) | timber 40 (8.45->12.54), firewood 48 (2.65->6.65), windows 1 (787.5->817), charcoal 18 (2.33->3.76) | ham 2 (101.85->106.4), tar 5 (10.03->11.4), cured meat 1 (24.57->29.07), tools 8 (4.91->5.37) | +329 |
| Vauxvais | 204 | 0.06 | 1.00 (112/turn) | beer 59 (3.99->5.22), firewood 51 (2.65->5.7), charcoal 18 (2.33->4.29), premium cheese 1 (30.24->33.82) | ham 1 (89.25->106.4), cloth 13 (8.14->8.65), cured meat 1 (25.83->29.07), seeds 6 (1.92->2.51) | +195 |
| Herschweig | 775 | 0.23 | 0.30 (34/turn) | beer 63 (3.99->6.41), wrought iron 3 (17.96->18.43), wine 2 (7.46->7.84) | ham 2 (90.83->106.4), lathes 1 (182.7->195.7), cloth 24 (8.09->8.65), cookware 4 (23.94->25.46) | +185 |
| Amsdermund | 1111 | 0.43 | 0.30 (34/turn) | wine 16 (7.46->9.59), hides 3 (13.33->18.81), nets 6 (38->40.66), honey 6 (8.14->9.4) | ham 2 (85.58->106.4), cloth 23 (7.56->8.65), casks 17 (5.78->7.03), cookware 4 (24.15->25.46) | +128 |
| Hanstein | 380 | 0.11 | 0.40 (45/turn) | charcoal 17 (2.33->4.52), timber 14 (8.45->11.59), garments 10 (23->23.94), slaked lime 2 (7.61->8.79) | ham 2 (92.92->106.4), grain 85 (2.52->2.85), seeds 18 (1.77->2.51), cloth 13 (8.03->8.65) | +124 |

**Best:** Grandgues at about +329 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 37.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 26 @ 3.98, stop 60 | off | a building is stalled on beer: no sell until it runs again |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| candles | 2 @ 76.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 4 @ 32.8, stop 13 |  | goal planner: buys 4 a turn for today's rates, keeps up to 13 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.4) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 11) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.0) |
| pasties |  | 1 @ min 17.2 | goal planner: sells 1 a turn at 17.2, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 2.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.4k (cash + stock at home prices); +189/turn over 6 turns, +82/turn over 24 turns.
- Limits: cash flow >= -464/turn, prestige >= -0.27/turn (values are after 200 tax a turn).
- Today's settings: value -238/turn, cash -157/turn, prestige +1.67/turn.
- Plan: value -54/turn, cash -38/turn, prestige -0.27/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +127 vs +51, +29 vs -126, -154 vs -144.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +2/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.54: +155/turn
  - brewery 1 0.14 -> 0.09: +11/turn
  - spinnery 1 1.65 -> 1.35: +5/turn
  - retting pit 1 0.91 -> 0.85: +2/turn
  - flax farm 1 4.64 -> 4.27: +3/turn
  - net maker 0.00 -> 0.29: +1/turn
  - weavery 1 0.50 -> 0.38: -7/turn
  - sewing shop 1 0.30 -> 0.22: +10/turn
- Model check over the last 60 turns: predicted +93/turn for the settings we ran, real +27/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.27, beer 3.15, timber 3.41, prestige 70.80, cash 0.00
- Orders it would set: bread buy 5 (v2 6); candles buy 2 (v2 None); cured meat buy 4 (v2 None); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 64 (v2 11); light armour buy 1 (v2 None); pasties sell 1 (v2 none); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +9/turn.
- Ship linen snake: Grandgues -> Vauxvais (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1982 coin: +4/turn, payback 444 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 416 (+127 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.00 |
| ret | 3 | 0.91 | 0.80 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 131/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: cured meat slot dry: 6.2 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 32.8, home ask 32.0; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.52; ask over the cap 2.1 (60 coin per prestige)
