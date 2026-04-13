class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False
        premap = {}
        for i,n in enumerate(nums):
            if n in premap:
                return True
                break
            else:
                premap[n] = i

        return False
                
           

        