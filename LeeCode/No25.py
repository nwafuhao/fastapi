"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""
from itertools import count
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #1. 检查是否有满足的k个节点
        count = 0
        cur = head
        while cur and count < k:
            cur = cur.next
            count += 1

        if count < k:
            return head #不够K个，不反转

        #2. 反转前K个节点
        prev = None
        cur = head
        for _ in range(k):
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp

        head.next = self.reverseKGroup(cur, k) #递归

        return prev

class Solution2:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        #创建哑节点，方便处理头节点
        dummy = ListNode(0)
        dummy.next = head

        prev_group_end = dummy #上一组的末尾
        while True:
            #检查是否满足k个节点
            group_start = prev_group_end.next
            group_end = prev_group_end

            for _ in range(k):
                group_end = group_end.next
                if not group_end: #不够k个节点
                    return dummy.next

            #2、断开并反转这K个节点
            next_group_start = group_end.next #下一组的头节点
            group_end.next = None #断开

            #反转group_start到group_end
            reversed_start, reversed_end = self.reverse(group_start)

            #3、连接反转后的节点
            prev_group_end.next = reversed_start
            reversed_end.next = next_group_start

            #更新prev_group_end
            prev_group_end = reversed_end

    def reverse(self, head):
        prev = None
        cur = head
        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp
        return prev, head



