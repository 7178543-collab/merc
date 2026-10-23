# v2 shadow report

Turn 13495, 2026-10-23 16:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,334, prestige 3,598 (478 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 99 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 116 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 102 | 26 | 28 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 0 | 0 | 500 | 88 | 0 | buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 9 | 10 | 5 | 0 | 5 | buy 9, buy @ 1.1 |

**0 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 53
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 156

## Notes

- labour: projection runs 100 over real use lately; planning 588, not 688

## Prestige spending, cheapest coin per prestige first

906 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 43.5 | 43.5 | running |
| hold banquet 3 (pies) | mansion | 8 | 46.9 | 46.9 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 47.9 | 47.9 | thin at home: hop beer, wine |
| hold banquet 2 (pies) | mansion | 7 | 49.2 | 49.2 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.6 | 50.6 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 51.1 | 51.1 | thin at home: wine, hop beer, ham |
| hold banquet 3 (meat) | mansion | 7.6 | 51.4 | 51.4 | thin at home: hop beer, cured meat |
| hold banquet 2 (fish) | mansion | 6.8 | 52.2 | 52.2 | thin at home: wine |
| jousting 3 | arena | 230 | 52.0 | 52.2 | needs a arena (build cost 23,540); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 49.8 | 52.5 | needs a chapel (build cost 29,518); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 50.4 | 53.0 | needs a church (build cost 64,071); thin at home: jewellery, candles, furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 53.1 | 53.1 | thin at home: wine, cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 13 @ 13.8; crew 0.1; est +155 a turn; stock: furniture 13 @ 13.8 (keep 145)
- **Flax Wyrm** on Caillechâtel: furniture buy 10 @ 12.1; crew 0.1; est +134 a turn; stock: furniture 10 @ 12.1 (keep 145)
- best towns now: Bedenis +234, Hofkirchen +224, Herschweig +198, Gosschweig +181, Clairas +177
- Bedenis would trade: furniture buy 16 @ 11.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~91 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 0.60 (55/turn) | beer 60 (3.16->4.89), wrought iron 6 (12.71->16.62), glass ingots 2 (57.23->68.4), wine 8 (6.14->7.46) | acid 1 (136.5->140.6), gears 2 (60.38->61.75), salt 4 (4.07->4.71) | +128 |
| Gosschweig | 1099 | 0.34 | 0.20 (18/turn) | garments 9 (18.4->24.13), flour 2 (19.53->28.5), wax 4 (20.79->23.56), cheese 8 (6.3->7.65) | premium ham 1 (260.4->294.5), candles 1 (63.53->70.5), spirits 1 (14.91->17.1) | +127 |
| Rouhomme | 368 | 0.09 | 0.40 (37/turn) | looms 1 (682.5->741), charcoal 13 (1.69->3.29), thread 7 (3.35->5.03), beer 60 (3.16->3.42) | spinning wheels 1 (222.6->235.6), lead bars 8 (12.08->12.92), wheels 3 (17.64->19.19), candles 1 (68.78->70.5) | +114 |
| Briclives | 1041 | 0.31 | 0.60 (55/turn) | beer 60 (3.16->4.6), soap 1 (91.88->122.55), malt 6 (6.83->11.11), arms 10 (26.46->27.74) | tools 1 (4.26->4.74) | +107 |
| Hanstein | 380 | 0.09 | 0.30 (27/turn) | thread 69 (3.35->4.41), timber 2 (5.76->8.88), charcoal 12 (1.69->2.62), dyed yarn 1 (5.93->7.22) | flax plants 66 (1.41->1.74), salt 4 (4.33->4.71), honey 4 (7.35->7.5), resin 2 (1.67->1.88) | +85 |

**Best:** Hofkirchen at about +128 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 84 @ min 3.38 |  |
| cured meat | 2 @ 22.6, stop 4 |  | uses 0.9/turn (mansion 1), makes 0.0, holds 0 = 0.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 13 @ 2.4, stop 32 |  | uses 8.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 23 @ min 20.0 | makes 4.4, uses 2.1, holds 116 (keeps 30): sells the surplus + 21/turn of the excess |
| grain | 76 @ 3.7, stop 169 |  | uses 42.2/turn (brewery 1), makes 0.0, holds 102 = 2.4 turns |
| labour | 88 @ 2.2, stop - |  | uses 588.5/turn (brewery 1, flax farm 1, household), makes 500.0, holds 0 = 0.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 13.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 5 @ 1.1, stop - |  | uses 4.9/turn (observed), makes 0.0, holds 9 = 1.8 turns |
| rope |  | 3 @ min 73.0 |  |
| timber |  | 10 @ min 6.5 | makes 8.4, uses 0.0, holds 376 (keeps 350): sells the surplus + 1/turn of the excess |
| tools | 4 @ 6.2, stop 28 |  | uses 3.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 57.2 turns |

## Goal: business value (shadow)
- no plan: goal plan failed: KeyError: 'value'

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 17.2 garments a turn.
Labour: own 500, everything else 460, chain may buy 350 -> chain allowance 390, chain plan 390 (+162 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.34 | 6.25 |
| ret | 3 | 0.87 | 1.11 |
| spin | 4 | 1.59 | 2.29 |
| weave | 3 | 0.25 | 0.67 |
| sew | 2 | 0.11 | 0.42 |

Buffers: flax fibres 50/82, thread 320/242, cloth 23/67
- chain plan needed 590 labour, budget left 390: cut to 390 (sewing capped at 0.42)

## Self-diagnosis

- R1: cured meat slot dry: 0.0 held, 0.9 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 21.6 (held back: failsafe level 3: reduce-only, would buy 2 @ 22 (ask 21.6, cap 42.0))
- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~63 a turn at 19.6, we sold 0 with 86 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
- R7 stale ask: timber ask 6.5 over the market for 3 turns: the town trades ~85 a turn at 6.2, we sold 0 with 26 over what we keep; floor 6.5 (config sell_floor / unit cost) is at or over the market: Taylor's call
