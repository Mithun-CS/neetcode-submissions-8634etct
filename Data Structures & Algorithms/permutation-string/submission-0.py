class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_counts[i] == s2_counts[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            r_idx = ord(s2[right]) - ord('a')
            s2_counts[r_idx] += 1
            if s1_counts[r_idx] == s2_counts[r_idx]:
                matches += 1
            elif s1_counts[r_idx] == s2_counts[r_idx] - 1:
                matches -= 1

            l_idx = ord(s2[left]) - ord('a')
            s2_counts[l_idx] -= 1
            if s1_counts[l_idx] == s2_counts[l_idx]:
                matches += 1
            elif s1_counts[l_idx] == s2_counts[l_idx] + 1:
                matches -= 1

            left += 1

        return matches == 26
        