class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        left=0
        res=0
        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char,0) + 1
            while (right-left + 1) - max(freq.values())  > k :
                freq[s[left]] -= 1
                left+=1
            res=max(res,right-left+1)
        return res




        