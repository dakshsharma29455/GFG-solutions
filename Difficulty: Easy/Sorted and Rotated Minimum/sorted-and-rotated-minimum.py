class Solution:
    def findMin(self, arr):
        n = len(arr)
        low = 0
        high = n-1
        while low < high:
            if arr[low] < arr[high]:
                return arr[low]
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low =  mid + 1
            else:
                high = mid
        return arr[low]     
        
        # code here
        