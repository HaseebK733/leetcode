# Last updated: 3/1/2026, 8:00:44 AM
# This solution uses a dynamic sliding window to move through the string, and a hashmap to keep count of the frequency of each character
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        longest = 0
4        l = 0 #initializing our left pointer
5        counter: dict[str, int] = defaultdict(int) #hashmap stores the amount of times a char has shown up
6        for r in range(len(s)): #going through the string s
7            counter[s[r]] +=1 #incrementing counter
8            while counter[s[r]] > 1: #if we get a count of >1 for any specific char
9                counter[s[l]] -=1 #we subtract the count of our left pointer's character
10                l +=1 #Then we move it forward
11            longest = max(longest, r-l+1) #at the end calculate the longest
12        return longest
13            
14
15
16        