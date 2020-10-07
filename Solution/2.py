# 2. 两数相加
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# 需要考虑特殊情况：
# 1，不同位数的两个数相加，
# 如：(3 -> 2 -> 1) + (5 -> 4 -> 3 -> 2 -> 1)
#      123 + 12345
# 2.进位，5 + 6 = 11
class Listwy:
    def __init__(self):
        self.head = None

    def __add__(self, other):
        cur = ListNode(other)
        cur.next = self.head
        self.head = cur

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add(l1,l2,nodeadd):
            if l1 or l2:
                if nodeadd == 1:
                    sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + 1
                else:
                    sum = (l1.val if l1 else 0) + (l2.val if l2 else 0)
                if sum >= 10:
                    curnode = sum - 10
                    nexnodeadd = 1
                else:
                    curnode = sum
                    nexnodeadd = 0


                outnode = ListNode(curnode)
                outnode.next = add(l1.next if l1 else None, l2.next if l2 else None, nexnodeadd)
            else:
                if nodeadd == 1:
                    outnode = ListNode(nodeadd)
                else:
                    return None
            return outnode
        return add(l1,l2,0)

L1 = Listwy()
L1.__add__(9)
L1.__add__(9)


L2 = Listwy()
L2.__add__(9)
L2.__add__(9)
L2.__add__(9)
L2.__add__(9)
S = Solution()
out = S.addTwoNumbers(L1.head,L2.head)
print(out.val)


# 提交未通过的测试用例：
# [9,9,9,9,9,9,9]
# [9,9,9,9]



