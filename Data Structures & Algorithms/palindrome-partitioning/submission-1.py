class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(i, current_path):
            if i == len(s):
                res.append(current_path)
                return
            
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    dfs(j + 1, current_path + [sub])
                    
        dfs(0, [])
        return res