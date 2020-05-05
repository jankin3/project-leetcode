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

s = Solution()
r = s.generateParenthesis(4)
print(r)

#输出
# r1 = ['()(()())', '((()()))', '(((())))', '((())())', '()(())()', '(()()())', '()((()))', '(()(()))', '()()()()', '((()))()', '()()(())', '(()())()', '(())()()', '(())(())']
# # 预期结果
# r2 = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
# print(set(r2)-set(r1))