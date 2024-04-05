class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        first = -1
        last = -1
        for i in range(0, n):
            if (target != nums[i]):
                continue
            if (first == -1):
                first = i
            last = i
 
        if (first == -1 and last==-1):
            return[-1,-1]
        elif(first!=-1 and last!=-1):
            return[first,last]