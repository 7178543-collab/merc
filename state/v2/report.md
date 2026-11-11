# v2 shadow report

Turn 13958, 2026-11-11 23:35. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,698, prestige 3,577 (457 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 9 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.44 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 34 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~76 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: projection runs 100 over real use lately; planning 490, not 590

## Prestige spending, cheapest coin per prestige first

443 turns left: prestige gained now converts 89.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 3 | arena | 230 | 54.9 | 55.2 | needs a arena (build cost 26,578); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.8 | 55.8 | thin at home: wine, ham, stockfish, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.5 | 58.5 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 59.2 | 59.2 | thin at home: wine, ham, stockfish |
| jousting 2 | arena | 210 | 60.2 | 60.5 | needs a arena (build cost 26,578); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 62.1 | 62.1 |  |
| hold banquet 3 (pies) | mansion | 8 | 62.6 | 62.6 | thin at home: pies |
| hold banquet 2 (pies) | mansion | 7 | 64.1 | 64.1 | thin at home: wine, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 64.3 | 64.3 | thin at home: wine |
| hold feast 2 | townhouse | 2.6 | 58.2 | 64.8 | needs a townhouse (build cost 7,198); thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 25 @ 14.6, pasties buy 3 @ 15.5; crew 0.1; est +295 a turn; stock: furniture 25 @ 14.6 (keep 145); stock: pasties 3 @ 15.5 (keep 14)
- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 13.9, pasties buy 3 @ 12.8; crew 0.2; est +247 a turn; stock: furniture 20 @ 13.9 (keep 145); stock: pasties 3 @ 12.8 (keep 14)
- best towns now: Donaunieder +330, Vauxvais +319, Bedenis +317, Heidlowe +298, Grandgues +295
- Donaunieder would trade: furniture buy 25 @ 13.1, pasties buy 6 @ 12.3; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Essenbrucke | 584 | 0.17 | 0.30 (32/turn) | beer 38 (3.68->5.22), dyed cloth 11 (11.55->14.34), lead ore 9 (9.13->11.49), slaked lime 2 (7.61->8.88) | spinning wheels 1 (177.45->203.3), cheese 4 (8.19->11.02), thread 38 (5.08->5.55), butter 1 (79.8->85.02) | +149 |
| Heilegg | 826 | 0.24 | 0.20 (21/turn) | nets 3 (38.2->39.9), wine 5 (6.2->7.22), slaked lime 2 (7.61->9.26), lead ore 8 (9.13->10.45) | windows 1 (703.5->760), cloth 24 (7.35->9.55), cheese 4 (8.45->11.02), garments 2 (22.68->24.8) | +134 |
| Amsdermund | 1111 | 0.40 | 0.30 (32/turn) | cured fish 7 (24.57->32.68), wine 5 (6.2->7.98), wool 5 (9.77->11.21) | cloth 24 (7.56->9.55), cheese 4 (8.51->11.02), cookware 4 (24.78->27.17), garments 2 (22.89->24.8) | +123 |
| Brunnham | 1281 | 0.50 | 0.20 (21/turn) | wine 5 (6.2->8.07), slaked lime 2 (7.61->9.31) | windows 1 (693->760), cloth 20 (7.67->9.55), cheese 4 (8.29->11.02), garments 2 (22.68->24.8) | +111 |
| Darmwald | 1022 | 0.35 | 0.60 (64/turn) | beer 76 (3.68->5.32), fleece 1 (8.14->12.63), slaked lime 2 (7.61->10.26), pickaxes 1 (12.29->13.39) | cheese 4 (8.72->11.02) | +86 |

**Best:** Essenbrucke at about +149 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 9 @ 3.66, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 9 = 2.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 6.3 | goal planner: sells 2 a turn at 6.3, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.6) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 112, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.5k (cash + stock at home prices); +276/turn over 6 turns, -185/turn over 24 turns.
- Limits: cash flow >= -237/turn, prestige >= -0.65/turn (values are after 200 tax a turn).
- Today's settings: value +40/turn, cash +116/turn, prestige -2.50/turn - breaks the prestige floor.
- Plan: value -11/turn, cash +116/turn, prestige -0.65/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +42 vs +118, +90 vs +118, -50 vs +110.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanbrücken: +3/turn
  - ship Flax Wyrm -> Essenbrucke: +2/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +9/turn
  - flax farm 1 4.64 -> 3.89: -2/turn
  - retting pit 1 0.91 -> 0.77: -2/turn
  - spinnery 1 1.65 -> 1.25: -15/turn
  - mansion 1 0.00 -> 0.44: -76/turn
- Model check over the last 61 turns: predicted +107/turn for the settings we ran, real +31/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.13, beer 3.06, timber 3.13, prestige 60.51, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> Hanbrücken (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Essenbrucke (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 411 (+121 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.78 |
| ret | 3 | 0.91 | 0.76 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 145/77, thread 1064/227, cloth 73/127

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: beer buy not filling: bid 3.44 under the home ask 3.5 for 4 turns, bought 0.0 of 9, 9.2 held (2.2 turns)
- R7 stale ask: flax fibres ask 8.65 over the market for 4 turns: the town trades ~12 a turn at 6.3, we sold 0 with 60 over what we keep (held back: acted on flax fibres at turn 13957 (one action per 2 turns))
