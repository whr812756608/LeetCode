class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_table = {}       # key in hash_table is the num in nums1 and nums2
                              # value of key can be any number 
                              # set the value of key to 0 for num in nums2 
                              # if ()hash_table.get(num) = value) return true 
                              # if... return ture if ...!=0 return False if ... =0
        result = []
      
        for num in nums1:
            hash_table[num] = 1     # set a value

        for num in nums2:
            if hash_table.get(num):
                result.append(num)
                hash_table[num] = 0  # for next element that have same value as num
                                     # hash_table.get(num)=0
                                     # if hash_table.get(num) return False
                                     # will not go through the if statement
        return result
