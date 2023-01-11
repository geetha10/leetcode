"""
Link: https://leetcode.com/problems/contains-duplicate-ii/description/
219. Contains Duplicate II
Easy

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""
class Solution(object):
    """
    Algorithm: 
    Method 1: dictionary
    1. Initialise a dict to store ebtries of nums array. key is num, value is index of its
       accurance in array.
    2. Iterate  through the nums array from index 0 to length of nums
        3. check if the number at index is already in the map.
            3.a if exists, get its value from dict, i.e its prev index
            3.b calculate the absolute diff of current index(second accurance of number in
             the araay) and the value form dict(prev occurance)
            3.c. check if the absolute diff <= k. if so, return true
        4. else,for each number at index, add the entry in dict, key is number and value is
         index
    5. Return false. you will come out of the loop if the absolute diff is > k or id there is
     no duplicate 
    Time Complexity: O(n)
    Space Complexity: O(n)

    Method 2:
    1. Initilise the left pointer to 0, right to 1
    2. Initialise a set to store the values of nums array
    3. Add element at index 0 to entriesSet
    4. Iterate the right pointer from 1 to len(nums) using while loop
        4. Check if the right-left <= k(k is the max window length we can have)
           4.a. check if nums[right] in exist entriesset,if exist. return Ture(as the window 
           length is less than k, its obvious that absolute diff would be less than k)
           4.b. if nums[right] not entries set, add it to entries set and increment right by 1
        5. else(which means window length is greater than k): remove the nums[left] from 
        entriesSet and increment left. This step re initialise the window  size
    6. return False at last
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # entriesMap = {}

        # for index in range(len(nums)):
        #     if nums[index] in entriesMap:
        #         diff = abs(entriesMap[nums[index]]-index)
        #         if diff <= k:
        #             return True
        #     entriesMap[nums[index]] = index
        
        # return False

        entriesSet = set()
        left = 0
        entriesSet.add(nums[0])
        right = 1
        while right < len(nums):
            if right-left <= k:
                if nums[right] in entriesSet:
                    return True
                entriesSet.add(nums[right])
                right += 1
            else:
                entriesSet.remove(nums[left])
                left+=1
        return False