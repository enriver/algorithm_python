# Group Anagrams

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=dict()
        
        for word in strs:
            s_word=' '.join(sorted(word))
            if s_word not in anagrams.keys():
                anagrams[s_word]=list()
                
            anagrams[s_word].append(word)
            
        return anagrams.values()