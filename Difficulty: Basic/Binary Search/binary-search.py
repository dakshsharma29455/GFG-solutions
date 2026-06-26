class Solution:
    def binarySearch(self, arr, k):
        n = len(arr)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == k:
                return True
            elif k > arr[mid]:
                low = mid +1
            else :
                high = mid -1
        return False       
        # code here
        