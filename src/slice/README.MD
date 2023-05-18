
## Slice a list or string in Python
# python切割的注意事项
- s[:] and s[::]
    - 
- 二分查找的问题分类：
    - 找寻一个值的位置，其算法基本模板为：
      ```Java
      class Solution {
          public int searchValue(int[] nums, int value) {
              // 搜索空间为闭区间 [0, nums.length-1]
              int low = 0, high = nums.length - 1; 
              while (low <= high) {	// 注意点 1
                  int mid = low + (high - low) / 2;
                  if (nums[mid] == value) {
                      return mid;		// 注意点 2
                  } else if (nums[mid] < value) {
                      low = mid + 1;
                  } else {
                      high = mid - 1;
                  }
              }
              return -1;
          }
      }
      ```

