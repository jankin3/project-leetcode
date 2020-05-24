### 题目链接
https://leetcode-cn.com/problems/regular-expression-matching/

### 题目描述
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素

所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
```python
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
```

### 思路
由简单到复杂；

+ 如果是两个普通字符串匹配．则遍历比较得出结果
+ 加上正则符号＇．＇，　仅仅增加一个万金油匹配，不影响流程
+ 加上正则符号＇＊＇，则需要在＊出现的时候判断分类，出现０，１，２．．．Ｎ 次结果，

    + 出现０次, 则isMatch(s, p[2:]) ,

    + 出现一次或者多次，则self.isMatch(s[1:], p)（前提是first_match）

### 代码  
据此，递归代码：
```python
    def isMatch_by_recursive(self, s, p):
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])
```
复杂度:
略复杂, to-do

### 优化－带备忘录的递归写法
思路类似只是翻译了一下上面的结果
```python
    def isMatch_by_dp(self, s, p):
        '带备忘录递归算法'
        memo = {}

        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == len(p): return i == len(s)

            first_match = i < len(s) and p[j] in {s[i], '.'}

            if j <= len(p)-2 and p[j + 1] == "*":
                res = dp(i, j + 2) or first_match and dp(i + 1, j)
            else:
                res = first_match and dp(i+1, j+1)
            memo[(i, j)] = res
            return res

        return dp(0, 0)
```
复杂度:
 时间复杂度:ij,因为每个i,j 会被计算一次
 空间复杂度:ij, 用来存储结果
