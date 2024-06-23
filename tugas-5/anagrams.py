from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            if tuple(sorted(tuple(s))) not in anagrams.keys():
                anagrams[tuple(sorted(tuple(s)))] = [s]
            else:
                anagrams[tuple(sorted(tuple(s)))].append(s)
        return list(anagrams.values())
