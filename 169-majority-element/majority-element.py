class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        candidate=None
        for i in nums:
            if c==0:
                candidate=i
            if i==candidate:
                c+=1 
            else:
                c-=1
            
        return candidate
        