### 题目地址
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

### 思路
我刚做题时候的思路是`断尾贪吃蛇`，就是开始就是一个贪吃蛇，字符串从头开始遍历开始，贪吃蛇越来越长，但是越到重复元素的时候后需要丢掉最开始吃的那一段尾巴。（后来想到这不就是一个队列么）

术语解释：
如果s[j]在[i, j)没有重复，直接前进
如果重复，重复的字符其位置为k，我们直接将i=k+1继续。

### 参考学习
`滑动窗口`，
滑动窗口是数组/字符串问题中常用的抽象概念。 窗口通常是在数组/字符串中由开始和结束索引定义的一系列元素的集合，即 [i, j)[i,j)（左闭，右开）。而滑动窗口是可以将两个边界向某一方向“滑动”的窗口。例如，我们将 [i, j)[i,j) 向右滑动 11 个元素，则它将变为 [i+1, j+1)[i+1,j+1)（左闭，右开）


```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        max_len = 1
        cur_long_str = s[0]
        for i in range(1, len(s)):
            cur_char = s[i:i+1]
            if cur_char in cur_long_str:
                # 砍断头部
                cur_long_str = cur_long_str[cur_long_str.find(cur_char) + 1:i] + cur_char
            else:
                cur_long_str += cur_char
            max_len = len(cur_long_str) if len(cur_long_str) > max_len else max_len

        return max_len

s = Solution()
print(s.lengthOfLongestSubstring("avaf"))
```