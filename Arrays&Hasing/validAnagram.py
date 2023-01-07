"""
Question:
242. Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Link: https://leetcode.com/problems/valid-anagram/
"""

class Solution(object):
    """
    Algorithm:
    1) check the length of both arrays. if not same return False
    2) create dict for counting elements occurance in bth the strings
    3) Iterate through the lenth of any one string
    4) IN EACH ITERATION, get the count of elemts from both the string at index i from their respective dict's and increase the count
    5) compare two dict's, if they are same return True, else return False

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 1) check the length of both arrays. if not same return False
        if len(s) != len(t):
            return False
        #2) create dict for counting elements occurance in bth the strings
        sDict=defaultdict(int)
        tDict=defaultdict(int)

        #defaultdict(int) returns value 0, id the elements is not already present  in dict else. Where as 
        #normal dict return None(if element is not present in dict)
        
        #3) Iterate through the lenth of any one string
        for i in range(len(s)):
            #4) IN EACH ITERATION, get the count of elemts from both the string at index i from their 
            #respective dict's and increase the count
            sDict[s[i]] = sDict[s[i]] + 1 
            tDict[t[i]] = tDict[t[i]] + 1
        #5) compare two dict's, if they are same return True, else return False
        return sDict == tDict