# pre-order
# in-order
# post-order

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preOrder(root: Node) -> list[int]:
    pre_order = []

    def travel(node: Node):
        if not node:
            return
        
        # 先に自分を追加
        pre_order.append(node.val)
        # 次に左の子を巡回
        travel(node.left)
        # 次に右の子を巡回
        travel(node.right)

    travel(root)
    return pre_order

def inOrder(root: Node) -> list[int]:
    in_order = []

    def travel(node: Node):
        if not node:
            return 
        
        # 先に左の子を巡回
        travel(node.left)
        # 次に親を追加
        in_order.append(node.val)
        # 次に右の子を追加
        travel(node.right)

    travel(root)
    return in_order

def postOrder(root: Node) -> list[int]:
    post_order = []

    def travel(node: Node):
        if not node:
            return 
        
        # 先に左の子を巡回
        travel(node.left)
        # 次に右の子を巡回
        travel(node.right)
        # 次に親を追加
        post_order.append(node.val)

    travel(root)
    return post_order

