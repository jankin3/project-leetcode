### 题目地址
https://leetcode-cn.com/problems/decode-string/

###　题目描述
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:
```python
s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
```
### 思路
采用栈的数据结构,
 1. 遍历字符串,进栈,
 2. 当遇到']' 的时候开始出栈,解码部分字符串然后放进栈中,然后继续操作
 
###总结
遇到需要返回处理部分数据的情况应该想到使用栈

### 代码
```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for k in s:
            if k != ']':
                stack.append(k)
            else:
                word = ''
                while True:
                    c = stack.pop()
                    if c!='[':
                        word = c + word
                    else:
                        # get number
                        n = ''
                        while True:
                            if stack and stack[-1].isdigit():
                                cn = stack.pop()
                                n = cn + n
                                # n = int(cn)*10*(len(str(n))) + n
                            else:
                                break
                        word = word * int(n)
                        stack.append(word)
                        break
        return ''.join(stack)
```