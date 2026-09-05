from heapq import heappop, heappush
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        H, W = len(heights), len(heights[0])
        N = H * W

        # 重み付き有向グラフ作成(graph[node_id] = [tuple(neighbor, abs_dif)])
        graph = self.buildGraph(heights)

        # ダイクストラ法の準備をしていく
        # 最小の最大高低差がすでに決定しているかのチェック配列
        decided = [False for _ in range(N)]

        # 最小ヒープ
        # これまでに見つかっている経路の中で最も条件の良い経路を優先して探索するために使う
        # min_heapは常にeffort(高低差の絶対値)が最小のノードをO(logN)で取り出せるデータ構造
        # 要素が1つしかない配列ならheapifyしなくても、そのあとheappush、heappopで中身をやり取りすれば、
        # 最小heap構造となる
        # 要素がtupleの場合、1つ目の要素を比較して、辞書順に並べるため並べたい対象のデータ(今回は高低差)を1つ目の要素に持ってくる
        # (effort, node)
        min_heap = [(0, 0)]

        # 各ノードへの最小effort(高低差の絶対値の最大値)を記録しておくもの
        # より小さい値で更新するため最初は無限で初期化しておく
        dist = [float("inf") for _ in range(N)]
        # ノード0(始点)では始点と始点の高低差は0なので0を入れておく
        dist[0] = 0

        while min_heap:
            effort, cur = heappop(min_heap)

            if cur == N-1: # 探索対象のノードが終点(ゴール)だったとき
                return effort
            
            if decided[cur]: # すでにノード探索済み
                continue
            decided[cur] = True # 探索済みにチェックする

            # 今いるノードcurと隣接する全てのノードを調べる
            for neighbor, weight in graph[cur]:
                # 現在のノードに来るまでにかかった最大の高低差effortと
                # 現在のノードから隣接するノードへの高低差の大きい方が新しいeffortとなる
                new_effort = max(effort, weight)
                # これまでに見つかった隣接するノードへの最小高低差と比較して小さい法で更新する
                if new_effort < dist[neighbor]:
                    dist[neighbor] = new_effort
                    # より楽な経路を、次に優先して探索する候補としてヒープに追加
                    # 楽な経路から順に試すことで、ゴールに辿り着いた時、その経路が一番楽であることが保証されているため
                    heappush(min_heap, (new_effort, neighbor))

        return -1


    def buildGraph(self, heights: List[List[int]]) -> List[List[tuple[int, int]]]:
        H, W = len(heights), len(heights[0])
        N = H * W
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # heightsを双方向の重み付き有向グラフに直す
        graph = [[] for _ in range(N)]

        for i in range(H):
            for j in range(W):
                # i, jをノードidに変換
                cur = i * W + j

                # 現在のノードから上下左右に隣接するノードを探索
                for dx, dy in directions:
                    ni, nj = i+dx, j+dy
                    
                    # 範囲内チェック
                    if 0 <= ni < H and 0 <= nj < W:
                        neighbor = ni * W + nj
                        # 現在のノードと隣接するノードの高低差の絶対値を記録していく
                        abs_dif = abs(heights[i][j] - heights[ni][nj])
                        graph[cur].append((neighbor, abs_dif))

        return graph


