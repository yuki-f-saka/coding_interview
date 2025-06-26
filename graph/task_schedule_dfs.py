# トポロジカルソートとは、必ずどのノードもエッジの出力先のノードより前に来るよう
# に位置する並び替
# えを指します。上の左のDAGを例にすると以下のような順序でトポロジカル
# ソートされます。トポロジカルソートは特に順序付きのフローで重要です。例えばあるタスク
# をするためには事前に終わらせておく必要なタスクは何を管理するのに役立ちます


# まずはdependenciesから隣接グラフを作る
def createGraph(N: int, dependencies: list[list[int]]) -> list[list[int]]:
    graph = [[] for _ in range(N)]
    for depend in dependencies:
        a, b = depend
        graph[a].append(b)
    
    # graph[i]がノードiのエッジの向き先のノード一覧をあらわす
    return graph

# 閉路(cycle)があったら、トポロジカルソートできないからまずは閉路の検出
def detectCycle(graph: list[list[int]]) -> bool:
    N = len(graph)

    # 以下の3つのstatusに分けてノードを色分けしていくイメージ
    # 0: 未探索
    # 1: 仮探索済み
    # 2: 完全探索済み

    status = [0 for _ in range(N)]

    # ノードuからスタートしたdfsで閉路があるか検出
    def dfs(u):
        # 行きで仮探索済み
        status[u] = 1

        # 探索
        for v in graph[u]:
            if status[v] == 1:
                # 仮探索済みなら、
                # 別の経路からvに一度探索したのにまた戻ってきてしまっているので
                # 閉路だ！サイクルがあるぞ！と判定する
                return True
            elif status[v] == 0:
                # 未探索ならもっと深く探索
                if dfs(v):
                    return True
            
            # 完全探索済みには何もしない
        
        # ノードuから下が完全探索済み or ノードuから下に何もない時
        status[u] = 2
        # ここまできてreturnされてなかったら閉路なし
        return False

    # dfs終了後
    for i in range(N):
        if status[i] == 2:
            continue
        else:
            # 仮探索済みや未探索が残っているので再度探索
            if dfs(i):
                return True
    
    return False

# 完全探索済みは、すでに探索したノードを繰り返し探索しないようにするためにある
# 仮探索済みは閉路検出のためにある


# トポロジカルソートはDFSの中の一種。
def topologicalSort(graph: list[list[int]]) -> list[int]:
    N = len(graph)

    ret = []
    visited = [False for _ in range(N)]

    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)

        # 帰り際にretに格納
        ret.append(u)

    for i in range(N):
        if visited[i]:
            continue
        dfs(i)

    ret.reverse()

    return ret

# 分解するとこのように3つの処理の流れからできている。


# ------------------------------------------------------------------------

# これをまとめると以下のようになる。
def taskSchedule(N: int, dependencies: list[list[int]]) -> list[int]:
    graph = createGraph(N, dependencies)

    # 0: 未探索
    # 1: 仮探索済み
    # 2: 完全探索済み
    status = [0 for _ in range(N)]

    ans = []

    def dfs(u):
        # 行きで仮探索済み
        status[u] = 1

        # 探索
        for v in graph[u]:
            if status[v] == 1:
                # 仮探索済みなら、
                # 別の経路からvに一度探索したのにまた戻ってきてしまっているので
                # 閉路だ！サイクルがあるぞ！と判定する
                return True
            elif status[v] == 0:
                # 未探索ならもっと深く探索
                if dfs(v):
                    return True
            
        # 完全探索済みには何もしない
        # 帰りに格納
        ans.append(u)
        # 完全探索済み
        status[u] = 2
        # 閉路なし
        return False
    
    for i in range(N):
        if status[i] == 2:
            continue
        if dfs(i):
            # サイクルあり
            return []
        
    # 最後に反転
    ans.reverse()

    return ans
    
