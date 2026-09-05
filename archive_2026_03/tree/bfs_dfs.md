In this directry, you will find several traversal implementation.
Binary trees are the easist to understand.
There are 2 primary ways to traverse them.
1. BFS stands for Breadth First Search
2. DFS stands for Depth First Search

## BFS
We have to use a queue to store the node in the tree.
First, we enqueue the root node.
Then while the queue is not empty, we dequeue a node and check whether it has left and right children.
If it does, we enqueue them.
We repeat this process until the queue is empty.
Breadth-first search is a level-order traversal that explores nodes layer by layer using a FIFO queue.

BFS is useful when we need to explore nodes in order of their distance from the root, or when level-order traversal is required.

```
from collections import deque

def BFS(root: Node) -> list[int]:
    que = deque([root])
    while que:
        node = que.popleft()
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
```

## DFS
We use a stack (or recursion) to traverse the tree.
First, we start from the root node and explore as far as possible along one branch before backtracking.
For each node, we visit it and then recursively process its children until we reach a leaf node.
When there are no more nodes to visit, we backtrack to the previous node and continue exploring the next branch.
We repeat this process until all nodes have been visited.
Depth-first search explores nodes by going deep before visiting neighbors.

DFS is useful when we need to explore an entire path, check connectivity, or solve problems that require backtracking.
```
def dfs(node:Node):
    if node.left:
        dfs(node.left)
    if node.right:
       dfs(node.right)
```