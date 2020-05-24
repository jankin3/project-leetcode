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
    def addTwoNumbers(self, l1, l2):
        more = 0
        l3 = ListNode()
        new_node = l3
        while True:
            _sum = l1.val + l2.val + more
            new_num = _sum % 10
            more = int(_sum / 10)

            new_node.next = ListNode(new_num)
            new_node = new_node.next
            if l1.next == None or l2.next == None:
                if more:
                    if l1.next == None:
                        l1.val = 0
                    else:
                        l1 = l1.next
                    if l2.next == None:
                        l2.val = 0
                    else:
                        l2 = l2.next
                    continue
                break
            else:
                l1 = l1.next
                l2 = l2.next

        if l1.next != None:
            new_node.next = l1.next
        if l2.next != None:
            new_node.next = l2.next
        l3 = l3.next
        return l3

    def addTwoNumbers_v2(self, l1, l2):
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

s = Solution()
l1_list = LinkList()
l1_list.initList([1])
l1 = l1_list.head
l2_list = LinkList()
l2_list.initList([9,9])
l2 = l2_list.head
r = s.addTwoNumbers_v2(l1, l2)
print('result')
while True:
    print(r.val)
    if r.next != None:
        r = r.next
    else:
        break


