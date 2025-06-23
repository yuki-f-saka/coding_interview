from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def BFS(root: Node):
    # init, enter only root into que
    que = deque([root])
    while que:
        node = que.popleft()
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)

# graphは隣接リスト
def BFS2(graph: list[list[int]]):
    # Nはグラフのノード数
    N = len(graph)

    # ノードのidが0のノードからBFSを行うとする
    root = 0

    # ノードiが探索済みかを示すboolean
    visited = [False for _ in range(N)]

    que = deque([0])
    while que:
        u = que.popleft()

        # (2)すでに探索済みのノードもキューに入りうる、その場合はスルーする
        if visited[u]:
            continue

        # ノードuは到達済みとして記録する
        visited[u] = True

        # (3)graph[u]はノードuとエッジで結ばれているノードを格納する配列
        for v in graph[u]:
            if visited[v]:
                continue
            que.append(v)