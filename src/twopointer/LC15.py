class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #a + b + c =0
        # index i, left, right
        nums.sort() # sort the list first!
        result = []
        n = len(nums)
        i = 0 # index of a

        for i in range(n-2):    # since answer contains a,b,c, the max index a can go is
                                # a = n-3, b = n-2, c = n-1 (last index)
                                # python [0,n-2) = [0,n-3]
            if nums[i] > 0:     # a > b > c, if a > 0, use BREAK!
                break
            
            if i >0 and nums[i] == nums[i-1]:
                continue                      # if write nums[i] == nums[i+1], [-1,-1,2]
                                              #  will be skip, so only compare to previous value
                                              # i and i -1
                                              # use continue to go to next k             
            left = i+1
            right = n-1

            while left < right:               
                s = nums[i] + nums[left] + nums[right]  # while loop condition is left < right
                                  # if left = right, left and right are point to same number
                                  # answer will be only two number a and b, WRONG
                if s > 0 :        # if a + b + c >0, reduce c by right-=1
                    right -=1
                elif s < 0 :      # elif here! if a + b + c >0, increase b by left +=1
                    left +=1      # 去重只要放在收割结果时就可以
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    left  +=1
                    right -=1  #先处理下标再去重，顺序很重要
                    while left < right and nums[right] == nums[right+1]: 
                        right -=1  #right 已经-1， 所以是 current right 和 right +1 比
                    while left < right and nums[left] == nums[left-1]:
                        left +=1   #left 已经+1， 所以是 current left 和 right -1 比
        return result
