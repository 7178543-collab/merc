# v2 shadow report

Turn 14176, 2026-11-21 01:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,126, prestige 3,735 (615 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 102 | 0 | 12 | 0 | 0 | min_holding 58, sell 18, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 12 | 7 | 9 | 0 | 0 | stop 26, buy 7, buy @ 3.7 |
| labour | 64 | 64 | 519 | 0 | 45 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **grain**: home ask 3.78 is above our ceiling 3.70 and last turn bought 7 of ~9 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.50 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~91 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.50 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 522, not 622
- labour expiry guard: 45 bought labour expired last turn, buy 20 (not 22) this turn

## Prestige spending, cheapest coin per prestige first

225 turns left: prestige gained now converts 67.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.8 | 51.2 | needs a arena (build cost 29,085); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.3 | 53.1 | needs a arena (build cost 29,085); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.5 | 54.9 | needs a arena (build cost 29,085); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.3 | 58.1 | needs a arena (build cost 29,085); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 60.2 | 60.2 | thin at home: hop beer, wine, stockfish, cheese, candles |
| maintain 1 | park | 0.5 | 60.6 | 60.6 | running |
| hold banquet 4 (premium) | mansion | 20 | 61.4 | 61.4 | thin at home: hop beer, wine, stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 55.1 | 63.4 | needs a cathedral (build cost 315,290); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 63.6 | 63.6 | thin at home: hop beer, cheese, candles |
| hold banquet 4 | mansion | 17.5 | 64.4 | 64.4 | thin at home: wine, hop beer, ham, stockfish, cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 65.7 | 65.7 | thin at home: wine, cheese, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 69.7 | 69.7 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 11 @ 4.96, pasties buy 12 @ 16.0; crew 0.1; est +29 a turn; stock: pasties 12 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: pasties buy 8 @ 14.9; crew 0.1; est +19 a turn; stock: pasties 8 @ 14.9 (keep 14)
- best towns now: Chatgnan +206, Blanans +204, Clairlond +197, Brunnham +168, Disscester +167
- Chatgnan would trade: furniture buy 16 @ 13.8, pasties buy 8 @ 15.1; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~130 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.14 | 0.40 (52/turn) | thread 67 (6.35->7.27), cured fish 26 (34.23->35.91), garments 10 (30.4->34.01), nets 3 (43.4->49.88) | cloth 3 (12.5->13.4), salt 8 (5.25->5.56) | +174 |
| Grandgues | 152 | 0.05 | 0.60 (78/turn) | thread 92 (6.35->7.03), charcoal 19 (2.71->5.56), firewood 31 (2.71->5.51), beer 11 (4->4.8) | cloth 2 (12.92->13.4), malt 3 (8.4->8.79), cured meat 3 (25.83->26) | +147 |
| Großaue | 1136 | 0.51 | 0.30 (39/turn) | lathes 1 (180.6->258.4), wool 4 (11.23->12.73) | cloth 24 (10.5->13.4), yarn 27 (6.04->6.93), garments 2 (29.19->31.6), dyed cloth 4 (16.07->16.62) | +145 |
| Heilegg | 826 | 0.30 | 0.90 (117/turn) | lathes 2 (180.6->195.7), wool 4 (11.23->17.1), nets 6 (43.4->45.98), thread 72 (6.35->6.79) | cloth 24 (11.65->13.4), cured meat 3 (24.78->26), cookware 5 (20.48->20.9) | +114 |
| Unterhufe | 595 | 0.21 | 0.20 (26/turn) | lathes 2 (180.6->189.05), wine 2 (7.46->9.59), wool 4 (11.23->11.49) | cloth 24 (10.61->13.4), fleece 6 (8.51->10.07), grain 8 (2.9->3.76), thread 49 (6.51->6.8) | +95 |

**Best:** Fontaux at about +174 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 18 @ min 3.88 | makes 19.3, uses 4.2, holds 102 (keeps 58): sells the surplus + 2/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.0) |
| grain | 18 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 12 = 1.3 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 20) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 42.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.4k (cash + stock at home prices); -34/turn over 6 turns, -135/turn over 24 turns.
- Limits: cash flow >= -297/turn, prestige >= -1.31/turn (values are after 200 tax a turn).
- Today's settings: value -167/turn, cash -179/turn, prestige +1.12/turn.
- Plan: value +49/turn, cash +51/turn, prestige -1.31/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +1 vs -169, -61 vs -173, +48 vs -189.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +24/turn
  - ship Flax Wyrm -> Blanans: +6/turn
  - mansion 1 1.00 -> 0.42: +154/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.08: +20/turn
  - spinnery 1 1.65 -> 1.23: +10/turn
  - retting pit 1 0.91 -> 0.78: +3/turn
  - flax farm 1 4.64 -> 3.93: +9/turn
  - brewery 1 0.14 -> 0.00: -25/turn
  - brewery 1 [brew mead 1] 0.00 -> 0.12: +37/turn
- Model check over the last 59 turns: predicted -93/turn for the settings we ran, real +12/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.63, beer 3.48, timber 3.94, prestige 64.97, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 20); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.12, worth +9/turn.
- Ship linen snake: Grandgues -> Amsdermund (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +86/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 419 (+130 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.17 |
| ret | 3 | 0.91 | 0.83 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 120/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
