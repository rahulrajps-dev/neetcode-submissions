class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for word in strs:
            sorted_word=tuple(sorted(word))
            groups[sorted_word]=[]
        for word in strs:
            sorted_word=tuple(sorted(word))
            if sorted_word in groups:
                groups[sorted_word].append(word)
        return list(groups.values())