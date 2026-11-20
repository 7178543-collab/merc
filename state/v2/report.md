# v2 shadow report

Turn 14155, 2026-11-20 04:41. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,371, prestige 3,627 (507 free, +1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 1 | 0 | 19 | 0 | 0 | stop 77, buy 39, buy @ 4.78 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 65 | 519 | 0 | 46 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.96 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.96 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 46 labour expired last turn (~93 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +3 crew for Flax Wyrm (crew 0.07, no projection from the game)
- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 519, not 588
- labour expiry guard: 46 bought labour expired last turn, buy 19 (not 19) this turn

## Prestige spending, cheapest coin per prestige first

246 turns left: prestige gained now converts 70.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.9 | 51.2 | needs a arena (build cost 28,272); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.3 | 52.9 | needs a arena (build cost 28,272); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.6 | 55.0 | needs a arena (build cost 28,272); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.2 | 57.9 | needs a arena (build cost 28,272); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 59.5 | 59.5 | thin at home: wine, stockfish, cheese |
| maintain 1 | park | 0.5 | 60.0 | 60.0 | running |
| hold banquet 3 (pies) | mansion | 8 | 60.8 | 60.8 | thin at home: cheese, pies |
| hold banquet 2 (pies) | mansion | 7 | 61.8 | 61.8 | thin at home: wine, cheese, pies |
| hold banquet 4 (premium) | mansion | 20 | 62.3 | 62.3 | thin at home: wine, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 62.6 | 62.6 | thin at home: wine, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 63.3 | 63.3 | thin at home: beer |
| hold banquet 3 (fish) | mansion | 7.6 | 63.9 | 63.9 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 20.4, pasties buy 6 @ 16.0; crew 0.1; est +50 a turn; stock: pasties 6 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: beer buy 19 @ 3.8, cured meat buy 2 @ 22.6, pasties buy 2 @ 12.3; crew 0.1; est +30 a turn; stock: pasties 2 @ 12.3 (keep 14)
- best towns now: Cobholme +360, Fulkirch +331, Nürnnieder +248, Bedenis +245, Heidlowe +242
- Cobholme would trade: furniture buy 40 @ 14.2; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~128 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.40 (51/turn) | bread 236 (3->4.46), thread 92 (6.4->6.84), flour 3 (20.37->29.45), tiles 5 (3.91->7.98) | cured meat 6 (21->27.8), cheese 6 (6.77->9.12), cloth 4 (12.29->13.5), flax plants 13 (1.75->1.92) | +446 |
| Amsdermund | 1111 | 0.49 | 0.50 (64/turn) | swords 1 (275.1->305.9), flour 3 (20.37->29.07), nets 5 (36.8->38), slaked lime 1 (8.51->11.4) | cloth 24 (9.77->13.5), cured meat 6 (21->27.8), cheese 6 (6.51->9.12), casks 9 (5.35->7.22) | +214 |
| Dortgart | 1045 | 0.44 | 0.30 (38/turn) | swords 1 (275.1->324.9), nets 6 (36.8->39.9), slaked lime 1 (8.51->10.92) | cloth 22 (9.35->13.5), cheese 6 (6.72->9.12), cured meat 3 (25.41->27.8), yarn 28 (6.35->6.93) | +169 |
| Clairas | 374 | 0.13 | 0.50 (64/turn) | charcoal 19 (2.39->4.48), salt 5 (6.3->6.55), logs 1 (8.61->11.3) | cloth 24 (11.03->13.5), cured meat 6 (23.52->27.8), tools 20 (6.09->7.31), beer 61 (4.2->4.75) | +169 |
| Angefont | 686 | 0.23 | 0.40 (51/turn) | garments 10 (32.6->36.48), thread 77 (6.4->7.03), flax fibres 4 (6.4->9.36), casks 6 (8.4->9.4) | beer 66 (3.82->4.75), cured meat 6 (23.1->27.8), cheese 6 (6.3->9.12), tools 20 (6.41->7.31) | +165 |

**Best:** Grandgues at about +446 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 39 @ ?, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 1 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 14 = 2.3 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 31.8) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 34 |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 19) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.9k (cash + stock at home prices); +77/turn over 6 turns, -19/turn over 24 turns.
- Limits: cash flow >= -349/turn, prestige >= -0.86/turn (values are after 200 tax a turn).
- Today's settings: value -126/turn, cash -137/turn, prestige +1.47/turn.
- Plan: value +53/turn, cash +57/turn, prestige -0.86/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -644 vs -178, +113 vs -178, -547 vs -110 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship Flax Wyrm -> Donaunieder: +3/turn
  - mansion 1 1.00 -> 0.44: +129/turn
  - ropewalk 1 0.25 -> 0.15: +12/turn
  - spinnery 1 1.65 -> 1.29: +10/turn
  - net maker 0.00 -> 0.29: +3/turn
  - retting pit 1 0.91 -> 0.82: +3/turn
  - flax farm 1 4.64 -> 4.10: +6/turn
  - brewery 1 0.14 -> 0.00: -8/turn
  - brewery 1 [brew mead 1] 0.00 -> 0.09: +20/turn
- Model check over the last 59 turns: predicted -10/turn for the settings we ran, real +77/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.74, beer 3.52, timber 3.69, prestige 58.21, cash 0.00
- Orders it would set: candles buy 2 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 19); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.09, worth +11/turn.
- Ship linen snake: stays on Grandgues (worth +17/turn).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +89/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 425 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.50 |
| ret | 3 | 0.91 | 0.90 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 96/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 0.6 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 39 @ 4.78, home ask none (no sellers at home)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.96; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.2 for 5 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
