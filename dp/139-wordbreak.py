class Solution:
    '暴力解法'
    def wordBreak(self, s: str, wordDict):
        mid_result = []
        mid_result.append(s)
        error_list = []
        while 1:
            if len(mid_result) == 0:
                return False
            new_mid_result = []
            for m in mid_result:
                for word in wordDict:
                    if word == m:
                        return True
                    if m.startswith(word):
                        new_mid_result.append(m.replace(word, '', 1))
                error_list.append(m)

            for e in error_list:
                if e in new_mid_result:
                    new_mid_result.remove(e)
            mid_result = list(set(new_mid_result))

    def workBreak_by_dp(self, s: str, wordDict):
        dp = {}
        dp[0] = True

        for i in range(1, len(s) + 1):
            print(dp)
            dp[i] = False
            for w in wordDict:
                if i-len(w) >= 0 and dp[i-len(w)] and s[i-len(w):i] == w:
                    dp[i] = True
                    break

        return dp[len(s)]

s = Solution()
r = s.workBreak_by_dp('abcbbbabc', ["abc", 'bbb'])
print(r)

# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]