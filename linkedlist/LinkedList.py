from typing import Any, Optional

class ListNode:
    def __init__(self, val:Any):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None

    def append(self, val: Any):
        if not self.head:
            # まだ空の場合、新しいノードをヘッドノートとする
            self.head = ListNode(val)
        else:
            # リストが空でない場合、リストの末尾に新しいノードを追加
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val)

    def remove(self, val: Any) -> Optional[ListNode]:
        if self.head is None:
            return
        
        if self.head.val == val:
            removed = self.head
            self.head = self.head.next
            return removed
        
        cur = self.head
        while cur.next:
            if cur.next.val == val:
                removed = cur.next
                cur.next = cur.next.next
                return removed
            cur = cur.next

    def search(self, val: Any) -> Optional[ListNode]:
        cur = self.head
        while cur:
            if cur.val == val:
                # 現在のノードが対象データを持つ場合、そのノードを返す
                return cur
            cur = cur.next
        return None

    def display(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

linked_list = LinkedList()
linked_list.append('A')
linked_list.append('B')
linked_list.append('C')

linked_list.display()

node = linked_list.search('B')
print(node.val if node else None) # 'B' が表示
node = linked_list.search('D')
print(node.val if node else None) # Noneが表示
linked_list.remove('B')
linked_list.display()