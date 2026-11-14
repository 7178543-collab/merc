# v2 shadow report

Turn 14010, 2026-11-14 03:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,915, prestige 3,512 (392 free, +0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 28 | 14 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 32, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 539 | 0 | 25 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 32.8), 4 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 25 labour expired last turn (~47 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 98 over real use lately; planning 552, not 651

## Prestige spending, cheapest coin per prestige first

391 turns left: prestige gained now converts 85.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 56.7 | 56.7 | running |
| jousting 3 | arena | 230 | 57.8 | 58.2 | needs a arena (build cost 29,693); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 59.4 | 59.4 | thin at home: pasties |
| hold banquet 1 (fish) | mansion | 4.2 | 59.6 | 59.6 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.7 | 59.7 |  |
| hold banquet 4 (pies) | mansion | 18 | 62.3 | 62.3 | thin at home: hop beer, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 59.5 | 62.4 | needs a cathedral (build cost 282,560); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 (premium) | mansion | 20 | 62.6 | 62.6 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 63.4 | 63.4 | thin at home: pasties, hop beer |
| jousting 2 | arena | 210 | 63.3 | 63.7 | needs a arena (build cost 29,693); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 65.2 | 65.2 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 65.3 | 65.3 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.084 | - | cured meat 6, pasties 1 | -155 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.1 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Heidlowe +26, Gottweiler +21, Orlesailles +20, Hofkirchen +20, Neuborn +18
- Heidlowe would trade: cured meat buy 4 @ 21.0, pasties buy 4 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.06 | 0.10 (12/turn) | beer 3 (3.66->4.14), casks 9 (6.88->7.12), hides 2 (13.33->13.77) | windows 1 (609->788.5), furniture 17 (15.86->17.29), seeds 9 (2.16->2.58), cured meat 4 (26.04->26.6) | +204 |
| Grandgues | 152 | 0.05 | 0.70 (81/turn) | timber 32 (8.14->12.06), firewood 35 (3.46->5.37), tapestries 1 (603.75->617.5), pasties 2 (14.18->15.58) | cloth 10 (7.93->9), cured meat 4 (24.15->26.6), candles 1 (84.53->88.5) | +156 |
| Chatgnan | 728 | 0.23 | 0.20 (23/turn) | tapestries 1 (603.75->650.75), ham 1 (89.25->118.75), yarn 5 (4.85->5.22) | bellows 1 (241.5->285), furniture 17 (15.44->17.29), ploughs 1 (72.98->83.12), candles 1 (84->88.5) | +153 |
| Marmont | 638 | 0.20 | 0.10 (12/turn) | cheese 6 (7.51->9.97), thread 7 (4.72->5.08), dyed yarn 1 (5.08->5.37) | sails 1 (840->969), tallow 1 (18.79->23.75), bellows 1 (283.5->285), candles 1 (87.15->88.5) | +146 |
| Coburgbaum | 619 | 0.19 | 0.90 (105/turn) | bread 152 (2.62->3.72), premium cheese 2 (30.45->33.06), hides 2 (13.33->15.86), wine 13 (6.51->6.93) | cloth 12 (7.77->9), cured meat 4 (23.52->26.6), candles 1 (86.1->88.5), salt 3 (4.51->4.94) | +114 |

**Best:** Vauxvais at about +204 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 15 @ 3.88, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 108 = 7.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 | off | a building is stalled on cured meat: no sell until it runs again |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.5 | goal planner: sells 2 a turn at 5.5, keeps 85 (no one offered it) |
| furniture | 2 @ 16.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.0) |
| grain | 9 @ 3.7, stop 33 |  | goal planner: buys 9 a turn for today's rates, keeps up to 33 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 52) |
| light armour | 1 @ 97.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.4) |
| pasties |  | 1 @ min 13.3 | goal planner: trial sale of an idle pile, 1 a turn at 13.3, keeps 0 (10 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 1.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.3k (cash + stock at home prices); -136/turn over 6 turns, -7/turn over 24 turns.
- Limits: cash flow >= -371/turn, prestige >= -0.38/turn (values are after 200 tax a turn).
- Today's settings: value -186/turn, cash -168/turn, prestige +2.05/turn.
- Plan: value -17/turn, cash -13/turn, prestige -0.38/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -102 vs -167, -105 vs -161, -237 vs -161.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship Flax Wyrm -> Neuborn: +4/turn
  - mansion 1 1.00 -> 0.42: +152/turn
  - spinnery 1 1.65 -> 1.35: +3/turn
  - retting pit 1 0.91 -> 0.84: +3/turn
  - flax farm 1 4.64 -> 4.21: +4/turn
  - net maker 0.00 -> 0.29: +2/turn
  - ropewalk 1 0.25 -> 0.00: -10/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.30: +10/turn
  - weavery 1 0.50 -> 0.37: -10/turn
  - sewing shop 1 0.30 -> 0.22: +16/turn
- Model check over the last 60 turns: predicted +24/turn for the settings we ran, real +52/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.25, beer 3.19, timber 3.98, prestige 60.37, cash 0.00
- Orders it would set: bread buy 5 (v2 8); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax fibres sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 52); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +10/turn.
- Ship linen snake: stays on Grandgues (worth +11/turn).
- Ship Flax Wyrm: Caillechâtel -> Neuborn (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 421 (+132 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.23 |
| ret | 3 | 0.91 | 0.85 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 115/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: tar buy not filling: bid 11 under the home ask 11.1 for 4 turns, bought 0.0 of 1, 0.5 held (1.5 turns); raise needs Taylor (ceiling 11.0)
