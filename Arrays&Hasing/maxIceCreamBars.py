"""
Question:
1833. Maximum Ice Cream Bars
Medium

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.

Link: https://leetcode.com/problems/maximum-ice-cream-bars/description/
"""

class Solution(object):
    """
    Algorithm:
    1. Sort the costs array in asending order
    2. Initialise the count to 0
    3. Iterate through the sorted cost array
        4. ckeck if the cost at index is <= coins
            4.a. if yes, increment the count and deduct the price(i.e cost of icecream) from the remaining coins balance
            4.b. else, break from the loop (it means boy cannot buy any icreams as remaining other are costly sicne they are in asc order)
    5.return count

    Time Complexity: O(logn)
    Space Complexity: O(1)
    """
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs = sorted(costs)
        count = 0
        for cost in costs:
            if cost <= coins:
                count += 1
                coins -= cost
            else:
                break
        return count
        