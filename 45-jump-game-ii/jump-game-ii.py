class Solution:
    def jump(self, nums: List[int]) -> int:
        c=0
        f=0
        j=0
        n=len(nums)
        for i in range(n-1):
            f=max(f,i+nums[i])
            if i==c:
                j+=1
                c=f 
        return j
        