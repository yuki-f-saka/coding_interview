class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node_G = Node("G")
node_H = Node("H")
node_I = Node("I")
node_D = Node("D", node_G, node_H)
node_E = Node("E")
node_F = Node("F", None, node_I)
node_B = Node("B", node_D, node_E)
node_C = Node("C", node_F)
node_A = Node("A", node_B, node_C)

def dfs(node: Node):
    print("{0}につきました".format(node.val))
    if node.left:
        # 子に対して再帰処理を行う、子へ行く
        print("{0}から{1}へいく".format(node.val, node.left.val))
        dfs(node.left)
        # 行った先の子に対する再帰処理が終わって帰ってきた
        print("{0}から{1}へ帰ってきた".format(node.left.val, node.val))
    
    if node.right:
        # 子に対して再帰処理を行う、子へ行く
        print("{0}から{1}へいく".format(node.val, node.right.val))
        dfs(node.right)
        # 行った先の子に対する再帰処理が終わって帰ってきた
        print("{0}から{1}へ帰ってきた".format(node.right.val, node.val))
    
    # 処理が全部終わり出ていく
    print("{0}から出ていきます".format(node.val))

dfs(node_A)