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

class Solution():
    def reverseList(self, head):
        '''
        反转一个单链表。
        :param head:
        :return:
        '''
        new_head = ListNode(0)
        new_head.next = head
         # 第二个节点开始
        while head.next != None:
            p = head.next
            head.next = p.next # delete
            # 插入到头部
            p.next = new_head.next
            new_head.next = p
        return new_head.next

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
        :param head:
        :param m:
        :param n:
        :return:
        '''
        if n == 1: return head
        prev = ListNode(0)
        prev.next = head
        cur = head
        head = prev
        for i in range(1, n):
            if i < m:
                prev = prev.next
                cur = cur.next
            if i >= m and i <= n:
                p = cur.next
                cur.next = p.next
                p.next = prev.next
                prev.next = p
        return head.next

s = Solution()
l = LinkList()
l.initList([1,2,4,6,7])
h = l.head
r = s.reverseList(h)
print('result')
while True:
    print(r.val)
    if r.next != None:
        r = r.next
    else:
        break