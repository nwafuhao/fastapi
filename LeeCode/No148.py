"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
#
# def list_to_linked(arr):
#     if not arr:
#         return None
#     head = ListNode(arr[0])
#     cur = head
#     for val in arr[1:]:
#         cur.next = ListNode(val)
#         cur = cur.next
#     return head
#
#
# def linked_to_list(head):
#     result = []
#     while head:
#         result.append(head.val)
#         head = head.next
#     return result
#
#
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
#
#         vals = []
#         cur = head
#         while cur:
#             vals.append(cur.val)
#             cur = cur.next
#
#         vals.sort()
#
#         new_head = ListNode(vals[0])
#         cur = new_head
#         for val in vals[1:]:
#             cur.next = ListNode(val)
#             cur = cur.next
#
#         return new_head
#
#
# # ====== 测试 ======
# if __name__ == '__main__':
#     solution = Solution()
#
#     # 测试1：乱序
#     head = list_to_linked([4, 2, 1, 3])
#     result = solution.sortList(head)
#     print(linked_to_list(result))  # [1, 2, 3, 4] ✅
#
#     # 测试2：倒序
#     head = list_to_linked([5, 4, 3, 2, 1])
#     result = solution.sortList(head)
#     print(linked_to_list(result))  # [1, 2, 3, 4, 5] ✅
#
#     # 测试3：空链表
#     result = solution.sortList(None)
#     print(result)  # None ✅
#
#     # 测试4：单节点
#     head = list_to_linked([1])
#     result = solution.sortList(head)
#     print(linked_to_list(result))  # [1] ✅
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 找中点（使用快慢指针）
        slow = head
        fast = head

        # 注意：这里用 fast 和 fast.next fast的步长是slowd的2倍
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 断开链表
        mid = slow.next
        slow.next = None

        # 递归排序
        left = self.sortList(head)
        right = self.sortList(mid)

        # 合并
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return dummy.next