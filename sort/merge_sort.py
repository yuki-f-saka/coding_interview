def merge(nums: list[int], left: int, mid: int, right: int):
    left_nums = nums[left:mid+1]
    right_nums = nums[mid+1:right+1]

    i, j, k = 0, 0, left

    # 二つの並び替えられた半分を元の配列に統合
    while i < len(left_nums) and j < len(right_nums):
        if left_nums[i] <= right_nums[j]:
            nums[k] = left_nums[i]
            i += 1
        else:
            nums[k] = right_nums[j]
            j += 1
        k += 1

    # left_numsとright_numsの残りの要素をコピー
    while i < len(left_nums):
        nums[k] = left_nums[i]
        i += 1
        k += 1
    while j < len(right_nums):
        nums[k] = right_nums[j]
        j += 1
        k += 1
    print("nums: {0}".format(nums))
        
def merge_sort(nums: list[int], left: int, right: int) -> list[int]:
    print("merge_sort({0}, {1}, {2})".format(nums, left, right))
    # これ以上は分割できない場合
    if left >= right:
        return nums

    # 配列の中間インデックス
    mid = (left + right)//2

    # 左右の半分を再帰的に並び替え
    merge_sort(nums, left, mid)
    merge_sort(nums, mid+1, right)

    # 並び替えられた半分を統合
    print("merge({0}, {1}, {2}, {3})".format(nums, left, mid, right))
    merge(nums, left, mid, right)

    return nums

print(merge_sort([5,4,3,2,1], 0, 4))