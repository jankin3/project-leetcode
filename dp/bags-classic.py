# -*- coding: utf-8 -*-

# 动态规划经典背包问题分析
def bag(n, c, w, p):
    '''
    ０１背包基本解法
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
    print(res)
    return res

def bag_one_dismensional(n, c, w, p):
    '''
    ０１背包一维数组解法
    :param n: 物品件数
    :param c: 最大承重
    :param w: 各个物品的重量
    :param p: 各个物品的价值
    :return: 二维数组
    '''
    res = [0 for j in range(c + 1)]
    for i in range(n+1):
        print(res)
        for j in range(c, w[i-1]-1, -1):
            if i == 0:
                res[j] = 0
            else:
                # 核心　此处通过比较判断得出是，加入该商品或者不加
                res[j] = max(res[j], res[j-w[i-1]] + p[i-1])
    print(res)
    return res

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
    print(res)
    return res


# 以下代码功能：标记出有放入背包的物品
# 反过来标记，在相同价值情况下，后一件物品比前一件物品的最大价值大，则表示物品i#有被加入到背包，x数组设置为True。设初始为j=c。
def show(n, c, w, res):
    print('max price:', res[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(1, n + 1):
        if res[i][j] > res[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    for i in range(n):
        if x[i]:
            print('the', i, 'rd,')


if __name__ == '__main__':
    n = 5
    c = 10
    w = [2, 2, 6, 5, 4]
    p = [3, 6, 5, 4, 6]
    res1 = bag(n, c, w, p)
    show(n, c, w, res1)
    # print('-'*10)
    res = bag_total_one_dismensional(n, c, w, p)
    # show(n, c, w, res)
