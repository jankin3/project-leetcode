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
                    # 计算该方案下的盈利
                    pre_profit = dp[j-2] if j >= 2 else 0
                    cur_profit = pre_profit + (prices[i] - prices[j])
                    max_profit = cur_profit if cur_profit > max_profit else max_profit
                else:
                    break
            dp[i] = max_profit

        return dp[len(prices)-1]


s = Solution()
s.maxProfit([3, 9, 4, 6, 7])
