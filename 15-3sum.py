class Solution:
    def threeSum_complicate_hash(self, nums):
        result_list = []
        nums.sort()
        negative_nums, positive_nums, zero_nums = [], [], []
        # chunk
        for x in nums:
            if x < 0:
                negative_nums.append(x)
            elif x > 0:
                positive_nums.append(x)
            else:
                zero_nums.append(x)
        # 1. contains 0
        if len(zero_nums) > 0:
            if len(zero_nums) >= 3:
                result_list.append([0, 0, 0])
            # 转换成2数之和
            r_list = self.twoSum(0, negative_nums + positive_nums)
            if r_list:
                result_list += [[0, r[0], r[1]] for r in r_list]

        # 2. not contains 0
        sum_n, sum_p = sum(negative_nums), sum(positive_nums)
        # 针对优化， 删除较长的部分
        if abs(sum_n) < abs(sum_p):
            for p in positive_nums:
                if p > abs(sum_n):
                    positive_nums.remove(p)
        else:
            for n in negative_nums:
                if abs(n) > sum_p:
                    negative_nums.remove(n)

        # 2-1 2正1负
        if len(positive_nums) > 1:
            history_set = set()
            for n in negative_nums:
                if n not in history_set:
                    history_set.add(n)
                    r_list = self.twoSum(abs(n), positive_nums)
                    if r_list:
                        for r in r_list:
                            result_list.append([n, r[0], r[1]])
        # 2-2 2负1正
        if len(negative_nums) > 1:
            history_set = set()
            for p in positive_nums:
                if p not in history_set:
                    history_set.add(p)
                    r_list = self.twoSum(p * (-1), negative_nums)
                    if r_list:
                        for r in r_list:
                            result_list.append([p, r[0], r[1]])

        return result_list

    def twoSum(self, target, nums):
        r_list = []
        target_map = {}
        h_set = set()
        for i, n in enumerate(nums):
            if n in target_map.keys() and n not in h_set:
                r_list.append([target_map[n], n])
                h_set.add(n)
            if target - n not in target_map.keys():
                # target_num => num
                target_map[target - n] = n
        return r_list

    def threeSum_simple_hash(self, nums):
        result_list = []
        target = 0
        history_set = set()
        nums.sort()

        for i, x in enumerate(nums):
            if x not in history_set and x <= 0:
                new_nums = nums.copy()
                new_nums = new_nums[i + 1:]
                r_list = self.twoSum(target - x, new_nums)
                for r in r_list:
                    is_use = False
                    for e in r:
                        if e in history_set:
                            is_use = True
                    if not is_use:
                        result_list.append([x, r[0], r[1]])
                history_set.add(x)

        return result_list

    def double_needle(self, nums):
        result_list = []
        target = 0
        nums.sort()

        for i, x in enumerate(nums):
            if x > 0:
                break
            if i > 0 and x == nums[i - 1]:
                continue
            target_nums = nums[i + 1:]
            r_list = self.find_two_sum_by_double_needle(target - x, target_nums)
            result_list += [[x, r[0], r[1]] for r in r_list]
        return result_list

    def find_two_sum_by_double_needle(self, target, target_nums):
        r_list = []
        left_index, right_index = 0, len(target_nums) - 1
        while left_index < right_index:
            if left_index > 0 and target_nums[left_index] == target_nums[left_index - 1]:
                left_index += 1
                continue
            if right_index < len(target_nums) - 1 and target_nums[right_index] == target_nums[right_index + 1]:
                right_index -= 1
                continue

            if target_nums[left_index] + target_nums[right_index] > target:
                right_index -= 1
            elif target_nums[left_index] + target_nums[right_index] < target:
                left_index += 1
            else:
                r_list.append([target_nums[left_index], target_nums[right_index]])
                right_index -= 1
                left_index += 1
        return r_list


s = Solution()
# r = s.find_two_sum_by_double_needle(2, [0,0,2,2])
# print(r)
r = s.double_needle([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])
print(r)
# #
# a = set([1,3,2])
# b = set([1,4,3])
# print(a == b)


# [-1,0,1,2,-1,-4]
# [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
