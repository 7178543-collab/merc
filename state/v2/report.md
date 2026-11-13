# v2 shadow report

Turn 14003, 2026-11-13 20:34. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,970, prestige 3,498 (378 free, +2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 107 | 27 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 556 | 0 | 8 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.26 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.26 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Tuning

- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.5 coin per prestige at mansion, vs 69.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 56.2 coin per prestige at mansion, vs 69.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +5 crew for Flax Wyrm (crew 0.10, no projection from the game)
- labour: projection runs 100 over real use lately; planning 556, not 649

## Prestige spending, cheapest coin per prestige first

398 turns left: prestige gained now converts 86.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (fish) | mansion | 6.8 | 56.2 | 56.2 |  |
| jousting 3 | arena | 230 | 56.9 | 57.3 | needs a arena (build cost 28,971); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 |  |
| maintain 1 | park | 0.5 | 57.6 | 57.6 | running |
| hold banquet 2 (pies) | mansion | 7 | 60.1 | 60.1 |  |
| hold mass 2 (premium) | cathedral | 360 | 58.4 | 61.1 | needs a cathedral (build cost 276,140); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| jousting 2 | arena | 210 | 62.3 | 62.7 | needs a arena (build cost 28,971); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 63.5 | 63.5 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 63.8 | 63.8 | thin at home: hop beer, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 64.2 | 64.2 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 65.5 | 65.5 |  |
| hold banquet 3 (pies) | mansion | 8 | 66.5 | 66.5 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.10 | 11 | 134102075 | 0 | - | pasties 2 | -27 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.048 | - | cured meat 6 | -141 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 23.8; crew 0.1; est +15 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.1 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- best towns now: Neuborn +27, Bordees +27, Orlesailles +27, Friedwerp +26, Hofkirchen +23
- Neuborn would trade: cured meat buy 6 @ 22.4, pasties buy 1 @ 15.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.50 (58/turn) | windows 1 (614.25->684), timber 25 (9.19->12.06), cured fish 7 (22.68->28.88), bread 148 (2.67->2.96) | cured meat 6 (24.57->28.2), garments 2 (22.68->24.8), dyed cloth 6 (11.45->11.59), tools 8 (5.15->5.37) | +236 |
| Karlmoor | 787 | 0.24 | 0.20 (23/turn) | windows 1 (614.25->821.75), rope 1 (76->79.33), leather 1 (23.73->25.65), thread 4 (4.84->5.13) | cured meat 6 (24.57->28.2), butter 1 (71.92->81.7), wrought iron 2 (12.5->14.82), pickaxes 2 (12.6->13.3) | +236 |
| Amsdermund | 1111 | 0.44 | 0.30 (35/turn) | windows 1 (614.25->712.5), cured fish 13 (22.68->28.12), nets 6 (35->40.66), cheese 10 (5.72->7.12) | cloth 24 (7.35->8), cured meat 6 (26.46->28.2), dyed cloth 6 (10.71->11.59), garments 2 (22.68->24.8) | +229 |
| Herschweig | 775 | 0.24 | 0.10 (12/turn) | windows 1 (614.25->793.25), nets 4 (35->38.19), leather 1 (23.73->27.93) | hop beer 3 (8.24->12.92), cured meat 6 (26.25->28.2), flax fibres 9 (5.72->6.45), furniture 1 (13.97->15.9) | +220 |
| Bordetes | 831 | 0.27 | 0.50 (58/turn) | windows 1 (614.25->750.5), cured fish 13 (22.68->26.22), charcoal 19 (2.77->5.94), rope 1 (76->85.02) | cloth 24 (7.56->8), cured meat 6 (27.09->28.2), garments 2 (22.89->24.8) | +216 |

**Best:** Grandgues at about +236 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 107 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| candles | 2 @ 84, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 10 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 16 = 2.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.2) |
| grain | 6 @ 3.7, stop 22 |  | goal planner: buys 6 a turn for today's rates, keeps up to 22 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 56) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| pasties |  | 1 @ min 15.5 | goal planner: sells 1 a turn at 15.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 74.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.4k (cash + stock at home prices); -92/turn over 6 turns, +64/turn over 24 turns.
- Limits: cash flow >= -415/turn, prestige >= -0.33/turn (values are after 200 tax a turn).
- Today's settings: value -190/turn, cash -161/turn, prestige +2.12/turn.
- Plan: value -15/turn, cash -1/turn, prestige -0.33/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -186 vs -147, -114 vs -143, -87 vs -182.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Neuborn: +6/turn
  - ship Flax Wyrm -> Friedwerp: +1/turn
  - mansion 1 1.00 -> 0.42: +145/turn
  - spinnery 1 1.65 -> 1.36: +8/turn
  - retting pit 1 0.91 -> 0.86: +1/turn
  - flax farm 1 4.64 -> 4.30: +4/turn
  - net maker 0.00 -> 0.29: -0/turn
  - weavery 1 0.50 -> 0.40: -2/turn
  - sewing shop 1 0.30 -> 0.23: +9/turn
- Model check over the last 59 turns: predicted +59/turn for the settings we ran, real +5/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.38, beer 3.13, timber 3.56, prestige 60.69, cash 0.00
- Orders it would set: bread buy 5 (v2 8); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 64 (v2 56); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Neuborn (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Friedwerp (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 418 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.12 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 123/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.26; ask over the cap 2.1 (60 coin per prestige)
