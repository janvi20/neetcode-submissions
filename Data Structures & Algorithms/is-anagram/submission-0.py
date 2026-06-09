class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counters = [0]*26
        if (len(s) == len(t)):
            for i in range(len(s)):
                counters[ord(s[i]) - ord('a')] += 1
                counters[ord(t[i]) - ord('a')] -= 1
            
            for c in counters:
                if c > 0:
                    return False
            return True
        else: 
            return False
        