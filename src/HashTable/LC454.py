class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import defaultdict
        
        hashmap = defaultdict(int)
        count = 0
        for a in nums1:      
            for b in nums2:
                hashmap[a+b]+=1   # use defaultdict(int) can generate a key and value if this key is not exsist in hashmap yet, value = int, but value can only be int
      
        for c in nums3:
            for d in nums4:
                if 0-(c+d) in hashmap:        # since 0 = (a+b) + (c+d)
                                              # if 0-(c+d) in hashmapm, it statsify 
                    count += hashmap[0-(c+d)] # Is NOT count +=1 here!!!
                                              # count += the value of hashmap[0-(c+d)]
                                              # the occurance time in ()a+b)
        return count
    
    # use dict(), frist need to check if the key already exist in hashmap,
    # if not, create a key and set its value to 1
    class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = dict()
        count = 0

        for a in nums1:
            for b in nums2:
                if a+b in hashmap:
                    hashmap[a+b] +=1
                else:
                    hashmap[a+b] =1
        
        for c in nums3:
            for d in nums4:
                if 0 - (c+d) in hashmap:
                    count += hashmap[0-(c+d)]
        return count
