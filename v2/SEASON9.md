# Season 9 notes (Oct 28-29 2026): what the numbers say

Method: v2/data recipes and buildings, the Oct 23 world market dump (99 towns), labour at 1.8, a 6% spread each side,
and **typical-town depth** (the median traded volume per turn across towns), taking 30% of it. A single recipe's
margin = outputs at the median price - inputs at the median price - labour at 1.8. Home-town numbers are not used
(this season's home town is mature; a Season 9 start town will be small). Reproduce: `python tools/scan_recipes.py <max tier>`
from the repo root (reads v2/data/recipes.json and state/dump/world.json.gz, writes state/scan_t<N>.json).

## Findings
1. **Margins are about the price of labour.** At market labour (1.6-2.2 coin) almost no recipe earns more than
   ~2.5 coin per labour; the whole textile chain is ~0 (spin +4/vol, retting -30, weave -1, sew -178). Tiers 2 and 3 are
   no better at median prices (negative once spreads are paid). This is a near-efficient market.
2. **Depth, not margin, caps every recipe.** At 30% of a typical town's trade the best single recipe earns ~34 coin a
   turn. A whole town of tier-1 recipes is worth ~150/turn before tax (6 per plot per turn, urban).
3. **Free labour is the only edge.** Every own labour unit earns its value-add (~1.6-2.7 coin) instead of costing 1.8.
   Own labour comes from Tenants (+50/level, prestige-priced), the farmstead and the household. So prestige is not
   vanity: it buys labour supply. Tenants L13 costs 500 prestige for +50 labour a turn (~+85 coin a turn): a ~300-turn
   payback in labour terms, worth it only early in a season.
4. **Park and banquet (this season)** spend ~300 of the ~500 own labour for ~12 prestige a turn, which only offsets the
   ~16/turn legacy drain. Fine for legacy, expensive for growth. Untested: what the freed labour would earn.
5. **Cash is flat by construction**: trade net ~230/turn vs overhead (tax 226 + other) 220-280/turn.

## Best tier-1 recipes at typical depth (per turn, one building)
| Recipe | Site | margin/labour | volume | profit/turn | build cost | payback (turns) |
|---|---|---|---|---|---|---|
| cut firewood 1 | logging camp | 2.35 | 21.45 | 34 | 72 | 2 |
| cut firewood 2 | logging camp | 2.67 | 18.59 | 34 | 72 | 2 |
| collect slabs 1 | slab yard | 1.85 | 2.79 | 30 | 935 | 31 |
| collect slabs 2 | slab yard | 2.67 | 2.23 | 30 | 935 | 31 |
| gather firewood 1 | woodshed | 1.61 | 69.72 | 28 | 360 | 13 |
| split timber 2 | logging camp | 0.4 | 17.03 | 15 | 72 | 5 |
| coaling 1 | burner hut | 1.18 | 12.32 | 10 | 288 | 29 |
| knight duty 1 | household | 0.22 | 2.84 | 10 | None | None |
| coaling 2 | burner hut | 1.53 | 9.86 | 9 | 288 | 32 |
| cut firewood 3 | logging camp | 4.0 | 6.49 | 8 | 72 | 9 |

Firewood (cut/collect/gather) and timber are the only scalable ones; all are bulk and low-value. The rest are depth-capped
at tens of coin a turn.

## What a Season 9 start should do (hypotheses to test, in order)
- Day one: own labour first (Tenants, farmstead), cheapest firewood/timber recipes on it, no prestige buildings (park,
  mansion, banquet) until labour supply is up.
- Pick one chain by margin per labour AND depth, not by popularity; skip textiles unless prices move.
- Keep fixed overhead (taxes) under ~half of expected trade net before adding any building.
- Build the guardian and honest-burn metric in from turn 1 (they exist now: guardian.py).

## v3 outline (not started; build only after the Season 9 map is known)
Keep: api/order-queue layer, LP planner (v2/goal.py), guardian.py, history format, alerts/email.
Cut: v1 scripts (merc_actor, chain_balancer, spare_labour, endgame) and their ~40 thresholds.
Add: a day-one scan (this document's method) that picks chains; an explicit liability line in business value (loans);
a payback gate on every spend (measured, not modelled); experiments logged and scored (goal_history).
Rule: smaller than v2, not bigger.
