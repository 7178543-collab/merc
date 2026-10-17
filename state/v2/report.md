# v2 shadow report

Turn 13338, 2026-10-17 03:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 15,273, prestige 3,244 (574 free, +3.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 198 | 0 | 19 | 0 | 0 | min_holding 60, sell 20, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 271 | 274 | 716 | 0 | 8 | buy 271, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 42 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 11 | 10 | 10 | 1 | 0 | buy 11, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.2 turns (holds 7, next step uses 31/turn) -> v2: check the step that makes it
- **porterage**: logging camp w/ tool ran short of porterage (buy is live (11 @ 1.1), 10 bought last turn); labour need rises ~22/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 76
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 198

## Notes

- labour: projection runs 72 over real use lately; planning 722, not 794

## Prestige spending, cheapest coin per prestige first

1063 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 55.2 | 55.2 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.0 | 56.0 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 56.3 | 56.3 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 57.3 | 57.3 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 57.9 | 57.9 |  |
| hold banquet 4 (pies) | mansion | 18 | 59.0 | 59.0 | thin at home: wine, stockfish |
| jousting 1 | arena | 170 | 59.1 | 59.2 | needs a arena (build cost 23,914); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 59.6 | 59.6 | running |
| hold prayer 2 | chapel | 13 | 57.6 | 60.0 | needs a chapel (build cost 30,586); thin at home: furniture |
| hold banquet 4 (premium) | mansion | 20 | 60.3 | 60.3 | thin at home: wine, stockfish, premium cheese, premium ham |
| hold sermon 2 (candles) | church | 31 | 57.7 | 60.3 | needs a church (build cost 77,232); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 5 | -110 |

## Ship plans (this turn's world prices)

- **linen snake** on Heilegg: candles buy 1 @ 74.5, nets sell 5 @ 40.8; crew 0.1; est +29 a turn
- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Caillechâtel +40, Marmont +37, Etallaen +32, Heilegg +29, Fulkirch +26
- Caillechâtel would trade: candles buy 1 @ 69.0, nets sell 9 @ 38.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 1.00 (98/turn) | bread 129 (2.29->3.08), charcoal 11 (1.78->4.67), timber 22 (6.35->8.55), thread 13 (4.82->6.08) | spinning wheels 0 (260.4->281.2), lead bars 0 (8.51->10.64), flax plants 0 (0.65->1.41), tools 2 (4.91->5.15) | +170 |
| Caillechâtel | 488 | 0.13 | 0.10 (10/turn) | nets 9 (34.2->37.24), beer 20 (2.95->4.14), garments 10 (19.71->21.09), wine 3 (6.25->8.5) | candles 1 (71.4->81), spinning wheels 1 (275.1->281.2), wool 2 (8.09->10.07), cloth 8 (8.56->8.75) | +81 |
| Grandgues | 152 | 0.04 | 0.30 (30/turn) | bread 142 (2.29->2.53), charcoal 13 (1.78->3.06), beer 20 (2.95->3.52), rope 1 (79.5->87.4) | pies 2 (17.64->19), wool 1 (9.13->10.07), salt 1 (4.12->4.22), thread 1 (4.6->4.88) | +73 |
| Karlmoor | 787 | 0.21 | 0.20 (20/turn) | nets 5 (34.2->40.28), garments 13 (19.71->21.09), tools 8 (4.5->5.98), beer 20 (2.95->3.5) | candles 1 (78.23->81), cloth 10 (8.29->8.75) | +58 |
| Gottweiler | 1135 | 0.39 | 0.20 (20/turn) | spinning wheels 1 (319.2->347.7), butter 1 (70.88->83.6), glassware 1 (49.98->54.62) | bellows 1 (241.5->258.4), cloth 10 (8.14->8.75), honey 2 (7.25->8.03), bronze ingots 1 (22.05->22.8) | +57 |

**Best:** Rouhomme at about +170 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 20 @ min 3.7 | makes 28.0, uses 19.2, holds 198 (keeps 60): sells the surplus + 11/turn of the excess |
| candles | 3 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 4 = 3.0 turns |
| cured meat | 7 @ 24.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 22 = 3.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 272 @ 2.2, stop - |  | uses 722.1/turn (brewery 1, flax farm 1, household), makes 450.0, holds 271 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 34.0 | makes 9.0, uses 0.0, holds 42 (keeps 15): sells the surplus + 1/turn of the excess |
| porterage | 11 @ 1.1, stop - |  | uses 11.0/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 6 @ min 77.5 | makes 4.5, uses 0.0, holds 19 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 9 = 9.3 turns |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (retting pit 1), makes 0.0, holds 199 = 50.4 turns |

## Chain sizing

Mode HOLD, garments sold 19.0/turn (+0.0 exported); plan makes 17.2 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 389 (+7 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.18 | 6.22 |
| ret | 3 | 1.10 | 1.11 |
| spin | 4 | 2.26 | 2.28 |
| weave | 3 | 0.69 | 0.68 |
| sew | 2 | 0.39 | 0.42 |

Buffers: flax fibres 57/85, thread 381/250, cloth 7/68
- chain plan needed 585 labour, budget left 389: cut to 389 (sewing capped at 0.42)

## Self-diagnosis

- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
