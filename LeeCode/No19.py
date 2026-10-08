"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""
from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_to_list(head):
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result

def list_to_linked(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    cur = head
    for num in nums[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        if not vals:
            return None

        vals.pop(-n)

        if not vals:
            return None

        head = ListNode(vals[0])
        cur = head
        for val in vals[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return head


class Solution02:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. 创建哑节点
        dummy = ListNode(0)
        dummy.next = head

        # 2. 快慢指针都从 dummy 开始
        slow = dummy
        fast = dummy

        # 3. fast 先走 n+1 步
        for _ in range(n + 1):
            fast = fast.next

        # 4. 一起走，直到 fast 到 None
        while fast:
            slow = slow.next
            fast = fast.next

        # 5. 删除节点
        slow.next = slow.next.next

        # 6. 返回头节点
        return dummy.next

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = list_to_linked(nums)
    solution = Solution02().removeNthFromEnd(head, 2)
    print(linked_to_list(solution))
