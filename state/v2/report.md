# v2 shadow report

Turn 14131, 2026-11-19 04:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,690, prestige 3,656 (536 free, +75.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 12 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 39, buy @ 3.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 1 | 1 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 533 | 0 | 31 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), 1 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 5) -> v2: buy 5

## Waste (money lost now)

- **labour**: 31 labour expired last turn (~62 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 116 over real use lately; planning 533, not 633

## Prestige spending, cheapest coin per prestige first

270 turns left: prestige gained now converts 74.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.3 | 50.6 | needs a arena (build cost 29,243); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.0 | 54.3 | needs a arena (build cost 29,243); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.7 | 55.2 | needs a arena (build cost 29,243); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.3 | 58.3 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.6 | 58.6 | thin at home: wine, cheese |
| maintain 1 | park | 0.5 | 59.4 | 59.4 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 60.0 | 60.0 | thin at home: hop beer, cheese |
| jousting 2 | arena | 210 | 59.9 | 60.5 | needs a arena (build cost 29,243); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 62.3 | 62.3 | thin at home: wine, cheese |
| hold banquet 3 (pies) | mansion | 8 | 62.3 | 62.3 | thin at home: hop beer, cheese |
| hold banquet 4 (pies) | mansion | 18 | 62.4 | 62.4 | thin at home: hop beer, wine, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 63.9 | 63.9 | thin at home: hop beer, wine, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 12 | 134102075 | 0.176 | - | furniture 11 | -152 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 14.3; crew 0.2; est +217 a turn; stock: furniture 20 @ 14.3 (keep 145)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.0 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- best towns now: Amsdermund +713, Gotthafen +487, Chatgnan +302, Fulkirch +300, Clairas +292
- Amsdermund would trade: candles buy 1 @ 76.5, furniture buy 65 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~126 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (113/turn) | firewood 26 (2.9->9.5), bread 161 (2.79->3.61), timber 39 (9.4->12.63), charcoal 19 (2.79->4.75) | jewellery 4 (94.5->98.8), garments 2 (33.39->36.6), beer 11 (3.53->3.78), flax fibres 4 (7.3->7.9) | +417 |
| Fontaux | 411 | 0.14 | 0.80 (101/turn) | thread 91 (5.1->7.27), timber 37 (9.4->12.06), clay 1 (3.8->11.97), seeds 8 (2.65->3.17) | flax fibres 19 (6.98->7.9), candles 1 (79.28->83.5), cured meat 3 (23.31->25), garments 2 (36.33->36.6) | +233 |
| Heidlowe | 662 | 0.22 | 0.10 (13/turn) | thread 36 (5.1->6.98), nets 3 (35.8->40.09), lead bars 1 (11.13->12.54), nails 1 (7.04->7.31) | cloth 24 (8.87->12.1), garments 2 (30.45->36.6), wax 1 (22.05->27.93), cured meat 3 (23.73->25) | +167 |
| Rouhomme | 368 | 0.12 | 0.60 (76/turn) | thread 70 (5.1->6.27), bread 161 (2.79->3.55), butter 1 (87.67->89.77), grain 2 (3.04->3.84) | garments 2 (32.55->36.6), tools 19 (4.73->5.18), candles 1 (80.85->83.5) | +152 |
| Herschweig | 775 | 0.26 | 0.20 (25/turn) | tools 16 (5.83->7.03), tiles 5 (3.86->7.36), thread 13 (5.1->5.56), lead bars 1 (11.13->12.06) | spinning wheels 3 (258.3->279.3), garments 2 (29.82->36.6), flax fibres 13 (6.72->7.9), cloth 20 (11.45->12.1) | +124 |

**Best:** Grandgues at about +417 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 24 @ 3.96, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 17 = 1.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 10 = 7.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 2 @ 3.7, stop 6 |  | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 33) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 1.2 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.3k (cash + stock at home prices); +194/turn over 6 turns, +122/turn over 24 turns.
- Limits: cash flow >= -445/turn, prestige >= -0.98/turn (values are after 200 tax a turn).
- Today's settings: value -167/turn, cash -160/turn, prestige +87.20/turn.
- Plan: value +482/turn, cash +275/turn, prestige +75.00/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +39 vs -122, -118 vs -150, +142 vs -144.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Clairas: +9/turn
  - ship Flax Wyrm -> Brunnham: +2/turn
  - mansion 1 1.00 -> 0.00: +246/turn
  - park 1 16.00 -> 0.00: +58/turn
  - weavery 1 0.50 -> 1.11: +32/turn
  - sewing shop 1 0.30 -> 0.68: +101/turn
  - flax farm 1 4.64 -> 7.24: +27/turn
  - retting pit 1 0.91 -> 1.43: +26/turn
  - spinnery 1 1.65 -> 2.52: +104/turn
  - net maker 0.00 -> 0.29: +21/turn
- Model check over the last 59 turns: predicted +96/turn for the settings we ran, real +122/turn.
- Worth of one more unit per turn: labour 1.39, thread 3.51, cloth 5.60, flax fibres 4.17, garments 16.20, nets 25.96, beer 3.06, timber 4.09, prestige 0.00, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 2 (v2 5); garments sell 11 (v2 10); grain buy 2 (v2 0); labour buy 64 (v2 33); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.32, worth +25/turn.
- Ship linen snake: Grandgues -> Clairas (+12/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brunnham (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +70/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate park 1: +96/turn (tax 96 saved).

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

Buffers: flax fibres 76/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 16.7 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 39 @ 3.94, home ask 3.78; our bid is already at/over the ask (sellers too thin)
- R1: bread slot dry: 2.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask none (no sellers at home)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
