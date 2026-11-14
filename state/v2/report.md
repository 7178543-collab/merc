# v2 shadow report

Turn 14009, 2026-11-14 02:40. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,152, prestige 3,511 (391 free, +2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 27 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 30, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 543 | 0 | 21 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: only 0.7 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.18 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.18 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 21 labour expired last turn (~40 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 99 over real use lately; planning 543, not 634

## Prestige spending, cheapest coin per prestige first

392 turns left: prestige gained now converts 86.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 56.7 | 56.7 | running |
| hold banquet 2 (pies) | mansion | 7 | 57.7 | 57.7 | thin at home: pasties, wine |
| jousting 3 | arena | 230 | 58.0 | 58.4 | needs a arena (build cost 27,768); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 59.0 | 59.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.4 | 59.4 | thin at home: wine |
| hold mass 2 (premium) | cathedral | 360 | 59.3 | 62.1 | needs a cathedral (build cost 271,670); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 (pies) | mansion | 18 | 62.3 | 62.3 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 62.9 | 62.9 | thin at home: pasties, hop beer |
| hold banquet 4 (premium) | mansion | 20 | 63.1 | 63.1 | thin at home: hop beer, wine, stockfish |
| jousting 2 | arena | 210 | 63.5 | 63.9 | needs a arena (build cost 27,768); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 65.4 | 65.4 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 66.0 | 66.0 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 23.4, pasties buy 3 @ 16.4; crew 0.1; est +16 a turn; stock: pasties 3 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.1 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- best towns now: Heidlowe +30, Hofkirchen +23, Gottweiler +23, Orlesailles +21, Darmwald +19
- Heidlowe would trade: cured meat buy 6 @ 21.0, pasties buy 3 @ 16.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.40 (46/turn) | timber 32 (8.19->12.06), charcoal 19 (2.62->3.86), pasties 2 (11.55->14.25), limestone 3 (20.79->23.18) | cured meat 6 (24.15->26.6), belts 1 (19.95->32.3), spinning wheels 1 (210->220.4), cloth 10 (7.98->8.8) | +168 |
| Blanans | 297 | 0.09 | 0.70 (81/turn) | timber 39 (8.19->11.69), limestone 4 (20.79->28.5), tools 14 (5.67->6.46), cheese 11 (7.67->8.31) | cloth 12 (7.56->8.8), salt 3 (5.1->5.56), garments 2 (22.89->23.2) | +131 |
| Hanbrücken | 531 | 0.16 | 0.50 (58/turn) | premium ham 1 (252->264.1), nets 4 (39->41.99), timber 19 (8.19->11.02), pasties 2 (11.55->13.49) | thread 51 (3.97->4.94), medicine 1 (109.2->132.05), cloth 15 (8.19->8.8), premium steel 1 (41.37->45.79) | +113 |
| Heidlowe | 662 | 0.20 | 0.10 (12/turn) | garments 10 (21->26.03), pasties 2 (11.55->13.49), lead ore 6 (9.13->10.45), wine 2 (6.51->6.84) | cured meat 6 (21.63->26.6), premium steel 1 (39.48->45.79), cloth 12 (8.51->8.8), furniture 1 (14.07->15.9) | +89 |
| Hanstein | 380 | 0.12 | 0.20 (23/turn) | charcoal 16 (2.62->4.33), tools 9 (5.67->6.08), pasties 2 (11.55->12.06) | windows 1 (771.75->788.5), lathes 1 (220.5->233.7), seeds 24 (1.84->2.58), cloth 11 (7.72->8.8) | +83 |

**Best:** Grandgues at about +168 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 108 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 4 = 0.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.6 | goal planner: sells 2 a turn at 5.6, keeps 85 (no one offered it) |
| furniture | 2 @ 16.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.6) |
| grain | 8 @ 3.7, stop 32 |  | goal planner: buys 8 a turn for today's rates, keeps up to 32 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 43) |
| light armour | 1 @ 97.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 38.0) |
| pasties |  | 1 @ min 10.8 | goal planner: sells 1 a turn at 10.8, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.0k (cash + stock at home prices); -232/turn over 6 turns, -19/turn over 24 turns.
- Limits: cash flow >= -381/turn, prestige >= -0.38/turn (values are after 200 tax a turn).
- Today's settings: value -186/turn, cash -161/turn, prestige +2.06/turn.
- Plan: value -16/turn, cash -5/turn, prestige -0.38/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -214 vs -162, -102 vs -167, -105 vs -161.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Heidlowe: +14/turn
  - ship Flax Wyrm -> Chatgnan: +1/turn
  - mansion 1 1.00 -> 0.42: +151/turn
  - spinnery 1 1.65 -> 1.35: +4/turn
  - retting pit 1 0.91 -> 0.84: +2/turn
  - flax farm 1 4.64 -> 4.24: +4/turn
  - net maker 0.00 -> 0.29: +2/turn
  - weavery 1 0.50 -> 0.38: -9/turn
  - sewing shop 1 0.30 -> 0.22: +14/turn
  - ropewalk 1 0.25 -> 0.00: -25/turn
- Model check over the last 60 turns: predicted +29/turn for the settings we ran, real +59/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.20, cloth 6.68, flax fibres 5.05, garments 19.30, nets 30.29, beer 3.18, timber 3.51, prestige 60.20, cash 0.00
- Orders it would set: bread buy 5 (v2 8); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax fibres sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 64 (v2 43); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +9/turn.
- Ship linen snake: Grandgues -> Heidlowe (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 420 (+131 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.22 |
| ret | 3 | 0.91 | 0.84 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 116/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.18; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
