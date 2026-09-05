"""
Find the Duplicate Number
Solved 
Medium
Company Tags
Hints
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

Follow-up: Can you solve the problem without modifying the array nums and using O(1) extra space?

Constraints:

1 <= n <= 10000
nums.length == n + 1
1 <= nums[i] <= n

https://neetcode.io/problems/find-duplicate-integer/question
"""

from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        If we can use more than O(n) space complexity,
        we can make counter. So the solution is really simple.
        the overall time complexity is O(n), and the space complexity is O(n).
        """
        # counter = Counter(nums)
        # most_times = counter.most_common(1)
        # return most_times[0][0]

        """
        Follow-up: Can you solve the problem without modifying 
        the array nums and using O(1) extra space?

        If we can sort this input list and traverse,
        we must find consecutive numbers. They are duplicate numbers.
        But we can't modify the array nums.
        """
        # nums.sort()
        # prev = 0
        # for i in range(len(nums)):
        #     if prev == nums[i]:
        #         return prev
        #     prev = nums[i]
        # return prev

        """
        sort() needs O(nlogn) time complexity
        and python sort needs O(n) space complexity.
        """

        """
        Key idea is that we can treat an array nums as a singly linked list.
        Because nums containing n+1 intergers and num is in the range[1,n].
        So we can treat the array as a linked list 
        because each index points to exactly one next index given by nums[i].
        """
        # Treat the array as a linked list:
        # node = index, next(node) = nums[index]
        
        # Phase 1: find an intersection point inside the cycle
        """
        slow と fast は linked list 上を移動するポインターで、
        slow は 1 step、fast は 2 step 進み、
        同じ node（index）を指したときに cycle 内で出会う。
        """
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]          # 1 step
            fast = nums[nums[fast]]    # 2 steps
            if slow == fast:
                break

        # Phase 2: find the cycle entrance (the duplicate number)
        """
        slowを初期位置に戻し、そこから両方を1つずつ進めると、
        Floydのアルゴリズムにより、必ずサイクルの入り口で出会う
        そしてサイクルの入り口は重複したintergerである。
        なのでslowをreturnする.
        """
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
