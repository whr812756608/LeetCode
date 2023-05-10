Class solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    # 四种转换， （）表示调用lowerbound
    # 画图易理解
    # >= lowerbound 的return值
    # >  大于       转换为 >=（x+1）；               lowerbound（nums，target+1）
    # <  小于       转换为 >= （x） -1； -1指左边一位数； lowerbound（nums，target）-1
    # <= 小于等于    转换为 >=（x+1）-1； -1指左边一位数； lowerbound（nums，target+1）-1
    
    def lower_bound(nums:List[int], target: int) -> int:
      # 左闭右闭模版
      left = 0
      right = len(nums) - 1
      
      while left <= right:
        mid = left + (right-left) //2
        # num【mid】< target,更新左端点
        if nums[mid] < target:
          left = mid + 1
        # num【mid】>= target,更新右端点
        # 注意要包括 = target的情况，否则会无限循环
        else:
          right = mid -1 
      return left
   
  # 调用lower bound
  # lower bound return start为大于等于x，return第一个符合要求数字的index
  start = lower_bound(nums,target)
  # end 为 小与等于x，最后一个符合要求数字的index
  # <=x 可转换为 >= (x+1) - 1, 
  # 先用lowerbound 求出大于等于 target+1的数；lower_boudn(nums,target+1)
  # 再减一得到其左边的数，lower_boudn(nums,target+1)-1，即为最后一个符合要求数字的index
  end = lower_bound(nums,target+1) -1
  if start == len(nums) or nums[start] != target:
    return [-1,1]
  
  return [start, end]

四种转换
