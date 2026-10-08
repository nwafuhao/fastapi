"""
给你一个链表的头节点 head ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

如果链表中存在环 ，则返回 true 。 否则，返回 false 。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def list_to_linked(nums):
    head = ListNode(nums[0])
    temp = head
    for i in nums[1:]:
        temp.next = ListNode(nums[i])
        temp = temp.next
    return head

def linked_to_list(head):
    result = []
    cur = head
    while cur:
        result.append(head.val)
        cur = cur.next
    return result

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

if __name__ == '__main__':
    tarLinked = list_to_linked([3,2,0,-4])
    solution = Solution().hasCycle(tarLinked)
    print(solution)