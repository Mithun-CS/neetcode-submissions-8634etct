class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs_backtrack(start_index, current_path, current_sum):
            if current_sum == target:
                result.append(current_path)
                return
            
            if current_sum > target:
                return
                
            for i in range(start_index, len(nums)):
                dfs_backtrack(i, current_path + [nums[i]], current_sum + nums[i])
                
        dfs_backtrack(0, [], 0)
        return result