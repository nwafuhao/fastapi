"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点
。如果两个链表不存在相交节点，返回 null 。
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            # A = A.next if A else headB
            # B = B.next if B else headA
            if A is not None:
                A = A.next
            else:
                A = headB
            if B is not None:
                B = B.next
            else:
                B = headA
        return A
    # 链表相交，则链表尾部一定相同，所以先遍历两个链表，找到尾部，如果尾部相同，则相交，否则不相交
    # 如果相交，则从尾部开始，两个链表长度相同，所以从尾部开始遍历，直到找到相同的节点
    # 如果不相交，则从尾部开始遍历，直到找到None
    # 时间复杂度：O(n+m)，n和m分别为两个链表的长度
    # 空间复杂度：O(1)


if __name__ == '__main__':
    # 1. 先创建共同部分
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)

    # 2. 创建链表A，指向共同部分
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common  # 指向共同部分

    # 3. 创建链表B，指向共同部分
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = common  # 指向共同部分

    # 现在两个链表真正相交了！
    # A: 4 → 1 → 8 → 4 → 5 → null
    #              ↗
    # B: 5 → 6 → 1
    #              ↘
    #              8 → 4 → 5 → null

    solution = Solution()
    result = solution.getIntersectionNode(headA, headB)
    print(result.val if result else None)  # 输出: 8

