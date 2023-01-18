"""
Link: https://leetcode.com/problems/maximum-average-subarray-i/description/
643. Maximum Average Subarray I
Easy
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""
import sys
class Solution(object):
    """
    Algorithm:
    1. If the length of nums array is 1. Return the nums[0]
    2. If k == length of nums array calculate the sum and return sum/k
    3. Initialise a variable(sumOfNums) to hold the sum to 0
    4. set left to 0
    5. Iterate through the nums array from right 0 to len(nums)
        6. if the right < k, add nums[right] to sum
        7. if the right >= k, 
            7.a Calculate the maxSum i.e max of maxSum(prevMax) and current sum
            7.b Calculate the diff of elements at index right,left
            7.c add the diff to sum
            7.d if the right is the last element if nums array, calculate maxSum again
            7.e increment the left by 1
        8. return the maxSum/k

    """
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == 1:
            return nums[0]
        maxSum = float("-inf")
        if k == len(nums):
            return float(sum(nums))/k
        
        sumOfNums = 0
        left = 0
        for right in range(len(nums)):
            if right < k:
                sumOfNums += nums[right]
            if right >= k:
                maxSum = max(sumOfNums,maxSum)
                diff = nums[right] - nums[left] 
                sumOfNums += diff
                if right == len(nums)-1:
                    maxSum = max(sumOfNums,maxSum)
                left += 1

        return float(maxSum)/k