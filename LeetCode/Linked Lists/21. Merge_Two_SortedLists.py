# https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: easy

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        arr1 = []
        c1 = list1
        while c1:
            arr1.append(c1.val)
            c1 = c1.next

        arr2 = []
        c2 = list2
        while c2:
            arr2.append(c2.val)
            c2 = c2.next
        
        arr = arr1 + arr2
        arr.sort()

        curr = temp = ListNode()
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
        return temp.next
