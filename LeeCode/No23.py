"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            lists = merged

        return lists[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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


# ============================================================
# 工具函数：辅助测试
# ============================================================

def list_to_linked(arr):
    """将列表转换为链表"""
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head


def linked_to_list(head):
    """将链表转换为列表（方便查看结果）"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def print_linked_list(head):
    """打印链表（带箭头）"""
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" → ".join(result) + " → None")


# ============================================================
# 测试函数
# ============================================================

def test_case(case_num, lists_data, expected):
    """测试单个用例"""
    print(f"\n{'=' * 50}")
    print(f"测试用例 {case_num}")
    print(f"{'=' * 50}")

    # 将数据转换为链表
    lists = []
    for data in lists_data:
        lists.append(list_to_linked(data))

    # 打印输入
    print("输入链表：")
    for i, head in enumerate(lists):
        print(f"  L{i + 1}: ", end="")
        print_linked_list(head)

    # 执行合并
    solution = Solution()
    result = solution.mergeKLists(lists)

    # 打印输出
    print("合并结果：")
    print("  ", end="")
    print_linked_list(result)

    # 转换为列表比较
    result_list = linked_to_list(result)
    print(f"结果列表：{result_list}")
    print(f"期望结果：{expected}")

    # 判断是否正确
    if result_list == expected:
        print("✅ 测试通过！")
    else:
        print("❌ 测试失败！")


# ============================================================
# 运行所有测试
# ============================================================

if __name__ == '__main__':
    # 测试1：正常情况
    test_case(1, [[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6])

    # 测试2：包含空链表
    test_case(2, [[], [1, 3, 4], [2, 6]], [1, 2, 3, 4, 6])

    # 测试3：所有链表都为空
    test_case(3, [[], [], []], [])

    # 测试4：只有一个链表
    test_case(4, [[1, 2, 3, 4, 5]], [1, 2, 3, 4, 5])

    # 测试5：包含负数
    test_case(5, [[-3, -1, 0], [-2, 2, 3], [-5, 4, 5]], [-5, -3, -2, -1, 0, 2, 3, 4, 5])

    # 测试6：长度不同（有短有长）
    test_case(6, [[1, 9], [2, 5, 8, 11], [3, 4, 7]], [1, 2, 3, 4, 5, 7, 8, 9, 11])

    # 测试7：只有一个节点
    test_case(7, [[1], [2], [3]], [1, 2, 3])

    # 测试8：空链表数组
    test_case(8, [], [])

    print(f"\n{'=' * 50}")
    print("所有测试完成！")
    print(f"{'=' * 50}")


