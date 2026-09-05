from collections import deque

def topologicalSort(graph: list[list[int]]) -> list[int]:
    N = len(graph)

    # 1. 各ノードでの入次数を記録
    indegree = [0 for _ in range(N)]
    for u, vs in enumerate(graph):
        for v in vs:
            # u -> vのグラフなのでvの入次数を+1
            indegree[v] += 1

    # 2. queには入次数0のノードを入れる
    que = deque([])
    for id in range(N):
        if indegree[id] == 0:
            que.append(id)

    ans = []
    while ans:
        # 3. uは入次数が0なので選んでグラフから取り除く
        # uを取り除いたので、uからでていく先のノードでは入次数が-1される
        u = que.popleft()
        ans.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                # 入次数が0になったらqueについか
                que.append(v)

    return ans if len(ans) == N else []