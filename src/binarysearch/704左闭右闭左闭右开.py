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

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 左闭右开写法
        left = 0  # left boundary (index 0)
        right = len(nums) # 右区间改为 len（nums） 防止数组只有一个元素
        
        while left < right:  #左闭右开 left 不能等于 right 合法区间 【1，2）
            mid = left + (right-left) //2  #防止left + right /2越界 

            if nums[mid] > target:    # nums[mid] > target
                right = mid      # 说明target 在 mid 左边，更新右端点
                                    # 更新为 right = mid
                                   #  右开区间，已知nums[mid] > target
                                   #  需要包含mid                                 
            elif nums[mid] < target: # nums[mid] < target
                left = mid + 1       # 说明target 在 mid 右边
                                     # 更新左端点，left = mid + 1
                                     #  左闭区间不需要包含mid
            else:                    # nums[mid] == target
                return mid
        return -1
