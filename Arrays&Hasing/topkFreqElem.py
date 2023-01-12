"""
Question:
Link: https://leetcode.com/problems/top-k-frequent-elements/
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #1) Create an emty dict to store count of the elements in nums array. num:key,count:value
        #2) Create an empty freqArraywhich is +1 of length of nums array and at each index it holds array 
        #as value
            #each index (0 to len(nums)+1) indicates the count/freq
            #at each index/freq store the values fron nums array who's count is same as index
        #3) Create a array to store result(TopK elements)
        #4) Iterate through the freqArray in reverse order i.e (length-1 to 0):
            #As each index is freq, and we need topK freq elements we have to iterate in reverse.
            #Each index at freqArray holds the array of nums whos count is same as value of index
            #4a)iterate through the array at index:
                #4.a.a) append the element/num to result array
                #4.b.b) check if the len if result array is equal to k:
                    #) if equal return result array
    #) this process continues untill the result array is of size k and returns the result. because of 
    #which we do not need an explicit return statment
       
        entries = defaultdict(int)
        freqArray = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            entries[num] += 1

        for num,freq in entries.items():
            freqArray[freq].append(num)

        result=[]

        for freq in range(len(freqArray)-1,0,-1):
            for num in freqArray[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        
        




        