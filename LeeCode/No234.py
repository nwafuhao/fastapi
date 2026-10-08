"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_to_list(head):
    result = []
    cur = head
    while cur:
        result.append(head.val)
        cur = cur.next
    return result

def list_to_linked(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

class Solution01:
    def isPalindrome(self, head: ListNode) -> bool:
        list01 = linked_to_list(head)

        left, right = 0, len(list01) - 1
        while left < right:
            if list01[left] != list01[right]:
                return False
            left += 1
            right -= 1
        return True

class Solution02:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # 1. 快慢指针找中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 反转后半部分
        prev = None
        while slow:
            next_temp = slow.next
            slow.next = prev
            prev = slow
            slow = next_temp

        # 3. 比较前后两部分
        left, right = head, prev
        while right:  # 只需要比较后半部分
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

if __name__ == '__main__':
    tarLinked = list_to_linked([1,2,2,1])
    solution = Solution01().isPalindrome(tarLinked)
    print(solution)
