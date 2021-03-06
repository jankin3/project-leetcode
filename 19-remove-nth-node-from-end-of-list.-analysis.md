### 题目地址
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

### 题目描述
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的

### 我的思路
双指针，A指针从头开始遍历，B指针是A指针的前n个位置，当A指针到达末尾的时候，B指针刚好是当前删除位置.

变形版，A指针在头指针的后n个位置，B在开始位置

### 其他的思路
双层遍历，第一次先算出链表长度，然后第二次找到位置

### 复杂度分析

时间复杂度：O(L)，该算法对含有 LL 个结点的列表进行了一次遍历。因此时间复杂度为 O(L)。

空间复杂度：O(1)，我们只用了常量级的额外空间。

### 代码
```python
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
```