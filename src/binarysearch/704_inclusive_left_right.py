class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 左闭右闭写法
        left = 0  # left boundary (index 0)
        right = len(nums)-1 # right boundary, len-1 (last index of nums )
        
        while left <= right:  #左闭右闭 left == right 合法区间 【1，1】
            mid = left + (right-left) //2  #防止left + right /2越界 

            if nums[mid] > target:    # nums[mid] > target
                right = mid - 1     # 说明target 在 mid 左边，更新右端点
                                    # 更新为 right = mid-1
                                   #  左闭右闭区间，已知nums[mid] > target
                                   #  不需要包含mid                                 
            elif nums[mid] < target: # 同理，nums[mid] < target
                left = mid + 1       # 说明target 在 mid 右边
                                     # 更新左端点，left = mid + 1
                                     #  左闭右闭区间不需要包含mid
            else:                    # nums[mid] == target
                return mid
        return -1
