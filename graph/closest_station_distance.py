from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solve(matrix : list[list[int]]) -> None:
    # (y, x, d)
    q = deque([])
    H, W = len(matrix), len(matrix[0])
    for i in range(H):
        for j in range(W):
            if matrix[i][j] == 0:
                # 一番初めに駅を入れておく
                q.append((i, j, 0))

    while q:
        uy, ux, d = q.popleft()
        for i in range(4):
            vy, vx = uy + dy[i], ux + dx[i]
            if matrix[vy][vx] > d and 0 <= vy and vy < H and 0 <= vx and vx < W:
                matrix[vy][vx] = d + 1
                q.append((vy, vx, d + 1))

