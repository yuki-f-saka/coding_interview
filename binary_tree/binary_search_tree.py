from typing import Optional

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        # 初めはのーどがないのでNoneを入れておく
        self.root = None

    # 探索
    def search(self, x: int):
        node = self.root
        while node:
            if node.val == x:
                return node
            elif node.val > x:
                node = node.left
            else:
                node = node.right
            
        # 見つからなかったためNoneを返す
        return None

    # 挿入
    def insert(self, x: int) -> Optional[Node]:
        new_node = Node(x)
        # まだ二分探索木に一つもノードがないのでnew_nodeをrootにする
        if not self.root:
            self.root = new_node
            return new_node
        
        # 新しいノードの親となるノードを探す
        parent = None
        node = self.root
        while node:
            if node.val == x:
                return node
            elif node.val > x:
                parent = node
                node = node.left
            else: 
                parent = node
                node = node.right

        if parent.val > x:
            parent.left = new_node
        else:
            parent.right = new_node

        return new_node
    
    # 削除でつかう探索のコード
    # 見つけたノード、その親ノード、親ノードの左右どちらについているかを返す
    # 親ノードの左についていた場合をtrueとする
    def searchForRemove(self, x: int) -> tuple[Optional[Node], Optional[Node], bool]:
        parent = None
        isLeft = False
        node = self.root
        while node:
            if node.val == x:
                return node, parent, isLeft
            elif node.val > x:
                parent = node
                node = node.left
                isLeft = True
            else:
                parent = node
                node = node.right
                isLeft = False

        return None, None, False

    # さくじょのパターン3用のヘルパー関数
    def getLeftestNode(self, node: Optional[Node]) -> tuple[Optional[Node], Optional[Node]]:
        if not node:
            return None, None
        
        parent = None
        leftestNode = node

        while leftestNode.left:
            parent = leftestNode
            leftestNode = leftestNode.left

        return leftestNode, parent

    # 削除
    def remove(self, x: int):
        node, parent, isLeft = BST.searchForRemove(self, x)

        # 削除したいものがなかった　
        if not node:
            return
        
        # パターン1 子ノードがない(つまり葉)
        if (not node.left) and (not node.right):

            # 親もない
            # つまり要素数1以下のnode
            if not parent:
                self.root = None
                return 
            
            if isLeft:
                parent.left = None
            else:
                parent.right = None

        # パターン2 左or右の子のどちらかがない(どちらかがある)
        elif (not node.left) or (not node.right):
            child = node.left or node.right
            # 親がない
            # つまりrootを削除するので、子がそのままrootになる
            if not parent:
                self.root = child
                return
            
            if isLeft:
                parent.left = child
            else:
                parent.right = child

        # パターン3 左右どちらにも子ノードを持つ
        else:
            left, right = node.left, node.right

            # rightLeftestNodeはnodeの右の部分木のうち最も左にあるノード
            # そもそもright != Noneなので、rightLeftestNodeは必ず存在する
            rightLeftestNode, rightLeftestNodeParent = BST.getLeftestNode()
            if not rightLeftestNodeParent:
                # rightLeftestNodeParentが存在しないということは、
                # rightLeftestNode == right
                rightLeftestNodeParent = node
        
            rightLeftestNodeParent.left = rightLeftestNode.right

            # nodeのleftとrightをleftRightestNodeにつける
            # 注意すべきはrightLeftestNodeがrightのとき
            # このときはleftのみをつなげる（当たり前だがrightをつなげると自己参照になってしまう
            if rightLeftestNode == right:
                rightLeftestNode.left = left
            else:
                rightLeftestNode.left, rightLeftestNode.right = left, right

            # 親がない、つまりrootを削除する
            # この場合rightLeftestNodeがそのままrootになる
            if not parent:
                self.root = rightLeftestNode
                return
            if isLeft:
                parent.left = rightLeftestNode
            else:
                parent.right = rightLeftestNode

        return
