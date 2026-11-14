# v2 shadow report

Turn 14017, 2026-11-14 10:19. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,814, prestige 3,521 (401 free, +0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 107 | 22 | 14 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 524 | 0 | 40 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 32.8), 4 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.52 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.52 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 40 labour expired last turn (~72 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 99 over real use lately; planning 557, not 656
- labour expiry guard: 40 bought labour expired last turn, buy 24 (not 57) this turn

## Prestige spending, cheapest coin per prestige first

384 turns left: prestige gained now converts 85.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 54.0 | 54.0 | running |
| jousting 3 | arena | 230 | 55.7 | 56.1 | needs a arena (build cost 27,043); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.9 | 58.9 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 60.2 | 60.2 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.3 | 60.3 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 61.4 | 61.4 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 61.0 | 61.4 | needs a arena (build cost 27,043); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 61.6 | 61.6 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 62.5 | 62.5 | running |
| hold banquet 4 (premium) | mansion | 20 | 63.7 | 63.7 | thin at home: hop beer, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 60.7 | 63.8 | needs a cathedral (build cost 296,815); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 65.0 | 65.0 | thin at home: hop beer, ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 11 | 134102075 | 0.148 | - | pasties 3 | -46 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.116 | - | cured meat 4 | -90 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.6 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.4 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Karlmoor +22, Clairlond +20, Disscester +17, Cobholme +16, Großmühle +16
- Karlmoor would trade: pasties buy 5 @ 12.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Blanans | 297 | 0.09 | 0.60 (68/turn) | timber 42 (8.14->12.44), cheese 11 (7.93->9.69), limestone 1 (17.64->24.89), flour 1 (19.21->21.28) | cloth 12 (7.56->9.8), dyed cloth 13 (10.71->12.16), flax fibres 3 (5.93->6.65), garments 2 (22.68->23.6) | +195 |
| Grandgues | 152 | 0.05 | 0.90 (102/turn) | timber 42 (8.14->11.59), firewood 29 (3.7->6.46), bread 156 (2.56->2.75), grindstones 1 (226.8->237.5) | cloth 8 (8.56->9.8), cured meat 4 (23.52->24), garments 2 (22.47->23.6), salt 2 (4.62->5.56) | +193 |
| Amsdermund | 1111 | 0.43 | 0.40 (45/turn) | wine 15 (6.3->9.79), grindstones 1 (226.8->262.2), nets 6 (37.6->39.52), flour 1 (19.21->23.37) | cloth 24 (7.35->9.8), dyed cloth 13 (9.97->12.16), casks 20 (5.35->6.98), butter 1 (76.65->87.4) | +182 |
| Heilegg | 826 | 0.26 | 0.50 (57/turn) | grindstones 1 (226.8->260.3), nets 6 (37.6->41.61), charcoal 20 (2.71->5.7), wine 15 (6.3->6.89) | cloth 24 (7.35->9.8), cheese 12 (5.21->6.89), dyed cloth 13 (11.03->12.16), casks 22 (6.09->6.98) | +176 |
| Fontaux | 411 | 0.12 | 0.30 (34/turn) | thread 78 (4.74->5.65), premium ham 1 (252->277.4), charcoal 20 (2.71->4.5), grindstones 1 (226.8->245.1) | cloth 12 (8.4->9.8), candles 1 (84->89), cured fish 6 (22.68->23.18), cured meat 4 (23.31->24) | +146 |

**Best:** Blanans at about +195 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 15 @ 3.88, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 107 = 7.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 | off | a building is stalled on cured meat: no sell until it runs again |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 24) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.6) |
| pasties |  | 1 @ min 12.5 | goal planner: sells 1 a turn at 12.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.6k (cash + stock at home prices); -77/turn over 6 turns, -94/turn over 24 turns.
- Limits: cash flow >= -326/turn, prestige >= -0.42/turn (values are after 200 tax a turn).
- Today's settings: value -174/turn, cash -150/turn, prestige +2.00/turn.
- Plan: value -11/turn, cash +0/turn, prestige -0.42/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +15 vs -142, -176 vs -143, -155 vs -159.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +1/turn
  - ship Flax Wyrm -> Unterhufe: +0/turn
  - mansion 1 1.00 -> 0.42: +147/turn
  - net maker 0.00 -> 0.29: +5/turn
  - flax farm 1 4.64 -> 4.14: -0/turn
  - retting pit 1 0.91 -> 0.83: -1/turn
  - spinnery 1 1.65 -> 1.34: +5/turn
  - sewing shop 1 0.30 -> 0.23: -12/turn
  - weavery 1 0.50 -> 0.38: +15/turn
- Model check over the last 59 turns: predicted -8/turn for the settings we ran, real +20/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.34, beer 3.20, timber 3.48, prestige 59.50, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 24); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Etallaen (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Unterhufe (+0/turn over staying).
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

Buffers: flax fibres 116/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.52; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
