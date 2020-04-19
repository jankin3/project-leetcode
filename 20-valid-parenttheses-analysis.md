### 题目地址
https://leetcode-cn.com/problems/valid-parentheses/

### 题目描述
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

### 我的思路
采用消除法，从左到右遍历，当遇到满足对应关系的括号消除，用一个栈(python直接用了list)存储已经遍历过但是仍然存在的元素。
如果最后栈为空则表示成功。否则，失败
```python
class Solution:
    def isValid(self, s: str):
        if s == '':
            return True

        if len(s) % 2 != 0:
            return False

        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        temp_list = []
        for char in s:
            if char in map.values():
                if temp_list and map.get(temp_list[-1], False) == char:
                    temp_list = temp_list[:-1]
                else:
                    return False
            else:
                temp_list.append(char)

        return False if temp_list else True
```