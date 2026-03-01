# Last updated: 3/1/2026, 9:35:29 AM
# Used binary search, calculated midpoint, compared midpoint to the last element, moved pointers towards the middle
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left, right = 0, len(nums) - 1 #initialize our two pointers
4        best_candidate = nums[0] #track our closest answer, set it to 0 for edge case where theres only 1 element
5        while left <= right: #while our pointers haven't crossed
6            mid = (left + right) //2 #calculate the middle
7            if nums[mid] <= nums[-1]: #compare our middle value to the last element
8                best_candidate = nums[mid] #set the closest answer to the middle value
9                right = mid - 1 #move our right pointer towards the middle
10            else: left = mid + 1 #move our left pointer towards the middle
11        return best_candidate #return the closest answer
12