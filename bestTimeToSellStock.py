"""
Question: 
121. Best Time to Buy and Sell Stock
Easy
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""
class Solution(object):
    """
    Algorithm: 
    
    Method 1(Time Limit Exceeded)
    1. Initialise a variable to hold maxProfit.
    2. Iterates through the prices array: from 0 to len prices array
    3. Initialise j= i+1, Iterate through prices array from i+1 to len of array
    4. calculate the profit i.e prices[j] - prices[i]: maxProfit would be max of maxProfit and calculated profit
    5. return maxProfit

    Time Complexity: O(n*2)
    Space Complexity: O(1)

    Method 2: Sliding Window
    1. Initialise a variable to hold maxProfit.
    2. Initialise left to 0
    3. Iterate right through the length of prices array from index 1
    4. if the prices[right] < prices[left], update the left value to right
    5. calculate the profit i.e prices[j] - prices[i]: maxProfit would be max of maxProfit and calculated profit
    6. return maxProfit

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxProfit = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            maxProfit = max(maxProfit, prices[right] - prices[left])

        return maxProfit