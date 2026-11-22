# v2 shadow report

Turn 14210, 2026-11-22 11:41. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,527, prestige 3,687 (567 free, -3.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 73 | 0 | 4 | 0 | 0 | min_holding 58, sell 11, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 19 | 8 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 534 | 0 | 30 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), but the home ask 33.20 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 4 (need 12) -> v2: buy 12

## Waste (money lost now)

- **labour**: 30 labour expired last turn (~56 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 33.20 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.0 coin per prestige at mansion, vs 73.4 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 534, not 634
- labour expiry guard: 30 bought labour expired last turn, buy 34 (not 34) this turn

## Prestige spending, cheapest coin per prestige first

191 turns left: prestige gained now converts 61.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.8 | 50.6 | needs a arena (build cost 27,878); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.5 | 55.4 | needs a arena (build cost 27,878); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 55.8 | 55.8 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 57.0 | 57.0 |  |
| hold banquet 4 (pies) | mansion | 18 | 63.2 | 63.2 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 63.5 | 63.5 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 64.8 | 64.8 | thin at home: hop beer, stockfish, premium cheese |
| hold mass 2 (premium) | cathedral | 360 | 53.3 | 65.0 | needs a cathedral (build cost 298,245); thin at home: furniture, jewellery, glassware, windows, premium garments |
| hold banquet 2 (pies) | mansion | 7 | 65.5 | 65.5 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 65.6 | 65.6 |  |
| hold mass 3 | cathedral | 460 | 58.3 | 67.4 | needs a cathedral (build cost 298,245); thin at home: coats, jewellery, glassware, candles, windows, sculptures, furniture, tapestries, books |
| hold banquet 4 | mansion | 17.5 | 67.8 | 67.8 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0 | beer 17 | pasties 7 | -76 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 13.0 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 12 a turn after crew: ship stays at 0
- best towns now: Bordetes +41, Heilegg +27
- Bordetes would trade: beer sell 15 @ 6.95, pasties buy 1 @ 13.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~118 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (118/turn) | firewood 38 (2.12->11.97), bread 221 (2.62->4.2), timber 25 (9.03->12.06), beer 13 (3.54->5.61) | bricks 6 (7.98->10.54), dyed cloth 5 (14.7->15.48), garments 1 (28.35->29.8), salt 0 (4.75->5.56) | +786 |
| Rouhomme | 368 | 0.12 | 0.90 (106/turn) | bread 266 (2.62->4.14), yarn 11 (4.62->5.89), nets 6 (37.4->39.33), grain 1 (2.26->5.22) | bricks 9 (4.75->10.54), cheese 7 (8.29->10.83), tools 17 (4.73->5.79), garments 2 (29.4->29.8) | +406 |
| Heilegg | 826 | 0.27 | 0.30 (35/turn) | yarn 28 (4.62->6.93), cured fish 13 (23.94->28.12), nets 6 (37.4->45.03), beer 16 (3.54->5.94) | cloth 24 (10.5->11.4), tools 17 (5.04->5.79), garments 2 (26.25->29.8), thread 22 (6.3->6.8) | +261 |
| Kirchwerp | 1072 | 0.42 | 0.30 (35/turn) | windows 2 (850.5->902.5), arms 5 (34.44->40.28), varnish 2 (21.42->26.6), honey 4 (9.4->12.16) | tools 17 (4.41->5.79), garments 2 (24.15->29.8), acid 1 (141.75->146.3), chisels 2 (8.4->9.69) | +188 |
| Brunnham | 1281 | 0.56 | 0.40 (47/turn) | nets 6 (37.4->44.84), cured fish 13 (23.94->26.98) | cloth 24 (8.87->11.4), thread 33 (5.41->6.8), acid 1 (135.45->146.3), garments 2 (27.3->29.8) | +161 |

**Best:** Grandgues at about +786 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.38 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 9) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 34) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 85.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 32.1k (cash + stock at home prices); +249/turn over 6 turns, +128/turn over 24 turns.
- Limits: cash flow >= -439/turn, prestige >= -1.11/turn (values are after 200 tax a turn).
- Today's settings: value -188/turn, cash -179/turn, prestige +1.05/turn.
- Plan: value -6/turn, cash +3/turn, prestige -1.11/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +221 vs -156, +193 vs -163, +131 vs -158.
- Route sales counted at most (what the ships really sold, a turn): beer 0.7.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +6/turn
  - ship Flax Wyrm -> Dortdorf: +4/turn
  - mansion 1 1.00 -> 0.48: +162/turn
  - spinnery 1 1.65 -> 1.33: +9/turn
  - retting pit 1 0.91 -> 0.83: +0/turn
  - flax farm 1 4.64 -> 4.20: +3/turn
  - net maker 0.00 -> 0.29: -4/turn
  - sewing shop 1 0.30 -> 0.22: -14/turn
  - weavery 1 0.50 -> 0.36: +21/turn
- Model check over the last 59 turns: predicted -138/turn for the settings we ran, real +24/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.91, beer 3.28, timber 3.69, prestige 74.22, cash 0.00
- Orders it would set: bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 34); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Vauxvais (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Dortdorf (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1962 coin: +4/turn, payback 493 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 91/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 33.2 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 33.8 (ask 33.2, cap 42.0))
- R5: tar buy not filling: bid 11 under the home ask 11.3 for 6 turns, bought 0.0 of 1, 0.4 held (1.3 turns); raise needs Taylor (ceiling 11.0)
