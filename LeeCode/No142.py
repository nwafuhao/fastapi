"""
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
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

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        if not fast or not fast.next:
            return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

if __name__ == '__main__':
    head = list_to_linked([3,2,0,-4])
    head.next.next.next.next = head.next
    print(Solution().detectCycle(head).val)

