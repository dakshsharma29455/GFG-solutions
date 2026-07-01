class Solution:
    def mergeSort(self, arr, l, r):
        if len(arr)>1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            self.mergeSort(left,0,len(left)-1)
            self.mergeSort(right,0,len(right)-1)
            i = j = k = 0
            while i<len(left) and j<len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        
        
        # code here
        