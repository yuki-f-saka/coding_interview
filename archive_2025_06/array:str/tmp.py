class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 正確に1ずつ増分した要素が合計でいくつあるか

        # 重複排除のためsetにする
        # ソートするとlistになる
        # cur_countとmax_countを用意して
        # 一つ前の要素と比較して、差分が1だったらcur_countを+1する
        # iとi-1
        # 差分が1以外の時に、そこで連続性が失われるから、cur_countをmax_countに記録してリセット

        sorted_list = sorted(set(nums)) # [2,3,4,5,10,20]
        print(sorted_list)
        cur_cnt, max_cnt = 1, 1
        for i in range(1, len(nums)):
            print("iは", i)
            if nums[i] - nums[i-1] == 1:
                cur_cnt += 1
            else:
                max_cnt = max(max_cnt, cur_cnt)
                cur_cnt = 1
            print("cur_cnt", cur_cnt)
            print("max_cnt", max_cnt)
            print("\n")

        return max_cnt


if __name__ == "__main__":
    import sys

    # If command-line arguments are provided, treat them as the input list.
    if len(sys.argv) > 1:
        try:
            nums = [int(x) for x in sys.argv[1:]]
        except ValueError:
            print("All arguments must be integers")
            sys.exit(1)
    else:
        # default sample
        nums = [2, 3, 4, 5, 10, 20]

    # Call the method (the function prints sorted_list internally)
    result = Solution().longestConsecutive(nums)
    print("result:", result)