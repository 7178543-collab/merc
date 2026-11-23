# v2 shadow report

Turn 14223, 2026-11-23 00:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,470, prestige 3,681 (561 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 68 | 0 | 12 | 0 | 0 | min_holding 58, sell 10, sell @ 4.18 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 20 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 551 | 0 | 13 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (12 @ 32.8), but the home ask 33.40 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **cured meat**: home ask 33.40 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 60.0 coin per prestige at mansion, vs 74.9 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 103 over real use lately; planning 551, not 646

## Prestige spending, cheapest coin per prestige first

178 turns left: prestige gained now converts 59.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.0 | 49.5 | needs a arena (build cost 26,636); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| jousting 3 | arena | 230 | 49.8 | 50.7 | needs a arena (build cost 26,636); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 52.6 | 53.1 | needs a arena (build cost 26,636); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.5 | 55.5 | needs a arena (build cost 26,636); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 60.0 | 60.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 61.2 | 61.2 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 63.6 | 63.6 | thin at home: wine, pies |
| hold banquet 4 (pies) | mansion | 18 | 63.9 | 63.9 | thin at home: hop beer, wine, stockfish |
| hold banquet 5 | mansion | 22 | 64.7 | 64.7 | thin at home: hop beer, wine, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 66.0 | 66.0 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 | mansion | 17.5 | 67.3 | 67.3 | thin at home: wine, hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | beer 8 | - | 39 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: cured meat buy 3 @ 29.4, pasties buy 8 @ 16.4; crew 0.1; est +22 a turn; stock: pasties 8 @ 16.4 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 14 a turn after crew: ship stays at 0
- best towns now: Bedenis +109, Chatgnan +106, Donaunieder +98, Clairlond +96, Großmühle +92
- Bedenis would trade: cured meat buy 3 @ 31.4, furniture buy 6 @ 13.8, pasties buy 8 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kleinburgh | 1440 | 0.58 | 0.30 (32/turn) | nets 2 (37.4->44.84), tools 16 (6.46->7.31), honey 1 (9.4->13.3) | sculptures 1 (1848->2603), tin ingots 4 (34.02->35.34), dyed cloth 3 (14.38->15.2), steel ingots 1 (18.27->19.38) | +762 |
| Grandgues | 152 | 0.04 | 1.00 (105/turn) | firewood 34 (2.35->9.88), thread 82 (6.05->7.03), glassware 4 (77.17->93.57), bread 206 (2.42->2.75) | bricks 9 (7.3->10.36), furniture 0 (15.86->16.9), lathes 0 (205.8->207.1), leather 0 (29.61->30.59) | +581 |
| Hofkirchen | 991 | 0.33 | 0.30 (32/turn) | nets 6 (37.4->44.84), wheels 3 (24.57->37.05), glass ingots 1 (63->74.58), resin 2 (2.9->7.84) | jewellery 4 (73.5->80.75), dyed cloth 5 (9.97->15.2), cured meat 3 (29.82->33.4), cloth 24 (9.61->10.2) | +184 |
| Kirchwerp | 1072 | 0.38 | 0.30 (32/turn) | glass ingots 1 (63->114), ploughs 1 (85.05->99.75), flax fibres 7 (7.98->9.31), honey 1 (9.4->13.21) | lathes 2 (189->207.1), jewellery 4 (73.5->80.75), tools 18 (4.3->5.61), cured meat 3 (30.45->33.4) | +172 |
| Darmwald | 1022 | 0.35 | 0.70 (74/turn) | charcoal 20 (2.31->7.41), nets 3 (37.4->45.41), ploughs 1 (85.05->103.55), rope 1 (89.5->95.95) | cured meat 3 (23.1->33.4), flax fibres 13 (5.62->7.6), jewellery 4 (77.7->80.75), tin ingots 2 (32.97->35.34) | +157 |

**Best:** Kleinburgh at about +762 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.88 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 81, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.0) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 51) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 87.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.4k (cash + stock at home prices); -119/turn over 6 turns, +40/turn over 24 turns.
- Limits: cash flow >= -436/turn, prestige >= -1.09/turn (values are after 200 tax a turn).
- Today's settings: value -163/turn, cash -165/turn, prestige +1.39/turn.
- Plan: value +37/turn, cash +38/turn, prestige -1.09/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +90 vs -176, +24 vs -190, +93 vs -184.
- Route sales counted at most (what the ships really sold, a turn): beer 1.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Darmwald: +23/turn
  - ship Flax Wyrm -> Grandgues: -0/turn
  - mansion 1 1.00 -> 0.41: +180/turn
  - net maker 0.00 -> 0.29: +9/turn
  - spinnery 1 1.65 -> 1.56: +4/turn
  - flax farm 1 4.64 -> 4.78: -1/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +16/turn
- Model check over the last 59 turns: predicted -151/turn for the settings we ran, real +67/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.65, thread 4.15, cloth 6.62, flax fibres 4.92, garments 19.16, nets 30.43, beer 2.96, timber 3.51, prestige 68.64, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 51); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Darmwald (+17/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1875 coin: +4/turn, payback 525 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 86/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: cured meat slot dry: 3.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 12 @ 32.8, home ask 33.4 (held back: acted on cured meat at turn 14222 (one action per 2 turns))
