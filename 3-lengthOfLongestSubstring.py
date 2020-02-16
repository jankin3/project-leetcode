class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        max_len = 1
        cur_long_str = s[0]
        for i in range(1, len(s)):
            cur_char = s[i:i+1]
            if cur_char in cur_long_str:
                # 砍断头部
                cur_long_str = cur_long_str[cur_long_str.find(cur_char) + 1:i] + cur_char
            else:
                cur_long_str += cur_char
            max_len = len(cur_long_str) if len(cur_long_str) > max_len else max_len

        return max_len

s = Solution()
print(s.lengthOfLongestSubstring("avaf"))