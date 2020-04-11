### 题目地址
https://leetcode-cn.com/problems/zigzag-conversion/

### 题目描述
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
```python
L   C   I   R
E T O E S I I G
E   D   H   N
```
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"

### 我的解题思路-反向思维
结果是需要一行一行的读取，按照这个思维，如果可以计算到每次读取的下一个字符串即可，分析发现，根据Z字型中心对称的特点，根据行数和走向可以计算出在原字符串中的index间隔，从而找到下一个字符串。

### 其他思路- 1.正向思维
模拟Z的排列，遍历一遍给所有的字符摆放到相应的位置。根据所需要的结果，只需分配行数个数的桶然后遍历装配数据即可

```python
class Solution:
    # 反向思维
    def convert(self, s: str, numRows: int):
        if len(s) < 3:
            return s
        if numRows == 1:
            return s

        result_str = ''
        for n in range(numRows):
            current_index = n
            if current_index > len(s) - 1:
                break
            result_str += s[current_index]
            num_which = 1
            while 1:
                num_which += 1
                # 第一行和最后一行特例
                if n == 0:
                    num_which = 2
                if n == numRows - 1:
                    num_which = 1

                # general
                if num_which % 2 == 0:
                    # 偶数 下三角
                    gap_num = 2 * (numRows - n - 1)
                else:
                    gap_num = 2 * n
                current_index += gap_num
                if current_index > len(s) - 1:
                    break
                next_char = s[current_index]
                result_str += next_char
        return result_str
    
    # 正向思维
    def convert_v2(self, s: str, numRows: int):
        if len(s) < 3 or numRows == 1:
            return s

        bucket_list = ['' for i in range(numRows)]
        cur_row = 0
        redirect_flag = True
        for c in s:
            bucket_list[cur_row] += c
            cur_row += 1 if redirect_flag else -1
            if cur_row == 0 or cur_row == numRows - 1:
                redirect_flag = not redirect_flag
        return ''.join(bucket_list)


s = Solution()
r = s.convert_v2('LEETCODEISHIRING', 4)
print(r)
# LCIRETOESIIGEDHN LDREOEIIECIHNTSG
# LCIRETOESIIGEDHN LDREOEIIECIHNTSG
```

