# v2 shadow report

Turn 14015, 2026-11-14 08:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,146, prestige 3,520 (400 free, +0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 28 | 14 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 507 | 0 | 57 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 32.8), 4 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.7 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.32 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.32 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 57 labour expired last turn (~103 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for Flax Wyrm (crew 0.02, no projection from the game)
- labour: projection runs 99 over real use lately; planning 509, not 608
- labour expiry guard: 57 bought labour expired last turn, buy 7 (not 9) this turn

## Prestige spending, cheapest coin per prestige first

386 turns left: prestige gained now converts 85.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 54.3 | 54.3 | running |
| jousting 3 | arena | 230 | 55.7 | 56.0 | needs a arena (build cost 27,473); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 59.0 | 59.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.9 | 59.9 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 60.1 | 60.1 | thin at home: cured fish |
| jousting 2 | arena | 210 | 61.0 | 61.4 | needs a arena (build cost 27,473); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 61.6 | 61.6 | thin at home: hop beer, ham, stockfish, glassware |
| hold banquet 2 (meat) | mansion | 6.8 | 61.8 | 61.8 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 63.2 | 63.2 | running |
| hold banquet 4 (premium) | mansion | 20 | 63.6 | 63.6 | thin at home: hop beer, ham, stockfish, glassware |
| hold banquet 4 | mansion | 17.5 | 65.0 | 65.0 | thin at home: hop beer, ham, stockfish, glassware |
| hold banquet 3 (pies) | mansion | 8 | 65.7 | 65.7 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 4 @ 23.0, pasties buy 6 @ 15.4; crew 0.1; est +16 a turn; stock: pasties 6 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.1 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Großmühle +31, Bedenis +20, Unterhufe +20, Gosschweig +19, Toqueque +18
- Großmühle would trade: cured meat buy 4 @ 22.6, pasties buy 6 @ 12.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Blanans | 297 | 0.09 | 0.60 (68/turn) | timber 41 (8.09->12.44), cheese 11 (7.61->8.74), tools 15 (5.67->6.27), casks 5 (6.46->7.46) | cloth 13 (7.56->9.8), tackles 2 (154.35->162.45), candles 1 (84->89), dyed cloth 3 (10.71->11.3) | +200 |
| Grandgues | 152 | 0.05 | 0.70 (79/turn) | timber 41 (8.09->11.69), firewood 30 (3.49->6.27), thread 12 (4.72->5.46), beer 3 (3.66->4.03) | cloth 8 (8.51->9.8), garments 2 (22.47->23.8), candles 1 (86.62->89), cured meat 4 (23.73->24.4) | +180 |
| Bordetes | 831 | 0.26 | 0.50 (57/turn) | cured fish 6 (26.67->35.34), charcoal 20 (2.58->5.22), casks 5 (6.46->7.17), honey 7 (8.56->9.03) | cloth 23 (7.56->9.8), ploughs 2 (63->83.12), butter 1 (63.53->77.42), candles 1 (88.2->89) | +159 |
| Hofkirchen | 991 | 0.36 | 0.30 (34/turn) | - | cloth 24 (7.35->9.8), jewellery 2 (84->104.5), looms 1 (651->693.5), cheese 14 (5.25->6.37) | +154 |
| Amsdermund | 1111 | 0.43 | 0.30 (34/turn) | wine 15 (6.35->8.69), nets 6 (38->40.09), premium ham 1 (258.3->264.1), yarn 2 (4.79->6.41) | cloth 24 (7.35->9.8), jewellery 2 (90.83->104.5), dyed cloth 3 (9.97->11.3), hop beer 1 (8.56->12.44) | +130 |

**Best:** Blanans at about +200 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 15 @ 3.88, stop 57 |  | uses 14.2/turn (household upkeep), makes 0.0, holds 108 = 7.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 | off | a building is stalled on cured meat: no sell until it runs again |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.5 | goal planner: sells 2 a turn at 5.5, keeps 85 (no one offered it) |
| furniture | 2 @ 16.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 7) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.0) |
| pasties |  | 1 @ min 12.5 | goal planner: sells 1 a turn at 12.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.4k (cash + stock at home prices); -176/turn over 6 turns, -97/turn over 24 turns.
- Limits: cash flow >= -339/turn, prestige >= -0.42/turn (values are after 200 tax a turn).
- Today's settings: value -171/turn, cash -143/turn, prestige +2.00/turn.
- Plan: value -9/turn, cash +1/turn, prestige -0.42/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -70 vs -168, -352 vs -158, +15 vs -142.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bedenis: -1/turn
  - ship Flax Wyrm -> Vauxvais: +2/turn
  - mansion 1 1.00 -> 0.42: +148/turn
  - spinnery 1 1.65 -> 1.36: +3/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - flax farm 1 4.64 -> 4.20: +5/turn
  - net maker 0.00 -> 0.29: -2/turn
  - ropewalk 1 0.25 -> 0.00: -11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.32: +10/turn
  - sewing shop 1 0.30 -> 0.21: -14/turn
- Model check over the last 60 turns: predicted +3/turn for the settings we ran, real +27/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.31, beer 3.19, timber 3.46, prestige 59.77, cash 0.00
- Orders it would set: bread buy 5 (v2 6); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax fibres sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 7); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.32, worth +11/turn.
- Ship linen snake: Grandgues -> Bedenis (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 421 (+132 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.27 |
| ret | 3 | 0.91 | 0.85 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 112/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.32; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.3 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
