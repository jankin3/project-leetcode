# -*- coding: utf-8 -*-
class Solution():
    '''
    【问题】将数组分为两部分，使得两部分的和最接近，返回两部分的差值。例如：

int[] array={1,0,1,7,2,4}，分为两部分为{1,0,1,2,4}，{7}，差值为1。
    '''
    def two_sublist_min_diff(self, l):
        half_sum = sum(l)/2

        dp = []
        # 初始化dp
        for i in range(len(l)):
            item = []
            for j in range(half_sum+1):
                item.append(0)
            dp.append(item)
        # 开始选择
        for i, k in enumerate(l):
            for j in range(half_sum+1):
                if k <= j:
                    if dp[i-1][j-k] + k > dp[i-1][j] and dp[i-1][j-k] + k <= j:
                        dp[i][j] = dp[i-1][j-k] + k # 添加该物品
                    else:
                        dp[i][j] = dp[i-1][j] #　不添加
                else:
                    # 当大于ｊ时，不能添加
                    dp[i][j] = dp[i - 1][j]
        # print(dp)
        # 找到添加的物品
        pick_index_list = []
        for i in range(len(l)):
            pick_index_list.append(0)
        j = half_sum
        for i in range(len(l)-1, -1, -1):
            # print(i, j)
            if dp[i][j] != dp[i-1][j] or i == 0:
                pick_index_list[i] = 1
                j = half_sum - l[i]
        # print(pick_list)

        pick_list, not_pick_list = [], []
        for i, item in enumerate(l):
            if pick_index_list[i] == 0:
                not_pick_list.append(item)
            else:
                pick_list.append(item)
        # print(pick_list, not_pick_list)
        return pick_list, not_pick_list

l = [1, 0, 1, 7, 2, 4]
s = Solution()
r = s.two_sublist_min_diff(l)
print(r)

