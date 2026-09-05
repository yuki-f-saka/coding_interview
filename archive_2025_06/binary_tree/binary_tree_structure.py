from collections import deque

# Nodeクラスは以下のように定義されているとします
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_structure(root: Node) -> list[list[int]]:
    que = deque([(root, 0)])
    cur_level = 0
    cur_level_arr = []
    ans = []

    while que:
        node, level = que.popleft()
        if level == cur_level:
            # 階層が同じ
            cur_level_arr.append(node.val)
        else: # level != cur_level
            # 階層が変わった
            # まだひとつ上の階層の情報を持っている
            ans.append(cur_level_arr)

            # 次の階層に更新
            cur_level = level
            cur_level_arr = [node.val]

        if node.left:
            que.append((node.left, level + 1))
        if node.right:
            que.append((node.right, level + 1))

    # 最後の階層に関しては階層が変わる前にループが終了してしまうため
    ans.append(cur_level_arr)

    return ans
