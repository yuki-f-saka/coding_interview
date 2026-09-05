"""
Copy Linked List with Random Pointer
Solved 
You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

Constraints:

0 <= n <= 100
-100 <= Node.val <= 100
random is null or is pointing to some node in the linked list.

https://neetcode.io/problems/copy-linked-list-with-random-pointer/history
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        First, Traverse the input list to create a new list and a hash map
        that maps each original node to its corresponding new node.
        Second, Traverse the input list and assign the random pointer of the new list.
        """
        hashmap = {}
        cur = head
        copy_head = copy = Node(0)
        while cur:
            copy.next = Node(cur.val)
            hashmap[cur] = copy.next
            cur = cur.next
            copy = copy.next
        copy = copy_head.next

        while head:
            copy.random = hashmap.get(head.random)
            head = head.next
            copy = copy.next
        
        return copy_head.next