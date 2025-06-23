class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        if self.next is None:
            return f"{{val: {self.val}, next: None}}"
        else:
            return f"{{val: {self.val}, next: {repr(self.next)}}}"
        
def delete_node_from_start(head: ListNode, n: int):
    dummy = ListNode(-1, head)
    cur = dummy

    while n > 1:
        n -= 1
        cur = cur.next
        