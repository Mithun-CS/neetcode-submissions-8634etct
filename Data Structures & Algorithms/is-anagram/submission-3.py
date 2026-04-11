class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for i in s:
            count[i] = count.get(i,0) + 1

        for i in t:
            if i not in count or count[i] == 0:
                return False
            count[i] -= 1

        return True
        