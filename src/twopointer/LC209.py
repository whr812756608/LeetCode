class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # 本题应用场景：子数组的和在窗口开始位置left移动时不断变小
        # while循环从满足要求不断变成不满足要求
        # 这就是单调性，单调性决定了能否用滑动窗口
        # 所求ans在while循环内更新
        # Time complexity O(N) for O(N), while O(N) O(2N) = O(N)
        # Space complexity O(1) ans

        n = len(nums)
        left = 0
        ans = n+1      # ans初始化为 n+1， 因为所求答案最大值为数组长度
        cur_sum = 0    # n+1 保证最大， 然后求min

        # 滑动窗口模版， 使用python enumerate
        # right 控制窗口结束位置，遍历整个数组的指针
        # x == nums【right】，为遍历指针的当前值
        for right,x in enumerate (nums):
            cur_sum += x                    #当窗口结束位置向右扩张一位，sum加上当前值
            while cur_sum >= target:        # 循环条件：sum 大于等于target（题意）
                sublength = right - left +1 # 判断所求subarray长度，右-左+1
                                            # 判断是否需要+1， let left == right
                                            # 此时subarray长度为0，不合法，所以+1
                ans = min(ans,sublength )   # 更新ans，while循环内部更新ans
                                            # 为满足要求到不满足要求
                cur_sum -= nums[left]       # 更新窗口内的总和，减去nums【left】 
                left +=1                    # 更新窗口开始位置left+=1
        return ans if ans <= n else 0       # 如果ans 超过n， return 0
        
         
