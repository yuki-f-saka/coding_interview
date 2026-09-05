"""
Find Minimum in Rotated Sorted Array
Medium
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question?list=neetcode150
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        if nums[l] is less than nums[r], nums[l] can be minimum value.
        [1,2,3,4,5,6]
         l         r

        Look at following array. 3,4,5,6 is left part and 1,2 is right part.
        the all values in left part is greater than right part.
        if nums[l] is less than nums[m], m is in left part. So the minimum value must be the right of m.
        [3,4,5,6,1,2]
         l   m     r
        
        else nums[l] is greather than nums[m], the minimum value must be the left of m.
        """
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res
        