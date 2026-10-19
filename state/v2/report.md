# v2 shadow report

Turn 13396, 2026-10-19 13:12. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,568, prestige 3,380 (710 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 207 | 0 | 4 | 0 | 0 | min_holding 60, sell 38, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 187 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 0 | 0 | 419 | 0 | 31 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 21 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.6 |
| porterage | 7 | 7 | 7 | 30 | 0 | buy 7, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: logging camp w/ tool, quarry 1 ran short of porterage (buy is live (7 @ 1.1), 7 bought last turn); labour need rises ~172/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 7, short of ~37 needed -> v2: buy 37

## Notes

- labour: projection runs 136 over real use lately; planning 423, not 559

## Prestige spending, cheapest coin per prestige first

1005 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.9 | 45.9 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 54.5 | 54.5 | thin at home: wine, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 54.7 | 54.7 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 52.7 | 55.3 | needs a chapel (build cost 31,684); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 55.5 | 55.5 | thin at home: pasties, wine |
| hold feast 2 | townhouse | 2.6 | 52.9 | 55.6 | needs a townhouse (build cost 6,836); thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 56.2 | 56.2 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 56.3 | 56.3 |  |
| hold banquet 3 (pies) | mansion | 8 | 56.5 | 56.5 | thin at home: pasties |
| hold sermon 2 (candles) | church | 31 | 54.3 | 57.2 | needs a church (build cost 80,446); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 53.6 | 57.3 | needs a church (build cost 80,446); thin at home: jewellery, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 57.4 | 57.4 | thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 120102307 | 0.312 | beer 39 | furniture 1 | 15 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: furniture buy 8 @ 14.2; crew 0.1; est +88 a turn; stock: furniture 8 @ 14.2 (keep 145)
- **linen snake** on Grandgues: furniture buy 8 @ 14.2; crew 0.1; est +88 a turn; stock: furniture 8 @ 14.2 (keep 145)
- best towns now: Karlmoor +136, Toqueque +124, Caillechâtel +123, Chatgnan +121, Briclives +118
- Karlmoor would trade: furniture buy 8 @ 13.2, nets sell 6 @ 42.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~93 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Brunnham | 1281 | 0.44 | 0.30 (28/turn) | grindstones 1 (443.1->536.75), nets 3 (35.6->39.9), tools 16 (4.1->4.73) | bellows 1 (264.6->285), candles 1 (69.3->79.5), salt 9 (4.24->5.56) | +129 |
| Rouhomme | 368 | 0.09 | 0.70 (65/turn) | bread 149 (2.06->2.74), timber 11 (6.2->8.84), cheese 14 (5.35->5.61), tar 2 (10.08->11.4) | bellows 1 (254.1->285), candles 1 (72.45->79.5), lead bars 10 (12.08->12.82), flax fibres 3 (5.57->6.65) | +127 |
| Vauxvais | 204 | 0.05 | 0.40 (37/turn) | bread 149 (2.06->2.66), beer 36 (2.75->3.02), tools 16 (4.1->4.5), cheese 5 (5.35->6.46) | flax fibres 10 (5.57->6.65), thread 9 (5.06->5.55), salt 4 (4.83->5.56), candles 1 (77.7->79.5) | +102 |
| Chatgnan | 728 | 0.18 | 0.20 (19/turn) | beer 36 (2.75->3.97), flax fibres 4 (4.5->6.6), varnish 2 (17.64->19.38), rope 1 (76.5->79.33) | bellows 1 (249.9->285), thread 16 (4.45->5.55), slaked lime 1 (6.51->7.65), yarn 3 (3.97->4.26) | +96 |
| Hofkirchen | 991 | 0.29 | 0.20 (19/turn) | tools 16 (4.1->4.45), wax 4 (22.47->22.8) | plate armour 1 (1470->1501), bellows 1 (268.8->285), flax fibres 14 (5.41->6.65), salt 9 (4.22->5.56) | +78 |

**Best:** Brunnham at about +129 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 34 @ min 3.54 | makes 28.0, uses 4.2, holds 207 (keeps 60): sells the surplus + 10/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 20.8 | makes 3.3, uses 2.1, holds 187 (keeps 30): sells the surplus + 13/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 423.1/turn (brewery 1, flax farm 1, household), makes 450.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.6 |  |
| pasties | 3 @ 15.3, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 37 @ 1.1, stop - |  | uses 36.9/turn (observed), makes 0.0, holds 7 = 0.2 turns |
| rope |  | 5 @ min 74.5 | makes 2.2, uses 0.0, holds 41 (keeps 0): sells the surplus + 3/turn of the excess |
| tools | 3 @ 6.2, stop 22 |  | uses 2.6/turn (retting pit 1), makes 0.0, holds 199 = 75.8 turns |

## Chain sizing

Mode HOLD, garments sold 9.2/turn (+0.0 exported); plan makes 3.3 garments a turn.
Labour: own 450, everything else 512, chain may buy 350 -> chain allowance 350, chain plan 138 (+10 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.40 | 2.55 |
| ret | 3 | 0.43 | 0.45 |
| spin | 4 | 0.88 | 0.98 |
| weave | 3 | 0.12 | 0.13 |
| sew | 2 | 0.08 | 0.08 |

Buffers: flax fibres 58/48, thread 392/141, cloth 17/14

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 1 (limited by porterage)
