# v2 shadow report

Turn 13973, 2026-11-12 14:02. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,680, prestige 3,538 (418 free, -2.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 5 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 37 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 493 | 0 | 36 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 4.12 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 4.12 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 36 labour expired last turn (~62 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +0 crew for linen snake (crew 0.00, no projection from the game)
- labour: projection runs 100 over real use lately; planning 493, not 584

## Prestige spending, cheapest coin per prestige first

428 turns left: prestige gained now converts 88.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 53.2 | 53.2 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 55.7 | 55.7 | thin at home: hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 55.5 | 55.8 | needs a arena (build cost 27,051); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 57.0 | 57.0 | thin at home: pasties, hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 57.7 | 57.7 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 57.8 | 57.8 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 57.9 | 57.9 | thin at home: pasties, pies |
| hold banquet 4 (premium) | mansion | 20 | 58.1 | 58.1 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.4 | 58.4 | thin at home: cured fish |
| jousting 2 | arena | 210 | 60.7 | 61.1 | needs a arena (build cost 27,051); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 65.7 | 65.7 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 4 @ 13.5; crew 0.1; est +41 a turn; stock: furniture 4 @ 13.5 (keep 145)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Clairlond +43, Disscester +42, Caillechâtel +41, Helmgreen +40, Bremcop +39
- Clairlond would trade: furniture buy 4 @ 12.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.06 | 0.10 (11/turn) | yarn 3 (3.49->4.75), hop beer 4 (10.82->11.3), limestone 1 (16.59->19.57), grain 2 (2.72->2.89) | windows 1 (677.25->779), cloth 18 (7.56->9.75), furniture 15 (15.75->18.52), raw cloth 5 (5.83->7.17) | +188 |
| Chribruck | 1202 | 0.46 | 0.40 (43/turn) | dyed cloth 6 (11.45->21.09), yarn 3 (3.49->4.67) | windows 1 (714->779), furniture 15 (14.6->18.52), cloth 16 (8.51->9.75) | +162 |
| Kirchwerp | 1072 | 0.38 | 0.50 (53/turn) | thread 99 (4.94->5.7), casks 6 (5.93->8.31), honey 2 (10.4->13.21), yarn 5 (3.49->4.33) | cloth 24 (7.56->9.75), flax fibres 19 (5.78->7.6), tools 15 (4.62->6.03), belts 4 (32.55->36.29) | +152 |
| Blanans | 297 | 0.09 | 0.60 (64/turn) | limestone 3 (16.59->30.21), timber 36 (8.35->10.07), yarn 7 (3.49->4.66) | furniture 15 (16.17->18.52), cloth 13 (7.56->9.75), swords 1 (224.7->241.3), windows 1 (766.5->779) | +142 |
| Amsdermund | 1111 | 0.41 | 0.50 (53/turn) | cookware 10 (28.14->31.92), nets 6 (37.8->40.09), wine 14 (6.93->7.93), acid 1 (115.5->119.7) | cloth 19 (7.56->9.75), furniture 15 (15.75->18.52), flax fibres 16 (5.78->7.6), tools 15 (5.1->6.03) | +136 |

**Best:** Vauxvais at about +188 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.98, stop 9 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 5 = 1.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 113, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.2) |
| pasties |  | 2 @ min 12.3 | goal planner: trial sale of an idle pile, 2 a turn at 12.3, keeps 0 (14 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.3k (cash + stock at home prices); +193/turn over 6 turns, -29/turn over 24 turns.
- Limits: cash flow >= -362/turn, prestige >= -0.49/turn (values are after 200 tax a turn).
- Today's settings: value +47/turn, cash +15/turn, prestige -2.30/turn - breaks the prestige floor.
- Plan: value -34/turn, cash -31/turn, prestige -0.49/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +366 vs -12, +161 vs -8, +150 vs +2.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +4/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.34: -3/turn
  - retting pit 1 0.91 -> 0.83: +1/turn
  - flax farm 1 4.64 -> 4.16: -3/turn
  - weavery 1 0.50 -> 0.44: -10/turn
  - ropewalk 1 0.25 -> 0.00: -15/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.22: +22/turn
  - mansion 1 0.00 -> 0.43: -98/turn
- Model check over the last 61 turns: predicted +106/turn for the settings we ran, real +14/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.22, beer 3.05, timber 3.29, prestige 67.03, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); pasties sell 2 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.22, worth +8/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+7/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +1/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1850 coin: +3/turn, payback 716 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 408 (+118 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.74 |
| ret | 3 | 0.91 | 0.75 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 147/77, thread 1064/226, cloth 73/127

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 4.12; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
