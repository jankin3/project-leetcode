### 题目地址
https://leetcode-cn.com/problems/permutations/
###题目描述

给定一个 没有重复 数字的序列，返回其所有可能的全排列。
```python
示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

###　思路－回溯法
基础版：　有ｎ个位置，需要放ｎ个数，visit每次放一个数记录一个使用，然后放下一个数，放完之后，撤回
```python
 def permute(self, nums: List[int]) -> List[List[int]]:
        def dp(pos):
            '''
            s : 数组
            pos: 位置
            '''
            if pos == len(nums) :
                # print('r:', r)
                ans.append(r[:])
                return 
            else:
                for i in range(0, len(nums)):
                    if visit[i] == False:
                        r[pos] = nums[i]
                        visit[i] = True
                        dp(pos+1)
                        visit[i] = False

        visit = [False for _ in range(len(nums))]
        r = ['' for _ in range(len(nums))]
        ans = []
        dp(0)
        return ans
```

优化版：有ｎ个位置，需要放ｎ个数，不使用visit数组，使已经｀放置过｀和｀未放置过｀有一个界限，具体的代码是采用交换将放置的数放到放置过的范围中．
```python
   def permute(self, nums: List[int]) -> List[List[int]]:
        def back(pos):
            '回溯'
            if pos == len(nums):
                ans.append(nums[:])
            else:
                for i in range(pos, len(nums)):
                    nums[i], nums[pos] = nums[pos], nums[i]
                    back(pos+1)
                    nums[i], nums[pos] = nums[pos], nums[i]
        ans = []
        back(0)
        return ans
```

### 升级题目
https://leetcode-cn.com/problems/permutations-ii/
给定一个可包含重复数字的序列，返回所有不重复的全排列。
```python
示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```
代码
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def back(pos):
            '回溯'
            if pos == len(nums):
                ans.append(nums[:])
            else:
                for i in range(pos, len(nums)):
                    nums[i], nums[pos] = nums[pos], nums[i]
                    exist_str = '|'.join([str(x) for x in nums]) + '-' + str(pos)
                    if exist_str not in exist_set: # 判断然后剪枝
                        exist_set.add(exist_str)
                        back(pos+1)
                        nums[i], nums[pos] = nums[pos], nums[i]
                    else:
                        nums[i], nums[pos] = nums[pos], nums[i]

                    
        ans = []
        exist_set = set() 
        back(0)
        return ans
```