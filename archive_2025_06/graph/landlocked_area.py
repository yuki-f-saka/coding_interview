from collections import deque

# 4方向への移動がわかりやすくなるようの方向配列を用意
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solve(matrix: list[list[int]]) -> list[int]:
    # matrixの行と列の数を用意
    H, W = len(matrix), len(matrix[0])

    # (1)各セルをノードとみなす
    N = H * W
    
    # 各セルに到達したかを記録する
    visited = [False for _ in range(N)]

    ans = []

    # 各セルを順番に見ていく
    for i in range(N):

        # (2)各セルのidからx,y座標を割り出す(id -> 座標への変換)
        iy, ix = i // W, i % W

        # すでに到達したノード or 海のノードはスキップ
        if visited[i] or matrix[iy][ix] == 1:
            continue

        # 連結グラフのノード数
        connnected_graph_size = 0

        # 連結グラフ内のノードのうち、最も4方向に近いノードのx,y座標を求めるための初期値を設定
        # 陸の中で一番端の座標を特定し、それが淵に触れていないかあとでチェックする用
        min_y, max_y, min_x, max_x = H, 0, W, 0

        # idがiのセルを起点としてBFSをする
        que = deque([i])
        while que:
            # ネストしたループになることで、どのように探索しているかをイメージすると、左上から順にノードを見ていき、
            # さらにその対象ノードを起点にして、BFSで上下左右に探索するイメージ。
            u = que.popleft()

            if visited[u]:
                continue

            # 連結したノードに達したら連結グラフのノード数を+1する
            visited[u] = True
            connnected_graph_size += 1

            # 連結グラフ内のノードのうち(陸ノードのうち)最も端っこの座標を更新
            # (forループの方で初期値が定義されるので、別の陸に入ったらこの初期値も一旦リセットされる)
            uy, ux = u // W, u % W
            min_y, max_y, min_x, max_x = (
                min(min_y, uy),
                max(max_y, uy),
                min(min_x, ux),
                max(max_x, ux),
            )

            # 4方向へのチェック
            for j in range(4):
                # 座標->idへの変換
                vy, vx = uy + dy[j], ux + dx[j]
                v = vy * W + vx

                # はみ出てないかチェック and 探索済みじゃないかチェック
                if (
                    0 <= vy
                    and vy < H
                    and 0 <= vx
                    and vx < W
                    and matrix[vy][vx] == 0
                    and not visited[v]
                ):
                    # キューに次の探索ノードとして格納
                    que.append(v)

        # 陸が淵に触れてないかチェック
        if (0 < min_y and max_y < H-1 and 0 < min_x and max_x < W-1):
            # ansに陸のサイズを追加
            ans.append(connnected_graph_size)

    return ans


