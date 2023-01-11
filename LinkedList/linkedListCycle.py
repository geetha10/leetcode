# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Question:
Link : https://leetcode.com/problems/linked-list-cycle/

141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


"""
class Solution(object):
    """
    Algorithm:
    1. Initialise two pointers slow , fast both of them pointing to head
    2. Iterate till fast and fast.next are not null.
        3.Increment slow by one i.e.to slow.next
        4.Increment slow by two i.e.to fast.next.next
        5.if slow and fast are equal. it means there is loop, return True
    
    6. If you come out of the while loop, it means there is no loop. return false

    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
    