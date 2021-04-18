# -*- coding: utf-8 -*-

import copy
class Solution():
    def coin_combine_recursive(self, l, n, m):
        # 递归思路，代码简单
        if n == 1:
            return [[m,],] if m in l else []
        else:
            r_list = []
            for x in l:
                x_result = []
                if m - x > 0 and n-1 > 0:
                    rest_list = self.find_n_m_sum(l, n-1, m-x)
                    if rest_list:
                        for r in rest_list:
                            x_result.append(r+[x])
                if x_result:
                    r_list += x_result
            return r_list

    def coin_combine(self, l, n, m):
        # 动态规划算法, 面试题目,实际不光计算出结果种类并且得出每种的结果分布
        dp = []
        for i in range(1, n+1):
            # print('-------------------i--------------------', i)
            n_list = []
            for j in range(1, m+1):
                # print('-------------------j--------------------', j)
                item = []
                if i == 1:
                    if j in l:
                        item = [[j]]
                    else:
                        item = []
                else:
                    for x in l:
                        if j - x > 0:

                            history_list = dp[i-1-1][j-x-1]
                            rest_list = copy.deepcopy(history_list)
                            # print('rest_list', rest_list)
                            if rest_list:
                                for result_item in rest_list:
                                    if x:
                                        result_item.append(x)
                                        # 排序为了去重
                                        result_item.sort()
                            for r in rest_list:
                                if r not in item:
                                    item.append(r)
                n_list.append(item)
            dp.append(n_list)
        return dp[n-1][m-1]

    def coin_combine_only_num(self, coins, num=0, amount=0):
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
l = [1, 2, 5]
# r = find_n_m_sum(l, 4, 22)
# print(r)

s = Solution()
for n in range(1, 6):
    r = s.coin_combine(l, n, 5)
    print(r)
r2 = s.coin_combine_only_num(l, 0, 5)
print('result')
# print(r)
print(r2)




