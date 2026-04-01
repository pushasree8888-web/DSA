class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        res=[]
        flag=False
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i]+nums[j]==target):
                    res.append(i)
                    res.append(j)
                    flag=True
                    break
            if flag==True:
                break   
                
        return res
        