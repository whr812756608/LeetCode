class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 第一个到来的士兵，直接插上自己阵营的旗帜占领这块高地，此时领主 winner 就是这个阵营的人，
        # winner = nums[0]
        # 现存兵力 count = 1。
        winner = nums[0]
        count = 1 
        for i in range(1,len(nums)):
            # 如果先判断count是否为0
            # 即每次新来的士兵都要判断是否该士兵winner（新占领的一方）
            # 这里count 不用 +=1， 因为下一行会自动把count +1
            if count == 0:
                winner = nums[i]
            if nums[i] == winner:
                # 如果新来的士兵和前一个士兵是同一阵营，则集合起来占领高地，领主不变，
                # winner 依然是当前这个士兵所属阵营，现存兵力 count++；
                count +=1
            else:
                #如果新来到的士兵不是同一阵营，则前方阵营派一个士兵和它同归于尽。 
                #此时前方阵营兵力count --。
                #（即使双方都死光，这块高地的旗帜 winner 依然不变，
                #因为已经没有活着的士兵可以去换上自己的新旗帜）
                count -=1

            # 把 判断count == 0 放在后面则要加1
            # 当下一个士兵到来，发现前方阵营已经没有兵力，新士兵就成了领主，
            # winner 变成这个士兵所属阵营的旗帜，
            # 现存兵力 count ++
            # if count == 0:
            #     winner = nums[i]
            #     count +=1
        return winner
        
        winner = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == winner:
                count +=1
            else:
                count -=1
            if count == 0:
                winner = nums[i]
                count +=1
        return winner

# 第一个到来的士兵，直接插上自己阵营的旗帜占领这块高地，此时领主 winner 就是这个阵营的人，现存兵力 count = 1。

# 如果新来的士兵和前一个士兵是同一阵营，则集合起来占领高地，领主不变，winner 依然是当前这个士兵所属阵营，现存兵力 count++；

# 如果新来到的士兵不是同一阵营，则前方阵营派一个士兵和它同归于尽。 此时前方阵营兵力count --。（即使双方都死光，这块高地的旗帜 winner 依然不变，因为已经没有活着的士兵可以去换上自己的新旗帜）

# 当下一个士兵到来，发现前方阵营已经没有兵力，新士兵就成了领主，winner 变成这个士兵所属阵营的旗帜，现存兵力 count ++。


