class Solution(object):
    def isAnagram(self, s:str, t:str) -> bool:
        counter = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i], 0) + 1
            counter[t[i]] = counter.get(t[i], 0) - 1

        for key, value in counter.items():
            if value != 0:
                return False
        return True