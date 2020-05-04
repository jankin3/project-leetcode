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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next

s = Solution()
l1 = LinkList()
l1.initList([1, 2, 5])
l2 = LinkList()
l2.initList([4, 6, 7])

r = s.mergeTwoLists(l1.head, l2.head)
while True:
    print(r.val)
    if r.next == None:
        break
    r = r.next