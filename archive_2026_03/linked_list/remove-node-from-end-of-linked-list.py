"""
Remove Node From End of Linked List
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

https://neetcode.io/problems/remove-node-from-end-of-linked-list/question?list=neetcode150
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        First of all, I can reverse linked list.
        Then I can remove nth node from beginning. nth is 1-indexed.
        After that reverse that again.
        return the head.

        Reversing takes O(sz) time complexity. sz means the number of nodes in the linked list.
        Remove nth node takes O(n).
        Seconds reversing takes O(sz) too.
        So total time complexity is O(sz + n + sz) -> O(n) I guess.

        It took 10 minites to walk through my thought.
        """
        if not head or not head.next:
            return None
        reversed_head = self.reverse(head)
        
        # removing nth from beginning is that previous node's next pointer aim to current next node.
        # [4, 3, 2, 1], n = 2 -> 4 linked to 2
        dummy = reversed_head
        if n == 1:
            reversed_head = reversed_head.next
            return self.reverse(reversed_head)
        else:
            while n - 2 > 0:
                reversed_head = reversed_head.next
                n -= 1
            reversed_head_next = reversed_head.next
            reversed_head.next = reversed_head_next.next

        return self.reverse(dummy)

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next

        return prev
