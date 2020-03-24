class Solution:
    def maxArea(self, height):
        max_s = 0
        left_index, right_index = 0, len(height) - 1
        while left_index < right_index:
            cur_s = (right_index - left_index) * min(height[left_index], height[right_index])
            max_s = max_s if max_s > cur_s else cur_s
            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return max_s

s = Solution()
r = s.maxArea([1, 3, 2, 5, 25, 24, 5])
print(r)
