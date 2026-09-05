class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# infinity
INF = 1 << 30

def goodNodes(root: Node) -> int:
    # globalスコープにしておくと再帰関数dfs内で値の変更ができる
    global ans
    ans = 0

    def dfs(node, max_value):
        if not node:
            return
        
        # nodeの値が経路上の最大値以上か確認
        if node.val >= max_value:
            # goodNodeなので+1
            global ans
            ans += 1

        max_value = max(max_value, node.val)

        dfs(node.left, max_value)
        dfs(node.right, max_value)

    # max_valueの初期値は極めて小さい値にすることで更新されるようにする
    dfs(root, -INF)
    return ans