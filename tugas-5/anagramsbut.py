from typing import List
from hashtable import HashTable


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = HashTable()
        for s in strs:
            if tuple(sorted(tuple(s))) not in anagrams.keys():
                anagrams[tuple(sorted(tuple(s)))] = [s]
            else:
                anagrams[tuple(sorted(tuple(s)))].append(s)  # type: ignore
        return sorted(list(anagrams.values()), key=lambda a: len(a), reverse=True)


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
