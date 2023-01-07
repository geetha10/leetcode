"""
Question:
728. Self Dividing Numbers
Easy
A self-dividing number is a number that is divisible by every digit it contains.

    For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

Link: https://leetcode.com/problems/self-dividing-numbers/solutions/?languageTags=python3&topicTags=string
"""
class Solution(object):
    """
    Algorithm:
    Method 1
    1. create an empty result array to store self divisible numbers in given range
    2. Iterarte num through the range left, rigth+1 (as we want to include rigth in range)
    3. create a variable(copyOfNUm) to copy the current number
        4. set isSelfDivisible to True
        5. Iterate till copyOfNum > 0
            6. calculate the units digit by performing modulo operation
            7. check if units digit == 0
                7.a. if yes, set isSelfDivisible to Flase abd break from loop
            8. check if num is not divisible by digit
                8.a. if yes, set isSelfDivisible to Flase abd break from loop
            9. update copyOfNUm to copyOfNum/10
        10. if isSelfDivisible is True
            10.a append num ro result array
    11. return result array

    Time Complexity: O(n^2)
    Space Complexity: O(1) or O(n)

    """
    """

    Method 2:
    1. create an empty result array to store self divisible numbers in given range
    2. Iterarte num through the range left, rigth+1 (as we want to include rigth in range)
        3. Convert num to string and stor it in variable strOfNum
        4. check if 0 is not in strOfNum
            5. set isDivisible to True
            6. Iterate trough each element(i.e digit) of strOfNum
                7. check if num is divisible int value of digit
                    7.a. if no, set isSelfDivisible to false and break from loop
            8. if selfDivisible is True, append the num to result array
    9.return result array
    """
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # Method 1
        # result = []
        # for num in range(left, right+1):
        #     copyOfNum = num
        #     isSelfDivisible = True
        #     while copyOfNum > 0:
        #         digit = copyOfNum % 10
        #         print(digit)
        #         if digit == 0:
        #             isSelfDivisible = False
        #             break
        #         if num % digit != 0:
        #             isSelfDivisible = False
        #             break
        #         copyOfNum = copyOfNum/10
        #     if isSelfDivisible:
        #         result.append(num)
        # return result

        # Method 2

        result = []

        for num in range(left,right+1):
            strOfNum = str(num)
            if "0" not in strOfNum:
                isSelfDivisible  = True
                for digit in strOfNum:
                    if num % int(digit) != 0:
                        isSelfDivisible = False
                        break
                if isSelfDivisible:
                    result.append(num)

        return result

