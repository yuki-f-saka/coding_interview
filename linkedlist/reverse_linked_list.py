from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next is None:
            return f"{{val: {self.val}, next: None}}"
        else:
            return f"{{val: {self.val}, next: {repr(self.next)}}}"

def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # two pointerで行う
    prev = None
    cur = head
    while cur:
        # curのnext_nodeとのつながりがこのあと切られるので先に保管しておく
        next_node = cur.next
        # curのnextポインタを前に向ける
        cur.next = prev
        # prev, curを一つずつ進める
        prev = cur
        cur = next_node
    
    return prev
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(reverse_linked_list(head))