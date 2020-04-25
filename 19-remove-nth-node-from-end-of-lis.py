# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None

    #链表初始化函数, 方法类似于尾插
    def initList(self, data):
        #创建头结点
        self.head = ListNode(data[0])
        p = self.head
        #逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        # 思路是双指针，A指针遍历，B指针是当前指针的前n个位置，当A指针到达末尾的时候，B指针刚好是当前删除位置
        node = ListNode(None)
        node.next = head

        front, back = node, node
        for i in range(n):
            front = front.next

        while True:
            if front.next == None:
                back.next = back.next.next
                break
            front = front.next
            back = back.next

        return node.next


s = Solution()
l = LinkList()
l.initList([1, 2, 3, 4, 5])
r = s.removeNthFromEnd(l.head, 3)
while True:
    print(r.val)
    if r.next == None:
        break
    r = r.next