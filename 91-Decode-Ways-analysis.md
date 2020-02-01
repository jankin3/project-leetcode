### 题目地址
https://leetcode.com/problems/decode-ways/description/
## 题目描述
```
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

### 思路
`分析`，这里的解码要么是两个数字1-26，要么是一个数字1-9，有些类似楼梯问题。
`递归`，看到题目我想的第一个方法是递归，直接把大问题拆解到小问题，比如这里输入1234567，可以直接拆解成1，234567和12，34567两个问题，代码如下numDecodings_by_recursion()
问题：1. 边界问题复杂 2. 有很多重复的计算

`动态规划` 参考了网上的答案，写出了动态规划的解答，见numDecodings_by_dp()。
这里，r[i]标识前i位字符串的答案，这里的递推关系是没增加一个新的字符串，新的答案是可以依赖旧的r[i-2]和r[i-1] 得到。

``` python
class Solution:
    def numDecodings_by_recursion(self, s):
        if len(s) == 1:
            return 1 if int(s) >= 1 and int(s) <= 9 else 0
        elif len(s) == 2:
            if s.startswith('0'):
                return 0
            if int(s) < 1:
                return 0
            elif int(s) > 26:
                return 0 if s.endswith('0') else 1
            else:
                return 2 if not s.endswith('0') else 1
        else:
            if s.startswith('0'):
                return 0
            pre_two_str = s[:2]
            if int(pre_two_str) >= 1 and int(pre_two_str) <= 26:
                if not pre_two_str.endswith('0'):
                    return self.numDecodings_by_recursion(s[1:]) + self.numDecodings_by_recursion(s[2:])
                else:
                    return self.numDecodings_by_recursion(s[2:])
            elif int(s) > 26 and not pre_two_str.endswith('0'):
                return self.numDecodings_by_recursion(s[1:])
            else:
                return 0
 
  def numDecodings_by_dp(self, s):
        r = {}
        r[0] = 0
        r[1] = 1 if int(s[0]) >= 1 and int(s[0]) <= 9 else 0

        for i in range(2, len(s) + 1):
            pre_one = s[i-1:i]
            pre_two = s[i-2:i]

            r[i] = 0
            if int(pre_two) >= 10 and int(pre_two) <= 26:
                r[i] = r[i-2]
            if int(pre_one) >= 1 and int(pre_one) <= 9:
                r[i] += r[i-1]

        return r[len(s)]

sol = Solution()
test_string = '93715976311287769483871907132267188677349946742344217846154932859125134924241649584251978418763151253'
print(sol.numDecodings_by_dp(test_string))
```