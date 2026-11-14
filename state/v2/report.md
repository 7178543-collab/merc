# v2 shadow report

Turn 14027, 2026-11-14 20:20. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,567, prestige 3,600 (480 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 57 | 0 | 12 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 533 | 0 | 31 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.46 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.46 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 31 labour expired last turn (~53 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 548, not 648
- labour expiry guard: 31 bought labour expired last turn, buy 34 (not 48) this turn

## Prestige spending, cheapest coin per prestige first

374 turns left: prestige gained now converts 84.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.5 | 52.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.3 | 55.3 |  |
| jousting 3 | arena | 230 | 56.2 | 56.5 | needs a arena (build cost 26,361); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.2 | 58.2 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.3 | 58.3 |  |
| hold banquet 3 (pies) | mansion | 8 | 60.6 | 60.6 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 60.6 | 60.6 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 61.9 | 61.9 | running |
| jousting 2 | arena | 210 | 61.5 | 61.9 | needs a arena (build cost 26,361); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 62.1 | 62.1 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 63.2 | 63.2 |  |
| hold banquet 4 (premium) | mansion | 20 | 63.4 | 63.4 | thin at home: hop beer, ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.108 | rope 1 | cured meat 3, pasties 7 | -154 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.4 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.4 (keep 14); best orders clear only -3 a turn after crew: ship stays at 0
- best towns now: Amsdermund +657, Chatgnan +478, Gotthafen +436, Cobholme +312, Fulkirch +280
- Amsdermund would trade: furniture buy 64 @ 14.4; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (100/turn) | timber 38 (7.98->11.97), firewood 28 (3.63->6.65), bread 157 (2.5->2.77), charcoal 19 (2.71->3.76) | tools 9 (5.78->7.03), cloth 6 (8.24->8.84), cured meat 3 (23.52->24.4), garments 2 (22.47->23.6) | +243 |
| Blanans | 297 | 0.09 | 0.60 (67/turn) | timber 42 (7.98->11.4), cheese 11 (7.67->11.3), jewellery 3 (96.08->98.8), limestone 2 (18.27->24.89) | cloth 13 (7.56->8.84), tools 17 (6.04->7.03), garments 2 (22.68->23.6), dyed cloth 6 (11.97->12.16) | +176 |
| Fontaux | 411 | 0.12 | 0.60 (67/turn) | thread 69 (4.66->5.65), timber 18 (7.98->11.49), nets 6 (34.4->38.19), charcoal 19 (2.71->4.33) | cloth 4 (8.19->8.84), candles 1 (87.67->88.5), resin 1 (1.73->2.72) | +143 |
| Clairas | 374 | 0.11 | 0.80 (89/turn) | timber 27 (7.98->11.21), lathes 1 (233.1->266), nets 4 (34.4->38.95), charcoal 19 (2.71->4.39) | tools 25 (6.62->7.03), cloth 6 (7.77->8.84), garments 2 (22.47->23.6), salt 4 (4.41->4.99) | +128 |
| Kirchwerp | 1072 | 0.40 | 0.50 (56/turn) | thread 91 (4.66->5.56), wax 14 (23.1->25.27), nets 6 (34.4->37.62), acid 1 (118.65->119.7) | tools 25 (5.83->7.03), cloth 13 (7.51->8.84), salt 4 (3.89->4.99), garments 2 (22.05->23.6) | +126 |

**Best:** Grandgues at about +243 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 17 @ 3.66, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 57 = 3.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 6 = 1.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 17.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 34) |
| light armour | 1 @ 106, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| pasties |  | 2 @ min 12.3 | goal planner: sells 2 a turn at 12.3, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 75.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.3k (cash + stock at home prices); -327/turn over 6 turns, -212/turn over 24 turns.
- Limits: cash flow >= -315/turn, prestige >= -0.75/turn (values are after 200 tax a turn).
- Today's settings: value -182/turn, cash -166/turn, prestige +1.60/turn.
- Plan: value -26/turn, cash -11/turn, prestige -0.75/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +309 vs -163, +108 vs -167, -213 vs -177.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bremcop: +7/turn
  - ship Flax Wyrm -> Chatgnan: +3/turn
  - mansion 1 1.00 -> 0.44: +142/turn
  - net maker 0.00 -> 0.29: +4/turn
  - spinnery 1 1.65 -> 1.34: +3/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - flax farm 1 4.64 -> 4.23: +4/turn
  - sewing shop 1 0.30 -> 0.22: -12/turn
  - weavery 1 0.50 -> 0.37: +11/turn
- Model check over the last 59 turns: predicted -59/turn for the settings we ran, real -71/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.22, beer 3.11, timber 3.42, prestige 59.10, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 34); light armour buy 1 (v2 None); pasties sell 2 (v2 none); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Bremcop (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 90/77, thread 1049/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.46; ask over the cap 2.1 (60 coin per prestige)
