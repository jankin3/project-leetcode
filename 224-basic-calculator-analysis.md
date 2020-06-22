# 基础计算器(困难)

### 问题地址
https://leetcode-cn.com/problems/basic-calculator/

### 问题描述
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。
```
示例 1:

输入: "1 + 1"
输出: 2
示例 2:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
```



### 思路

1. 先转化为后缀表达式
2. 然后计算后缀表达式



#####　转化为后缀表达式

1. 两个栈,s1用来保留后缀表达式(这里使用数组而不是字符串,因为数有多个数字组成而且有符号), 另一个s2用来存储了临时的符号
2. 从左到右遍历字符串
3. 当遇到数字的时候, 找到所有连续的数字放入s1
4.  当遇到四则操作符号的时候, 比较优先级
   + 如果当前的优先级大于或者等于栈顶的优先级,则入栈s2,
   + 如果小于,则开始s2出栈,放入s1中, 再次执行比较优先级
5. 当遇到左右括号
   + 左括号直接进栈s2
   + 右括号则需要出栈直到遇到左括号

6. 重复2-5,直到结束
7. s2出栈进入到s1中



##### 计算后缀表达式

这个就比较简单了．使用

1. 一个栈来存储操作数
2. 从左到右遍历
3. 遇到符号则出站２个数计算，然后放入栈中



### to-do

实际代码的时间和空间待优化，16％左右



### 代码

```
class Solution():
    def calculate(self, s):
        s = s.replace(' ', '')
        end_list = []  # 后缀表达式
        c_stack = []  # 存储运算符号的栈
        privilege_level = {
            '+': 1,
            '-': 1,  
            '*': 2,
            '/': 2, 
        }
        i = 0
        while i < len(s):
            # print(end_list, c_stack)
            if s[i] == '-' and (s[i-1] == '(' or i == 0): # 处理负号
                num, i = self.find_all_num(s, i+1)
                end_list.append(-1 * num)
                i += 1

            if s[i] in ('(', ')'): #括号
                if s[i] == '(':
                    c_stack.append(s[i])
                elif s[i] == ')':  # 左括号之前的出站放入后缀表达式
                    while c_stack:
                        cur_c = c_stack.pop()
                        if cur_c == '(':
                            break
                        else:
                            end_list.append(cur_c)
            elif s[i] in privilege_level: # 运算符
                while True:
                    if c_stack and c_stack[-1] in privilege_level:
                        c = c_stack[-1]
                        if privilege_level[c] >= privilege_level[s[i]]: # 优先级大于或者等于
                            c = c_stack.pop()
                            end_list.append(c)
                        else:
                            c_stack.append(s[i])
                            break
                    else:
                        c_stack.append(s[i])
                        break
            elif s[i].isdigit(): #数字
                num, i = self.find_all_num(s, i)
                end_list.append(num)
                        
            i += 1

        # 将符号栈中的符号依次出栈进入后缀表达式
        while c_stack:
            cur_c = c_stack.pop()
            end_list.append(cur_c)

        return self.end_calculate(end_list)
        # print(n_stack, c_stack)

    def end_calculate(self, end_list):
        '计算后缀表达式的值'
        c_list = ('+', '-', '*', '/')
        stack = [] # 存放操作数字的栈s
        for item in end_list:
            if item in c_list:
                r = stack.pop()
                l = stack.pop()
                sub_result = self.calculate_simple(l, r, item)
                stack.append(sub_result)
            else:
                stack.append(item)
        return stack[0]


    def find_all_num(self, s, i):
        '连接所有的数字部分组成数'
        num = int(s[i])
        while True:
            if i + 1 < len(s) and s[i + 1].isdigit():
                num = num * 10 + int(s[i + 1])
                i += 1
            else:
                break
        return num, i

    def calculate_simple(self, l, r, c) -> int:
        l = int(l)
        r = int(r)
        if c == '+':
            return int(l + r)
        elif c == '-':
            return int(l - r)
        elif c == '*':
            return int(l * r)
        elif c == '/':
            return int(l / r)


sol = Solution()
r = sol.calculate("-1+((2+3)*4)-5")
print('result:')
print(r)
```

