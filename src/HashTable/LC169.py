class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = dict()
        for n in nums:
            if n in hashmap:
                hashmap[n] +=1
            else:
                hashmap[n] = 1
        
        from collections import defaultdict
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] +=1
        
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n,0)+1

        for key, value in hashmap.items():
            if value > len(nums)/2:
                return key
