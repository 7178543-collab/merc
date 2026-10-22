# v2 shadow report

Turn 13466, 2026-10-22 11:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,353, prestige 3,567 (447 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 128 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 56 | 0 | 2 | 0 | 0 | min_holding 30, sell 24, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 279 | 290 | 735 | 0 | 5 | buy 279, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 10 | 1 | 0 | buy 10, buy @ 1.1 |

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 38/turn) -> v2: check the step that makes it
- **porterage**: logging camp w/ tool ran short of porterage (buy is live (10 @ 1.1), 10 bought last turn); labour need rises ~22/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Waste (money lost now)

- **linen snake**: linen snake cost 24 coin last turn (crew 0.25) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 72
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 185

## Notes

- labour: projection runs 75 over real use lately; planning 735, not 797

## Prestige spending, cheapest coin per prestige first

935 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 47.9 | 47.9 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 48.7 | 48.7 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 48.8 | 48.8 | thin at home: wine, pies |
| hold sermon 2 (candles) | church | 31 | 49.1 | 51.6 | needs a church (build cost 64,471); thin at home: candles, furniture |
| hold banquet 4 | mansion | 17.5 | 51.7 | 51.7 | thin at home: wine, hop beer, ham |
| hold mass 2 (premium) | cathedral | 360 | 51.3 | 52.1 | needs a cathedral (build cost 247,190); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 3 | arena | 230 | 52.5 | 52.6 | needs a arena (build cost 25,413); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 53.1 | 53.1 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 54.0 | 54.0 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 54.2 | 54.2 | thin at home: hop beer |
| hold feast 2 | townhouse | 2.6 | 51.4 | 54.3 | needs a townhouse (build cost 6,798); thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.25 | 24 | - | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: furniture buy 2 @ 14.2, nets sell 1 @ 38.2, tools buy 3 @ 4.38; crew 0.1; est +18 a turn; stock: furniture 2 @ 14.2 (keep 145)
- best towns now: Caillechâtel +40, Bordetes +27, Clairas +25, Brunnham +24, Bremcop +24
- Caillechâtel would trade: beer sell 46 @ 4.42, furniture buy 2 @ 12.8, nets sell 2 @ 37.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.05 | 0.20 (20/turn) | lathes 1 (205.8->298.3), tackles 1 (152.25->212.8), beer 57 (3.18->3.84), casks 8 (5.62->8.03) | flax fibres 6 (5.78->8.84), cloth 38 (7.35->7.6), tiles 2 (3.28->4.35), tools 3 (4.77->4.98) | +227 |
| Heilegg | 826 | 0.22 | 0.70 (69/turn) | grindstones 1 (239.4->347.7), casks 9 (5.62->9.17), lead ore 5 (9.55->13.3), furniture 12 (11.76->13.39) | gold bars 1 (782.25->817), flax fibres 6 (5.88->8.84), pasties 2 (12.18->13.2), raw cloth 1 (6.2->6.93) | +221 |
| Clairas | 374 | 0.10 | 0.10 (10/turn) | sails 1 (645.75->802.75), nets 3 (35.6->37.43), lead ore 1 (9.55->13.77), tackles 1 (152.25->154.85) | flax fibres 6 (5.3->8.84), candles 1 (72.98->74), grain 26 (2.6->2.8), pasties 2 (12.71->13.2) | +189 |
| Boistot | 1230 | 0.43 | 0.10 (10/turn) | tackles 1 (152.25->305.9), lead ore 2 (9.55->12.25), slaked lime 1 (8.03->10.45), tallow 1 (20.79->22.04) | flax fibres 3 (5.93->8.84), wax 3 (21.42->22.8), candles 1 (72.98->74), raw cloth 1 (5.62->6.93) | +165 |
| Caillechâtel | 488 | 0.13 | 0.30 (29/turn) | beer 46 (3.18->5.03), medicine 1 (126->139.65), nets 9 (35.6->37.05), belts 1 (32.34->39.14) | flax fibres 6 (4.79->8.84), flax plants 28 (1.23->1.64), raw cloth 1 (5.78->6.93) | +141 |

**Best:** Vauxvais at about +227 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 3.38 | makes 56.0, uses 4.2, holds 128 (keeps 60): sells the surplus + 1/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 19 @ min 20.0 | makes 19.3, uses 2.1, holds 56 (keeps 30): sells the surplus + 2/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 285 @ 2.2, stop - |  | uses 734.9/turn (brewery 1, flax farm 1, household), makes 450.0, holds 279 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 34.6 | sell; ships offer 1 a turn abroad, so home sells 10 (was 11) |
| pasties | 3 @ 13.8, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 11 @ 1.1, stop - |  | uses 10.6/turn (observed), makes 0.0, holds 10 = 0.9 turns |
| rope |  | 2 @ min 72.0 |  |
| tools | 4 @ 6.2, stop 29 |  | uses 3.6/turn (retting pit 1), makes 0.0, holds 199 = 55.6 turns |

## Chain sizing

Mode HOLD, garments sold 14.8/turn (+2.3 exported); plan makes 19.3 garments a turn.
Labour: own 450, everything else 415, chain may buy 350 -> chain allowance 385, chain plan 384 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.81 | 5.82 |
| ret | 3 | 1.03 | 1.03 |
| spin | 4 | 2.13 | 2.13 |
| weave | 3 | 0.76 | 0.75 |
| sew | 2 | 0.47 | 0.47 |

Buffers: flax fibres 44/76, thread 277/222, cloth 0/75
- chain plan needed 656 labour, budget left 385: cut to 385 (sewing capped at 0.47)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
