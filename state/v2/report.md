# v2 shadow report

Turn 14206, 2026-11-22 07:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,628, prestige 3,701 (581 free, -3.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 115 | 0 | 4 | 0 | 0 | min_holding 58, sell 16, sell @ 3.52 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 23 | 9 | 9 | 0 | 0 | stop 29, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 534 | 0 | 30 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), but the home ask 31.80 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 3 (need 12) -> v2: buy 12

## Waste (money lost now)

- **labour**: 30 labour expired last turn (~58 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.74 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **cured meat**: home ask 31.80 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 62.0 coin per prestige at mansion, vs 73.9 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 534, not 634
- labour expiry guard: 30 bought labour expired last turn, buy 34 (not 34) this turn

## Prestige spending, cheapest coin per prestige first

195 turns left: prestige gained now converts 62.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.2 | 50.7 | needs a arena (build cost 28,152); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 50.2 | 51.0 | needs a arena (build cost 28,152); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.9 | 54.4 | needs a arena (build cost 28,152); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.9 | 55.8 | needs a arena (build cost 28,152); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 57.9 | 57.9 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 62.0 | 62.0 |  |
| hold banquet 4 (pies) | mansion | 18 | 62.8 | 62.8 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 53.6 | 64.5 | needs a cathedral (build cost 297,460); thin at home: furniture, jewellery, glassware, windows, premium garments |
| hold banquet 4 (premium) | mansion | 20 | 64.6 | 64.6 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 2 (pies) | mansion | 7 | 66.7 | 66.7 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 67.2 | 67.2 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 67.7 | 67.7 | thin at home: wine, hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 12 | 151802239 | 0 | beer 20 | pasties 2 | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.0 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 12 a turn after crew: ship stays at 0
- best towns now: Heidlowe +45, Hofkirchen +44, Bordetes +40, Chatgnan +35, Clairas +32
- Heidlowe would trade: beer sell 19 @ 5.55, pasties buy 5 @ 13.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~123 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (123/turn) | firewood 30 (2.23->11.21), bread 269 (2.88->3.76), timber 24 (9.29->11.69), beer 17 (3.63->5.03) | cloth 4 (6.88->12.4), bricks 6 (6.98->9.31), garments 1 (28.35->30.2), coats 0 (74.55->77.9) | +571 |
| Rouhomme | 368 | 0.12 | 0.90 (111/turn) | bread 296 (2.88->4.6), rope 1 (87.5->92.15), grain 1 (3.1->3.93), resin 3 (2.42->2.93) | tools 16 (4.73->6.17), bricks 10 (5.25->9.31), cloth 24 (11.76->12.4) | +458 |
| Heilegg | 826 | 0.28 | 0.40 (49/turn) | nets 6 (38.6->48.92), beer 19 (3.63->5.32), cured fish 9 (26.88->28.5), salt 3 (6.3->8.98) | cloth 24 (9.66->12.4), thread 58 (6.2->6.9), tools 16 (5.04->6.17) | +227 |
| Kirchwerp | 1072 | 0.44 | 0.50 (62/turn) | glassware 6 (77.17->87.88), nets 6 (38.6->43.89), honey 5 (9.03->13.21), cloth 23 (13.02->14.25) | tools 16 (4.41->6.17), garments 2 (24.15->30.2), cookware 6 (21->22.99), raw cloth 4 (8.87->10.73) | +204 |
| Amsdermund | 1111 | 0.47 | 0.40 (49/turn) | furniture 10 (14.6->18.81), nets 4 (38.6->45.03), varnish 1 (21->25.08), acid 1 (139.65->142.5) | cloth 24 (10.19->12.4), wool 11 (8.61->11.78), tools 16 (5.04->6.17), garments 2 (25.2->30.2) | +153 |

**Best:** Grandgues at about +571 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 19 @ min 3.38 | makes 19.3, uses 4.2, holds 115 (keeps 58): sells the surplus + 3/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| candles | 2 @ 82, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 2 @ 14.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.2) |
| grain | 7 @ 3.7, stop 27 |  | goal planner: buys 7 a turn for today's rates, keeps up to 27 (v2 had 16) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 34) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 37.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.9k (cash + stock at home prices); +50/turn over 6 turns, +111/turn over 24 turns.
- Limits: cash flow >= -401/turn, prestige >= -1.17/turn (values are after 200 tax a turn).
- Today's settings: value -167/turn, cash -142/turn, prestige +0.98/turn.
- Plan: value +12/turn, cash +32/turn, prestige -1.17/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +159 vs -178, +121 vs -170, +207 vs -150.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Chatgnan: +6/turn
  - ship Flax Wyrm -> Blanans: +0/turn
  - mansion 1 1.00 -> 0.49: +157/turn
  - spinnery 1 1.65 -> 1.34: +9/turn
  - retting pit 1 0.91 -> 0.85: +2/turn
  - flax farm 1 4.64 -> 4.25: +3/turn
  - net maker 0.00 -> 0.29: -4/turn
  - sewing shop 1 0.30 -> 0.23: -9/turn
  - weavery 1 0.50 -> 0.38: +19/turn
- Model check over the last 59 turns: predicted -135/turn for the settings we ran, real +39/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.93, beer 3.32, timber 3.69, prestige 72.37, cash 0.00
- Orders it would set: bread buy 5 (v2 6); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 7 (v2 16); labour buy 64 (v2 34); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Chatgnan (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1990 coin: +3/turn, payback 652 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 424 (+135 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.42 |
| ret | 3 | 0.91 | 0.88 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 101/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 31.8 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 32.4 (ask 31.8, cap 42.0))
- R1: prestige rate -3.22 a turn vs 12-turn median +0.51; likely: dry slot: cured meat; mansion 1 projected 0 (cured meat)
- R5: tar buy not filling: bid 11 under the home ask 11.4 for 5 turns, bought 0.0 of 1, 0.5 held (1.5 turns); raise needs Taylor (ceiling 11.0)
