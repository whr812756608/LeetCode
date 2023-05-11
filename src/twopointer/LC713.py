class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 本题应用场景：子数组的乘积在窗口开始位置left移动时不断变小
        # while循环从 不满足要求 不断变成  满足要求
        # while循环结束时 才满足要求 子数组的乘积小于k
        # 所求ans在while循环外更新
        # Time complexity O(N) for O(N), while O(N) O(2N) = O(N)
        # Space complexity O(1) ans

        left  = 0
        cur_product = 1 
        ans = 0

        if k <=1:
            return 0 

        # 对于一个给定的窗口结束位置right
        # 使用while cur_product >= k 循环 不断缩小窗口开始位置left
        # 直到满足 cur_product < k 的窗口[l,r]
        # 结束循环并计算子数组个数 [l,r],[l+1,r],[l+2,r]....[r,r] == right-left +1
        for right, x in enumerate (nums):
            cur_product *= x
            while cur_product >= k:
                cur_product /= nums[left]
                left +=1
            sublength = right - left + 1
            ans += sublength
        return ans 
