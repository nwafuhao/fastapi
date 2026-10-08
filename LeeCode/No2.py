"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head


def linked_to_list(head):
    result = []
    cur = head
    while cur:
        result.append(head.val)
        cur = cur.next
    return result


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            cur.next = ListNode(digit)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# ====== 测试 ======
if __name__ == '__main__':
    solution = Solution()

    # 测试1：342 + 465 = 807
    l1 = list_to_linked([2, 4, 3])
    l2 = list_to_linked([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_to_list(result))  # [7, 0, 8] ✅

    # 测试2：9999 + 1 = 10000
    l1 = list_to_linked([9, 9, 9, 9])
    l2 = list_to_linked([1])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_to_list(result))  # [0, 0, 0, 0, 1] ✅

    # 测试3：0 + 0 = 0
    l1 = list_to_linked([0])
    l2 = list_to_linked([0])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_to_list(result))  # [0] ✅

    # 测试4：5 + 5 = 10
    l1 = list_to_linked([5])
    l2 = list_to_linked([5])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_to_list(result))  # [0, 1] ✅


