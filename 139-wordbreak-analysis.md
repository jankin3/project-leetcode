
## 题目地址

https://leetcode.com/problems/word-break/description/

## 题目描述

```
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

```

## 思路
1. 暴力解法，直接从头匹配，分解成子字符串(可能多个)，直到可以匹配结束
2. 动态规划，同样是分解成子字符串，这里的递归方式是当前一个子字符串是否可以被分解依据他的子字符串的判断结果。表达就是，
`dp[i]标识当前前i个字符串是否可以被分解，dp[i]依赖于dp[i-len(word)]的结果可以判断得出`。


```python
class Solution:
    '暴力解法'
    def wordBreak(self, s: str, wordDict):
        mid_result = []
        mid_result.append(s)
        error_list = []
        while 1:
            if len(mid_result) == 0:
                return False
            new_mid_result = []
            for m in mid_result:
                for word in wordDict:
                    if word == m:
                        return True
                    if m.startswith(word):
                        new_mid_result.append(m.replace(word, '', 1))
                error_list.append(m)

            for e in error_list:
                if e in new_mid_result:
                    new_mid_result.remove(e)
            mid_result = list(set(new_mid_result))

    def workBreak_by_dp(self, s: str, wordDict):
        dp = {}
        dp[0] = True

        for i in range(1, len(s) + 1):
            print(dp)
            dp[i] = False
            for w in wordDict:
                if i-len(w) >= 0 and dp[i-len(w)] and s[i-len(w):i] == w:
                    dp[i] = True
                    break

        return dp[len(s)]

s = Solution()
r = s.workBreak_by_dp('abcbbbabc', ["abc", 'bbb'])
print(r)

# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
```