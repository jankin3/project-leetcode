class Solution:
    def convert(self, s: str, numRows: int):
        if len(s) < 3:
            return s
        if numRows == 1:
            return s

        result_str = ''
        for n in range(numRows):
            current_index = n
            if current_index > len(s) - 1:
                break
            result_str += s[current_index]
            num_which = 1
            while 1:
                num_which += 1
                # 第一行和最后一行特例
                if n == 0:
                    num_which = 2
                if n == numRows - 1:
                    num_which = 1

                # general
                if num_which % 2 == 0:
                    # 偶数 下三角
                    gap_num = 2 * (numRows - n - 1)
                else:
                    gap_num = 2 * n
                current_index += gap_num
                if current_index > len(s) - 1:
                    break
                next_char = s[current_index]
                result_str += next_char
        return result_str

    def convert_v2(self, s: str, numRows: int):
        if len(s) < 3 or numRows == 1:
            return s

        bucket_list = ['' for i in range(numRows)]
        cur_row = 0
        redirect_flag = True
        for c in s:
            bucket_list[cur_row] += c
            cur_row += 1 if redirect_flag else -1
            if cur_row == 0 or cur_row == numRows - 1:
                redirect_flag = not redirect_flag
        return ''.join(bucket_list)


s = Solution()
r = s.convert_v2('LEETCODEISHIRING', 4)
print(r)
# LCIRETOESIIGEDHN LDREOEIIECIHNTSG
# LCIRETOESIIGEDHN LDREOEIIECIHNTSG