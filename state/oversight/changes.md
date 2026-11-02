# Changes in the last 24 h (applied queue entries, newest first)

- 11-02T07:42 [v2-diagnose] item="limestone", set={"sell_price": "17"}, building="152202386005001" | v2 diagnose R7 stale ask: sell price 17.3 -> 17 (last trade 17, floor 16.34)
- 11-02T02:13 [queue] item="cured meat", set={"buy_volume": 0} | Nov 2 Claude: banquet is off (turn 13721, mansion 0, free prestige +22.9); the standing cured-meat buy (6/turn at 29) ke
- 11-02T01:03 [prestige_rules] building="152002388", producer={"recipe": "hold banquet 1 (meat)", "target": 0} | banquet rule: cash 5032 under 10000
- 11-01T17:23 [queue] item="candles", set={"buy_volume": 6, "buy_price": "74", "max_holding": 62}, confirm=true | Nov 1 Claude (Taylor: add prestige): stock 55 candles for the church ask (+100 prestige, -100 if missed, 120 turns left)
- 11-01T16:41 [queue] item="meat", set={"buy_volume": 7, "buy_price": "1.91"} | Nov 1 Claude: fine-food slot dry (+0.3 prestige/turn, ~13 coin)
- 11-01T16:41 [queue] item="fish", set={"buy_volume": 7, "buy_price": "1.76"} | Nov 1 Claude: fine-food slot dry (+0.3 prestige/turn, ~12 coin)
- 11-01T16:41 [queue] item="donations", set={"buy_volume": 40, "buy_price": "1.02"} | Nov 1 Claude: luxury slot dry (+1 prestige/turn, ~40 coin); diagnose was held back by failsafe WATCH
- 11-01T15:54 [queue] override={"banquet": "auto"} | Nov 1 Claude: back to auto; new rescue rule in prestige_rules runs the banquet while free prestige < 15 (cash > 4k)
- 11-01T15:44 [prestige_rules] building="152002388", producer={"recipe": "hold banquet 1 (meat)", "target": 1, "provider_i | banquet rule: Taylor's override from the app: banquet on; recipe hold banquet 1 (meat) (fish 0.0, meat 0.5 held)
- 11-01T15:44 [prestige_rules] item="cured meat", set={"buy_volume": 6, "buy_price": "29", "max_holding": 10} | banquet rule (meat fallback): Taylor's override from the app: banquet on
- 11-01T15:44 [queue] override={"banquet": "on"} | Nov 1 Claude: free prestige -9.6 falling 1.26/turn (T5 drop risk); banquet +4.2/turn until free prestige is back over ~1
