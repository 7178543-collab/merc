# v2 shadow report

Turn 13501, 2026-10-23 22:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,037, prestige 3,591 (471 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 87 | 0 | 4 | 0 | 0 | min_holding 60, sell 66, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 37 | 12 | 7 | 0 | 0 | stop 28, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 131 | 0 | 2 | 0 | 0 | min_holding 30, sell 35, sell @ 20 |
| grain | 118 | 0 | 33 | 0 | 0 | stop 103, buy 26, buy @ 3.7 |
| labour | 43 | 47 | 530 | 0 | 17 | buy 43, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 10 | 10 | 9 | 0 | 1 | buy 10, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **wax**: net maker152202386007001 ran short of wax (no buy order); labour need rises ~12/turn when they restart -> v2: add a wax buy
- **wax**: needed (0.1/turn) but there is NO buy order, stock 0.0 -> v2: add buy 1

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57
- **flax plants**: flax plants buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 149

## Notes

- labour: projection runs 106 over real use lately; planning 530, not 630

## Prestige spending, cheapest coin per prestige first

900 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.1 | 44.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 47.8 | 47.8 | thin at home: hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 48.6 | 48.6 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.6 | 50.6 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 51.2 | 51.2 | thin at home: wine, hop beer, ham |
| jousting 3 | arena | 230 | 51.9 | 52.0 | needs a arena (build cost 23,951); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 52.6 | 52.6 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 50.1 | 52.9 | needs a chapel (build cost 30,006); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 50.5 | 53.0 | needs a church (build cost 62,775); thin at home: candles, furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 53.2 | 53.2 | thin at home: hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 53.6 | 53.6 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 53.6 | 53.6 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: beer sell 25 @ 4.38, furniture buy 6 @ 12.7; crew 0.1; est +88 a turn; stock: furniture 6 @ 12.7 (keep 145)
- **linen snake** on Grandgues: furniture buy 6 @ 13.8; crew 0.1; est +66 a turn; stock: furniture 6 @ 13.8 (keep 145)
- best towns now: Heidlowe +99, Hofkirchen +98, Chatgnan +97, Bedenis +96, Caillechâtel +88
- Heidlowe would trade: furniture buy 7 @ 11.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~92 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 0.60 (55/turn) | beer 68 (3.16->5.42), lead bars 5 (15.75->17.67), looms 1 (556.5->565.25), wheels 1 (17.12->19.38) | garments 2 (18.48->19.5) | +125 |
| Disscester | 1474 | 0.53 | 0.20 (18/turn) | looms 1 (556.5->674.5), mouldboards 1 (31.5->36.1), nets 3 (35->36.67), rope 3 (73->74.58) | - | +117 |
| Briclives | 1041 | 0.31 | 0.60 (55/turn) | beer 68 (3.16->5.27), cured meat 4 (22.26->24.7), harnesses 1 (54.08->59.85), flour 1 (19.43->24.7) | chisels 1 (8.4->11.88), tools 3 (4.28->4.76) | +117 |
| Brunnham | 1281 | 0.43 | 0.20 (18/turn) | looms 1 (556.5->665), harnesses 1 (54.08->58.9), wheels 1 (17.12->19.57), hides 1 (12.6->14.25) | candles 1 (67.2->71.5) | +113 |
| Angefont | 686 | 0.17 | 0.20 (18/turn) | looms 1 (556.5->617.5), harnesses 1 (54.08->62.22), wheels 1 (17.12->19.19) | flax fibres 28 (4.85->5.9), thread 34 (4.26->4.6), candles 1 (70.35->71.5), tools 3 (4.33->4.76) | +97 |

**Best:** Hofkirchen at about +125 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 69 @ min 3.38 | goal planner: sells 69 (v2 had 10) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 7 @ 2.4, stop 28 |  | uses 6.8/turn (brewery 1, household upkeep), makes 0.0, holds 37 = 5.4 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| grain | 31 @ 3.7, stop 124 |  | goal planner: buys 31 a turn for today's rates, keeps up to 124 (v2 had 40) |
| labour | 43 @ 2.2, stop - |  | goal planner: buys 43 for today's rates (v2 had 30) |
| light armour | 1 @ 87.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 10 @ 1.1, stop - |  | goal planner: buys 10 for today's rates (v2 had 9) |
| rope |  | 4 @ min 72.0 |  |
| tar | 1 @ 9.15, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| timber |  | 10 @ min 6.5 | makes 8.4, uses 0.0, holds 383 (keeps 350): sells the surplus + 2/turn of the excess |
| tools | 4 @ 6.2, stop 28 |  | uses 3.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 58.6 turns |
| wax | 1 @ 23.2, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.7k (cash + stock at home prices); +84/turn over 6 turns, +56/turn over 24 turns.
- Limits: cash flow >= +123/turn, prestige >= -0.71/turn (values are after 240 tax a turn).
- Today's settings: value +133/turn, cash +264/turn, prestige -1.36/turn - breaks the prestige floor.
- Plan: value +164/turn, cash +254/turn, prestige -0.71/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -187 vs +377, -199 vs +322, +140 vs +238.
- Route sales counted at most (what the ships really sold, a turn): garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bedenis: +6/turn
  - ship Flax Wyrm -> Vauxvais: +3/turn
  - logging camp w/ tool 7.00 -> 0.00: +7/turn
  - logging camp w/ tool [cut firewood 1] 0.00 -> 20.00: +15/turn
  - quarry 1 0.00 -> 0.08: +4/turn
  - flax farm 1 4.66 -> 5.83: -4/turn
  - retting pit 1 0.83 -> 1.01: -6/turn
  - sewing shop 1 0.00 -> 0.10: -7/turn
  - weavery 1 0.00 -> 0.16: +5/turn
  - spinnery 1 1.70 -> 2.09: +8/turn
- Model check over the last 6 turns: predicted +186/turn for the settings we ran, real +84/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.47, thread 3.63, cloth 5.84, flax fibres 4.20, garments 16.95, nets 35.00, beer 2.55, timber 6.04, prestige 55.12, cash 0.00
- Orders it would set: beer sell 69 (v2 10); grain buy 31 (v2 40); labour buy 43 (v2 30); light armour buy 1 (v2 None); porterage buy 10 (v2 9); tar buy 1 (v2 None)
- Recipe: logging camp w/ tool split timber 2 -> cut firewood 1 at 20.00, worth +15/turn.
- Recipe: net maker make nets 2 -> make nets 3 at 1.00, worth +39/turn.
- Ship linen snake: Grandgues -> Bedenis (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+3/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +74/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot net maker for ~1302 coin: +33/turn, payback 39 turns
  - new pulleyworks (make tackles 1) for ~3111 coin: +24/turn, payback 132 turns, doesn't pay yet (materials thin at home: tiles)
  - new weaponsmith (forge arms 1) for ~2615 coin: +19/turn, payback 137 turns, doesn't pay yet (materials thin at home: bricks)
- Trim: donate weavery 1: +16/turn (tax 18 saved).
- Trim: donate quarry 1: +16/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 439, chain may buy 0 -> chain allowance 61, chain plan 180 (-24 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.66 | 4.11 |
| ret | 3 | 0.83 | 0.73 |
| spin | 4 | 1.70 | 1.50 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 39/64, thread 425/190, cloth 44/0
- chain plan needed 180 labour, budget left 61: cut to 180

## Self-diagnosis

- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~59 a turn at 19.5, we sold 0 with 101 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
