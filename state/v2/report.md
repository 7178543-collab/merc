# v2 shadow report

Turn 13483, 2026-10-23 04:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,703, prestige 3,616 (496 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 107 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 137 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 187 | 187 | 677 | 0 | 10 | buy 187, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 21, next step uses 32/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 180

## Notes

- labour: projection runs 75 over real use lately; planning 702, not 777

## Prestige spending, cheapest coin per prestige first

918 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 3 (pies) | mansion | 8 | 48.8 | 48.8 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 50.6 | 50.6 | thin at home: hop beer, wine |
| hold banquet 3 (fish) | mansion | 7.6 | 51.5 | 51.5 | thin at home: hop beer |
| jousting 3 | arena | 230 | 53.0 | 53.2 | needs a arena (build cost 24,929); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 50.9 | 53.4 | needs a church (build cost 64,794); thin at home: candles, furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 53.6 | 53.6 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 51.3 | 54.1 | needs a chapel (build cost 31,140); thin at home: furniture |
| hold banquet 4 | mansion | 17.5 | 54.2 | 54.2 | thin at home: wine, hop beer, ham |
| hold banquet 1 (fish) | mansion | 4.2 | 54.5 | 54.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 54.7 | 54.7 | thin at home: wine, pies |
| hold sermon 2 | church | 24 | 52.4 | 55.6 | needs a church (build cost 64,794); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.32 | 0.50 (50/turn) | beer 55 (3.18->4.99), glass ingots 2 (55.12->68.4), lead ore 2 (8.72->12.35), flax fibres 3 (4.69->6.17) | cheese 9 (5.15->5.75), blades 2 (11.97->12.54), garments 2 (19.32->19.9), candles 1 (71.4->72) | +102 |
| Gotthafen | 964 | 0.30 | 0.20 (20/turn) | medicine 1 (140.7->205.2), lead ore 2 (8.72->13.01), casks 4 (5.72->7.41), thread 7 (3.84->4.37) | candles 1 (66.67->72), wine 8 (5.72->6.65), canvas 3 (30.45->31.35), resin 2 (1.23->1.88) | +87 |
| Neuborn | 780 | 0.21 | 0.10 (10/turn) | grain 8 (2.58->3.8), flour 2 (19.74->22.61), dyed yarn 1 (7.3->7.65) | windows 1 (447.3->503.5), ham 1 (57.75->68.4), cheese 9 (4.94->5.75), slaked lime 1 (7.04->7.84) | +78 |
| Bordees | 1112 | 0.38 | 0.10 (10/turn) | leather 1 (27.3->33.06), wheels 1 (18.06->21.47), nets 2 (35->36.67), chisels 2 (15.33->15.96) | looms 1 (520.8->584.25), candles 1 (71.4->72), wine 6 (6.25->6.65) | +71 |
| Heilegg | 826 | 0.23 | 0.50 (50/turn) | beer 55 (3.18->3.88), grindstones 1 (283.5->296.4), lead ore 2 (8.72->12.92), nets 8 (35->35.72) | premium ham 1 (277.2->309.7), candles 1 (70.35->72), cheese 9 (5.41->5.75) | +60 |

**Best:** Hofkirchen at about +102 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 37 @ min 20.0 | makes 16.4, uses 2.1, holds 137 (keeps 30): sells the surplus + 23/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 202 @ 2.2, stop - |  | uses 701.7/turn (brewery 1, flax farm 1, household), makes 500.0, holds 187 = 0.9 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 13.1, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.4/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 77.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 53.2 turns |

## Goal: business value (shadow)
- Value now 15.9k (cash + stock at home prices); +73/turn over 6 turns, -107/turn over 24 turns.
- Limits: cash flow >= +96/turn, prestige >= -0.81/turn (after 236 tax and crew).
- Today's settings: value +37/turn, cash +35/turn, prestige -1.49/turn - breaks the prestige floor and cash floor.
- Plan: value +102/turn, cash +331/turn, prestige -0.81/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.50 -> 1.00: +23/turn
  - logging camp w/ tool 7.00 -> 2.92: +11/turn
  - quarry 1 0.00 -> 0.08: +4/turn
  - sewing shop 1 0.40 -> 0.05: -29/turn
  - weavery 1 0.67 -> 0.09: +38/turn
  - spinnery 1 2.05 -> 1.54: +31/turn
  - retting pit 1 1.00 -> 0.75: +5/turn
  - flax farm 1 5.61 -> 4.20: +15/turn
  - mansion 1 0.00 -> 0.16: -38/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.61, thread 3.97, cloth 6.39, flax fibres 4.58, garments 18.55, nets 34.60, beer 2.80, timber 5.30, prestige 55.40, cash 0.00
- Orders it would set (dry run): beer sell 54 (v2 52); labour buy 174 (v2 202); porterage buy 11 (v2 10); rope sell 3 (v2 2)
- Investments:
  - Tenants L13 for 500 prestige: +80/turn (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.2/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 415, chain may buy 0 -> chain allowance 85, chain plan 158 (-200 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.61 | 3.59 |
| ret | 3 | 1.00 | 0.64 |
| spin | 4 | 2.05 | 1.32 |
| weave | 3 | 0.67 | 0.00 |
| sew | 2 | 0.40 | 0.00 |

Buffers: flax fibres 46/50, thread 240/147, cloth 21/0
- chain plan needed 158 labour, budget left 85: cut to 158

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R7 stale ask: garments ask 20 over the market for 3 turns: the town trades ~64 a turn at 19.9, we sold 0 with 107 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
