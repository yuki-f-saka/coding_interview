"""
Merge Two Sorted Linked Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

https://neetcode.io/problems/merge-two-sorted-linked-lists/question?list=neetcode150
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        2つのlinkedlistをくっつけてソート済みの1つのlinkedlistにする
        わからないが、おそらくlist1とlist2の先頭のノードのvalを比較して、
        小さい方を新規linkedlistにくっつけていく作業。
        """
        dummy = ListNode(0, None)
        merged_list = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur1_next = list1.next
                merged_list.next = list1
                list1 = cur1_next
            else:
                cur2_next = list2.next
                merged_list.next = list2
                list2 = cur2_next
            # merged_listをループごとに最新のノードに更新
            merged_list = merged_list.next
        
        if list1:
            merged_list.next = list1
        if list2:
            merged_list.next = list2
                
        # ここでdummyを固定しておいたのでmerged_listの先頭を参照できる
        return dummy.next