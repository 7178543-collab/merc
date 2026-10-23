# Goal planner (v2/goal.py)

Taylor, Oct 22: "stop fixing little things over and over and get the bot working correctly. I want the bot to have a
goal and pursue it." Goal picked: **business value** (cash + stock at market value). Authority: everything inside the
hard limits.

## Why the old bot kept breaking
About ten scripts each chased their own number with 40+ hand-set thresholds (failsafe, chain balancer, church rules,
spare labour, endgame switch, ship rules). Nothing weighed one move against another, so they fought: the farmstead
expansion bought labour the chain already had, the brake parked the ships, the church hold starved garment sales.

## How the goal planner decides
Every run it solves one linear program over a turn of steady flow (scipy HiGHS, < 1 s):

- **Choices**: every building's rate (current recipe), household duty, how much of each item to buy and sell at home,
  how much of a pile to draw down, how much output to put into stock.
- **Value per turn** (maximised): sales - purchases + 0.5 x market value of stock built - market value of stock drawn.
  Market value = 0.9 x the home last price (0.3 x our cost for goods with no home trade). Unsold stock only counts at
  half value, so the plan never "grows value" by piling up goods nobody buys.
- **Item balances**: made + bought + drawn = used + sold + stocked, for every item, every turn. Own labour (farmstead,
  workers) is supply like any other; build sites and household upkeep are fixed demand. This is what makes a labour
  overbuy impossible by construction.
- **Market depth**: sales at our current price up to what we really sold over the last 12 turns, plus a second step at
  7% under to win up to half the town's trade; buys at the home ask up to what the town trades.
- **Hard limits (constraints, never switches)**:
  - cash floor 4k: under it the plan must earn cash back over 24 turns; over it, it may spend down to the floor;
  - free prestige never planned under 300 (Taylor's Tenants rule); it may drift down to 300 over 240 turns, and the
    cheapest prestige the plan owns (park, banquet) is bought to hold it;
  - building sizes, worker labour for duty, storage space, sell reserves (min_holding) never drawn.

The duals give **shadow prices**: what one more unit of labour, thread, cloth, prestige or cash is worth per turn.
They explain every change in plain coin.

## What it reports (state/v2/goal.json, report.md "Goal")
- Value now (cash + stock) and its real trend from the history file.
- What today's settings earn per turn vs what the plan earns, and each building change with its own gain.
- Investments priced by re-solving: the next Tenants level (+50 own labour, prestige cost carried through the prestige
  floor) and +1 plot for every building the plan wants bigger, with payback in turns.
- Its own scorecard: each run logs the value it predicted; later runs compare with what really happened
  (state/v2/goal_history.jsonl).

## Rollout
1. Shadow (from Oct 23): plan + report only. Nothing changes in the game.
2. After 2-3 days, if the plan's numbers hold up against real turns, it takes over one job at a time
   (v2/config.json goal.live): building rates and duty first, then labour and input buys, then sell volumes,
   then the cash/prestige limits replace the failsafe's stand-down and the endgame switch.
3. Old scripts retire as their jobs move: chain_balancer/chain.py sizing, spare_labour, the banquet and quarry cash
   rules, endgame.py.

## Not modelled yet (stated so nobody trusts it blindly)
Ship exports and crew (v2 ships logic still runs them), contracts and church asks, price elasticity beyond the two
steps, recipe changes, new buildings (only +1 plot of existing ones), management room.
