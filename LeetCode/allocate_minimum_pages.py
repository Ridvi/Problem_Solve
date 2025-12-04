class Solution:
    def isvalid(self, arr, k, mid):
        student = 1
        pages_sum = 0
        
        for page in arr:
            if pages_sum + page <= mid:
                pages_sum += page
            else:
                student += 1
                pages_sum = page
                
        return student <= k  # True if mid is feasible

    def findPages(self, arr, k):
        if k > len(arr):
            return -1
        
        st = max(arr)  # min possible max pages
        end = sum(arr)
        ans = -1
        
        while st <= end:
            mid = st + (end - st) // 2
            
            if self.isvalid(arr, k, mid):
                ans = mid
                end = mid - 1
            else:
                st = mid + 1
                
        return ans
