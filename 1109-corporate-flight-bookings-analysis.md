### 题目地址
https://leetcode-cn.com/problems/corporate-flight-bookings/

### 题目描述
这里有 n 个航班，它们分别从 1 到 n 进行编号。

我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座位。

请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。


### 思路
暴力法:
直接遍历每条数据, 然后加上每个航班预定座位号
时间复杂度: m*n(m表示所给的数组的大小)

优化:
对于每个i->j段的航班,因为是连续的数据,使用数组change统计预定的座位数的变化量,
`即可以对于开始i,在航班i记录+k个座位,对于末尾j,在航班j+1位置-k个位置`
然后统计人数的时候,可以从头开始遍历一遍change数组,即可得出当时人数
时间复杂度: m+n
```python
    def corpFlightBookings(self, bookings, n):
        change = []
        for i in range(n):
            change.append(0)

        for item in bookings:
            change[item[0] - 1] += item[2]
            if item[1] <= n - 1:
                change[item[1]] -= item[2]
        #print(change)
        in_booking = []
        for i, c in enumerate(change):
            if i == 0:
                in_booking.append(c)
            else:
                in_booking.append(c+in_booking[-1])
        return in_booking

```

### 知识点
此问题的特征在于`时间段是连续的`,所以可以通过时间段的两段的点去统计对应的数据
类似问题: 站内同时在线人数问题?
