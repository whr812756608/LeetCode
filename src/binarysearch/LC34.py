Class solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    
    def lower_bound(nums:List[int], target: int) -> int:
      left = 0
      right = len(nums) - 1
      
      while left <= right:
        mid = left + (right-left) //2
        if nums[mid] < target:
          left = mid + 1
        else:
          right = mid -1 
      return left
   
  start = lower_bound(nums,target)
  end = lower_bound(nums,target+1) -1
  if start == len(nums) or nums[start] != target:
    return [-1,1]
  
  return [start, end]
