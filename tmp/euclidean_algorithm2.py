class Solution:
    def euclidian2(self):
        # aとbで大きい方から小さい方を引き続ける
        # 一致したらreturn
        a = 50
        b = 15

        while a != b:
            if a > b:
                a /= b
            else:
                b /= a

        print(a)

sol = Solution()
sol.euclidian()