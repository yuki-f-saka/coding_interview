class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_front(self, value:int):
        new_node = ListNode(value)
        first_node = self.head.next

        new_node.next = first_node
        new_node.prev = self.head

        first_node.prev = new_node
        self.head.next = new_node

    def insert_back(self, value:int):
        new_node = ListNode(value)
        last_node = self.tail.prev

        new_node.next = self.tail
        new_node.prev = last_node
        last_node.next = new_node
        self.tail.prev = new_node

    def insert_search(self, value:int) -> Optional[ListNode]:
        cur = self.head.next
        while cur != self.tail:
            if cur.val == value:
                return cur
            cur = cur.next
        return None
    
    def delete(self, node: ListNode):
        if node == self.head or node == self.tail:
            return
        
        node.prev.next = node.next
        node.next.prev = node.prev