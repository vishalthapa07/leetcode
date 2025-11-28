import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for chr in s:
            if chr.isalnum():
                s2 += chr.lower()
        
        i = 1
        result = False
        if len(s2) == 0:
            return True
        for c in s2:
            if (c != s2[len(s2)-i]):
                result = False
                break
            else:
                result = True
            i = i + 1
        return result
            
