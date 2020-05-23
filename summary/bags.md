# 01背包问题
### 基础版本
##### 问题描述
给出n个珍珠的体积v[i]和其价值price[i]，将他们装入一个大小为C的背包，最多能装入的总价值有多大？
思路：d[i][j] 表示当前ｉ个物品的体积为ｊ时的最大价值． 根据递推关系式得出递推关系是：　
```python
# v, p 分别是体积和价值, i-1表示有移位
# 如果不加入该商品，　价值不变
d[i][j] = d[i-1][j]
#　如果加入该商品，
d[i][j] = d[i-1][j-ｗ[i-1]] + p[i-1]
合并
d[i][j] = max(d[i-1][j],　d[i-1][j-ｗ[i-1]] + p[i-1])
```
##### 核心代码
```python
def bag(n, c, w, p):
    '''
    背包动态规划过程
    :param n: 物品件数
    :param c: 最大承重
    :param w: 各个物品的重量
    :param p: 各个物品的价值
    :return: 二维数组
    '''
    res = [[-1 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(n+1):
        for j in range(c+1):
            if i == 0:
                res[i][j] = 0
            else:
                res[i][j] = res[i-1][j]

            # compare
            if w[i-1] <= j and i > 0:
                # 核心　此处通过比较判断得出是，加入该商品或者不加
                res[i][j] = max(res[i][j], res[i-1][j-w[i-1]] + p[i-1])

    return res
```
##### 复杂度：
时间ｎ*c, 空间ｎ*c

### 优化－(一维数组)
时间复杂度无法优化，空间复杂度上，可以看出每次res[i][j] = max(res[i][j], res[i-1][j-w[i-1]] + p[i-1])产生｀递推计算其实只和前一列的结果相关｀．所以可以只用一位数组来存储数据．又因为后面的数据要依赖以前面的结果，所以采用倒序的方式计算
代码
```python
def bag_simple(n, c, w, p):
    '''
    背包动态规划过程
    :param n: 物品件数
    :param c: 最大承重
    :param w: 各个物品的重量
    :param p: 各个物品的价值
    :return: 二维数组
    '''
    res = [0 for j in range(c + 1)]
    for i in range(n+1):
        for j in range(c, w[i-1]-1, -1): # 倒序，防止覆盖
            if i == 0:
                res[j] = 0
            else:
                res[j] = max(res[j], res[j-w[i-1]] + p[i-1])
    return res
```

### 变形1-完全背包问题
问题描述：有N种物品和一个容量为V的背包，每种物品都有无限件可用。第i种物品的费用是c[i]，价值是w[i]。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。
```python
def bag_total_one_dismensional(n, c, w, p):
    '''
    完全背包问题
    :param n: 物品件数
    :param c: 最大承重
    :param w: 各个物品的重量
    :param p: 各个物品的价值
    :return: 二维数组
    '''
    res = [0 for j in range(c + 1)]
    for i in range(n+1):
        print(res)
        for j in range(w[i-1], c+1):
            if i == 0:
                res[j] = 0
            else:
                res[j] = max(res[j], res[j-w[i-1]] + p[i-1])
    return res
```

问题描述: 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
 

### 变形２
问题描述：给定不同面额的硬币和一个总金额m和总的硬币数量ｎ. 写出函数来计算可以凑成总金额的硬币组合