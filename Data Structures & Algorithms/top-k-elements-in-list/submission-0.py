class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count={}
        sorted_freq={}
        for i in nums:
            if i in freq_count:
                freq_count[i]+=1
            else:
                freq_count[i]=1
        sorted_freq=sorted(freq_count.items(),key=lambda x:x[1],reverse=True)
        return [item[0] for item in sorted_freq[:k]]

        