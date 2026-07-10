class Solution:
    
    def getSingle(self,arr):
        ans = 0
        for num in arr:
            ans ^= num
        return ans
        # code here
