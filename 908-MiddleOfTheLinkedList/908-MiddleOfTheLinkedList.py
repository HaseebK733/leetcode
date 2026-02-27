# Last updated: 2/27/2026, 10:18:18 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head #initialize our two pointers and start them at the head of our linked list
        while fast and fast.next: #while fast is at a valid node and the next node isn't pointing at none we move our fast pointer forward by 2 nodes at a time and our slow pointer by 1 node at a time
            fast = fast.next.next
            slow = slow.next
        return slow #eventually our fast pointer is gonna reach the end and then we simply return our slow pointer
        