"""
Question:
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest
substring
without repeating characters.
"""

class Solution(object):
    """
    Algorithm:
    1. Create a set for holding char/elements of longest substring named charSet, a varaiable to hold maxLen
    2. Initalise the left to 0
    3. Iterate right through the length of input string
        4. If s[right] in charSet, Remove s[left] increment left till left is pointing to index, substring from left to right dosent have any dupliucates. 
        5. add s[right] to cahrset
        6. calcualte the maxLen. it would be max of maxLen, right - left + 1 (since we are refering to indices)
    7. return maxLen

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet, maxLen = set(), 0   
        left = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            maxLen = max(maxLen, right-left+1)

        return maxLen    