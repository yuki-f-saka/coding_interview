"""
Binary Search
Easy
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.

https://neetcode.io/problems/binary-search/question?list=neetcode150
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        return index of target else -1
        this list is sorted -> You can choose binary search
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + ((right - left) // 2)
            # mid = (left + right) // 2  <- can lead to overflow when other programming language
            # ちなみにpythonのintはメモリが許す限り無限に大きくなるのでoverflowしない
            # Go, Java, C++などは普通にintのmaxが決まっているのでoverflowする
            
            # Because left + right may exceed the maximum integer value before division.
            # ex. 
            # int の最大値 = 2,147,483,647で、もし以下のような状態だと、(left+right)の時点でint最大を超過するから
            # left  = 2,000,000,000
            # right = 2,100,000,000
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1