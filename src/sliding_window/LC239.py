class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # 如果数组为空或 k = 0，直接返回空
        if not nums or not k:
            return []
        # 如果数组只有1个元素，直接返回该元素
        if len(nums) == 1:
            return [nums[0]]

        # 初始化队列和结果，队列存储数组的下标
        queue = collections.deque()
        res = []

        for i in range(k):
            # 对于新进入的元素，如果队列前面的数比它小，那么前面的都出队列
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            # 新元素入队列
            queue.append(i)
        res.append(nums[queue[0]])


        for i in range(k,len(nums)):
            # 如果当前队列最左侧存储的下标等于 i-k 的值，代表目前队列已满。
            # 但是新元素需要进来，所以列表最左侧的下标出队列

            # 对于新进入的元素，如果队列前面的数比它小，那么前面的都出队列
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            # 新元素入队列
            queue.append(i)

            if queue and queue[0] == i - k:
                queue.popleft()
            # 当前的大值加入到结果数组中
            res.append(nums[queue[0]])

        return res
