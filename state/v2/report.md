# v2 shadow report

Turn 13496, 2026-10-23 17:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,953, prestige 3,597 (477 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 72 | 0 | 4 | 0 | 0 | min_holding 60, sell 84, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 7 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 119 | 0 | 2 | 0 | 0 | min_holding 30, sell 23, sell @ 20 |
| grain | 101 | 27 | 28 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 88 | 0 | 500 | 102 | 0 | buy 88, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 5 | 9 | 5 | 0 | 4 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax plants**: flax plants buffer 0.9 turns (holds 73, next step uses 78/turn) -> v2: check the step that makes it
- **labour**: buying 88, short of ~102 needed -> v2: buy 102
- **porterage**: buying 5, short of ~9 needed -> v2: buy 9

## Tuning

- **flax fibres**: flax fibres buffer thin: 2.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 53

## Notes

- labour: projection runs 100 over real use lately; planning 602, not 677

## Prestige spending, cheapest coin per prestige first

905 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 43.5 | 43.5 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.2 | 47.2 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.2 | 48.2 | thin at home: hop beer, wine |
| hold banquet 2 (pies) | mansion | 7 | 49.6 | 49.6 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.6 | 50.6 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 51.4 | 51.4 | thin at home: wine, hop beer, ham |
| jousting 3 | arena | 230 | 51.6 | 51.8 | needs a arena (build cost 23,538); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 52.2 | 52.2 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 49.7 | 52.3 | needs a chapel (build cost 29,510); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 50.1 | 52.6 | needs a church (build cost 63,823); thin at home: candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 |  |
| hold feast 2 | townhouse | 2.6 | 51.5 | 54.3 | needs a townhouse (build cost 6,226); thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0.16 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.208 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 11 @ 13.8; crew 0.1; est +130 a turn; stock: furniture 11 @ 13.8 (keep 145)
- **Flax Wyrm** on Caillechâtel: furniture buy 10 @ 12.7; crew 0.1; est +128 a turn; stock: furniture 10 @ 12.7 (keep 145)
- best towns now: Gosschweig +173, Hofkirchen +165, Etallaen +159, Bedenis +156, Heidlowe +154
- Gosschweig would trade: furniture buy 12 @ 12.6, garments sell 9 @ 22.2; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~91 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Gosschweig | 1099 | 0.34 | 0.20 (18/turn) | garments 9 (18.4->24.51), bellows 1 (312.9->342), wax 6 (20.06->23.56), cheese 7 (6.2->8.26) | candles 1 (63.53->70.5), grindstones 1 (260.4->271.7) | +129 |
| Hofkirchen | 991 | 0.29 | 0.50 (45/turn) | beer 57 (3.16->5.08), wrought iron 6 (12.81->14.82), thread 6 (3.35->4.18), dyed yarn 1 (6.25->7.36) | harnesses 1 (51.45->55.57), blades 1 (11.76->12.06) | +88 |
| Briclives | 1041 | 0.31 | 0.60 (54/turn) | beer 57 (3.16->4.75), malt 5 (7.35->10.07), arms 8 (26.46->27.74), wine 4 (5.51->6.27) | grindstones 1 (252->271.7), belts 2 (27.3->28.5), tools 1 (4.26->4.72) | +86 |
| Hanstein | 380 | 0.09 | 0.30 (27/turn) | thread 69 (3.35->4.41), charcoal 12 (1.68->2.66), flax fibres 7 (5.15->5.56), timber 2 (6.15->8.46) | flax plants 69 (1.52->1.78), candles 1 (68.78->70.5), beer 4 (3.04->3.5), resin 2 (1.68->1.88) | +85 |
| Darmwald | 1022 | 0.30 | 1.00 (91/turn) | thread 22 (3.35->5.13), charcoal 11 (1.68->6.46), furniture 10 (13.65->15.86), beer 51 (3.16->3.86) | - | +81 |

**Best:** Gosschweig at about +129 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 84 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| cured meat | 1 @ ?, stop 4 |  | uses 0.9/turn (mansion 1), makes 0.0, holds 6 = 6.4 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 13 @ 2.4, stop 32 |  | uses 8.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 2.9 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 24 @ min 20.0 | makes 4.4, uses 2.1, holds 119 (keeps 30): sells the surplus + 22/turn of the excess |
| grain | 77 @ 3.7, stop 169 |  | uses 42.2/turn (brewery 1), makes 0.0, holds 101 = 2.4 turns |
| labour | 89 @ 2.2, stop - |  | goal planner: buys 89 for today's rates (v2 had 102) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 14.0, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 9) |
| rope |  | 3 @ min 73.5 |  |
| timber |  | 10 @ min 6.5 | makes 8.4, uses 0.0, holds 376 (keeps 350): sells the surplus + 1/turn of the excess |
| tools | 4 @ 6.2, stop 28 |  | uses 3.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 57.2 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.3k (cash + stock at home prices); +26/turn over 6 turns, +38/turn over 24 turns.
- Limits: cash flow >= +85/turn, prestige >= -0.74/turn (values are after 240 tax a turn).
- Today's settings: value +181/turn, cash +291/turn, prestige -0.74/turn.
- Plan: value +455/turn, cash +527/turn, prestige -0.74/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +58/turn
  - ship Flax Wyrm -> Kirchwerp: -0/turn
  - brewery 1 0.65 -> 1.00: +97/turn
  - quarry 1 0.00 -> 0.08: +5/turn
  - ropewalk 1 0.75 -> 1.00: +2/turn
  - weavery 1 0.25 -> 0.67: -1/turn
  - spinnery 1 1.59 -> 4.00: +25/turn
  - logging camp w/ tool 7.00 -> 0.00: -6/turn
  - logging camp w/ tool [cut firewood 1] 0.00 -> 20.00: +16/turn
  - net maker 0.50 -> 0.00: -29/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.45, thread 3.89, cloth 6.07, flax fibres 4.32, garments 17.32, nets 34.00, beer 3.50, timber 6.15, prestige 54.58, cash 0.00
- Orders it would set: labour buy 89 (v2 102); porterage buy 5 (v2 9)
- Recipe: logging camp w/ tool split timber 2 -> cut firewood 1 at 20.00, worth +16/turn.
- Recipe: net maker make nets 1 -> make nets 2 at 1.00, worth +30/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+140/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Kirchwerp (+39/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - new chandlery (make candles 2) for ~3905 coin: +82/turn, payback 48 turns
  - Tenants L13 for 500 prestige: +72/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot brewery 1 for ~2870 coin: +63/turn, payback 45 turns
  - +1 plot net maker for ~1307 coin: +15/turn, payback 88 turns
  - +1 plot ropewalk 1 for ~2619 coin: +12/turn, payback 218 turns
  - +1 plot spinnery 1 for ~1810 coin: +7/turn, payback 249 turns, doesn't pay yet
- Trim: donate quarry 1: +15/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 460, chain may buy 0 -> chain allowance 40, chain plan 172 (-57 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.34 | 3.91 |
| ret | 3 | 0.87 | 0.70 |
| spin | 4 | 1.59 | 1.43 |
| weave | 3 | 0.25 | 0.00 |
| sew | 2 | 0.11 | 0.00 |

Buffers: flax fibres 53/59, thread 362/174, cloth 27/0
- chain plan needed 172 labour, budget left 40: cut to 172

## Self-diagnosis

- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~62 a turn at 19.5, we sold 0 with 89 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
- R7 stale ask: timber ask 6.5 over the market for 4 turns: the town trades ~83 a turn at 6.15, we sold 0 with 26 over what we keep; floor 6.5 (config sell_floor / unit cost) is at or over the market: Taylor's call
