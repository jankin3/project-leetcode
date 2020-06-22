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
