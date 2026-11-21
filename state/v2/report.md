# v2 shadow report

Turn 14192, 2026-11-21 17:01. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,685, prestige 3,711 (591 free, +0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 58 | 0 | 19 | 0 | 0 | min_holding 58, sell 15, sell @ 3.74 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 33 | 6 | 9 | 0 | 0 | stop 33, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 564 | 0 | 0 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.66 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Tuning

- **cured meat**: home ask 32.40 is above our ceiling 29.00 and last turn bought 8 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 61.8 coin per prestige at mansion, vs 77.4 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 114 over real use lately; planning 564, not 641

## Prestige spending, cheapest coin per prestige first

209 turns left: prestige gained now converts 65.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 51.0 | 51.5 | needs a arena (build cost 28,836); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.4 | 53.2 | needs a arena (build cost 28,836); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.9 | 55.4 | needs a arena (build cost 28,836); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.4 | 58.2 | needs a arena (build cost 28,836); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.4 | 60.4 | thin at home: stockfish, candles |
| hold banquet 4 (pies) | mansion | 18 | 60.7 | 60.7 | thin at home: stockfish, cheese, candles |
| maintain 1 | park | 0.5 | 61.2 | 61.2 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 61.8 | 61.8 |  |
| hold mass 2 (premium) | cathedral | 360 | 53.7 | 63.3 | needs a cathedral (build cost 311,560); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 65.7 | 65.7 | thin at home: stockfish, cheese, candles |
| hold banquet 3 (pies) | mansion | 8 | 66.3 | 66.3 | thin at home: cheese, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 69.1 | 69.1 | thin at home: cheese, pies, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 27.0; crew 0.1; est +22 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 14.5 (keep 14); best orders clear only 12 a turn after crew: ship stays at 0
- best towns now: Blanans +95, Heidlowe +78, Orlesailles +76, Rotterburg +70, Briclives +60
- Blanans would trade: cured meat buy 6 @ 27.6, furniture buy 4 @ 12.7, pasties buy 8 @ 16.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~128 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (128/turn) | bread 213 (2.9->3.61), firewood 32 (2.79->7.79), charcoal 15 (2.94->7.12), beer 105 (4.05->4.26) | fleece 5 (10.4->14.54), cured meat 5 (27.93->32.6), lathes 0 (212.1->235.6), cheese 6 (11.34->13.3) | +390 |
| Kirchwerp | 1072 | 0.46 | 0.70 (89/turn) | thread 91 (7->9.5), dyed cloth 17 (20.89->22.8), varnish 5 (17.12->20.9), casks 9 (6.83->9.36) | lathes 1 (189->235.6), cheese 8 (10.24->13.3), fleece 2 (10.92->14.54), garments 2 (28.98->31.8) | +340 |
| Heilegg | 826 | 0.29 | 1.00 (128/turn) | beer 97 (4.05->5.79), varnish 6 (17.12->22.99), charcoal 14 (2.94->6.74), arms 11 (31.92->33.25) | fleece 5 (9.19->14.54), cured meat 4 (31.08->32.6), garments 1 (29.82->31.8) | +243 |
| Amsdermund | 1111 | 0.48 | 0.30 (38/turn) | varnish 3 (17.12->20.52), canvas 1 (46.83->52.25), butter 1 (74.03->75.52) | dyed cloth 5 (9.97->18.81), lathes 1 (189->235.6), fleece 7 (9.35->14.54), cured meat 6 (26.25->32.6) | +225 |
| Rouhomme | 368 | 0.12 | 0.80 (102/turn) | bread 256 (2.9->3.78), rope 1 (86.5->94.52), chisels 1 (9.92->12.82), grain 2 (3.3->5.13) | fleece 6 (9.29->14.54), tools 15 (5.04->5.94), cheese 8 (12.5->13.3), garments 2 (29.4->31.8) | +202 |

**Best:** Grandgues at about +390 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| bread | 5 @ 2.82, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 72, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 2 = 0.3 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 31.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 64) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 44.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 84.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.3k (cash + stock at home prices); +213/turn over 6 turns, +109/turn over 24 turns.
- Limits: cash flow >= -362/turn, prestige >= -1.21/turn (values are after 200 tax a turn).
- Today's settings: value -149/turn, cash -160/turn, prestige +0.55/turn.
- Plan: value +21/turn, cash +26/turn, prestige -1.21/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -24 vs -189, +72 vs -191, +228 vs -186.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +5/turn
  - ship Flax Wyrm -> Blanans: +4/turn
  - mansion 1 1.00 -> 0.58: +125/turn
  - ropewalk 1 0.25 -> 0.15: +11/turn
  - spinnery 1 1.65 -> 1.23: +12/turn
  - retting pit 1 0.91 -> 0.78: +3/turn
  - flax farm 1 4.64 -> 3.94: +8/turn
  - net maker 0.00 -> 0.29: -4/turn
  - sewing shop 1 0.30 -> 0.24: -7/turn
  - weavery 1 0.50 -> 0.40: +8/turn
- Model check over the last 58 turns: predicted -128/turn for the settings we ran, real +36/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.62, beer 3.35, timber 3.71, prestige 67.53, cash 0.00
- Orders it would set: arms buy 1 (v2 None); bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); garments sell 11 (v2 10); grain buy 9 (v2 11); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Amsdermund (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1994 coin: +1/turn, payback 3152 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 418 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.12 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 123/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 0.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.82, home ask 2.76; our bid is already at/over the ask (sellers too thin)
