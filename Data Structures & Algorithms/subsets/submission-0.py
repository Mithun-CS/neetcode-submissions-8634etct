class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs_backtrack(start_index, current_path):
            result.append(current_path)
            
            for i in range(start_index, len(nums)):
                dfs_backtrack(i + 1, current_path + [nums[i]])
                
        dfs_backtrack(0, [])
        return result
        