from collections import deque

def shortestPass(matrix: list[list[int]]) -> int:
    # 上下左右のノードを見るのに適した配列を用意する
    # [上、右、下、左]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    # 行数、列数を置く
    H = len(matrix) # 行数
    W = len(matrix[0]) # 列数

    # 左上のセル（スタート地点）をキューに格納
    # (y座標、x座標、スタートからの距離)
    que = deque([(0, 0, 0)])

    # 探索済みセットを用意
    visited = set([])

    # 探索開始
    while que:
        uy, ux, d = que.popleft()

        # 右下のセルかどうか確認
        if uy == H-1 and ux == W-1:
            return d # 距離を返す

        # 探索済みならスキップ
        if (uy, ux) in visited:
            continue

        # 探索済みにマークする
        visited.add((uy, ux))

        # 4方向の隣接するセルを見る
        for i in range(4):
            vy, vx = uy + dy[i], ux + dx[i]
            # 隣接するセルが範囲内かの確認、隣接するセルが0であるか確認
            if 0 <= vy and vy < H and 0 <= vx and vx < W and matrix[vy][vx] == 0:
                # 隣接するセルが探索済みならスキップ
                if (vy, vx) in visited:
                    continue

                # 次のセルとしてキューに追加
                que.append((vy, vx, d+1))

    # 経路が見つからなかった
    return -1