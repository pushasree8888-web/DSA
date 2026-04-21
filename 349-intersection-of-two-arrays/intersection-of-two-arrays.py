class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set(nums1)
        r = set()

        for num in nums2:
            if num in res:
                r.add(num)

        return list(r)