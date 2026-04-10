class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        current_state = {}
        max_freq = 0
        

        for right in range(len(s)):
            element = s[right]
            current_state[element] = current_state.get(element,0) + 1
            max_freq = max(max_freq, current_state[element])

            while (right - left + 1) - max_freq > k:
                element_left = s[left]
                current_state[element_left] -= 1

                if current_state[element_left] == 0:
                    del current_state[element_left]
                left += 1
        
        max_length = max(max_length, right- left + 1)
        return max_length
        