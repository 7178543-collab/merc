# v2 shadow report

Turn 14211, 2026-11-22 12:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,750, prestige 3,684 (564 free, -3.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 73 | 0 | 4 | 0 | 0 | min_holding 58, sell 15, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 19 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 529 | 0 | 35 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), but the home ask 33.00 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: home ask 2.48 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 35 labour expired last turn (~64 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 33.00 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 58.0 coin per prestige at mansion, vs 74.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 529, not 626
- labour expiry guard: 35 bought labour expired last turn, buy 29 (not 29) this turn

## Prestige spending, cheapest coin per prestige first

190 turns left: prestige gained now converts 61.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.1 | 50.0 | needs a arena (build cost 28,892); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 53.8 | 54.7 | needs a arena (build cost 28,892); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.9 | 54.9 | running |
| maintain 2 | park | 2 | 56.9 | 56.9 | thin at home: sculptures |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 |  |
| hold banquet 5 | mansion | 22 | 62.0 | 62.0 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 4 (pies) | mansion | 18 | 65.1 | 65.1 | thin at home: hop beer, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 65.3 | 65.3 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 66.1 | 66.1 |  |
| hold mass 2 (premium) | cathedral | 360 | 54.2 | 66.2 | needs a cathedral (build cost 303,960); thin at home: furniture, jewellery, glassware, windows, premium garments |
| hold banquet 4 (premium) | mansion | 20 | 66.5 | 66.5 | thin at home: hop beer, stockfish, premium cheese |
| hold mass 3 | cathedral | 460 | 58.3 | 67.7 | needs a cathedral (build cost 303,960); thin at home: coats, jewellery, glassware, candles, windows, sculptures, furniture, tapestries, books |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 15 @ 5.55, pasties buy 2 @ 16.4; crew 0.1; est +20 a turn; stock: pasties 2 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 12.7 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Bordetes +48, Rouhomme +25, Grandgues +20, Heilegg +18
- Bordetes would trade: beer sell 15 @ 7.1, pasties buy 2 @ 13.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (116/turn) | bread 233 (2.67->4.2), firewood 37 (2.1->11.97), timber 25 (9.29->12.06), beer 13 (3.32->5.75) | tapestries 0 (929.25->988), bricks 5 (8.45->10.45), flax fibres 3 (7.82->9.4), garments 1 (28.35->29.8) | +853 |
| Rouhomme | 368 | 0.11 | 0.90 (105/turn) | bread 280 (2.67->3.89), beer 16 (3.32->5.56), yarn 13 (4.91->5.89), seeds 8 (3.04->3.61) | bricks 11 (4.7->10.45), tools 18 (4.73->5.61), cheese 7 (9.35->10.83), dyed cloth 9 (14.7->15.39) | +368 |
| Vauxvais | 204 | 0.06 | 0.20 (23/turn) | yarn 19 (4.91->5.7), beer 16 (3.32->3.84), nets 6 (37.4->38.19), fleece 1 (7.77->8.55) | furniture 14 (9.55->15.58), flour 5 (15.23->22.23), bricks 4 (4.85->10.45), tackles 2 (163.8->171.95) | +195 |
| Amsdermund | 1111 | 0.44 | 0.60 (70/turn) | windows 2 (850.5->878.75), tallow 1 (24.78->43.51), casks 9 (6.83->9.03), nets 6 (37.4->39.9) | thread 54 (6.04->6.85), cheese 7 (8.09->10.83), dyed cloth 9 (13.86->15.39), wool 5 (9.13->11.21) | +182 |
| Kirchwerp | 1072 | 0.42 | 0.20 (23/turn) | swords 2 (258.3->286.9), arms 5 (35.07->40.28), nets 6 (37.4->40.09), varnish 2 (21.42->26.6) | cheese 7 (7.98->10.83), jewellery 2 (73.5->81.22), tools 18 (4.41->5.61), garments 2 (24.15->29.8) | +168 |

**Best:** Grandgues at about +853 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 10 @ min 3.38 | sell; ships offer 15 a turn abroad, so home sells 10 (was 15) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 1 @ 16.8, stop 150 |  | goal planner: buys 1 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 29) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 85.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 32.4k (cash + stock at home prices); +296/turn over 6 turns, +117/turn over 24 turns.
- Limits: cash flow >= -448/turn, prestige >= -1.10/turn (values are after 200 tax a turn).
- Today's settings: value -185/turn, cash -176/turn, prestige +1.07/turn.
- Plan: value -8/turn, cash +0/turn, prestige -1.10/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +193 vs -163, +131 vs -158, +224 vs -179.
- Route sales counted at most (what the ships really sold, a turn): beer 1.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +7/turn
  - ship Flax Wyrm -> Corstoft: +6/turn
  - mansion 1 1.00 -> 0.48: +161/turn
  - spinnery 1 1.65 -> 1.34: +10/turn
  - retting pit 1 0.91 -> 0.84: +0/turn
  - flax farm 1 4.64 -> 4.23: +3/turn
  - net maker 0.00 -> 0.29: -6/turn
  - sewing shop 1 0.30 -> 0.21: -16/turn
  - weavery 1 0.50 -> 0.35: +20/turn
- Model check over the last 59 turns: predicted -139/turn for the settings we ran, real +34/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.95, beer 3.29, timber 4.16, prestige 73.96, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 1 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 29); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Vauxvais (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Corstoft (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2008 coin: +4/turn, payback 522 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 88/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 33.0 -> **buy 12 @ 33.6 (ask 33.0, cap 42.0)** (ok)
- R5: tar buy not filling: bid 11 under the home ask 11.3 for 6 turns, bought 0.0 of 1, 0.1 held (0.5 turns); raise needs Taylor (ceiling 11.0)
