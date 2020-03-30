### 题目地址
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

### 题目描述
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
```python
#给定 nums = [2, 7, 11, 15], target = 9

#因为 nums[0] + nums[1] = 2 + 7 = 9
#所以返回 [0, 1]
```

### 思路
1. 暴力法

遍历每个元素 xx，并查找是否存在一个值与 target - x 相等的目标元素。

时间复杂度：O(n^2) ，空间复杂度：O(1)

> 我的思路
刚开始做题目的时候想的也是暴力法优化版。遍历每个元素，在其位置之后寻找target-x. 因为其位置之前如果有的话，肯定已经早被选到了。
时间复杂度略低于O(n^2),但是仍然是暴力版

2. 哈希表法

基础版，遍历第一趟，记录target - x到哈希表，遍历第二趟就开始寻找第一趟的结果list.
优化版，遍历一遍，一边遍历记录到哈希表，同时一边check当前对象是否满足哈希表已经存在的数据
时间复杂度：O(n),空间复杂度：O(n)


知识点：`哈希表`，寻找索引与元素对应关系适合使用。

### 解答:
```python
class Solution:
    def twoSum(self, nums, target):
        target_map = {}
        for i, n in enumerate(nums):
            if n in target_map.keys():
                return [target_map[n], i]
            if target - n not in target_map.keys():
                # target_num => index
                target_map[target - n] = i
        return []
```