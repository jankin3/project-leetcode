class Solution:
    def twoSum(self, nums, target):
        target_map = {}
        for i, n in enumerate(nums):
            if n in target_map.keys():
                return [target_map[n], i]
            if target - n not in target_map.keys():
                # target_num => index
                target_map[target - n] = i
        return []

s = Solution()
r = s.twoSum(nums=[2, 7, 11, 15], target=9)
print(r)