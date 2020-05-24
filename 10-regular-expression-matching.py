# -*- coding: utf-8 -*-
class Solution:
    def isMatch_by_recursive(self, s, p):
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

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

    # 带备忘录的递归
    # def isMatch(text, pattern) -> bool:
    #     memo = dict()  # 备忘录
    #
    #     def dp(i, j):
    #         if (i, j) in memo: return memo[(i, j)]
    #         if j == len(pattern): return i == len(text)
    #
    #         first = i < len(text) and pattern[j] in {text[i], '.'}
    #
    #         if j <= len(pattern) - 2 and pattern[j + 1] == '*':
    #             ans = dp(i, j + 2) or \
    #                   first and dp(i + 1, j)
    #         else:
    #             ans = first and dp(i + 1, j + 1)
    #
    #         memo[(i, j)] = ans
    #         return ans
    #
    #     return dp(0, 0)

s_obj = Solution()
s1 = "miss"
p = "mis*"
r = s_obj.isMatch_by_dp(s1, p)
print(r)
