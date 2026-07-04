class Solution:
    def longestUniqueSubstr(self, s):
        char_hash = {}
        l = 0
        r = 0
        max_len = 0
        n = len(s)
        while r < n:
            if s[r] in char_hash:
                if char_hash[s[r]] >= l:
                    l = char_hash[s[r]] + 1
            new_len = r -l + 1
            max_len = max(new_len,max_len)
            char_hash[s[r]] = r
            r += 1
            
        return max_len    
        # code here
        