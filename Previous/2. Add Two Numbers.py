"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return_ll = ListNode()
        ll_pointer = return_ll
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            if l1 == None and l2 == None:  # if both are empty, there must be a carry
                ll_pointer.next = ListNode(1)
                break
            else:
                one = 0
                two = 0
                if l1 != None:
                    one = l1.val
                if l2 != None:
                    two = l2.val
                sum = one + two + carry
                carry = sum // 10
                ll_pointer.next = ListNode(sum % 10)
                ll_pointer = ll_pointer.next
                if l1 != None:
                    l1 = l1.next
                if l2 != None:
                    l2 = l2.next

        return_ll = return_ll.next
        return return_ll


"""More brute force method, requiring iterating across both l1 and l2 linked lists, storing those values in
corresponding ints, summing those ints,then iterating across every digit within the sum to construct the new linked list"""
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         one = 0
#         two = 0
#         l1_counter = 0
#         l2_counter = 0
#         l1_pointer = l1
#         l2_pointer = l2
#         while (l1_pointer != None):
#             one = one + l1_pointer.val * 10 ** l1_counter
#             l1_counter += 1
#             l1_pointer = l1_pointer.next
#         while (l2_pointer != None):
#             two = two + l2_pointer.val * 10 ** l2_counter
#             l2_counter += 1
#             l2_pointer = l2_pointer.next

#         sum = one + two
#         print(sum)
#         sol_ll = ListNode(sum % 10)
#         sol_ll_pointer = sol_ll
#         sum = sum // 10
#         while sum != 0:
#             sol_ll_pointer.next = ListNode(sum%10)
#             sol_ll_pointer = sol_ll_pointer.next
#             sum = sum // 10

#         return sol_ll
