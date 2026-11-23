# v2 shadow report

Turn 14233, 2026-11-23 10:27. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,985, prestige 3,686 (566 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 75 | 0 | 4 | 0 | 0 | min_holding 58, sell 1, sell @ 3.16 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 8 | 6 | 6 | 3 | 0 | stop 32, buy 8, buy @ 3.7 |
| labour | 65 | 64 | 528 | 0 | 36 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), but the home ask 30.20 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **grain**: brewery 1 ran short of grain (buy is live (8 @ 3.7), 6 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.9 turns of grain left and buying 8 (need 18) -> v2: buy 18

## Waste (money lost now)

- **labour**: 36 labour expired last turn (~59 coin): holding 65 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 30.20 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 106 over real use lately; planning 528, not 626
- labour expiry guard: 36 bought labour expired last turn, buy 28 (not 28) this turn

## Prestige spending, cheapest coin per prestige first

168 turns left: prestige gained now converts 57.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| jousting 3 (premium) | arena | 420 | 51.9 | 52.4 | needs a arena (build cost 25,983); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.1 | 55.1 | needs a arena (build cost 25,983); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 55.7 | 56.2 | needs a arena (build cost 25,983); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 59.3 | 59.3 |  |
| jousting 2 | arena | 210 | 59.3 | 60.3 | needs a arena (build cost 25,983); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 2 | park | 2 | 60.8 | 60.8 | thin at home: sculptures |
| hold banquet 2 (fish) | mansion | 6.8 | 61.0 | 61.0 | thin at home: cheese |
| hold banquet 5 | mansion | 22 | 62.9 | 62.9 | thin at home: pasties, hop beer, stockfish, sculptures |
| hold banquet 2 (pies) | mansion | 7 | 63.3 | 63.3 | thin at home: pasties, cheese |
| hold banquet 4 (pies) | mansion | 18 | 64.6 | 64.6 | thin at home: pasties, hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 66.8 | 66.8 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | beer 6, rope 1 | pasties 2 | 29 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 10 @ 5.4, pasties buy 1 @ 12.4, rope sell 1 @ 85.5; crew 0.1; est +32 a turn; stock: pasties 1 @ 12.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.3 (keep 14); best orders clear only -7 a turn after crew: ship stays at 0
- best towns now: Bordetes +69, Grandgues +32, Fontaux +27, Toqueque +24, Clarfranche +21
- Bordetes would trade: beer sell 10 @ 8.25, pasties buy 1 @ 15.1, rope sell 1 @ 96.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.06 | 0.20 (21/turn) | grain 153 (2.75->3.95), rope 1 (65.5->79.8), wax 11 (29.61->30.02), beer 10 (3.46->3.67) | thread 8 (3.09->6), cloth 10 (9.03->10.8), tools 17 (5.78->6.7), bricks 8 (6.77->9.59) | +273 |
| Grandgues | 152 | 0.04 | 0.70 (74/turn) | firewood 38 (2.23->5.7), timber 29 (8.19->9.45), beer 10 (3.46->5.22), rope 1 (65.5->82.65) | bricks 10 (6.3->9.59), thread 62 (5.57->6), tools 11 (5.72->6.7), flax fibres 3 (6.67->8.05) | +208 |
| Hofkirchen | 991 | 0.33 | 1.00 (106/turn) | grain 109 (2.75->3.7), glass ingots 1 (55.12->76), flour 2 (22.68->34.2), ploughs 2 (84->92.15) | lathes 1 (202.65->226.1), jewellery 1 (74.03->87.4), cloth 16 (9.61->10.8), tools 11 (5.15->6.7) | +195 |
| Hanstein | 380 | 0.11 | 0.90 (95/turn) | timber 13 (8.19->12.06), firewood 16 (2.23->6.98), charcoal 17 (2.62->4.43), rope 1 (65.5->79.8) | thread 21 (4.81->6), flax fibres 9 (5.83->8.05), cloth 13 (9.66->10.8), wool 11 (10.08->11.02) | +170 |
| Clairas | 374 | 0.11 | 0.90 (95/turn) | firewood 27 (2.23->6.65), rope 1 (65.5->80.75), glass ingots 2 (55.12->57) | flax fibres 16 (5.46->8.05), cloth 19 (9.71->10.8), tools 17 (5.62->6.7), yarn 9 (4.54->5.98) | +143 |

**Best:** Vauxvais at about +273 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 8 @ 3.7, stop 31 |  | goal planner: buys 8 a turn for today's rates, keeps up to 31 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 28) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 40.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 10 @ min 64.0 | sell; ships offer 1 a turn abroad, so home sells 10 (was 1) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.3k (cash + stock at home prices); +33/turn over 6 turns, -16/turn over 24 turns.
- Limits: cash flow >= -416/turn, prestige >= -1.11/turn (values are after 200 tax a turn).
- Today's settings: value -187/turn, cash -141/turn, prestige +1.36/turn.
- Plan: value +26/turn, cash +37/turn, prestige -1.11/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +150 vs -139, +156 vs -159, +70 vs -161.
- Route sales counted at most (what the ships really sold, a turn): beer 1.5.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bordetes: +4/turn
  - ship Flax Wyrm -> Fontaux: +3/turn
  - mansion 1 1.00 -> 0.41: +187/turn
  - net maker 0.00 -> 0.29: +11/turn
  - spinnery 1 1.65 -> 1.44: +4/turn
  - flax farm 1 4.64 -> 4.35: -2/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +14/turn
- Model check over the last 59 turns: predicted -157/turn for the settings we ran, real +65/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.12, cloth 6.58, flax fibres 4.89, garments 19.04, nets 30.32, beer 2.86, timber 3.35, prestige 67.03, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 18); labour buy 64 (v2 28); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Bordetes (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Fontaux (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1872 coin: +3/turn, payback 643 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 85/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 30.2 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 30.8 (ask 30.2, cap 42.0))
- R1: prestige rate -2.84 a turn vs 12-turn median +1.03; likely: dry slot: cured meat; mansion 1 projected 0 (cured meat)
