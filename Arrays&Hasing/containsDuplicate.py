"""
Question:
217. Contains Duplicate
Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Link: https://leetcode.com/problems/contains-duplicate/
"""

class Solution(object):
    """
    Algorithm:
    1) create an empty set
    2) Iterate through the nums array
    3) For each emement in array check if it is alrray present in the set
        3).a) if already persent return True
    4) if not present create an enrty in the set
    5) Finally return False if no duplicate is present

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 1) create an empty set
        entries = set()
        #2) Iterate through the nums array
        for n in nums:
            #3) For each emement in array check if it is alrray present in the set
            if n in entries:
                #3).a) if already persent return True
                return True
            #3). b) if not present create an enrty in the set
            entries.add(n)
        #5) Finally return False if no duplicate is present
        return False