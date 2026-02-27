# Last updated: 2/27/2026, 10:18:19 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sortedS = sorted(s)
        sortedT = sorted(t)
        if sortedS == sortedT:
            return True
        return False
        