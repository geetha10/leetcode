"""
Question:
Link: https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
1684. Count the Number of Consistent Strings
Easy

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
"""

class Solution(object):
    """
    Algorithm:
    1. Initialise count to 0
    2. Iterate through words Array
        3. Initialise isConsistent to True
        4. Iterate through current word. check if each char is in allowed string
            4.a. if the char is not in allowed string set isConsistent to False
        5. if isConsistent is true, Increase the count
    6. return the count
    """
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            isConsistent = True
            for char in word:
                if char not in allowed:
                    isConsistent = False
            if isConsistent:
                count += 1
        return count
        
        