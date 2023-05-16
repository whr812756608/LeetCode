class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = [0]*26 # hash_table array
        # create a len = 26 letters list
        # the key(index) is ord(r)-ord('a') = 0,1,2,3,...25 for a,b,c,...,z
        # the value is the occurance of letters, initlized to 0
        # error when hashmap= []
        
        for r in ransomNote:
            hashmap[ord(r)-ord('a')] +=1
        
        for m in magazine:
            hashmap[ord(m)-ord('a')] -=1
        
        for i in range(26):
            if hashmap[i] > 0:
                return False
        return False
