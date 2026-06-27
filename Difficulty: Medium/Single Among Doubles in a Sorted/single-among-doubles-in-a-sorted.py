class Solution:
    def single(self, arr):
        # code here
        n = len(arr)
        if n == 1:
            return arr[0]
        for i in range(n):
            if i == 0:
                if arr[i] != arr[i+1]:
                    return arr[i]
            elif i == n-1:
                if arr[i] != arr[i-1]:
                    return arr[i]
            else:
                if arr[i] != arr[i+1] and arr[i] != arr[i-1]:
                    return arr[i]
        