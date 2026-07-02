# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0 
        start = head
        cursor = head
        prev = None
        while cursor:
            tmpc = cursor
            cursor = cursor.next 
            prev = tmpc
            index+=1
            print(index)
        actIndex = index-n
        print(actIndex)
        index = 0
        cursor = head
        prev = None
        while cursor:
            if actIndex == index:
                tmp = cursor.next
                cursor.next = None
                cursor = tmp
                if prev:
                    prev.next = cursor
                    return start
                else:
                    return cursor
            tmpc = cursor
            cursor = cursor.next 
            prev = tmpc
            index+=1
            print(index)
            
