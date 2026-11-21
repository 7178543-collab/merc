# v2 shadow report

Turn 14186, 2026-11-21 11:31. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,819, prestige 3,721 (601 free, -3.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 59 | 0 | 4 | 0 | 0 | min_holding 58, sell 15, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 11 | 9 | 0 | 0 | stop 36, buy 10, buy @ 3.7 |
| labour | 64 | 64 | 515 | 0 | 49 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), but the home ask 30.40 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: home ask 2.74 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 49 labour expired last turn (~104 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 3.04 is above our ceiling 2.60 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **cured meat**: home ask 30.40 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 529, not 629
- labour expiry guard: 49 bought labour expired last turn, buy 16 (not 29) this turn

## Prestige spending, cheapest coin per prestige first

215 turns left: prestige gained now converts 66.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.0 | 52.7 | needs a arena (build cost 30,194); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 56.9 | 57.8 | needs a arena (build cost 30,194); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.9 | 60.9 | thin at home: hop beer, stockfish, candles |
| hold banquet 4 (pies) | mansion | 18 | 61.7 | 61.7 | thin at home: hop beer, stockfish, cheese, candles |
| hold mass 2 (premium) | cathedral | 360 | 53.6 | 62.9 | needs a cathedral (build cost 318,600); thin at home: furniture, jewellery, glassware, candles, premium garments |
| maintain 1 | park | 0.5 | 63.6 | 63.6 | running |
| hold banquet 3 (pies) | mansion | 8 | 66.6 | 66.6 | thin at home: hop beer, cheese, candles |
| hold banquet 4 | mansion | 17.5 | 66.9 | 66.9 | thin at home: hop beer, ham, stockfish, cheese, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 67.3 | 67.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 69.3 | 69.3 | thin at home: cheese, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 75.4 | 75.4 | running |
| jousting 1 | arena | 170 | 75.2 | 76.3 | needs a arena (build cost 30,194); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.0 (keep 14); best orders clear only -7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Blanans +92, Vauxvais +74, Boistot +70, Disscester +70, Kleinburgh +68
- Blanans would trade: furniture buy 7 @ 12.7, grain buy 8 @ 3.04, pasties buy 2 @ 16.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~130 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.60 (78/turn) | firewood 37 (2.88->7.12), charcoal 19 (2.44->7.17), thread 82 (6.7->7.03), lathes 1 (180.6->195.7) | tackles 1 (154.35->170.05) | +248 |
| Kirchwerp | 1072 | 0.47 | 0.60 (78/turn) | furniture 8 (16.38->24.89), thread 37 (6.7->8.41), casks 10 (6.51->9.36), glassware 5 (77.17->80.75) | cheese 8 (10.19->13.39), nails 6 (5.41->6.84), chisels 3 (8.4->9.69) | +226 |
| Heilegg | 826 | 0.30 | 0.70 (91/turn) | garments 10 (31->35.72), casks 10 (6.51->11.3), acid 1 (119.7->147.25), charcoal 19 (2.44->6.08) | - | +190 |
| Hanstein | 380 | 0.13 | 0.20 (26/turn) | charcoal 18 (2.44->4.18), nets 1 (45.8->52.25), cookware 4 (25.2->26.22), rope 1 (84->86.92) | thread 51 (5.1->6.85), cheese 8 (8.77->13.39), yarn 28 (5.72->6.27), flax fibres 5 (6.46->8.15) | +172 |
| Calange | 218 | 0.08 | 0.10 (13/turn) | swords 2 (233.1->288.8), garments 10 (31->36.48), cloth 1 (9.9->10.36) | cheese 8 (13.12->13.39), grain 8 (3.44->3.8), seeds 5 (1.94->2.3), chisels 1 (9.55->9.69) | +161 |

**Best:** Grandgues at about +248 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.88 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 4) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 29.0, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| furniture | 2 @ 16, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.2) |
| grain | 10 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 35 = 3.9 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 16) |
| light armour | 1 @ 112, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 44.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 81.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.3 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.0k (cash + stock at home prices); +163/turn over 6 turns, +77/turn over 24 turns.
- Limits: cash flow >= -326/turn, prestige >= -1.26/turn (values are after 200 tax a turn).
- Today's settings: value -181/turn, cash -201/turn, prestige +0.52/turn.
- Plan: value +13/turn, cash +17/turn, prestige -1.26/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -212 vs -179, +137 vs -183, +266 vs -192.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Blanans: +3/turn
  - ship Flax Wyrm -> Magdeach: +1/turn
  - mansion 1 1.00 -> 0.58: +133/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +9/turn
  - spinnery 1 1.65 -> 1.18: +25/turn
  - retting pit 1 0.91 -> 0.75: +3/turn
  - flax farm 1 4.64 -> 3.77: +7/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.09: -1/turn
  - weavery 1 0.50 -> 0.41: -13/turn
- Model check over the last 59 turns: predicted -129/turn for the settings we ran, real -1/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.59, beer 3.56, timber 3.77, prestige 71.20, cash 0.00
- Orders it would set: bread buy 5 (v2 4); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 4 (v2 12); firewood buy 4 (v2 8); fish buy 0 (v2 None); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 16); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.24, worth +14/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.09, worth +2/turn.
- Ship linen snake: Grandgues -> Blanans (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Magdeach (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2047 coin: +2/turn, payback 830 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 132/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 0.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 3.04 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.1 (ask 3.04, cap 4.3))
- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 29, home ask 30.4 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 31 (ask 30.4, cap 42.0))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R1: prestige rate -3.68 a turn vs 12-turn median -0.98; likely: dry slot: bread, cured meat, fish; mansion 1 projected 0 (cured meat)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 12.4 for 6 turns, bought 0.0 of 1, 0.3 held (1.3 turns); raise needs Taylor (ceiling 11.0)
