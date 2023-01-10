"""
Question:
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution(object):
    """
    Algorithm:
    1. Create write pointer pointing at index 0
    2. Iterate through the nums array with read pointer from 0 to len(nums)
        3. if the number is not equal to target num(which means you have to keep the number), copy the number to the nums at index of write and     
        increment the wirte pointer
    4. Iterate through the nums array with write pointer from range write to len(nums):
        5. POP all the elements from index wirite till end of array 

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write = 0
        for read in range(0, len(nums)):
            # checking if the num at index is equal to target
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        for write in range(write, len(nums)):
            nums.pop()
        