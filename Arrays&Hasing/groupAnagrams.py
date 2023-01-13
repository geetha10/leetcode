"""
Question:
Link: https://leetcode.com/problems/group-anagrams/
49. Group Anagrams
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        #1)Create empty dictionary to store entries- sorted word as key and value is a tuple of word at index
        #2) Iterate through the strs array
        #3)In each iteration. 
            #3a) get the word at index and sort it
            #3b) check if the sorted word is laready present in the entries dictionary
                #a) if present add the current word to the values tuple of that key in dict
                #b) else create the new entry with sorted word as key in dict
        #4) Return the all values in the dict 
        #Time Complexity: O(nlogn)
        #Space Complexity: O(n)
        entries ={}
    
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in entries:
                entries[sortedWord].append(word)
            else:
                entries[sortedWord] = [word]

        return entries.values()
                

if __name__ == "__main__":
    s = Solution()
    out = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(out)