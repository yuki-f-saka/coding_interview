"""
Reverse Linked List
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
https://neetcode.io/problems/reverse-a-linked-list/question?list=neetcode150

そもそもLinked Listとは何か？
Linked Listはノードの集合で、各ノードはデータと次のノードへの参照（ポインタ）を持っている

配列だと以下のような問題がある。
- サイズ変更が難しい
- 要素の追加すると、それ以降の要素のシフトが必要
それを解決するために、Linked Listが考えられた
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        たぶん図でイメージするほうがよい
        団子を一つ一つ入れ替えていくイメージ

        - 2pointerをuseする
            - prevとcur
        - whileループ
            - cur.nextをstoreしておく
            - cur.nextをprevにむける
            - pointerをmoveさせる
                - prevをcurへ
                - curを保管しておいたnextへ
        - 全ての付け替えが終わったら、prevが次の先頭になってるからreturnする
        """
        prev = None
        cur = head

        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next
        return prev
