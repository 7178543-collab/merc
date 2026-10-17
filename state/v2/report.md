# v2 shadow report

Turn 13344, 2026-10-17 09:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,770, prestige 3,262 (592 free, +3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 157 | 0 | 19 | 0 | 0 | min_holding 60, sell 17, sell @ 3.96 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 274 | 273 | 723 | 26 | 0 | buy 274, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 28 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 35.6 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.8 turns (holds 24, next step uses 31/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 49 coin last turn (crew 0.50) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 78
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 73 over real use lately; planning 749, not 822

## Prestige spending, cheapest coin per prestige first

1057 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 57.1 | 57.1 | thin at home: wine, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 57.4 | 57.4 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 57.6 | 57.6 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 57.9 | 57.9 |  |
| hold prayer 2 | chapel | 13 | 56.4 | 58.7 | needs a chapel (build cost 29,536); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 57.0 | 59.5 | needs a church (build cost 76,127); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 56.7 | 60.0 | needs a church (build cost 76,127); thin at home: jewellery, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 60.5 | 60.5 | thin at home: cured fish |
| jousting 1 | arena | 170 | 60.4 | 60.5 | needs a arena (build cost 23,269); thin at home: protection, light armour, arms; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 58.2 | 61.1 | needs a townhouse (build cost 7,900); thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 61.6 | 61.6 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.5 / 0.50 | 49 | - | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Karlmoor +80, Caillechâtel +36, Toqueque +26, Birkeningen +26, Grandgues +25
- Karlmoor would trade: nets sell 8 @ 46.4, rope sell 2 @ 72.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Karlmoor | 787 | 0.20 | 0.20 (20/turn) | nets 8 (36.6->49.88), stockfish 1 (108.15->133), garments 13 (19.43->21.09), tackles 1 (169.05->182.4) | wool 5 (10.34->13.11), grain 13 (2.69->3.36) | +182 |
| Vauxvais | 204 | 0.05 | 0.10 (10/turn) | rope 3 (65.5->76.47), soap 2 (74.03->85.02), garments 13 (19.43->20.71), flax fibres 4 (4.73->5.89) | beer 53 (3.46->4.16), wool 4 (10.5->13.11), thread 19 (5.23->5.7), pies 1 (17.43->19.76) | +128 |
| Neuborn | 780 | 0.20 | 0.90 (88/turn) | garments 13 (19.43->26.03), charcoal 13 (1.75->4.75), timber 19 (6.35->9.88), flax fibres 4 (4.73->5.89) | candles 1 (76.65->81), wool 1 (9.61->13.11), cured meat 6 (22.05->22.8), thread 10 (5.25->5.7) | +127 |
| Toqueque | 642 | 0.17 | 0.30 (29/turn) | tackles 1 (169.05->214.7), nets 4 (36.6->41.04), wrought iron 4 (13.86->17.48), rope 1 (65.5->78.85) | dyed cloth 2 (6.04->9.97), wool 2 (10.19->13.11), bricks 1 (7.35->10.92), garments 2 (21.84->22.2) | +122 |
| Pontmont | 341 | 0.09 | 0.20 (20/turn) | bellows 1 (319.2->345.8), rope 3 (65.5->69.83), flour 1 (16.59->19.38), tools 16 (4.5->4.71) | beer 53 (3.4->4.16), bricks 1 (6.56->10.92), wool 2 (11.45->13.11), candles 1 (79.8->81) | +85 |

**Best:** Karlmoor at about +182 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 16 @ min 4.26 | makes 28.0, uses 19.2, holds 157 (keeps 60): sells the surplus + 7/turn of the excess |
| cured meat | 12 @ 23.8, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 10 = 1.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 299 @ 2.2, stop - |  | uses 748.6/turn (brewery 1, flax farm 1, household), makes 450.0, holds 274 = 0.9 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 35.6 |  |
| porterage | 11 @ 1.1, stop - |  | uses 11.1/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 8 @ min 67.0 | makes 4.5, uses 0.0, holds 41 (keeps 0): sells the surplus + 3/turn of the excess |
| timber |  | 29 @ min 6.7 | makes 8.4, uses 0.0, holds 605 (keeps 350): sells the surplus + 21/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 50.0 turns |

## Chain sizing

Mode HOLD, garments sold 16.1/turn (+0.0 exported); plan makes 17.6 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 390 (+3 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.30 | 6.20 |
| ret | 3 | 1.12 | 1.10 |
| spin | 4 | 2.31 | 2.27 |
| weave | 3 | 0.66 | 0.68 |
| sew | 2 | 0.39 | 0.43 |

Buffers: flax fibres 58/85, thread 391/250, cloth 24/68
- chain plan needed 583 labour, budget left 389: cut to 389 (sewing capped at 0.43)

## Self-diagnosis

- R1: cured meat slot dry: 10.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 6 @ 29, home ask 22.8; our bid is already at/over the ask (sellers too thin)
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
