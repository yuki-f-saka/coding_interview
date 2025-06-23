def binary_search_1(nums: list[int], x: int) -> int:
    low, high = 0, len(nums)-1

    while low <= high:
        mid = (high + low) // 2
        if nums[mid] < x:
            low = mid + 1
        elif nums[mid] > x:
            high = mid - 1
        else:
            return mid
        
    return -1

# 再帰を使う方法
def binary_search_2(nums: list[int], x: int) -> int:
    def binary_search_recursive(nums: list[int], low: int, high: int, x: int):
        if low > high:
            return -1
        
        mid = (low + high) // 2
        if nums[mid] < x:
            return binary_search_recursive(nums, mid + 1, high, x)
        elif nums[mid] > x:
            return binary_search_recursive(nums, low, mid - 1, x)
        else:
            return mid
        
    return binary_search_recursive(nums, 0, len(nums)-1, x)

# 答えの候補の中から条件を満たす限界ギリギリまで二分探索をして答えを求める方法
def age_game() -> int:
    # 初期値の選び方
    '''
    Aさんの年齢は0歳以上、150歳以下
    つまり条件を満たす中での限界ギリギリ、許容度MAXの部分から始める
    ok = 150というのは、年齢制限として150歳以下と言われているので、151だと条件に合致しない。
    no = -1というのは、条件に絶対に合致しないポイント

    okは条件を絶対に満たす値
    noは条件を絶対に満たさない値
    '''
    ok, no = 150, -1

    # 最終的な答えが見つかったときにはokとnoが隣り合う
    # つまりabs(ok - no) == 1のときに、答えに辿り着いたと言えるので、
    # そうじゃない時はまだループして探索できるよーという意味
    while abs(ok - no) > 1:
        mid = (ok + no) // 2
        if A_answer(mid):
            ok = mid
        else:
            no = mid

    return ok 

'''
Guess How Old A Is 2
難易度: ★★ 重要度: 高
以下の制約の元、Aさんの年齢当を当てる関数を作成してください。
- あなたはAさんの年齢をできるだけ少ない質問の回数で当てたいです。
- あなたはAさんに対して「Aさんは x 歳より小さいですか」としか質問できないです（ x は
- 整数で、あなたが任意に決めることができます。 ）
- Aさんはあなたの質問に対して「はい」か「いいえ」でしか答えないです。
- Aさんの年齢は0歳以上、150歳以下であることは事前にわかっています。
'''
def age_game() -> int:
    # A_answer(x)は引数xに対して、Aさんがx歳より小さい条件を満たしていたらTrueを返却する定義済みの関数

    # 「Aさんがx歳よりも小さい」の否定 ->「Aさんがx歳以上」
    # not A_answer(x) = True

    # 絶対に条件を満たすのは0 -> Aさんは０歳以上ですか？絶対yes
    # 絶対に条件を満たさないのは151 -> -> Aさんは151歳以上ですか？絶対no。Aさんは150歳以上ですかならまだワンチャンある。
    ok, no = 0, 151
    while abs(ok - no) > 1:
        mid = (ok + no) // 2
        if not A_answer(mid):
            # Aさんはmid歳以上ですか？
            ok = mid
        else:
            no = mid

    return ok
