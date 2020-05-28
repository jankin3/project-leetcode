### 题目地址
https://leetcode-cn.com/problems/longest-consecutive-sequence/

### 题目描述
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

###思路
这个题目的难点是时间复杂度．
思路是找到连续数序列最小的元素，然后查找后续连续序列是否在此序列中

### 代码
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exist_set = set(nums)
        long_num = 0

        for num in nums:
            if num-1 not in exist_set: # cur is first
                cur_num = num
                cur_long_num = 1

                while cur_num+1 in exist_set:
                    cur_num += 1
                    cur_long_num += 1
                    
                long_num = max(long_num, cur_long_num)
        return long_num
```