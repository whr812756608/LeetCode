class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()

        for i, num in enumerate (nums):
            # first check if target - value in hashtable
            if target - num in hashtable:
                return [hashtable[target-num],i]
            # add the nums as key to hashtable, value is index i 
            hashtable[num] = i
        return []
