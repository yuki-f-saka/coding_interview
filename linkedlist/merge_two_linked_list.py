class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next is None:
            return f"{{val: {self.val}, next: None}}"
        else:
            return f"{{val: {self.val}, next: {repr(self.next)}}}"
        
def merge_two_lists(head1: ListNode, head2: ListNode):
    cur1 = head1
    cur2 = head2

    while cur1 and cur2:
        # cur1,cur2の次のノードをキープしておく
        cur1_next = cur1.next
        cur2_next = cur2.next

        # cur1 -> cur2 -> cur1.nextと繋ぐ
        cur1.next = cur2
        cur2.next = cur1_next
        
        cur1 = cur1_next
        cur2 = cur2_next

    return head1

head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(5)
head2 = ListNode(2)
head2.next = ListNode(4)
head2.next.next = ListNode(6)
print(merge_two_lists(head1, head2)) # {val: 1, next: {val: 2, next: {val: 3, ne
head1 = ListNode(1)
head2 = ListNode(2)
print(merge_two_lists(head1, head2))