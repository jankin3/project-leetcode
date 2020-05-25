# 二分查找
描述: 一种在有序数组中查找某一特定元素的搜索算法。搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半
时间复杂度:log2n

###　变形１-查找最新(最后)出现的下标

```python
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
```
###　变形2-查找第一个出现的大于等于x的值,(查找最后一个小于x的值)

```python
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
```

### 应用
１．设计一个根据ｉｐ找到城市信息的函数
  + 建立连续ｉｐ段的最大值对应城市的键值对
  + 二分查找第一个出现大于ｉｐ值的键，其值则是结果
 分析：多个键值对应一个ｖａｌ，多对一，并且键值是连续的．则可以聚合键值 