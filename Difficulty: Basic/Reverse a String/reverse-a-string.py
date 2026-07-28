class Solution:
    def reverseString(self, s: str) -> str:
        # code here
        s = list(s)
        l,r = 0, len(s) - 1
        while l < r :
            s[l],s[r] = s[r],s[l]
            l,r = l+1,r-1
        return "".join(s)    
        