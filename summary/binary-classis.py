# -*- coding: utf-8 -*-

class Solution():
    def binary_search(self, l, x):
        '基本二分查找'
        if not l: return -1
        left, right = 0, len(l) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if l[mid] < x:
                left = mid + 1
            elif l[mid] > x:
                right = mid - 1
            else:
                return l[mid]
        return -1

    def binary_search_first(self, l, x):
        '变形1, 查找最新(最后)出现的下标'
        if not l: return -1
        left, right = 0, len(l) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if l[mid] < x:
                left = mid + 1
            elif l[mid] > x:
                right = mid - 1
            else:
                if mid == 0 or l[mid - 1] != l[mid]:  # 当mid到达最左边或者mid和前面一个数不等的时候证明是第一个数
                    return mid
                right = mid - 1
        return mid

    def binary_search_first_bigger(self, l, x):
        '变形2,查找第一个出现的大于等于x的值,(查找最后一个小于x的值)'
        if not l: return -1
        left, right = 0, len(l) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if l[mid] < x:
                left = mid + 1
            else:
                if mid == 0 or l[mid - 1] < x:
                    return l[mid]
                right = mid - 1
        return -1


s = Solution()
r = s.binary_search_first_bigger([1, 2,4, 5, 7, 12, 14], 3)
print(r)
