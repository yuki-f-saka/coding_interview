import random
from typing import List

# partition intのリストとその中のパーティションしたい範囲の最初lowと最後highを指定して、
# pivotのインデックスを返す関数
def partition(nums: List[int], low: int, high: int) -> int:
    # pivotのインデックスをlowからhighの間でランダムに選ぶ
    pivot_index = random.randint(low, high)
    pivot_value = nums[pivot_index]

    # pivotを末尾に移動
    nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
    # store_indexはpivotより小さい値の最後のインデックスを指す
    store_index = low

    # リストをパーティションに分ける
    for j in range(low, high):
        # nums[j]がpivotより小さい場合
        if nums[j] < pivot_value:
            # store_indexの値とjの値を交換
            nums[store_index], nums[j] = nums[j], nums[store_index]
            # store_indexを1つ進める
            store_index += 1

    # この時点ではpivot_indexは末尾にあるので、store_indexの値と交換してpivotを正しい位置に移動
    nums[store_index], nums[high] = nums[high], nums[store_index]
    # pivotのインデックスを返す
    return store_index

# quickselectはnumsの中からk番目に小さい要素を返す関数
def quickselect(nums: List[int], low: int, high: int, k: int) -> int:
    # リストの長さが1の場合
    if low == high:
        return nums[low]

    # パーティションを実行してpivot_indexを取得
    pivot_index = partition(nums, low, high)

    # 例えば、この時点でパーティションが完了しているので、pivotの値が5であれば、
    # numsは[1, 4, 2, 5, 7, 8, 6]のようにpivotである5を境に左側が小さい値、右側が大きい値に分かれている
    # index=0,1,2はpivotより小さい値、index=3はpivot、index=4,5,6はpivotより大きい値なので、
    # index=0,1,2の順番に関係なく、index=3の値がnumsの中で4番目に小さい値である
    # kがpivot_indexと一致する場合、pivotの値を返す
    # k=3, pivot_index=3の場合、nums[3]が4番目に小さい値
    if k == pivot_index:
        return nums[k]
    # kがpivot_indexより小さい場合、左側の部分を探索
    elif k < pivot_index:
        return quickselect(nums, low, pivot_index - 1, k)
    # kがpivot_indexより大きい場合、右側の部分を探索
    else:
        return quickselect(nums, pivot_index + 1, high, k)

def kth_smallest(nums: List[int], k: int) -> int:
    # k-1を指定しているのは、0-indexedであるため
    # 例えば、k=1の場合、最小値を取得したいので、index=0を指定する
    # k=2の場合、2番目に小さい値を取得したいので、index=1を指定する
    # というように、1番小さい要素というのは、indexで言うと0番目の要素であるため
    # k-1を指定している
    return quickselect(nums, 0, len(nums) - 1, k - 1)