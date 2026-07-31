class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cur_sum = 0
        prefix_sums = {0: 1}
        
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            
            count += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
            
        return count