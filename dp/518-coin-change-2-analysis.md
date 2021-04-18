## 题目地址

https://leetcode-cn.com/problems/coin-change-2/

## 题目描述
给定n中不同面额的硬币coins和一个总金额amount。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

### 思路
｀完全背包｀问题，不过不是获取最大价值，而是得到固定价值的组合

### 复杂度分析
时间复杂度： n*amount
空间复杂度： m

###　代码
```python
#　https://leetcode-cn.com/problems/coin-change-2/
# -*- coding: utf-8 -*-
import copy
class Solution():
    def coin_combine_only_num(self, coin, amount):
    '''
    只计算出种类,递归的思路不同
    :param amount:
    :param coins:
    :return:
    '''
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]

# # 去重优化
l = [1, 2, 5, 10, 20, 50]
# r = find_n_m_sum(l, 4, 22)
# print(r)

s = Solution()
r = s.coin_combine(l, 100)
print('result')
print(r)
```