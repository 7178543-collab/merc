# v2 shadow report

Turn 13429, 2026-10-20 22:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,523, prestige 3,394 (724 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 53 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.2 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 5, next step uses 46/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 63
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 162
- **timber**: build materials for park 1, net maker152202386007001 are in (266.1 held, 80 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 55% (EXPANSION), about 6 turns left; still to deliver: labour 117, limestone 27, timber 18; ready for labour
- **net maker152202386007001** 59% (INITIAL), about 5 turns left; still to deliver: labour 82, timber 62, tools 9; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 27 | 65.7 | 0 | off: covered |
| timber | 80 | 266.1 | 0 | off: covered; switch v1's buy off |
| tools | 9 | 199.8 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 37

## Notes

- labour: projection runs 92 over real use lately; planning 719, not 811

## Prestige spending, cheapest coin per prestige first

972 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 53.9 | 53.9 | thin at home: pasties, hop beer |
| maintain 1 | park | 0.5 | 50.4 | 54.4 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 55.2 | 55.2 | thin at home: hop beer, cured fish |
| hold sermon 2 (candles) | church | 31 | 52.7 | 55.3 | needs a church (build cost 71,481); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 55.4 | 55.4 |  |
| hold prayer 2 | chapel | 13 | 52.7 | 55.6 | needs a chapel (build cost 33,868); thin at home: furniture |
| hold sermon 2 | church | 24 | 53.0 | 56.4 | needs a church (build cost 71,481); thin at home: furniture |
| jousting 1 | arena | 170 | 57.4 | 57.5 | needs a arena (build cost 26,742); thin at home: protection, light armour, arms; needs weaponry skill |
| jousting 3 | arena | 230 | 57.6 | 57.7 | needs a arena (build cost 26,742); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 58.1 | 58.1 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 58.4 | 58.4 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 58.6 | 58.6 | thin at home: pasties, wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.032 | rope 2 | furniture 2 | -2 |
| linen snake | 0.0 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: furniture buy 2 @ 14.1, rope sell 4 @ 80.5; crew 0.1; est +43 a turn; stock: furniture 2 @ 14.1 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; stock: furniture 2 @ 14.2 (keep 145); best orders clear only 14 a turn after crew: ship stays at 0
- best towns now: Bedenis +43, Neuborn +43, Clarfranche +42, Disscester +38, Cobholme +35
- Bedenis would trade: furniture buy 2 @ 13.5, rope sell 3 @ 82.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bordees | 1112 | 0.39 | 0.10 (10/turn) | lathes 1 (210->275.5), axes 1 (14.8->15.86), butter 1 (63.53->65.55), copper ingots 1 (12.6->13.68) | wax 2 (18.06->23.18), stockfish 2 (120.75->125.4), mouldboards 1 (33.81->38.57), wool 1 (6.83->7.6) | +86 |
| Dortgart | 1045 | 0.35 | 0.10 (10/turn) | glass ingots 2 (48.93->53.67), dye 1 (43.89->48.92), rope 2 (73->75.52), axes 1 (14.8->16.53) | jewellery 2 (59.33->75.05), spinning wheels 1 (224.7->247), stockfish 1 (113.4->125.4), resin 1 (1.06->2.22) | +80 |
| Neuborn | 780 | 0.21 | 0.50 (52/turn) | rope 4 (73->79.33), beer 51 (3.14->3.93), soap 1 (92.4->100.7), charcoal 12 (2.03->4.33) | stockfish 1 (113.4->125.4), flour 2 (14.38->16.43), flax plants 1 (1.03->1.56), resin 1 (1.45->2.22) | +79 |
| Toqueque | 642 | 0.18 | 0.20 (21/turn) | butter 1 (63.53->68.4), rope 1 (73->76.95), copper ingots 1 (12.6->13.49), hop beer 3 (8.4->8.84) | spinning wheels 1 (228.9->247), stockfish 2 (116.55->125.4), flax fibres 19 (5.1->6.25), jewellery 1 (66.67->75.05) | +77 |
| Heidlowe | 662 | 0.18 | 0.20 (21/turn) | bellows 1 (289.8->319.2), glass ingots 2 (48.93->56.05), seeds 9 (1.78->3.32), dye 1 (43.89->48.92) | flax fibres 29 (5.62->6.25), gears 1 (62.48->68.4), stockfish 1 (120.75->125.4), jewellery 1 (72.98->75.05) | +76 |

**Best:** Bordees at about +86 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 25.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 22 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 269 @ 2.2, stop - |  | uses 719.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.2 |  |
| pasties | 3 @ 15.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 9.8/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 4 @ min 71.0 | makes 2.2, uses 0.0, holds 22 (keeps 0): sells the surplus + 2/turn of the excess |
| timber |  | 8 @ min 6.8 |  |
| tools | 6 @ 6.2, stop 45 |  | uses 5.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 36.0 turns |

## Chain sizing

Mode HOLD, garments sold 20.8/turn (+0.0 exported); plan makes 22.1 garments a turn.
Labour: own 450, everything else 425, chain may buy 350 -> chain allowance 375, chain plan 374 (-6 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.08 | 5.14 |
| ret | 3 | 0.90 | 0.91 |
| spin | 4 | 1.86 | 1.88 |
| weave | 3 | 0.90 | 0.87 |
| sew | 2 | 0.57 | 0.54 |

Buffers: flax fibres 52/73, thread 368/214, cloth 5/87
- chain plan needed 503 labour, budget left 375: cut to 375 (sewing capped at 0.54)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
