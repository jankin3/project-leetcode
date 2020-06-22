class Solution():
    def calculate(self, s):
        '双栈存储, 开始计算'
        s = s.replace(' ', '')
        n_stack = []  # 存储数字的栈
        c_stack = []  # 存储运算符号的栈
        i = 0
        while i < len(s):
            print(n_stack, c_stack)
            if i == 0 and s[i] == '-':
                num, i = self.find_all_num(s, i+1)
                n_stack.append(-1 * num)
            if s[i] in ('(', ')'):
                if s[i] == '(':
                    c_stack.append(s[i])
                else:  # 括号内部出栈计算
                    while True:
                        cur_c = c_stack.pop()
                        if cur_c == '(':
                            break
                        right_n = n_stack.pop()
                        left_n = n_stack.pop()
                        c_result = self.calculate_simple(left_n, right_n, cur_c)
                        n_stack.append(c_result)

                    if c_stack and c_stack[-1] in ('*', '/'):  # 前一个符号是*//的计算
                        r = n_stack.pop()
                        l = n_stack.pop()
                        c_result = self.calculate_simple(l, r, c_stack.pop())
                        n_stack.append(c_result)
            elif s[i] in ('*', '/'):
                if s[i + 1] != '(' and s[i + 1] != ' ':
                    cur_c = s[i]
                    i += 1
                    r, i = self.find_all_num(s, i)
                    l = n_stack.pop()
                    c_result = self.calculate_simple(l, r, cur_c)
                    n_stack.append(c_result)
                else:
                    c_stack.append(s[i])
            else:
                if s[i].isdigit():
                    num, i = self.find_all_num(s, i)
                    n_stack.append(num)
                elif s[i] == '-':
                    if i == 0 or s[i-1] == '(':
                        num, i = self.find_all_num(s, i+1)
                        n_stack.append(-1 * num)
                    else:
                        c_stack.append(s[i])
                else:
                    c_stack.append(s[i])
                        
            i += 1
        # print(n_stack, c_stack)

        n = len(c_stack)
        for j in range(n):
            c = c_stack.pop(0)
            l = n_stack.pop(0)
            r = n_stack.pop(0)
            c_result = self.calculate_simple(l, r, c)
            n_stack.insert(0, c_result)
        return n_stack[0]

    def find_all_num(self, s, i):
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
r = sol.calculate("2-4-(8+2-6+(8+4-(1)+8-10))")
print('result:')
print(r)
