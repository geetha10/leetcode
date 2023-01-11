"""
Question:
Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

class Solution(object):
    """
    Algorithm:
    1. Create an empty dict(entriesMap) to store count entries
    2. initialise left,maxLen to 0
    3. Iterate the string with right pointer from 0 to len(s)
        4. inrement the count of current char in entriesMap
        5. check if right-left+1(length of current subtring) - max Occurance element value > k
        (if it is greater tha k, it means we entered a window where if we change k chars it 
        is not a repeting string)
            5.a if it exceeds k, decrement the count of caht ar index by 1 and increment left
        
        6. calculate maxLen(i.e max(maxLen, length of current substring))
    7. return maxLen

    Time Complexity: O(n)
    space Complexity: O(n)
    """
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        entriesMap = {}
        left, maxLen = 0,0
        
        for right in range(len(s)):
            entriesMap[s[right]] = 1+ entriesMap.get(s[right], 0)
            
            if (right - left + 1) - max(entriesMap.values()) > k:
                entriesMap[s[left]] -= 1
                left += 1
            
            maxLen =  max(maxLen, right - left + 1)
        return maxLen
        