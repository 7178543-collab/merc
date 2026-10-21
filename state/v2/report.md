# v2 shadow report

Turn 13438, 2026-10-21 07:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,402, prestige 3,528 (858 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 49 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.4 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 1, next step uses 42/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 65
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 167
- **timber**: build materials for net maker152202386007001 are in (321.4 held, 54 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **net maker152202386007001** 64% (INITIAL), about 5 turns left; still to deliver: labour 72, timber 54, tools 8; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 54 | 321.4 | 0 | off: covered; switch v1's buy off |
| tools | 8 | 199.5 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 15

## Notes

- labour: projection runs 96 over real use lately; planning 714, not 806

## Prestige spending, cheapest coin per prestige first

963 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 3 (pies) | mansion | 8 | 52.1 | 52.1 | thin at home: pasties, hop beer, pies |
| hold sermon 2 (candles) | church | 31 | 50.6 | 53.2 | needs a church (build cost 70,548); thin at home: candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 55.5 | 55.5 |  |
| hold prayer 2 | chapel | 13 | 52.7 | 55.5 | needs a chapel (build cost 32,936); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 55.8 | 55.8 | thin at home: hop beer, cured fish |
| hold sermon 2 | church | 24 | 52.5 | 55.9 | needs a church (build cost 70,548); thin at home: furniture |
| hold banquet 4 (pies) | mansion | 18 | 56.4 | 56.4 | thin at home: pasties, hop beer, wine, pies |
| hold mass 1 | cathedral | 180 | 56.3 | 58.1 | needs a cathedral (build cost 282,690); thin at home: jewellery, glassware, candles |
| hold banquet 2 (pies) | mansion | 7 | 58.3 | 58.3 | thin at home: pasties, wine, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 58.5 | 58.5 | thin at home: hop beer |
| jousting 3 | arena | 230 | 58.6 | 58.7 | needs a arena (build cost 26,516); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.092 | - | furniture 1 | -14 |
| linen snake | 0.1 / 0.10 | 10 | 185801747 | 0.08 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn
- best towns now: Karlmoor +41, Bordetes +24, Bedenis +24, Etallaen +21, Cobholme +18
- Karlmoor would trade: candles buy 1 @ 71.5, garments sell 15 @ 23.4, pasties buy 1 @ 13.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.21 | 0.30 (31/turn) | garments 21 (20.12->24.51), beer 51 (3.16->4.48), nets 3 (37.8->41.99), light armour 2 (81.38->86.45) | glass ingots 1 (46.62->69.35), tin ingots 1 (31.92->36.48), candles 1 (72.98->75) | +184 |
| Bordetes | 831 | 0.23 | 0.20 (20/turn) | cheese 21 (8.51->11.78), rope 4 (74->80.27), wrought iron 3 (12.81->16.15), slaked lime 1 (12.6->17.1) | glass ingots 1 (42.21->69.35), spinning wheels 2 (208.95->220.4), wine 26 (5.88->6.55), nails 11 (5.06->5.56) | +164 |
| Gottweiler | 1135 | 0.40 | 0.20 (20/turn) | silver bars 1 (205.8->304), coats 2 (61.43->70.3), thread 9 (4.64->5.22) | ploughs 1 (53.03->71.25), cheese 18 (6.83->7.6), glass ingots 1 (64.58->69.35), butter 1 (56.18->59.38) | +144 |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | windows 1 (485.1->565.25), silver bars 1 (205.8->229.9), seeds 8 (2.14->4.27), yarn 9 (4.05->4.94) | spirits 1 (15.75->22.99), cheese 23 (7.04->7.6), candles 1 (71.4->75), garments 2 (18.9->20.2) | +143 |
| Caillechâtel | 488 | 0.13 | 0.20 (20/turn) | beer 31 (3.16->5.75), nets 5 (37.8->38.38), malt 1 (5.12->6.32), yarn 4 (4.05->4.33) | glass ingots 1 (44.31->69.35), lead ore 1 (6.3->10.54), hinges 1 (28.56->32.11), iron ore 1 (3->4.26) | +101 |

**Best:** Etallaen at about +184 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 264 @ 2.2, stop - |  | uses 714.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.8 |  |
| pasties | 3 @ ?, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.0/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 5 @ min 72.0 | makes 2.2, uses 0.0, holds 34 (keeps 0): sells the surplus + 3/turn of the excess |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 29 |  | uses 3.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 55.3 turns |

## Chain sizing

Mode HOLD, garments sold 21.7/turn (+0.0 exported); plan makes 21.7 garments a turn.
Labour: own 450, everything else 418, chain may buy 350 -> chain allowance 382, chain plan 382 (+6 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.24 | 5.37 |
| ret | 3 | 0.93 | 0.96 |
| spin | 4 | 1.92 | 1.97 |
| weave | 3 | 0.85 | 0.85 |
| sew | 2 | 0.53 | 0.53 |

Buffers: flax fibres 50/72, thread 305/212, cloth 1/85
- chain plan needed 529 labour, budget left 382: cut to 382 (sewing capped at 0.53)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
