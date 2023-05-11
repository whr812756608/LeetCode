class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        # 数组有负数并且按从小到大排列
        # 最左和最右的数字平方后一定是最大的
        # 双指针，left 指向最左 left = 0
        # right 指向数组最后一位 right = len（nums） - 1
        # 同时创建一个新数组ans，长度等于原数组 n
        # 指针k 指向新数组最后一位 k= n-1
        # ans数组从后往前（从大到小）填数
        # 每次比较 nums【left】^2 和 nums【right】^2
        # 如果左边大 则将 nums【left】^2 填入新数组， 同时左指针+=1， k-=1
        # 如果右边大（或等于） 则将 nums【right】^2 填入新数组， 同时右指针-=1， k-=1
        # 终止条件 while left <= right，当左指针大于右指针时停止
        # 注意 <= ，当left = right 时，左右指针指向同一个数，也要将这个数放进新数组
        '''
        n = len(nums)      # 获取数组长度n
        left = 0           # 双指针，left 指向最左 left = 0
        right = n -1       # right 指向数组最后一位 right = len（nums） - 1
        ans = [-1]*n       # 同时创建一个新数组ans，长度等于原数组 n
        k = n-1            # 指针k 指向新数组最后一位 k= n-1
                           # ans数组从后往前（从大到小）填数


        while left <= right:  # 终止条件 while left <= right，当左指针大于右指针时停止
        # 注意 <= ，当left = right 时，左右指针指向同一个数，也要将这个数放进新数组

            left_val = nums[left]*nums[left]      #nums【left】^2
            right_val = nums[right]*nums[right]   #nums【right】^2

            if left_val >= right_val:    #左边大 则将 nums【left】^2 填入新数组， 
                ans[k] = left_val        #则将 nums【left】^2 填入新数组
                left +=1                 #同时左指针+=1，往右移动一位

            else:                        # 如果右边大（或等于）     
                ans[k] = right_val       # 则将 nums【right】^2 填入新数组 
                right -=1                # 同时右指针-=1，往左移动一位
            k -=1                        # 无论左右结果都在新数组填了数，k-=1
        return ans
