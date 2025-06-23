def dijkstra(graph: list[list[tuple[int, int]]]) -> list[int]:
    N = len(graph)

    # 最短距離が決まっていないノード
    undecided = set([i for i in range(N)])

    # 操作1
    # 各ノードへの最短距離を無限距離にて初期化
    distance = [float("inf") for _ in range(N)]
    # 始点のノードまでの距離は0
    distance[0] = 0

    while len(undecided) > 0:
        # 操作2
        # 最短距離を決定するノード
        target_node = -1
        # 最短距離を決定するノードまでの距離
        target_node_d = float("inf")

        # 未定のノードの中で最も距離が近いノードを一つえらぶ
        for node_id in undecided:
            if distance[node_id] < target_node_d:
                target_node = node_id
                target_node_d = distance[node_id]

        undecided.remove(target_node)

        # 操作3
        for edge in graph[target_node]:
            node_id, d = edge
            if distance[node_id] > distance[target_node] + d:
                distance[node_id] = distance[target_node] + d

    return distance