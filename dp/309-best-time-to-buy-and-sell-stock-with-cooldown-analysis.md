## 题目地址

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

## 题目描述

```
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

## 思路
动态规划，有了前两题的经验，此题目直接从动态规划的思路开始做起。
其中，状态转移主要是`计算第i天的盈利是依赖于i天的每个节点的盈利去计算一个最大值的盈利`

```python
class Solution:
    def maxProfit(self, prices) -> int:
        dp = {}
        dp[0] = 0
        if len(prices) <= 1:
            return dp[0]

        dp[1] = prices[1] - prices[0] if prices[1] > prices[0] else 0
        for i in range(2, len(prices)):
            max_profit = dp[i - 1]
            for j in range(i-1, -1, -1):
                if prices[j] < prices[i]:
                    # 计算该方案下的盈利,并比较获得最大盈利
                    pre_profit = dp[j-2] if j >= 2 else 0
                    cur_profit = pre_profit + (prices[i] - prices[j])
                    max_profit = cur_profit if cur_profit > max_profit else max_profit
                else:
                    break
            dp[i] = max_profit

        return dp[len(prices)-1]


s = Solution()
s.maxProfit([3, 9, 4, 6, 7])

```