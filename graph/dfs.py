def Solution(graph: list[list[int]]):
    N = len(graph)

    root = 0

    visited = [False for _ in range(N)]

    def dfs(u):
        visited[u] = True
        print(u)
        for v in graph[u]:
            if visited[v]:
                continue
            dfs(v)

    dfs(root)

def DFS(node: Node):
    if node.left:
        DFS(node.left)
    if node.right:
        DFS(node.right)
