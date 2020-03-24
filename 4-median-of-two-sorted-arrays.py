# to do
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m1 = self.getSingleListMedian(nums1)
        m2 = self.getSingleListMedian(nums2)
        if m1 < m2:
            if (len(nums1) + len(nums2)) % 2 != 0:
                median_index = (len(nums1) + len(nums2) - 1) % 2
                exist_num = len(nums1) / 2 if len(nums1) % 2 == 0 else len(nums1) + 1 / 2
                least_num = median_index - exist_num
                small_l_start = exist_num

                while least_num > 0:
                    pass


    def getSingleListMedian(self, l):
        print(int(len(l) / 2))
        if len(l) % 2 == 0:
            x1, x2 = self.getMedianIndex(len(l))
            return (l[x1] + l[x2]) / 2.0
        else:
            return l[self.getMedianIndex(len(l))]

    def getMedianIndex(self, n):
        if n % 2 == 0:
            return [int((n / 2)) - 1, int((n / 2))]
        else:
            return int(n / 2)


s = Solution()

# r = s.getSingleListMedian([1, 2, 3, 7, 13])
# print(r)
r = s.findMedianSortedArrays([1, 2, 3, 6, 7, 13], [4, 9, 10])
print(r)
