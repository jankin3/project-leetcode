# 第Ｋ个字典序的数字
### 题目地址
https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/

###题目描述
给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。

注意：1 ≤ k ≤ n ≤ 109。

```python
示例 :

输入:
n: 13   k: 2

输出:
10

解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
```

### 思路
思路是建立一个十叉树，然后在书中进行先序遍历．
根据题目的特征，树非常接近满叉树，所以快速计算出每棵树下面的子节点的数量．
分解步骤
1. 计算出每棵树下面的子节点的数量
2. 如果超出ｋ的位置，则向右寻找
3. 如果没有超出ｋ的位置,　则说明位置在子树中，向下寻找

代码
```python
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def getNodeNums(n, x):
            '获取该节点下面所有的节点数目'
            pre = x
            stop = pre + 1
            count = 0
            while pre <= n:
                count += min(stop, n+1) - pre

                stop = stop * 10
                pre = pre * 10
            return count

        def find_last_num(n, x):
            '获取该节点下面最后一个节点的值'
            pre = x
            stop = pre + 1
            last_num = x
            while pre <= n:
                last_num = min(n, stop-1)

                stop = stop * 10
                pre = pre * 10
            return last_num

        pos = 0 # 当前累加的位置
        start= 0 #　多叉树的位置
        while pos < k:
            for i in range(0, 10):
                if start == 0 and i == 0: # 第一次没有０开始
                    continue
                cur_num = start * 10 + i
                cur_len = getNodeNums(n, cur_num)
                if pos + cur_len < k: # 长度不够继续下一个节点
                    pos += cur_len
                    continue
                elif pos + cur_len > k: # 向下走
                    if pos + 1 == k: #如果刚好是多了一个节点则是该节点
                        return cur_num
                    start = cur_num
                    pos += 1
                    break
                else:
                    return find_last_num(n, cur_num)

```