# Last updated: 2/27/2026, 10:19:53 AM
# This solution uses a hashmap to keep track of values
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        my_map = {} #creating an empty hashmap
4        
5
6        for index, num in enumerate(nums): #using enumerate for loop so we can track index and value
7            missing_num = target - num
8            if missing_num in my_map: #checking to see if the missing number exists in our hashmap
9                return[my_map[missing_num], index] #if it does then we return the missing num and the index
10            my_map[num] = index #otherwise we just add the current number  and the index to our hashmap for further comparisons
11
12            #in line 9 we use [] to create a list since our final answer needs to be a list of the indices that add up to the target.