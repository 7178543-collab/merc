# v2 shadow report

Turn 14140, 2026-11-19 13:07. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,680, prestige 3,648 (528 free, -1.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 47 | 12 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 47, buy 12, buy @ 3.62 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 501 | 0 | 63 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.78 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.78 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 63 labour expired last turn (~119 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.2 coin per prestige at mansion, vs 68.2 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 502, not 602
- labour expiry guard: 63 bought labour expired last turn, buy 2 (not 2) this turn

## Prestige spending, cheapest coin per prestige first

261 turns left: prestige gained now converts 73.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 47.3 | 47.6 | needs a arena (build cost 27,341); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 50.9 | 51.2 | needs a arena (build cost 27,341); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 53.4 | 54.0 | needs a arena (build cost 27,341); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 56.7 | 56.7 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 57.2 | 57.2 |  |
| hold banquet 4 (pies) | mansion | 18 | 57.9 | 57.9 | thin at home: hop beer, stockfish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 58.6 | 58.6 | thin at home: hop beer, cheese, pies |
| jousting 2 | arena | 210 | 58.5 | 59.1 | needs a arena (build cost 27,341); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.4 | 60.4 | thin at home: hop beer, stockfish, premium ham |
| hold banquet 2 (pies) | mansion | 7 | 61.2 | 61.2 | thin at home: cheese, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 61.4 | 61.4 | thin at home: hop beer, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 62.0 | 62.0 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 3 @ 24.6, pasties buy 12 @ 16.4; crew 0.1; est +29 a turn; stock: pasties 12 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.1 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Gotthafen +519, Cobholme +366, Fulkirch +317, Birkeningen +303, Brunnham +286
- Gotthafen would trade: cured meat buy 3 @ 23.8, furniture buy 44 @ 13.6, pasties buy 4 @ 15.1; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~122 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (122/turn) | timber 36 (8.56->12.54), thread 83 (5.5->6.6), bread 166 (3.28->3.76), charcoal 17 (2.52->5.03) | cheese 2 (6.77->8.6), garments 1 (33.39->34.2) | +348 |
| Fontaux | 411 | 0.13 | 1.00 (122/turn) | thread 92 (5.5->7.27), timber 40 (8.56->11.59), garments 10 (33.4->36.48), wine 20 (6.77->7.74) | cloth 13 (11.76->12.5), leather 1 (24.78->30.78), raw cloth 2 (11.03->14.25), cheese 3 (7.25->8.6) | +280 |
| Heidlowe | 662 | 0.21 | 0.30 (37/turn) | beer 65 (3.49->5.08), blades 1 (19.95->32.3), nets 1 (35.8->37.43) | tapestries 1 (661.5->703), cloth 24 (11.65->12.5), raw cloth 2 (9.77->14.25), yarn 10 (5.57->6.65) | +193 |
| Heilegg | 826 | 0.28 | 0.30 (37/turn) | coats 3 (92.92->114), casks 11 (6.67->9.17), wine 20 (6.77->7.84), varnish 9 (17.12->18.43) | cloth 24 (11.03->12.5), raw cloth 2 (9.97->14.25), cheese 3 (6.56->8.6), wax 5 (26.46->27.55) | +174 |
| Kirchwerp | 1072 | 0.44 | 0.30 (37/turn) | wine 20 (6.77->10.54), nails 16 (8.29->9.5), casks 11 (6.67->8.22), slaked lime 1 (6.93->12.35) | cloth 7 (10.4->12.5), flax fibres 20 (5.62->6.95), raw cloth 2 (9.45->14.25), garments 2 (29.82->34.2) | +151 |

**Best:** Grandgues at about +348 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 12 @ 3.48, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 47 = 4.0 turns |
| bread | 5 @ 3.2, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 76.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 17.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 32.4) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 34 |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 2) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.3k (cash + stock at home prices); +19/turn over 6 turns, +91/turn over 24 turns.
- Limits: cash flow >= -445/turn, prestige >= -0.95/turn (values are after 200 tax a turn).
- Today's settings: value -137/turn, cash -133/turn, prestige +0.95/turn.
- Plan: value +7/turn, cash +16/turn, prestige -0.95/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -319 vs -134, -29 vs -146, -113 vs -142.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +21/turn
  - ship Flax Wyrm -> Angefont: +2/turn
  - mansion 1 1.00 -> 0.55: +110/turn
  - brewery 1 0.14 -> 0.01: +17/turn
  - net maker 0.00 -> 0.28: +6/turn
  - spinnery 1 1.65 -> 1.40: -0/turn
  - retting pit 1 0.91 -> 0.79: +2/turn
  - flax farm 1 4.64 -> 3.99: +8/turn
  - weavery 1 0.50 -> 0.44: -10/turn
- Model check over the last 59 turns: predicted +59/turn for the settings we ran, real +55/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.82, beer 3.32, timber 3.62, prestige 63.80, cash 0.00
- Orders it would set: bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 2); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Ship linen snake: Grandgues -> Amsdermund (+12/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 84/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: bread slot dry: 0.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 3.2, home ask 3.12; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.78; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.6 for 3 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
