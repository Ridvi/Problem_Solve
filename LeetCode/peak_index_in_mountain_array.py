class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start =1
        end=len(arr)-2
        while(start<=end):
            mid=start+(end-start)//2
            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                return mid

            if arr[mid]>arr[mid-1]:
                start=mid+1
            else:
                end=mid-1

             
