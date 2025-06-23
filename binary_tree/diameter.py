class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter(root: Node) -> int:
    # nodeを根とする木の最長経路と深さの2つを返す
    def dfs(node: Node) -> tuple[int, int] :
        # 子が存在するかに関わらず(1)(2)で再帰関数に引数を渡すためNoneが最終的に渡される
        if node == None:
            # ここでは木の深さを0にしているため、
            # Noneの場合は木の深さを根より1少ない-1とする
            return 0, -1

        # 左の部分木の最長経路と深さ
        b_max, b_depth = dfs(node.left) # - (1)
        # 右の部分木の最長経路と深さ
        c_max, c_depth = dfs(node.right) # - (2)

        # 左の部分木と右の部分木の最も深い経路を繋げた経路で更新
        a_max = max(b_depth+c_depth+2, b_max, c_max)

        # nodeを根とする木の深さをかえす
        return a_max, max(b_depth, c_depth) + 1

    ans, _ = dfs(root)
    return ans

def diameter2(root: Node) -> int:
    global ans
    ans = 0

    # 木の深さのみを返す
    def dfs(node) -> int:
        global ans
        if not node:
            # ここでは木の根の深さを1とした
            # Noneである場合は深さをそれより1小さい0とする
            return 0
        
        # 左の部分木の深さ
        left_max_depth = dfs(node.left)
        # 右の部分木の深さ
        right_max_depth = dfs(node.right)

        # 左の部分木と右の部分木の最も深い経路を繋げた経路で更新
        ans = max(ans, left_max_depth+right_max_depth)

        # nodeを根とする木の深さを返却
        return max(left_max_depth, right_max_depth) + 1
    
    dfs(root)
    return
        


        