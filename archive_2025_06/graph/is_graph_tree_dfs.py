def validTree(N: int, edges: list[list[int]]) -> bool:
    # edgesからgraphを作成
    graph = [[] for _ in range(N)]
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)

    visited = set([])

    # 閉路があるかを返す
    def dfs(u, parent):
        visited.add(u)

        hasCycle = False

        for v in graph[u]:
            if v == parent:
                continue

            if v in visited:
                return True

            hasCycle = dfs(v, u)

        return hasCycle
    
    # dfs == Trueの時は閉路があるので、not dfsが閉路なしの状態
    # N == len(visited)は連結リストであるかどうか
    return (not dfs(0, -1)) and N == len(visited)
