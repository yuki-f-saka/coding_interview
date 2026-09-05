"""
Linked List Cycle Detection
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

https://neetcode.io/problems/linked-list-cycle-detection/question?list=neetcode150

constraints
1 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # headから始まるlinkedlistがずっと続くならtrue、途中で同じノードを経由するならfalse
        # if the linked list starting from head continues forever, it's true.
        # if pass the same node multi times, it's false.

        # 「ずっと続くなら」これを具体的にいうと、
        # linkedlistをlookupしていき、node.nextがどこかでNullになるならそこで終わり。続かない。
        # 途中で同じノードに当たったらcycleしているからずっと続く
        
        # 途中で同じノードに当たるにはどうすればいいか
        # slowとfastの2pointerを使えばいい。
        if not head or not head.next: # <- ここはwhile文の制約でheadやhead.nextがNullならループに入らないから余計な実装
            return False
        
        slow = fast = head
        # 正解を見るとslowはfastより先にNullにはならないため、
        # while fast and fast.next でいい
        while slow and fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False