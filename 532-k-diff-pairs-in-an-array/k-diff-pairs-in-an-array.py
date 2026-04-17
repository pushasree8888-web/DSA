class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0 
        dictionary=Counter(nums)
        count=0 
        for num in dictionary:
            if k==0:
                if dictionary[num]>1 :
                    count+=1 
            else:
                if num+k in dictionary:
                    count+=1 
        return count

        

        
        