# v2 shadow report

Turn 13464, 2026-10-22 09:05. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,732, prestige 3,569 (899 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 130 | 0 | 4 | 0 | 0 | min_holding 60, sell 54, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 65 | 0 | 2 | 0 | 0 | min_holding 30, sell 26, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 285 | 296 | 740 | 0 | 6 | buy 285, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 20 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 34.6 |
| porterage | 10 | 11 | 10 | 0 | 1 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 45/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 176

## Notes

- labour: projection runs 75 over real use lately; planning 740, not 807

## Prestige spending, cheapest coin per prestige first

937 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 48.4 | 48.4 | thin at home: wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.4 | 49.4 | thin at home: pies |
| hold banquet 2 (pies) | mansion | 7 | 49.7 | 49.7 | thin at home: wine, pies |
| hold sermon 2 (candles) | church | 31 | 49.1 | 51.6 | needs a church (build cost 66,399); thin at home: candles, furniture |
| hold banquet 4 | mansion | 17.5 | 52.0 | 52.0 | thin at home: wine, ham |
| jousting 3 | arena | 230 | 52.3 | 52.5 | needs a arena (build cost 26,011); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 53.8 | 53.8 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 54.3 | 54.3 |  |
| hold feast 2 | townhouse | 2.6 | 51.5 | 54.3 | needs a townhouse (build cost 6,630); thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 54.8 | 54.8 |  |
| hold sermon 2 | church | 24 | 51.5 | 54.8 | needs a church (build cost 66,399); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.268 | nets 1 | furniture 5 | -49 |
| linen snake | 0.2 / 0.20 | 19 | 185801747 | 0.116 | - | furniture 2 | -29 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: furniture buy 11 @ 14.2, nets sell 1 @ 38.8, rope sell 2 @ 75.5, tools buy 3 @ 4.38; crew 0.1; est +154 a turn; stock: furniture 11 @ 14.2 (keep 145)
- **linen snake** on Neuborn: furniture buy 11 @ 14.4; crew 0.1; est +122 a turn; stock: furniture 11 @ 14.4 (keep 145)
- best towns now: Calange +208, Essenbrucke +198, Marmont +188, Gosschweig +179, Herschweig +176
- Calange would trade: furniture buy 11 @ 9.65, rope sell 2 @ 79.5, tools buy 3 @ 4.68; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Chatgnan | 728 | 0.19 | 0.10 (10/turn) | looms 1 (740.25->1064), rope 2 (63.11->77.42), chisels 1 (14.07->16.62), pasties 1 (10.4->12.25) | herbs 1 (27.3->29.26), iron ore 1 (2.04->3.61), flax plants 3 (1.18->1.68), lead ore 1 (10.45->11.78) | +354 |
| Bedenis | 566 | 0.15 | 0.10 (10/turn) | plate armour 1 (1044.75->1244.5), tapestries 1 (614.25->650.75), rope 2 (63.11->73.15), chisels 1 (14.07->18.14) | gold bars 1 (782.25->817), slaked lime 2 (6.83->10.64), tools 24 (4.62->4.94), malt 3 (6.51->7.22) | +310 |
| Heilegg | 826 | 0.22 | 0.30 (29/turn) | plate armour 1 (1044.75->1168.5), rope 2 (63.11->75.52), grindstones 1 (277.2->296.4), coats 3 (55.12->58.42) | gold bars 1 (782.25->817), pasties 2 (12.18->13.2) | +208 |
| Hanbrücken | 531 | 0.14 | 0.50 (49/turn) | tackles 1 (168->233.7), grindstones 1 (277.2->338.2), rope 2 (63.11->73.15), lead ore 4 (13.65->16.53) | glass ingots 1 (45.15->48.92), canvas 1 (26.67->27.93), grain 26 (2.48->2.8), pasties 2 (12.5->13.2) | +188 |
| Essenbrucke | 584 | 0.15 | 0.20 (20/turn) | lathes 1 (153.3->210.9), plate armour 1 (1044.75->1073.5), rope 2 (63.11->75.52), garments 13 (19.5->21.28) | gold ore 1 (116.55->152), grain 26 (2.27->2.8), bellows 1 (281.4->285), cloth 4 (7.09->7.45) | +182 |

**Best:** Chatgnan at about +354 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 3.38 | makes 56.0, uses 4.2, holds 130 (keeps 60): sells the surplus + 2/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 24 @ min 20.0 | makes 23.0, uses 2.1, holds 65 (keeps 30): sells the surplus + 4/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 290 @ 2.2, stop - |  | uses 740.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 285 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 34.6 | sell; ships offer 1 a turn abroad, so home sells 10 (was 9) |
| pasties | 3 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.3/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 66.0 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 53.7 turns |

## Chain sizing

Mode HOLD, garments sold 14.8/turn (+2.3 exported); plan makes 23.0 garments a turn.
Labour: own 450, everything else 403, chain may buy 350 -> chain allowance 397, chain plan 398 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.54 | 5.57 |
| ret | 3 | 0.98 | 0.99 |
| spin | 4 | 2.03 | 2.04 |
| weave | 3 | 0.90 | 0.89 |
| sew | 2 | 0.56 | 0.56 |

Buffers: flax fibres 45/73, thread 289/216, cloth 0/89
- chain plan needed 605 labour, budget left 397: cut to 397 (sewing capped at 0.56)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R3: net maker152202386007001 (net maker) finished but idle 6 turns (no recipe) (held back: failsafe level 1: reduce-only, would start make nets 1 at 0.5 (storehouse provider))
