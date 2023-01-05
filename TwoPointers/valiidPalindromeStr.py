"""
Question:
125. Valid Palindrome
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution(object):
    """
    Algorithm:
    1. Create a variable and assign all alphaNumeric values to it 1.e(a-z and 0-9)
    2. Convert the input string to lower case
    3. Initialise left to 0 and right to len(s) -1
    4. Iterate through the string till left < right(It iterates till half i.e mid of the string)
        5. In each iteratin, check if the char at index left is equal to char at right.
            5.a. if not equal return False
            5.b. else. Increment left, decrement right
    6. After the loop return True. Because if it comes out of loop it means it is palindrome string

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        aplhaNumericChars="abcdefghijklmnopqrstuvwxyz0123456789"
        palindromeStr =""
        for char in s:
            if char in aplhaNumericChars:
                palindromeStr = palindromeStr  + char
        
        left = 0
        right = len(palindromeStr)-1
        
        while left<right:
            if palindromeStr[left] != palindromeStr[right]:
                return False
            left += 1
            right -= 1
        
        return True
