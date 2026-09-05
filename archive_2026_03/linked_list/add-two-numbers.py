"""
Add Two Numbers
Medium
Company Tags
Hints
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Constraints:

1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9

https://neetcode.io/problems/add-two-numbers/question?list=neetcode150
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        walk through
        First, we traverse the l1 to get each node's value, and then we multiply the first by 1, 
        the next by 10, the following by 100 and so on, and finally sum them up to form a single number.
        We do the same thing to the l2 as well.
        We have two single numbers, so we add them together.
        We divide that number by 10, then the remainder is first node's value, and dividing 100 and so on.

        But this idea needs to 3 times traverse. So we take O(3n) time complexity.

        Another idea
        Traverse l1 and l2 in parallel and add them.
        We create a new linked list node's value by the sum.
        If the sum results in a carry, for example when 8 plus 8 equals 16, the carry will be added to the next node in the linked list.
        we take just O(m+n) time complexity when we do that way.
        m is l1 length and n is l2 length.
        """

        """
        First solution is wrong.
        NO:
        ・while cur1 and cur2
        ・Only one time link the tail to carry

        cur1 = l1
        cur2 = l2
        carry = 0
        dummy = res = ListNode()
        while cur1 and cur2:
            sum = cur1.val + cur2.val + carry
            if sum > 9:
                carry = 1
                sum = sum - 10
            else:
                carry = 0
            res.next = ListNode(sum)
            res = res.next
            cur1 = cur1.next
            cur2 = cur2.next
        if carry == 1:
            res.next = ListNode(carry)
        return dummy.next
        """

        cur1, cur2 = l1, l2
        carry = 0
        dummy = ListNode(0)
        tail = dummy

        while cur1 or cur2 or carry:
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0

            s = v1 + v2 + carry
            carry = s // 10
            digit = s % 10

            tail.next = ListNode(digit)
            tail = tail.next

            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None

        return dummy.next
