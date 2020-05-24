### 题目地址
https://leetcode-cn.com/problems/add-two-numbers/

### 题目描述
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
```python
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
```

### 思路
思路比较简单,模拟手算的过程.
1. 建立一个带头结点的ｌ３链表来存储新的数据
2. 遍历，开始累加l1.var, l2.var(如果list为空则var为0), more(进位)
3. 链表各自后移.仅仅当任意一个ｌｉｓｔ结束并且进位为０的时候结束．
4. 续上后续的ｌｉｓｔ

### 反思
这个题目完全属于思路不复杂,但是细节非常多的问题.刚开始解题的时候没有想清楚`进位与list结束`的关系.导致修改代码很多次.需要谨记在心.

###　代码
```python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None

    # 链表初始化函数, 方法类似于尾插
    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        more = 0
        l3 = ListNode()
        new_node = l3
        while True:
            p = 0 if l1 == None else l1.val
            q = 0 if l2 == None else l2.val
            _sum = p + q + more
            new_num = _sum % 10
            more = int(_sum / 10)

            new_node.next = ListNode(new_num)
            new_node = new_node.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            if not more and (l1 == None or l2 == None):
                break

        if l1 != None:
            new_node.next = l1
        if l2 != None:
            new_node.next = l2
        l3 = l3.next
        return l3
```