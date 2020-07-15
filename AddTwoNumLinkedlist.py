
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 342 + 465 = 807

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        # Fill this in.
        head = l1
        while l1 != None and l2 != None:
            tmp = l1.val + l2.val
            if tmp < 10:
                l1.val = tmp
            else:
                l1.val = tmp % 10
                if l1.next == None:
                    l1.next = ListNode(1)
                else:
                    l1.next.val += 1

            l1 = l1.next
            l2 = l2.next
        return head

# 342
l1 = ListNode(2)    # 2 -> None
l1.next = ListNode(4)   # 4 -> None
l1.next.next = ListNode(3)  # 3 -> None


# Or another way to create linked list
# 465
l2 = ListNode(5)
l2_second = ListNode(6)
l2_third = ListNode(4)
l2.next = l2_second
l2_second.next = l2_third

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8

# while l1:
#     print(l1.val)
#     l1 = l1.next
#
#     print(l2.val)
#     l2 = l2.next
