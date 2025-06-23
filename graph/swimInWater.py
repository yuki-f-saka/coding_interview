from heapq import heappop, heappush

# 問題の要点
# セルを通れるまでの最小時間はすでに与えられている。ゴールのセルは最短でもgrid[n-1][n-1]時間経過しないと通れない
# 始点から終点までの通る道の中で通るマスの最大海抜が最小値となるような問題
# 「最小化された最大値問題」と分類できる

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 始点が決まっている重み付きの有向グラフなので、ダイクストラ法を使用して解くことが求められる。
        # (0,0)->(n-1,n-1)
        # return 終点までの最短到達時間

        n = len(grid)
        # 探索済みノードの記録
        visited = [[False] * n for _ in range(n)]

        # 最小ヒープ(ここまでの中での最大海抜、x, y)
        min_heap = [(grid[0][0],0,0)]

        # 方向キー
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while min_heap:
            max_height, x, y = heappop(min_heap)
            if x == n-1 and y == n-1: # 取り出したcurrent nodeが終点だった時
                return max_height
            if visited[x][y]:
                continue
            visited[x][y] = True
            
            # ダイクストラ法の一番重要な部分
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heappush(min_heap, (max(max_height, grid[nx][ny]) , nx, ny))

        # 到達することはないが戻り値が必要なので
        return -1
