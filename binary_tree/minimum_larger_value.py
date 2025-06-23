from typing import Optional

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def MinumumLargerValue(root: Node, p: Node) -> Optional[Node]:
    # そもそもpに右の子がある場合 -> 右の部分木の中で最も左のノードが最小となる
    if p.right:
        curr = p.right
        while curr.left: # 右の子ノードから見て左へ左へとにかく探索
            curr = curr.left

        return curr # 探索終了したので、一番右の子ノードから見て左
    
    # pに右の子が存在しない場合
    # -> p.valが一番右になるような(最大になるような)部分木が存在する
    # -> その部分木の根から見て、親となるノードが求めるノードとなる
    # 整理すると「求めるノードの左の部分木の最大値がp.valに等しい」
    # 以下のdfs関数では「p.valより大きい最小のノードを再帰的に探索して返却する」
    def dfs(node: Node) -> Optional[Node]:
        if not node:
            return None
        
        if p.val < node.val:
            # nodeが候補となりうるのでp.valより大きいnodeがある限りは左に探索していく
            # -> nodeよりnode.leftの方が小さいから、p.valより大きいギリギリを攻めていく
            left_candidate = dfs(node.left)
            return left_candidate if left_candidate else node
        else:
            # p.val >= node.val
            # つまり現在のnodeは条件に合致しない
            # より大きいものがないか探すので、右に探索
            return dfs(node.right)

    return dfs(root)