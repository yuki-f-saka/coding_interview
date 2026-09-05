INF = float("inf")

def coinChange(coins: list[int], amount: int) -> int:
    # dp[i] iを作るのに最低限必要なコインの枚数
    dp = [INF for _ in range(amount+1)]

    dp[0] = 0

    for i in range(1, amount+1):
        for c in coins:
            if i - c >= 0:
                # i-cを作るのに、最小な枚数+1枚でiが作れる
                # つまりdp[i-c]+1がdp[i]の候補となりうる
                dp[i] = min(dp[i], dp[i-c]+1)

    return dp[amount] if dp[amount] != INF else -1