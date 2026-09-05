# 幅優先探索のあるノードにおいてその親より上の階層の情報が必要なパターンは
# 深さ優先探索のあるノードから根までの経路の情報が必要なパターンを内包しているため応用できる

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def goodNodes(root: Node) -> int:
    ans = 0

    que = deque([(root, root.val)])
    while que:
        node, path_max = que.popleft()
        if node.val >= path_max:
            ans += 1

        if node.left:
            que.append((node.left, max(path_max, node.left.val)))
        if node.right:
            que.append((node.right, max(path_max, node.right.val)))

    return ans