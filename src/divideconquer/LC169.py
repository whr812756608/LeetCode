class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        def getmajorityElement(nums,left,right):
            if left == right: #左闭右闭
                return nums[left]

            mid = left + (right-left)//2

            maxLeft  = getmajorityElement(nums,left,mid)
            maxRight = getmajorityElement(nums,mid+1,right)

            if maxLeft == maxRight:
                return maxLeft

            else:
                leftcnt = 0
                rightcnt = 0

                for i in range(left,right+1):
                    if nums[i] == maxLeft:
                        leftcnt += 1
                    if nums[i] == maxRight:
                        rightcnt += 1
                        
                if leftcnt > rightcnt:
                    return maxLeft
                else:
                    return maxRight

        return getmajorityElement(nums,0, len(nums)-1)
