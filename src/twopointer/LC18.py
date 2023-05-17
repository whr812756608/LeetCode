class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        k = 0 
        res = []
        n = len(nums)
        nums.sort()

        for k in range(n-3):
            if k>0 and nums[k] == nums[k-1]: #去重，k和k前一位比，
                                             #k前一位最小为0， 所以要判断k大于0
                continue
            for i in range(k+1,n-2):
                if i > k+1 and nums[i] == nums[i-1]: #二次去重，i和i前一位比，
                                                     #i前一位为k， 所以要判断i大于k+1 ！！！！
                    continue
                left = i+1
                right = n-1
                while left < right:
                    s = nums[k] + nums[i] +nums[left] + nums[right]
                    if s > target:
                        right -=1
                    elif s < target:
                        left +=1
                    else:
                        res.append([nums[k],nums[i],nums[left],nums[right]])
                        left +=1
                        right -=1
                        while left < right and nums[left] == nums[left-1]:
                            left +=1
                        while left < right and nums[right] == nums[right+1]:
                            right-=1
        return res
