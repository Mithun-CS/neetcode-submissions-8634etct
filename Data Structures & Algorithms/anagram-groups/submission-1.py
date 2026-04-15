class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            
            anagram_map[sorted_s].append(s)
        
        return list(anagram_map.values())
        
        