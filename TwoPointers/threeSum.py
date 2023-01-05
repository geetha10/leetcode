"""
Question: 

15. 3Sum
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution(object):
    """
    Algorithm:
    Method: Two Pointers
    It is very similar to Two Sum problem.
    
    1. Sort the numbers of nums Array, 
    2. Initialise the triplets array to store result triplets.
    3. Iterate through sorted array till its length.
        4. For removing the duplicate triplets. 
        4.a if i>0 and nums[i-1] == nums[i], continue the loop i.e skip doing anything in current iteration
        5. After skipping all duplicates for i, Initilaise left to i +1, right to len(nums) -1
        6. Iterate(while loop) till j < k:
            7. calculate sum of nums at index i, left and right and store in curSum variable 
            8. if curSum == 0:
                8.a. append values of nums at index i, left, right to triplets array
                8.b. increment left, decrement right
                8.c. to skip duplicates from left. check if left<right and nums[left] == nums[left-1]: increment left
                8.d. to skip duplicates from right. check if left<right and nums[right] == nums[right+1]: decrement left
            9. if curSum < 0: increment left
            10. else: decrement right

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        triplets = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if  curSum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
                elif curSum < 0:
                    left +=1
                else:
                    right -= 1
        return triplets
