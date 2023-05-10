class solution:
  def serachInsert(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) -1 
    
    while left <= right:
      mid = left + (right - left) // 2
      if nums[mid] < target:
        left = mid + 1
      elif nums[mid] > target:
        right = mid - 1
      else:
        return mid 
    return right + 1  # return left 也许， 
     # 终止时 right 在 left 左边， right + 1 = left
     # 插入到right 和 left 中间
      
      
