def Knapsack(N: int, W: int, values: list[int], weights: list[int]) -> int:
    # dpの定義を置く
    # 問題文からdp[i][w]：i番目までの商品の中から選んで、合計の重さがW以下となる最大合計価値 とする
    
    # 最初は全て0で初期化しておく
    # dp[i][w] を 0<=i<=N, 0<=w<=W まで定義するために
    dp = [[0 for _ in range(W+1)] # w=0 から W まで W+1 個
            for _ in range(N+1)] # i=0 から N まで N+1 個

    for i in range(1, N+1):
        # i = 1の時、1個目の商品を選びたい->valuesやweightsのindexに置き換えるとi-1なので、index=0を選ぶ
        vi, wi = values[i-1], weights[i-1]
        for w in range(1, W+1):
            # i番目を選ばない
            dp[i][w] = max(dp[i][w], dp[i-1][w])
            # i番目を選ぶ
            if W - wi >= 0:
                dp[i][w] = max(dp[i][w], dp[i-1][W-wi]+vi)

    return dp[N][W]




