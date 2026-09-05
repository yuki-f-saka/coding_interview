"""
Reorder Linked List
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Constraints:

1 <= Length of the list <= 1000.
1 <= Node.val <= 1000

https://neetcode.io/problems/reorder-linked-list/question?list=neetcode150
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        特殊な順番に並び替える
        [0, n-1, 1, n-2, 2, n-3, ...]
        tail部分がheadの次に来るのはどうすればいいか？
        * A案: headとtailという一番端に2pointerを持ってきて、中心に向けて1つずつ探索
        * B案: linkedlistを半分に区切って、前半を昇順、後半を降順に、交互に並べる

        A案のtailを取っていくのが難しそう
        B案の方がテクの組み合わせでできそう

        (1)半分に区切るのは1回目のlookupでこのlinkedlistのlengthをcountして、2回目のlookupでlengthの半分までをlookupすればいい。
        (2)後半を降順にするのは、reverse_linked_listでやった
        (3)交互にくっつけていくのは、merged_linked_listのテク
        """
        if not head or not head.next:
            return

        # 半分に区切る
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        n = 1

        front = head
        back = None
        while front:
            if n == (length + 1) // 2: 
                # 半分に達したらそこから先は後半リストに切り出す
                back = front.next
                # 前半はここまでなので切る
                front.next = None
                break
            n += 1
            front = front.next

        # 前半、後半に切ることができたので、後半をreverseする
        reversed_back = self.reverseList(back)

        # frontとreversed_backを交互にmergeしていく
        curr = head
        front = head.next
        while front or reversed_back:
            if reversed_back:
                curr.next = reversed_back
                reversed_back = reversed_back.next
                curr = curr.next
            if front:
                curr.next = front
                front = front.next
                curr = curr.next
        
        return

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next
        return prev