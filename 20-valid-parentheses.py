class Solution:
    def isValid(self, s: str):
        if s == '':
            return True

        if len(s) % 2 != 0:
            return False

        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        temp_list = []
        for char in s:
            if char in map.values():
                if temp_list and map.get(temp_list[-1], False) == char:
                    temp_list = temp_list[:-1]
                else:
                    return False
            else:
                temp_list.append(char)

        return False if temp_list else True

s = Solution()
r = s.isValid("{[]}")
print(r)