# 例題. How
# Many Minutes Does It Take to Create Products?
# 難易度: ★★★ 重要度: 高
# あなたは製品を生産する機械をいくつか持っています。それぞれの機械が1つ製品を生産するの
# にかかる分数を表した配列 A が与えれます。 i 番目の機械が1つの製品を生産するのに必要な
# 分数は A[i] で表されます。あなたは X 個の製品が必要です。すべての機械を同時に稼働させた
# とき、製品を X 個生産するまでには最短で何分かかりますか？

# 制約
# 1 <= len(A) <= 10**5
# 1 <= A[i] <= 10**9
# 1 <= X <= 10**9
# 例.
# Input: A = [1,2,3], X = 6
# Output: 4

# 経過時間をtとすると、「t分後に製品がX個生産されている」を判定する関数があるとする
# def condition(t: int) -> bool:

# この条件を満たす限界の値が答え

def MinimumMin(A: list[int], X: int) -> int:
    # t分後に製品がX個以上生産される場合True、そうでなければFalseを返す
    def condition(t: int) -> bool:
        product_sum = 0
        for a in A:
            product_sum += t // a
        return product_sum >= X

    # 最も遅い機械で10**9かかる。最もXが多い時10**9個必要なので、初期値okはその限界ギリギリ(10**9 * 10**9 = 10**18)にする
    ok, no = 10**18, 0
    while abs(ok - no) > 1:
        mid = (ok + no) // 2
        if condition(mid):
            ok = mid
        else:
            no = mid
    return ok