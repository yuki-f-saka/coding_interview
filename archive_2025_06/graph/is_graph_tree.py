from collections import deque

def validTree(N: int, edges: list[list[int]]) -> bool:
    # (1)
    # edgesから隣接リストのグラフを作成
    graph = [[] for _ in range(N)]
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)

    # (2)
    # キューには発見したノードとその親ノードを入れる
    # 根には親は存在しないので仮値として-1を入れる
    que = deque([(0, -1)])

    # (3)
    # 今回ではvisitedにsetを使用
    # visitedに全てのノードが追加されていればグラフは連結であるとみなせる
    # (ノード0から全てのノードへ到達可能を意味する)
    visited = set()
    while que:
        u, parent = que.popleft()

        # もしノードがすでに確認済みならスキップ
        if u in visited:
            continue

        # uは確認済みとする
        visited.add(u)

        for v in graph[u]:
            # (4)
            # uの親はスキップ
            # uの親は当然探索済みだから
            if v == parent:
                continue
            # (5)
            # vはuの子であるべき
            # つまり、未探索の状態であるべき
            # しかし、すでに到達しているということは閉路があることを示す
            if v in visited:
                return False
            que.append((v, u))

    # visitedに入っている数がグラフのノード数と等しければこのグラフは連結
    return len(visited) == N