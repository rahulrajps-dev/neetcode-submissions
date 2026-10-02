class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen={}
        length=0
        for right in range(len(s)):
            seen[s[right]] = 1 + seen.get(s[right],0)

            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left+=1
            length =  max(length,right-left + 1)
       
        return length

