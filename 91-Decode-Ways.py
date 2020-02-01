class Solution:
    result_recursion = {}
    def numDecodings_by_recursion(self, s):
        if self.result_recursion.get(s, None):
            return self.result_recursion.get(s)

        if len(s) == 1:
            return 1 if int(s) >= 1 and int(s) <= 9 else 0
        elif len(s) == 2:
            if s.startswith('0'):
                return 0
            if int(s) < 1:
                return 0
            elif int(s) > 26:
                return 0 if s.endswith('0') else 1
            else:
                return 2 if not s.endswith('0') else 1
        else:
            if s.startswith('0'):
                return 0
            pre_two_str = s[:2]
            if int(pre_two_str) >= 1 and int(pre_two_str) <= 26:
                if not pre_two_str.endswith('0'):
                    return self.numDecodings_by_recursion(s[1:]) + self.numDecodings_by_recursion(s[2:])
                else:
                    return self.numDecodings_by_recursion(s[2:])
            elif int(s) > 26 and not pre_two_str.endswith('0'):
                return self.numDecodings_by_recursion(s[1:])
            else:
                return 0

    def numDecodings_by_dp(self, s):
        r = {}
        r[0] = 0
        r[1] = 1 if int(s[0]) >= 1 and int(s[0]) <= 9 else 0

        for i in range(2, len(s) + 1):
            pre_one = s[i-1:i]
            pre_two = s[i-2:i]

            r[i] = 0
            if int(pre_two) >= 10 and int(pre_two) <= 26:
                r[i] = r[i-2]
            if int(pre_one) >= 1 and int(pre_one) <= 9:
                r[i] += r[i-1]

        return r[len(s)]

sol = Solution()
test_string = '93715976311287769483871907132267188677349946742344217846154932859125134924241649584251978418763151253'
print(sol.numDecodings_by_dp(test_string))
# print(sol.numDecodings_by_recursion(test_string))
