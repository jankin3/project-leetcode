class Solution:
    def longestPalindrome(self, s: str):
        '''
        思路： 遍历， 以每个当前字符串为中心
        '''
        if len(s) == 1:
            return s
        result = ''
        for i, char in enumerate(s):
            if i == 0:
                result = char
                if i + 1 < len(s) and char == s[i + 1]:
                    result = s[:i + 2]
                continue
            # 奇数
            pos = 1
            while True:
                if i - pos >= 0 and i + pos < len(s) and s[i - pos] == s[i + pos]:
                    result = s[i - pos:i + pos + 1] if 2 * pos + 1 > len(result) else result
                    pos += 1
                else:
                    break
            # 偶数
            pos = 1
            if i + 1 < len(s) and char == s[i + 1]:
                result = s[i:i + 2] if 2 > len(result) else result
                while True:
                    if i - pos >= 0 and i + pos + 1 < len(s) and s[i - pos] == s[i + pos + 1]:
                        result = s[i - pos:i + pos + 2] if 2 * (pos + 1) > len(result) else result
                        pos += 1
                    else:
                        break
        return result


s = Solution()
r = s.longestPalindrome('ccc')
print(r)
