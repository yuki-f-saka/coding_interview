from heapq import heappop, heappush

def dijkstra(graph: list[list[tuple[int, int]]]) -> list[int]:
    N = len(graph)

    # 最短距離を決定するノードの候補を残しておくヒープ
    # (最短距離、ノードid)
    # 最小の最短距離を取り出せるようにタプルの最初の要素を最短距離としている
    heap = [0, 0]

    # 各ノードの最短距離が決まっているかを格納
    decided = [False for _ in range(N)]

    ## 操作1 ##
    # 各ノードへの最短距離inf(無限距離)として初期化
    distance = [float("inf") for _ in range(N)]
    # 始点であるノード0への距離は当然0
    distance[0] = 0

    while heap:
        # 操作2
        _, target_node = heap.heappop()
        # すでに最短距離が決まっているノードならスキップ
        if decided[target_node]:
            continue
        decided[target_node] = True

        # 操作3
        for edge in graph[target_node]:
            node_id, d = edge
            if distance[node_id] > distance[target_node] + d:
                distance[node_id] = distance[target_node] + d
                heappush(heap, (distance[node_id], node_id))

    return distance
