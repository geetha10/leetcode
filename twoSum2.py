"""
Question:
167. Two Sum II - Input Array Is Sorted
Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Link:
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""
class Solution(object):
    """
    Approach: Two Pointers
    
    Algorithm:
    
    1. Initialize left pointer to 0
    2. Initialize rigth pointer to last index i.e len(numbers)-1
    3. Iterate till left is less than right(while loop) - This loops till mid point of the array
        4. Calculate the sum of numbers at index left, right. 
        5. if sum == target: return [left,right]
        6. if sum is less than target, increment left
        7. if sum id greater than target, decrement right
    
    Time complexity: o(n)

    Space complexity: 1

    """
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(numbers)-1

        while left < right:
            sumOfNums = numbers[left]+numbers[right]
            
            if sumOfNums == target:
                return [left+1,right+1]
            if  sumOfNums < target:
                left +=1
            
            if sumOfNums > target:
                right -=1
            