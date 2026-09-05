def fib(n):
    memo = [0 for _ in range(n+1)]
    memo[0] = 1
    memo[1] = 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]

# メモリ計算量を節約したのがこちら
def fib2(N):
    if N < 2:
        return 1
    prev, pprev = 1, 1
    cur = -1
    for i in range(2, N+1):
        cur = prev + pprev
        prev, pprev = cur, prev
    return cur

# 配るDPで実装した例がこちら
def fib3(n):
    memo = [0 for _ in range(n+1)]

    memo[0] = 1

    for i in range(n):
        memo[i+1] += memo[i]
        if i+2 < n+1:
            memo[i+2] += memo[i]
    
    return memo[n]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) # ステップの数

        # dp[i]: ステップiに辿り着くまでに必要な最低コストとする
        dp = [0 for _ in range(n)]

        if n == 0: # ステップが存在しないのでコスト0
            return 0 
        if n == 1: # ステップが一つしか存在しないのでそのステップのコストが最小
            return cost[0]

        # 最初の2ステップはそれ自体に乗る必要があるため、コストはそのまま
        dp[0] = cost[0]
        dp[1] = cost[1]

        # ステップ2から順に、最小コストを計算していく
        for i in range(2, n):
            # ステップ i にたどり着くには、ステップ i-1 または i-2 からジャンプできる
            # それぞれにかかるコストの最小値 + 今のステップのコスト
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        # ゴールはステップ n の1つ上であり、n-1 または n-2 からジャンプして到達できる
        # よって最後の2ステップのうち小さい方のコストが答え
        return min(dp[n-1], dp[n-2])

