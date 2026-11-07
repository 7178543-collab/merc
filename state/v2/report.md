# v2 shadow report

Turn 13848, 2026-11-07 09:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,211, prestige 3,375 (255 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 8, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 507 | 0 | 22 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.30 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.30 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~35 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 607

## Prestige spending, cheapest coin per prestige first

553 turns left: prestige gained now converts 93.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 53.3 | 53.3 | thin at home: pasties, wine, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 53.9 | 53.9 |  |
| jousting 3 | arena | 230 | 54.4 | 54.6 | needs a arena (build cost 26,542); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 56.4 | 56.4 | thin at home: pasties, cheese, pies |
| hold banquet 4 | mansion | 17.5 | 56.8 | 56.8 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 57.1 | 57.1 |  |
| hold banquet 2 (pies) | mansion | 7 | 57.2 | 57.2 | thin at home: pasties, wine, cheese, pies |
| hold banquet 4 (premium) | mansion | 20 | 57.5 | 57.5 | thin at home: wine, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 57.9 | 57.9 | thin at home: wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 58.9 | 58.9 | thin at home: cheese |
| jousting 2 | arena | 210 | 59.6 | 59.8 | needs a arena (build cost 26,542); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.0 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.7 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Bedenis +31, Rouhomme +31, Bordees +30, Toqueque +27, Angefont +24
- Bedenis would trade: pasties buy 8 @ 13.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.30 (31/turn) | beer 98 (3.46->4.69), looms 1 (609->698.25), cured fish 10 (24.15->28.69), garments 10 (18.78->22.04) | candles 1 (81.38->84.5), thread 17 (5.17->5.35), cloth 7 (8.66->8.75), glass ingots 1 (53.55->53.67) | +324 |
| Hofkirchen | 991 | 0.32 | 0.80 (82/turn) | beer 98 (3.46->5.27), bellows 1 (273->340.1), garments 10 (18.78->23.37), grain 2 (2.62->3.67) | cheese 4 (5.78->7.55), thread 22 (4.77->5.35), slaked lime 2 (7.25->10.83), candles 1 (79.8->84.5) | +248 |
| Etallaen | 774 | 0.21 | 1.00 (102/turn) | beer 94 (3.46->4.64), garments 10 (18.78->22.8), cured fish 6 (24.15->27.36), cured meat 4 (23.52->27.93) | thread 17 (4.73->5.35), candles 1 (78.23->84.5), flax fibres 4 (5.25->5.9), chisels 2 (8.29->8.69) | +161 |
| Kirchwerp | 1072 | 0.37 | 0.30 (31/turn) | garments 10 (18.78->28.69), thread 47 (4.66->5.42), bellows 1 (273->290.7), casks 6 (6.46->8.31) | cheese 4 (6.2->7.55), flax fibres 27 (5.17->5.9) | +144 |
| Brebronn | 862 | 0.25 | 0.10 (10/turn) | garments 10 (18.78->29.83), belts 1 (35.49->43.51), flax fibres 2 (5.3->9.79) | candles 1 (76.65->84.5), cheese 4 (6.14->7.55), blades 1 (11.03->13.01), wrought iron 1 (9.92->12.25) | +139 |

**Best:** Grandgues at about +324 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 5 @ min 3.06 | goal planner: sells 5 a turn at 3.06, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.4k (cash + stock at home prices); +117/turn over 6 turns, -47/turn over 24 turns.
- Limits: cash flow >= -300/turn, prestige >= +1.88/turn (values are after 200 tax a turn).
- Today's settings: value +83/turn, cash +76/turn, prestige -1.98/turn - breaks the prestige floor.
- Plan: value -108/turn, cash -99/turn, prestige +1.88/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +19 vs +56, +152 vs +70, +139 vs +69.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Unterhufe: +1/turn
  - ship Flax Wyrm -> Chatgnan: +1/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.57: +0/turn
  - flax farm 1 4.64 -> 4.49: -0/turn
  - sewing shop 1 0.30 -> 0.36: -8/turn
  - weavery 1 0.50 -> 0.60: +9/turn
  - mansion 1 0.00 -> 0.92: -202/turn
- Model check over the last 60 turns: predicted +103/turn for the settings we ran, real +70/turn.
- Worth of one more unit per turn: labour 1.63, thread 4.10, cloth 6.54, flax fibres 4.86, garments 18.93, nets 29.33, beer 2.90, timber 3.22, prestige 55.94, cash 0.00
- Orders it would set: beer sell 5 (v2 none); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Unterhufe (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+1/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 437 (+148 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.93 |
| ret | 3 | 0.91 | 0.99 |
| spin | 4 | 1.65 | 1.74 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 550/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.36 (ask 3.3, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.3; ask over the cap 2.1 (60 coin per prestige)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.9 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
