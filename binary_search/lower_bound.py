class binary:
    '''
    Lower Bound（下界の位置）
    難易度: ★★ 重要度: 高
    整数を要素とする昇順にソート済みの配列 nums と目的の値 x を引数とします。
    その値が配列に存在する場合は存在する位置（インデックス）のうちの最小を返す関数を作成してください。
    目的の値が配列内に存在しない場合、関数は-1 を返して下さい。

    条件: nums[i]がx以上である
    条件を満たすギリギリの境界を求める
    '''
    def lower_bound(nums: list[int], x: int) -> int:
        N = len(nums)

        # xがnumsの最小値以上　かつ　numsの最大値以下でないとxはnumsに含まれていない
        if not (nums[0] <= x and x <= nums[N-1]):
            return -1

        # numsの最小値がxだった場合はnumsのすべての要素が条件を満たしてしまうため、
        # noの初期値を設定できない。(noの初期値は必ず条件を満たさないものでなければいけない。
        # -> 条件を満たさないnoと条件を満たすokが隣り合う場所を特定するための二分探索。
        if nums[0] == x:
            return 0
        
        ok, no = N - 1, 0
        # abs(ok - no) == 1のときにokとnoが隣り合うのでそれまでループ
        while abs(ok - no) > 1:
            mid = (ok + no) // 2
            if nums[mid] >= x:
                ok = mid
            else:
                no = mid
        # okとnoが隣り合うことはwhileループを抜けたことでわかっているので、
        # nums[ok]がxと一致するという問題の条件を最後にチェックしてreturn
        return ok if nums[ok] == x else -1
