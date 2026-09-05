# subsets backtrack

from copy import deepcopy as cp

def subsets(nums: list[int]) -> list[list[int]]:
    N = len(nums)
    ans = []

    # 選んだ要素を入れておく部分配列。動的に変化していく
    subset = []

    # i番目の要素を選ぶかどうかの再起処理(0スタート)
    # 操作を行うだけで何かを返す必要はない
    def rec(i) -> None:
        if i == N:
            # deepcopyを使用して要素は同じだが異なる配列としてansを追加
            print("決定したsubset: {0}".format(subset))
            ans.append(cp(subset))
            return 
        
        # (1)i番目の要素を選ぶ
        subset.append(nums[i])
        # i番目の要素を追加すると決めたので次はi+1番目を考える
        print("{0}番目の数である{1}を選んだ時のsubset: {2}".format(i, nums[i], subset))
        rec(i+1)

        # (2)i番目の要素を選ばない
        # 上のコードでsubsetにi番目の要素をappend(追加)しているのでpop(削除)しておく
        subset.pop()
        # i番目の要素を選ばないと決めたので次はi+1番目をどうするか考える
        print("{0}番目の数である{1}を選ばなかった時のsubset: {2}".format(i, nums[i], subset))
        rec(i+1)
        return
    
    rec(0)
    return ans

nums = [1, 2, 3]
subsets(nums)
