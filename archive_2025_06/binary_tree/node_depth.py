from collections import deque

# Nodeクラスは以下のように定義されているとします
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def depth(root: Node) -> list[int]:
    que = deque([(root, 0)])
    ans = []
    while que:
        node, level = que.popleft()
        ans.append(level)

        if node.left:
            que.append((node.left, level + 1))
        if node.right:
            que.append((node.right, level + 1))

    return ans