### 题目地址
https://leetcode-cn.com/problems/generate-parentheses/

### 题目描述
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
```python
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
```

### 我的思路
分析发现每个n都是由n前面的结果可以得到。

分成两个类型:  
1. 左右i(n-i), (n-i)i, 即左右两个子集拼凑
2. 包含(n-i), 即包含n-1的子集和

分析:
时间复杂度 --todo
空间复杂度 --todo

### 代码
```python
class Solution:
    def generateParenthesis(self, n: int):
        result_dict = {}
        for i in range(1, n+1):
            print('i:%s' % i)
            if i == 1:
                result_dict[i] = ['()']
            else:
                # 1. 左右()old, old()
                side_add_list = []
                for j in range(1, int(i/2)+1):
                    for l in result_dict[j]:
                        for r in result_dict[i-j]:
                            side_add_list.append(l + r)
                            side_add_list.append(r + l)

                # # 2. 包含 (old)
                contains_list = ['(' + item + ')' for item in result_dict[i - 1]]
                combine_list = list(set(side_add_list + contains_list))
                result_dict[i] = combine_list

        return result_dict[n]
```