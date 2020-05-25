#单链表翻转－基本
### 题目地址
https://leetcode-cn.com/problems/reverse-linked-list/

###题目描述
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

### 思路-迭代法
1. 建立一个空的头结点
2. 遍历一遍元素，将后续元素不断加入头结点的后面

### 代码
```python
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
```

# 变形版本
### 题目地址
https://leetcode-cn.com/problems/reverse-linked-list-ii/

###题目描述
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

### 思路-迭代法
思路相似
1. 建立一个空的头结点
2. 找到开始位置
3. 遍历一遍元素，将后续元素不断加入头结点的后面