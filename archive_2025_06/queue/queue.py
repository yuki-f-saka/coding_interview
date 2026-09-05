from typing import Any

class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.count = 0

    def enqueue(self, item: Any):
        new_node = Node(item)

        if self.empty():
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

        self.count += 1

    def dequeue(self) -> Any:
        if self.empty:
            raise IndexError("Dequeue from an empty queue")
        
        tmp_data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.back = None
        
        self.count -= 1
        return tmp_data

    def empty(self) -> bool:
        return self.front is None

    def size(self) -> int:
        return self.count