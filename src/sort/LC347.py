class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}
        for i in range (len(nums)):
            map_[nums[i]] = map_.get(nums[i],0)+1
            #When write map_.get(nums[i]) instead of map_.get(nums[i], 0), 
            #If the key nums[i] is not present in the dictionary map_, it will error
            #If nums[i] is not present in the dictionary, map_.get(nums[i]) will return None.
            #In this case, when you try to add 1 to None in the line map_.get(nums[i], 0) + 1,
            #TypeError will occur because you cannot add an integer to None.
        print(map_)

        pri_que = []
        for key, value in map_.items():
            heapq.heappush(pri_que,(value,key))
            # The reason for using (value, key) instead of (key, value) in heapq.heappush
            #(pri_que, (value, key)) is to prioritize elements based on the first element of the tuple, which is the (value)
            if len(pri_que) > k:  # only maintacne k elements, if len > k, heapq.heappop
                heapq.heappop(pri_que)
        res = [0] * k
        for i in range(k-1,-1,-1): # 反向遍历，因为是小顶堆，小的元素（低频）在队首
            # 输出从高频到低频要反向遍历
            res[i] = heapq.heappop(pri_que)[1]
             # [1] is used to access the second element of the tuple, 
             #  which is the key value.
            # print(heapq.heappop(pri_que))
        return res


