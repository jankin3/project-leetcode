# -*- coding: utf-8 -*-
#给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        题目:https://leetcode-cn.com/problems/maximum-subarray/
        给定一个整数数组 nums ，找到一个具有最大和的连续子数组
        :param nums:
        :return:
        '''
        ans, cur_sum = nums[0], 0

        for n in nums:
            if cur_sum < 0:  # 不需要累加负值，则置位０
                cur_sum = 0
            cur_sum += n
            if cur_sum < 0:
                cur_sum = n  # 如果累加之后为０，则放弃累加，把子序列的头置位
            ans = ans if ans > cur_sum else cur_sum

        return ans
